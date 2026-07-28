"""Two-country council: citizens vote locally, then the other group decides."""
from __future__ import annotations
from packages.core import db
from packages.core.repositories import outbox_repo
from packages.core.services import country_trade

ACTIONS={
 "friend":"دوستی رسمی","trade_partner":"شراکت تجاری","defensive_ally":"پیمان دفاعی",
 "aid_food":"ارسال ۵۰ واحد غذا","aid_energy":"ارسال ۵۰ واحد انرژی","aid_irt":"ارسال ۵۰۰ هزار تومان",
}
RELATIONS=frozenset({"friend","trade_partner","defensive_ally"})
AID={"aid_food":"food","aid_energy":"energy","aid_irt":"IRT"}

async def _citizen_country(conn,player_id:int)->int:
 value=await conn.fetchval("SELECT country_id FROM citizenships WHERE player_id=$1 AND is_active",player_id)
 if not value:raise PermissionError("citizen_required")
 return int(value)

async def _citizen_count(conn,country_id:int)->int:
 return int(await conn.fetchval("SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active",country_id) or 0)

def threshold(citizens:int)->int:
 return 1 if citizens<=2 else 2 if citizens<=6 else 3

async def create(proposer:int,target:int,actor:int,action:str,key:str):
 if action not in ACTIONS:raise ValueError("invalid_council_action")
 if proposer==target:raise ValueError("same_country")
 async with db.transaction() as conn:
  if await _citizen_country(conn,actor)!=proposer:raise PermissionError("citizen_required")
  if not await conn.fetchval("SELECT 1 FROM countries WHERE id=$1",target):raise ValueError("country_not_found")
  row=await conn.fetchrow("""INSERT INTO country_council_proposals
   (proposer_country_id,target_country_id,created_by_player_id,action_code,idempotency_key)
   VALUES($1,$2,$3,$4,$5)
   ON CONFLICT(proposer_country_id,target_country_id,action_code)
   WHERE status IN ('local_voting','remote_voting') DO NOTHING RETURNING id""",proposer,target,actor,action,key)
  if not row:raise ValueError("proposal_exists")
  proposal_id=int(row['id'])
  await conn.execute("INSERT INTO country_council_votes(proposal_id,country_id,player_id,vote) VALUES($1,$2,$3,'yes')",proposal_id,proposer,actor)
  await conn.execute("UPDATE country_council_proposals SET local_yes=1 WHERE id=$1",proposal_id)
  return await _advance_vote(conn,proposal_id)

async def vote(proposal_id:int,player_id:int,choice:str):
 if choice not in {"yes","no"}:raise ValueError("invalid_vote")
 execute=False
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM country_council_proposals WHERE id=$1 FOR UPDATE",proposal_id)
  if not row:raise ValueError("proposal_not_found")
  if row['status'] not in {'local_voting','remote_voting'}:raise ValueError("proposal_closed")
  expected=int(row['proposer_country_id'] if row['status']=='local_voting' else row['target_country_id'])
  if await _citizen_country(conn,player_id)!=expected:raise PermissionError("wrong_country_vote")
  inserted=await conn.fetchval("""INSERT INTO country_council_votes(proposal_id,country_id,player_id,vote)
   VALUES($1,$2,$3,$4) ON CONFLICT DO NOTHING RETURNING player_id""",proposal_id,expected,player_id,choice)
  if not inserted:raise ValueError("already_voted")
  field=("local_" if row['status']=='local_voting' else "remote_")+choice
  await conn.execute(f"UPDATE country_council_proposals SET {field}={field}+1,updated_at=now() WHERE id=$1",proposal_id)
  result=await _advance_vote(conn,proposal_id);execute=result.pop('execute',False)
 if execute:return await _execute(proposal_id)
 return result

async def _advance_vote(conn,proposal_id:int):
 row=await conn.fetchrow("SELECT * FROM country_council_proposals WHERE id=$1 FOR UPDATE",proposal_id)
 side='local' if row['status']=='local_voting' else 'remote'
 country=int(row['proposer_country_id'] if side=='local' else row['target_country_id'])
 needed=threshold(await _citizen_count(conn,country));yes=int(row[f'{side}_yes']);no=int(row[f'{side}_no'])
 if no>=needed:
  await conn.execute("UPDATE country_council_proposals SET status='rejected',updated_at=now() WHERE id=$1",proposal_id)
  return {"id":proposal_id,"status":"rejected","yes":yes,"no":no,"needed":needed}
 if yes<needed:return {"id":proposal_id,"status":str(row['status']),"yes":yes,"no":no,"needed":needed}
 if side=='local':
  await conn.execute("UPDATE country_council_proposals SET status='remote_voting',remote_closes_at=now()+interval '24 hours',updated_at=now() WHERE id=$1",proposal_id)
  chat=await conn.fetchval("SELECT g.telegram_id FROM countries c JOIN groups g ON g.id=c.group_id WHERE c.id=$1",row['target_country_id'])
  source=await conn.fetchval("SELECT name FROM countries WHERE id=$1",row['proposer_country_id'])
  await outbox_repo.enqueue(conn,f"council:{proposal_id}:remote","intergroup_council",{"text":f"🌍 {source} یک پیشنهاد تازه فرستاده: {ACTIONS[str(row['action_code'])]}. از بخش شورای جهان رأی بدهید."},chat)
  return {"id":proposal_id,"status":"remote_voting","yes":yes,"no":no,"needed":needed}
 # Mark execution intent while locked; the effect runs after commit to avoid nested transaction deadlocks.
 await conn.execute("UPDATE country_council_proposals SET updated_at=now() WHERE id=$1",proposal_id)
 return {"id":proposal_id,"status":"remote_voting","yes":yes,"no":no,"needed":needed,"execute":True}

async def _official(country_id:int,*,diplomacy:bool)->int|None:
 roles=['foreign_minister'] if diplomacy else ['economy_minister','foreign_minister']
 return await db.fetchval("""SELECT COALESCE(c.president_player_id,(SELECT player_id FROM country_offices
  WHERE country_id=c.id AND role_code=ANY($2::text[]) ORDER BY id LIMIT 1)) FROM countries c WHERE c.id=$1""",country_id,roles)

async def _execute(proposal_id:int):
 row=await db.fetchrow("SELECT * FROM country_council_proposals WHERE id=$1",proposal_id)
 if not row or row['status']!='remote_voting':raise ValueError("proposal_closed")
 action=str(row['action_code']);a=int(row['proposer_country_id']);b=int(row['target_country_id']);key=f"council:{proposal_id}:execute"
 try:
  actor=await _official(a,diplomacy=action in RELATIONS)
  if not actor:raise ValueError("source_official_required")
  if action in RELATIONS:
   target_actor=await _official(b,diplomacy=True)
   if not target_actor:raise ValueError("target_official_required")
   await country_trade.propose_relation(a,b,int(actor),action,key+":propose")
   await country_trade.accept_relation(b,a,int(target_actor),key+":accept")
  else:
   try:await country_trade.send_aid(a,b,int(actor),AID[action],key)
   except ValueError as exc:
    # Council aid is also a negotiated transfer. If there is no active crisis,
    # move the agreed preset atomically without granting humanitarian reputation.
    if str(exc)!="recipient_has_no_crisis":raise
    asset=AID[action];amount=int(__import__('packages.core.config',fromlist=['get_config']).get_config().section("country_trade.aid.presets")[asset])
    from packages.core.repositories import ledger_repo
    async with db.transaction() as conn:
     for cid in sorted((a,b)):
      if not await ledger_repo.lock_country(conn,cid):raise ValueError("country_not_found")
     debit=await ledger_repo.change_country(conn,a,asset,-amount);credit=await ledger_repo.change_country(conn,b,asset,amount)
     await ledger_repo.insert(conn,player_id=None,country_id=a,key=key+":debit",reason="council_group_aid",asset=asset,account=ledger_repo.country_account(asset),amount=-amount,balance=debit,metadata={"recipient":b,"proposal_id":proposal_id})
     await ledger_repo.insert(conn,player_id=None,country_id=b,key=key+":credit",reason="council_group_aid",asset=asset,account=ledger_repo.country_account(asset),amount=amount,balance=credit,metadata={"donor":a,"proposal_id":proposal_id})
 except (ValueError,PermissionError) as exc:
  await db.execute("UPDATE country_council_proposals SET status='failed',failure_code=$2,updated_at=now() WHERE id=$1 AND status='remote_voting'",proposal_id,str(exc))
  return {"id":proposal_id,"status":"failed","reason":str(exc)}
 await db.execute("UPDATE country_council_proposals SET status='approved',executed_at=now(),updated_at=now() WHERE id=$1 AND status='remote_voting'",proposal_id)
 return {"id":proposal_id,"status":"approved"}

async def dashboard(country_id:int):
 return await db.fetch("""SELECT p.*,a.name proposer_name,b.name target_name FROM country_council_proposals p
  JOIN countries a ON a.id=p.proposer_country_id JOIN countries b ON b.id=p.target_country_id
  WHERE (p.proposer_country_id=$1 OR p.target_country_id=$1) AND p.status IN('local_voting','remote_voting')
  ORDER BY p.created_at DESC LIMIT 12""",country_id)

async def detail(proposal_id:int):
 return await db.fetchrow("""SELECT p.*,a.name proposer_name,b.name target_name FROM country_council_proposals p
  JOIN countries a ON a.id=p.proposer_country_id JOIN countries b ON b.id=p.target_country_id WHERE p.id=$1""",proposal_id)

async def has_voted(proposal_id:int,player_id:int)->bool:
 return bool(await db.fetchval("SELECT 1 FROM country_council_votes WHERE proposal_id=$1 AND player_id=$2",proposal_id,player_id))

async def countries_except(country_id:int):
 return await db.fetch("SELECT id,name FROM countries WHERE id<>$1 AND status<>'forming' ORDER BY name LIMIT 30",country_id)

async def expire_due()->int:
 return int(await db.fetchval("""WITH x AS (UPDATE country_council_proposals SET status='expired',updated_at=now()
  WHERE (status='local_voting' AND local_closes_at<=now()) OR (status='remote_voting' AND remote_closes_at<=now()) RETURNING 1)
  SELECT count(*) FROM x""") or 0)
