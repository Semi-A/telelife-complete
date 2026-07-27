"""Atomic inter-country trade, escrow, diplomacy, sanctions and emergency aid."""
from __future__ import annotations
from datetime import UTC,datetime
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo,outbox_repo
from packages.core.services.country_trade_rules import pair,tariff_bp,net_after_tariff,open_limit,RELATIONS

DIPLOMAT_ROLES=("foreign_minister",)

def _account(asset:str)->str:return ledger_repo.country_account(asset)

async def _authorized(conn,country_id:int,player_id:int,*,diplomacy:bool=False)->bool:
 country=await conn.fetchrow("SELECT president_player_id FROM countries WHERE id=$1",country_id)
 if not country:return False
 if int(country["president_player_id"] or 0)==player_id:return True
 roles=("foreign_minister",) if diplomacy else ("economy_minister","foreign_minister")
 return bool(await conn.fetchval("SELECT 1 FROM country_offices WHERE country_id=$1 AND player_id=$2 AND role_code=ANY($3::text[])",country_id,player_id,list(roles)))

async def _relation(conn,a:int,b:int)->str:
 lo,hi=pair(a,b)
 return str(await conn.fetchval("SELECT status FROM country_relations WHERE country_low_id=$1 AND country_high_id=$2",lo,hi) or "neutral")

async def _reputation(conn,country_id:int)->int:
 await conn.execute("INSERT INTO country_international_reputation(country_id) VALUES($1) ON CONFLICT DO NOTHING",country_id)
 return int(await conn.fetchval("SELECT score FROM country_international_reputation WHERE country_id=$1 FOR UPDATE",country_id) or 50)

async def _adjust_rep(conn,country_id:int,delta:int,field:str|None=None)->None:
 await _reputation(conn,country_id)
 cfg=get_config();minimum=cfg.int_("country_trade.reputation.minimum");maximum=cfg.int_("country_trade.reputation.maximum")
 field_sql={"fulfilled":"fulfilled_contracts=fulfilled_contracts+1,","cancelled":"cancelled_contracts=cancelled_contracts+1,"}.get(field,"")
 await conn.execute(f"UPDATE country_international_reputation SET {field_sql} score=GREATEST($3::int,LEAST($4::int,score+$2::int)),updated_at=now() WHERE country_id=$1",country_id,delta,minimum,maximum)

async def create_contract(proposer_id:int,recipient_id:int,actor_id:int,preset:str,key:str):
 cfg=get_config();presets=cfg.section("country_trade.contracts.presets")
 if preset not in presets:raise ValueError("invalid_trade_preset")
 spec=presets[preset];offered_asset=str(spec["offered_asset"]);requested_asset=str(spec["requested_asset"]);offered=int(spec["offered_amount"]);requested=int(spec["requested_amount"])
 if offered_asset not in cfg.get("country_trade.assets.allowed") or requested_asset not in cfg.get("country_trade.assets.allowed"):raise ValueError("invalid_asset")
 async with db.transaction() as conn:
  # Deterministic lock order prevents reciprocal contracts from deadlocking.
  for cid in sorted((proposer_id,recipient_id)):
   if not await ledger_repo.lock_country(conn,cid):raise ValueError("country_not_found")
  if not await _authorized(conn,proposer_id,actor_id):raise PermissionError("trade_permission_required")
  blocked=await conn.fetchval("SELECT 1 FROM country_sanctions WHERE status='active' AND ((imposing_country_id=$1 AND target_country_id=$2) OR (imposing_country_id=$2 AND target_country_id=$1))",proposer_id,recipient_id)
  if blocked:raise ValueError("trade_sanctioned")
  rep=await _reputation(conn,proposer_id);opened=int(await conn.fetchval("SELECT count(*) FROM country_trade_contracts WHERE proposer_country_id=$1 AND status='open'",proposer_id) or 0)
  if opened>=open_limit(rep):raise ValueError("open_contract_limit")
  relation=await _relation(conn,proposer_id,recipient_id);tariff=tariff_bp(relation)
  row=await conn.fetchrow("""INSERT INTO country_trade_contracts(proposer_country_id,recipient_country_id,offered_asset,offered_amount,requested_asset,requested_amount,tariff_bp,created_by_player_id,idempotency_key,expires_at) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,now()+($10::double precision*interval '1 hour')) ON CONFLICT(idempotency_key) DO NOTHING RETURNING *""",proposer_id,recipient_id,offered_asset,offered,requested_asset,requested,tariff,actor_id,key,cfg.int_("country_trade.contracts.expiry_hours"))
  if not row:return None
  balance=await ledger_repo.change_country(conn,proposer_id,offered_asset,-offered)
  await ledger_repo.insert(conn,player_id=None,country_id=proposer_id,key=f"{key}:escrow",reason="trade_escrow_hold",asset=offered_asset,account=_account(offered_asset),amount=-offered,balance=balance,metadata={"contract_id":int(row["id"])})
  await conn.execute("INSERT INTO country_trade_escrow(contract_id,asset_code,amount) VALUES($1,$2,$3)",row["id"],offered_asset,offered)
  await conn.execute("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,$3,'trade_created',$4,$5)",proposer_id,recipient_id,actor_id,f"{key}:audit",{"contract_id":int(row["id"]),"preset":preset})
  chat=await conn.fetchval("SELECT g.telegram_id FROM countries c JOIN groups g ON g.id=c.group_id WHERE c.id=$1",recipient_id)
  await outbox_repo.enqueue(conn,f"{key}:notify","country_trade_offer",{"text":f"📦 قرارداد تجاری تازه‌ای برای کشور ثبت شد. پیشنهاد #{int(row['id'])} را در بخش تجارت بررسی کنید."},chat)
  return row

async def accept_contract(contract_id:int,actor_id:int,key:str):
 async with db.transaction() as conn:
  contract=await conn.fetchrow("SELECT * FROM country_trade_contracts WHERE id=$1 FOR UPDATE",contract_id)
  if not contract:raise ValueError("contract_not_found")
  if contract["status"]!="open" or contract["expires_at"]<=datetime.now(UTC):raise ValueError("contract_not_open")
  a=int(contract["proposer_country_id"]);b=int(contract["recipient_country_id"])
  for cid in sorted((a,b)):
   if not await ledger_repo.lock_country(conn,cid):raise ValueError("country_not_found")
  if not await _authorized(conn,b,actor_id):raise PermissionError("trade_permission_required")
  if await conn.fetchval("SELECT 1 FROM country_sanctions WHERE status='active' AND ((imposing_country_id=$1 AND target_country_id=$2) OR (imposing_country_id=$2 AND target_country_id=$1))",a,b):raise ValueError("trade_sanctioned")
  escrow=await conn.fetchrow("SELECT * FROM country_trade_escrow WHERE contract_id=$1 FOR UPDATE",contract_id)
  if not escrow or escrow["status"]!="held":raise ValueError("escrow_not_held")
  requested=str(contract["requested_asset"]);requested_amount=int(contract["requested_amount"]);offered=str(contract["offered_asset"]);offered_amount=int(contract["offered_amount"])
  paid_balance=await ledger_repo.change_country(conn,b,requested,-requested_amount)
  await ledger_repo.insert(conn,player_id=None,country_id=b,key=f"{key}:recipient-debit",reason="trade_settlement_debit",asset=requested,account=_account(requested),amount=-requested_amount,balance=paid_balance,metadata={"contract_id":contract_id})
  offered_net,offered_fee=net_after_tariff(offered_amount,int(contract["tariff_bp"]));requested_net,requested_fee=net_after_tariff(requested_amount,int(contract["tariff_bp"]))
  b_balance=await ledger_repo.change_country(conn,b,offered,offered_net)
  await ledger_repo.insert(conn,player_id=None,country_id=b,key=f"{key}:recipient-credit",reason="trade_settlement_credit",asset=offered,account=_account(offered),amount=offered_net,balance=b_balance,metadata={"contract_id":contract_id,"tariff":offered_fee})
  a_balance=await ledger_repo.change_country(conn,a,requested,requested_net)
  await ledger_repo.insert(conn,player_id=None,country_id=a,key=f"{key}:proposer-credit",reason="trade_settlement_credit",asset=requested,account=_account(requested),amount=requested_net,balance=a_balance,metadata={"contract_id":contract_id,"tariff":requested_fee})
  await conn.execute("UPDATE country_trade_escrow SET status='released',released_at=now(),updated_at=now() WHERE contract_id=$1",contract_id)
  updated=await conn.fetchval("UPDATE country_trade_contracts SET status='accepted',accepted_by_player_id=$2,accepted_at=now(),updated_at=now() WHERE id=$1 AND status='open' RETURNING id",contract_id,actor_id)
  if not updated:raise RuntimeError("trade_state_conflict")
  gain=get_config().int_("country_trade.reputation.contract_fulfilled_gain")
  await _adjust_rep(conn,a,gain,"fulfilled");await _adjust_rep(conn,b,gain,"fulfilled")
  await conn.execute("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,$3,'trade_accepted',$4,$5) ON CONFLICT(idempotency_key) DO NOTHING",b,a,actor_id,key,{"contract_id":contract_id})
  return {"offered_net":offered_net,"requested_net":requested_net,"tariff_bp":int(contract["tariff_bp"])}

async def _refund(conn,contract,reason:str,key:str)->bool:
 escrow=await conn.fetchrow("SELECT * FROM country_trade_escrow WHERE contract_id=$1 FOR UPDATE",contract["id"])
 if not escrow or escrow["status"]!="held":return False
 cid=int(contract["proposer_country_id"]);asset=str(escrow["asset_code"]);amount=int(escrow["amount"])
 await ledger_repo.lock_country(conn,cid);balance=await ledger_repo.change_country(conn,cid,asset,amount)
 await ledger_repo.insert(conn,player_id=None,country_id=cid,key=f"{key}:refund",reason="trade_escrow_refund",asset=asset,account=_account(asset),amount=amount,balance=balance,metadata={"contract_id":int(contract["id"]),"reason":reason})
 await conn.execute("UPDATE country_trade_escrow SET status='refunded',released_at=now(),updated_at=now() WHERE contract_id=$1",contract["id"])
 return True

async def cancel_contract(contract_id:int,actor_id:int,key:str)->bool:
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM country_trade_contracts WHERE id=$1 FOR UPDATE",contract_id)
  if not row or row["status"]!="open":return False
  if not await _authorized(conn,int(row["proposer_country_id"]),actor_id):raise PermissionError("trade_permission_required")
  if not await _refund(conn,row,"cancelled",key):return False
  await conn.execute("UPDATE country_trade_contracts SET status='cancelled',cancelled_at=now(),updated_at=now() WHERE id=$1",contract_id)
  await _adjust_rep(conn,int(row["proposer_country_id"]),-get_config().int_("country_trade.reputation.cancellation_penalty"),"cancelled")
  return True

async def expire_due()->int:
 limit=get_config().int_("country_trade.scheduler.expiry_batch_size");done=0
 async with db.transaction() as conn:
  rows=await conn.fetch("SELECT * FROM country_trade_contracts WHERE status='open' AND expires_at<=now() ORDER BY expires_at,id FOR UPDATE SKIP LOCKED LIMIT $1",limit)
  for row in rows:
   if await _refund(conn,row,"expired",f"trade-expire:{row['id']}"):
    await conn.execute("UPDATE country_trade_contracts SET status='expired',updated_at=now() WHERE id=$1",row["id"]);done+=1
 return done

async def propose_relation(country_id:int,target_id:int,actor_id:int,status:str,key:str)->bool:
 if status not in {"friend","trade_partner","defensive_ally"}:raise ValueError("invalid_relation")
 lo,hi=pair(country_id,target_id)
 async with db.transaction() as conn:
  if not await _authorized(conn,country_id,actor_id,diplomacy=True):raise PermissionError("diplomacy_permission_required")
  inserted=await conn.fetchval("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,$3,'relation_proposed',$4,$5) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",country_id,target_id,actor_id,key,{"status":status})
  if not inserted:return False
  hours=get_config().int_("country_trade.diplomacy.proposal_hours")
  await conn.execute("""INSERT INTO country_relations(country_low_id,country_high_id,proposed_status,proposed_by_country_id,proposal_expires_at,changed_by_player_id) VALUES($1,$2,$3,$4,now()+($5::double precision*interval '1 hour'),$6) ON CONFLICT(country_low_id,country_high_id) DO UPDATE SET proposed_status=EXCLUDED.proposed_status,proposed_by_country_id=EXCLUDED.proposed_by_country_id,proposal_expires_at=EXCLUDED.proposal_expires_at,changed_by_player_id=EXCLUDED.changed_by_player_id,updated_at=now()""",lo,hi,status,country_id,hours,actor_id)
  chat=await conn.fetchval("SELECT g.telegram_id FROM countries c JOIN groups g ON g.id=c.group_id WHERE c.id=$1",target_id)
  await outbox_repo.enqueue(conn,f"{key}:notify","country_relation_offer",{"text":"🤝 یک پیشنهاد رسمی دیپلماتیک برای کشور ثبت شد. از بخش روابط خارجی بررسی‌اش کنید."},chat)
  return True

async def accept_relation(country_id:int,target_id:int,actor_id:int,key:str)->bool:
 lo,hi=pair(country_id,target_id)
 async with db.transaction() as conn:
  if not await _authorized(conn,country_id,actor_id,diplomacy=True):raise PermissionError("diplomacy_permission_required")
  row=await conn.fetchrow("SELECT * FROM country_relations WHERE country_low_id=$1 AND country_high_id=$2 FOR UPDATE",lo,hi)
  if not row or not row["proposed_status"] or int(row["proposed_by_country_id"] or 0)==country_id or row["proposal_expires_at"]<=datetime.now(UTC):raise ValueError("relation_proposal_missing")
  await conn.execute("UPDATE country_relations SET status=proposed_status,proposed_status=NULL,proposed_by_country_id=NULL,proposal_expires_at=NULL,changed_by_player_id=$3,updated_at=now() WHERE country_low_id=$1 AND country_high_id=$2",lo,hi,actor_id)
  await conn.execute("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,$3,'relation_accepted',$4,$5) ON CONFLICT(idempotency_key) DO NOTHING",country_id,target_id,actor_id,key,{"status":str(row["proposed_status"])})
  return True

async def impose_sanction(country_id:int,target_id:int,actor_id:int,key:str)->bool:
 pair(country_id,target_id)
 async with db.transaction() as conn:
  if not await _authorized(conn,country_id,actor_id,diplomacy=True):raise PermissionError("diplomacy_permission_required")
  inserted=await conn.fetchval("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key) VALUES($1,$2,$3,'sanction_imposed',$4) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",country_id,target_id,actor_id,key)
  if not inserted:return False
  await conn.execute("""INSERT INTO country_sanctions(imposing_country_id,target_country_id,imposed_by_player_id) VALUES($1,$2,$3) ON CONFLICT(imposing_country_id,target_country_id) DO UPDATE SET status='active',imposed_by_player_id=EXCLUDED.imposed_by_player_id,imposed_at=now(),lifted_at=NULL""",country_id,target_id,actor_id)
  await _adjust_rep(conn,country_id,-get_config().int_("country_trade.reputation.sanction_imposer_cost"))
  return True

async def send_aid(donor_id:int,recipient_id:int,actor_id:int,asset:str,key:str)->int:
 cfg=get_config();presets=cfg.section("country_trade.aid.presets")
 if asset not in presets:raise ValueError("invalid_aid_asset")
 amount=int(presets[asset])
 async with db.transaction() as conn:
  for cid in sorted((donor_id,recipient_id)):await ledger_repo.lock_country(conn,cid)
  if not await _authorized(conn,donor_id,actor_id,diplomacy=True):raise PermissionError("diplomacy_permission_required")
  crisis=await conn.fetchrow("SELECT id FROM country_crises WHERE country_id=$1 AND status='active' ORDER BY severity DESC,id LIMIT 1 FOR UPDATE",recipient_id)
  if not crisis:raise ValueError("recipient_has_no_crisis")
  used=int(await conn.fetchval("SELECT COALESCE(sum(amount),0) FROM country_humanitarian_aid WHERE donor_country_id=$1 AND sent_at>=date_trunc('day',now())",donor_id) or 0)
  if asset!="IRT" and used+amount>cfg.int_("country_trade.aid.daily_limit_per_country"):raise ValueError("aid_daily_limit")
  inserted=await conn.fetchval("INSERT INTO country_humanitarian_aid(donor_country_id,recipient_country_id,asset_code,amount,crisis_id,sent_by_player_id,idempotency_key) VALUES($1,$2,$3,$4,$5,$6,$7) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",donor_id,recipient_id,asset,amount,crisis["id"],actor_id,key)
  if not inserted:return 0
  dbal=await ledger_repo.change_country(conn,donor_id,asset,-amount);rbal=await ledger_repo.change_country(conn,recipient_id,asset,amount)
  await ledger_repo.insert(conn,player_id=None,country_id=donor_id,key=f"{key}:debit",reason="humanitarian_aid",asset=asset,account=_account(asset),amount=-amount,balance=dbal,metadata={"recipient":recipient_id})
  await ledger_repo.insert(conn,player_id=None,country_id=recipient_id,key=f"{key}:credit",reason="humanitarian_aid",asset=asset,account=_account(asset),amount=amount,balance=rbal,metadata={"donor":donor_id})
  await _reputation(conn,donor_id)
  await conn.execute("UPDATE country_international_reputation SET aid_sent=aid_sent+$2::bigint WHERE country_id=$1",donor_id,amount)
  await _adjust_rep(conn,donor_id,cfg.int_("country_trade.reputation.aid_gain"))
  return amount

async def overview(country_id:int):
 return await db.fetchrow("""SELECT r.score,r.fulfilled_contracts,r.aid_sent,
 (SELECT count(*) FROM country_trade_contracts t WHERE (t.proposer_country_id=$1 OR t.recipient_country_id=$1) AND t.status='open') open_contracts,
 (SELECT count(*) FROM country_relations x WHERE (x.country_low_id=$1 OR x.country_high_id=$1) AND x.status<>'neutral') active_relations,
 (SELECT count(*) FROM country_sanctions s WHERE s.status='active' AND (s.imposing_country_id=$1 OR s.target_country_id=$1)) sanctions
 FROM country_international_reputation r WHERE r.country_id=$1""",country_id)

async def incoming(country_id:int):
 return await db.fetch("""SELECT t.*,c.name proposer_name FROM country_trade_contracts t JOIN countries c ON c.id=t.proposer_country_id WHERE t.recipient_country_id=$1 AND t.status='open' AND t.expires_at>now() ORDER BY t.expires_at,t.id LIMIT 20""",country_id)

async def countries_except(country_id:int):return await db.fetch("SELECT id,name FROM countries WHERE id<>$1 ORDER BY name LIMIT 50",country_id)


async def outgoing(country_id:int):
 return await db.fetch("""SELECT t.*,c.name recipient_name FROM country_trade_contracts t JOIN countries c ON c.id=t.recipient_country_id WHERE t.proposer_country_id=$1 AND t.status='open' AND t.expires_at>now() ORDER BY t.expires_at,t.id LIMIT 20""",country_id)

async def pending_relations(country_id:int):
 return await db.fetch("""SELECT r.*,c.id counterparty_id,c.name counterparty_name FROM country_relations r JOIN countries c ON c.id=CASE WHEN r.country_low_id=$1 THEN r.country_high_id ELSE r.country_low_id END WHERE (r.country_low_id=$1 OR r.country_high_id=$1) AND r.proposed_status IS NOT NULL AND r.proposed_by_country_id<>$1 AND r.proposal_expires_at>now() ORDER BY r.proposal_expires_at""",country_id)

async def lift_sanction(country_id:int,target_id:int,actor_id:int,key:str)->bool:
 pair(country_id,target_id)
 async with db.transaction() as conn:
  if not await _authorized(conn,country_id,actor_id,diplomacy=True):raise PermissionError("diplomacy_permission_required")
  inserted=await conn.fetchval("INSERT INTO country_diplomacy_audit(country_id,counterparty_country_id,actor_player_id,action_code,idempotency_key) VALUES($1,$2,$3,'sanction_lifted',$4) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",country_id,target_id,actor_id,key)
  if not inserted:return False
  result=await conn.execute("UPDATE country_sanctions SET status='lifted',lifted_at=now() WHERE imposing_country_id=$1 AND target_country_id=$2 AND status='active'",country_id,target_id)
  return result.endswith(' 1')

async def expire_relations()->int:
 result=await db.execute("UPDATE country_relations SET proposed_status=NULL,proposed_by_country_id=NULL,proposal_expires_at=NULL,updated_at=now() WHERE proposed_status IS NOT NULL AND proposal_expires_at<=now()")
 return int(result.rsplit(' ',1)[-1] or 0)

async def recent_reference(limit:int=10):
 return await db.fetch("""SELECT offered_asset,requested_asset,count(*) trades,round(avg(requested_amount::numeric/offered_amount),4) average_ratio FROM country_trade_contracts WHERE status='accepted' GROUP BY offered_asset,requested_asset ORDER BY count(*) DESC,offered_asset,requested_asset LIMIT $1""",limit)
