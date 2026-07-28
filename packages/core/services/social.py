"""Consent-first social interactions for citizens of the same country."""
from __future__ import annotations
from packages.core import db
from packages.core.repositories import ledger_repo

HELP_AMOUNTS={10_000,50_000,100_000,200_000}
CATEGORIES={"harassment","fraud","threat","spam","other"}

def pair(a:int,b:int)->tuple[int,int]:
 if a==b:raise ValueError("self_interaction")
 return min(a,b),max(a,b)

async def country_for(player_id:int,conn=None):
 q="SELECT country_id FROM citizenships WHERE player_id=$1 AND is_active"
 return await (conn.fetchval(q,player_id) if conn else db.fetchval(q,player_id))

async def require_peers(conn,actor:int,target:int)->int:
 pair(actor,target);a=await country_for(actor,conn);b=await country_for(target,conn)
 if not a or a!=b:raise PermissionError("same_country_required")
 return int(a)

async def citizens(country_id:int,exclude:int,limit:int=24):
 return await db.fetch("""SELECT p.id,p.first_name,p.reputation,p.level FROM citizenships cs JOIN players p ON p.id=cs.player_id
 WHERE cs.country_id=$1 AND cs.is_active AND p.id<>$2 AND NOT p.is_banned ORDER BY p.reputation DESC,p.level DESC,p.id LIMIT $3""",country_id,exclude,limit)

async def dashboard(country_id:int,player_id:int):
 return {
  "friends":int(await db.fetchval("SELECT count(*) FROM social_relationships WHERE kind='friendship' AND status='active' AND (player_low_id=$1 OR player_high_id=$1)",player_id) or 0),
  "marriage":await db.fetchrow("""SELECT r.id,p.first_name partner_name FROM social_relationships r JOIN players p ON p.id=CASE WHEN r.player_low_id=$1 THEN r.player_high_id ELSE r.player_low_id END WHERE r.kind='marriage' AND r.status='active' AND (r.player_low_id=$1 OR r.player_high_id=$1)""",player_id),
  "pending":await db.fetch("""SELECT r.id,r.kind,p.first_name proposer_name FROM social_relationships r JOIN players p ON p.id=r.proposed_by WHERE r.status='pending' AND r.proposed_by<>$1 AND (r.player_low_id=$1 OR r.player_high_id=$1) ORDER BY r.created_at DESC LIMIT 10""",player_id),
  "competitions":await db.fetch("""SELECT c.id,c.status,c.round_no,c.challenger_score,c.opponent_score,c.turn_player_id,p.first_name opponent_name FROM social_competitions c JOIN players p ON p.id=CASE WHEN c.challenger_id=$1 THEN c.opponent_id ELSE c.challenger_id END WHERE c.country_id=$2 AND ((c.status='pending' AND c.opponent_id=$1) OR (c.status='active' AND (c.challenger_id=$1 OR c.opponent_id=$1))) ORDER BY c.created_at DESC LIMIT 5""",player_id,country_id),
  "cases":int(await db.fetchval("SELECT count(*) FROM citizen_cases WHERE country_id=$1 AND status IN ('review','voting')",country_id) or 0),
  "resource_activity":await db.fetch("""SELECT t.transfer_type,t.asset_code,t.amount,t.created_at,a.first_name actor_name,b.first_name recipient_name
    FROM citizen_resource_transfers t JOIN players a ON a.id=t.actor_id LEFT JOIN players b ON b.id=t.recipient_id
    WHERE t.country_id=$1 ORDER BY t.created_at DESC LIMIT 5""",country_id),
 }

async def propose(kind:str,actor:int,target:int):
 if kind not in {"friendship","marriage"}:raise ValueError("invalid_relationship")
 low,high=pair(actor,target)
 async with db.transaction() as conn:
  country=await require_peers(conn,actor,target)
  if kind=="marriage":
   blocked=await conn.fetchval("""SELECT 1 FROM social_relationships WHERE kind='marriage' AND
    ((status IN ('pending','active') AND ($1 IN (player_low_id,player_high_id) OR $2 IN (player_low_id,player_high_id)))
     OR (status='ended' AND cooldown_until>now() AND ($1 IN (player_low_id,player_high_id) OR $2 IN (player_low_id,player_high_id))))""",actor,target)
   if blocked:raise ValueError("marriage_unavailable")
  try:return await conn.fetchrow("INSERT INTO social_relationships(country_id,kind,player_low_id,player_high_id,proposed_by) VALUES($1,$2,$3,$4,$5) RETURNING *",country,kind,low,high,actor)
  except Exception as exc:
   if "uq_social" in str(exc):raise ValueError("relationship_exists") from exc
   raise

async def respond(relationship_id:int,actor:int,accept:bool):
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM social_relationships WHERE id=$1 AND status='pending' FOR UPDATE",relationship_id)
  if not row:raise ValueError("request_not_found")
  if actor==row["proposed_by"] or actor not in {row["player_low_id"],row["player_high_id"]}:raise PermissionError("request_target_required")
  if accept and row["kind"]=="marriage" and await conn.fetchval("SELECT 1 FROM social_relationships WHERE id<>$1 AND kind='marriage' AND status='active' AND ($2 IN(player_low_id,player_high_id) OR $3 IN(player_low_id,player_high_id))",relationship_id,row["player_low_id"],row["player_high_id"]):raise ValueError("marriage_unavailable")
  status="active" if accept else "rejected"
  return await conn.fetchrow("UPDATE social_relationships SET status=$2,accepted_at=CASE WHEN $2='active' THEN now() END,ended_at=CASE WHEN $2='rejected' THEN now() END WHERE id=$1 RETURNING *",relationship_id,status)

async def divorce(actor:int):
 row=await db.fetchrow("""UPDATE social_relationships SET status='ended',ended_at=now(),cooldown_until=now()+interval '7 days'
 WHERE kind='marriage' AND status='active' AND $1 IN(player_low_id,player_high_id) RETURNING id""",actor)
 if not row:raise ValueError("marriage_not_found")
 return row

async def help(actor:int,target:int,amount:int,key:str):
 if amount not in HELP_AMOUNTS:raise ValueError("invalid_amount")
 async with db.transaction() as conn:
  # Serialize outgoing help so retries and the daily limit are exact.
  helper=await ledger_repo.lock_player(conn,actor)
  if not helper:raise ValueError("player_not_found")
  previous=await conn.fetchrow("SELECT * FROM citizen_help_events WHERE idempotency_key=$1",key)
  if previous:return previous
  country=await require_peers(conn,actor,target)
  if int(helper["wallet_toman"])<amount:raise ValueError("insufficient_balance")
  daily=int(await conn.fetchval("SELECT count(*) FROM citizen_help_events WHERE helper_id=$1 AND created_at>=date_trunc('day',now())",actor) or 0)
  if daily>=3:raise ValueError("help_daily_limit")
  rep=1 if daily<2 else 0
  debit=await ledger_repo.change_player(conn,actor,"IRT",-amount)
  credit=await ledger_repo.change_player(conn,target,"IRT",amount)
  await conn.execute("UPDATE players SET reputation=LEAST(1000,reputation+$2) WHERE id=$1",actor,rep)
  debit_ok=await ledger_repo.insert(conn,player_id=actor,country_id=None,key=f"{key}:debit",reason="citizen_help",asset="IRT",account="wallet",amount=-amount,balance=debit,metadata={"recipient_id":target,"country_id":country})
  credit_ok=await ledger_repo.insert(conn,player_id=target,country_id=None,key=f"{key}:credit",reason="citizen_help_received",asset="IRT",account="wallet",amount=amount,balance=credit,metadata={"helper_id":actor,"country_id":country})
  if not (debit_ok and credit_ok):raise RuntimeError("citizen_help_ledger_conflict")
  return await conn.fetchrow("INSERT INTO citizen_help_events(country_id,helper_id,recipient_id,amount_toman,reputation_awarded,idempotency_key) VALUES($1,$2,$3,$4,$5,$6) RETURNING *",country,actor,target,amount,rep,key)

async def challenge(actor:int,target:int):
 async with db.transaction() as conn:
  country=await require_peers(conn,actor,target)
  try:return await conn.fetchrow("INSERT INTO social_competitions(country_id,challenger_id,opponent_id) VALUES($1,$2,$3) RETURNING *",country,actor,target)
  except Exception as exc:
   if "uq_competition" in str(exc):raise ValueError("competition_exists") from exc
   raise

async def competition_respond(cid:int,actor:int,accept:bool):
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM social_competitions WHERE id=$1 AND status='pending' FOR UPDATE",cid)
  if not row:raise ValueError("competition_not_found")
  if actor!=row["opponent_id"]:raise PermissionError("request_target_required")
  status="active" if accept else "rejected"
  return await conn.fetchrow("UPDATE social_competitions SET status=$2,turn_player_id=CASE WHEN $2='active' THEN challenger_id END,resolved_at=CASE WHEN $2='rejected' THEN now() END WHERE id=$1 RETURNING *",cid,status)

async def play(cid:int,actor:int,move:str):
 if move not in {"focus","risk"}:raise ValueError("invalid_move")
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM social_competitions WHERE id=$1 AND status='active' AND expires_at>now() FOR UPDATE",cid)
  if not row:raise ValueError("competition_not_found")
  if int(row["turn_player_id"] or 0)!=actor:raise PermissionError("not_your_turn")
  score=2 if move=="focus" else (3 if (cid+actor+int(row["round_no"]))%2 else 0)
  challenger=actor==row["challenger_id"];round_no=int(row["round_no"])+(0 if challenger else 1)
  cs=int(row["challenger_score"])+(score if challenger else 0);os=int(row["opponent_score"])+(0 if challenger else score)
  done=round_no>=3;next_player=row["opponent_id"] if challenger else row["challenger_id"]
  winner=(row["challenger_id"] if cs>os else row["opponent_id"] if os>cs else None) if done else None
  await conn.execute("UPDATE social_competitions SET challenger_score=$2,opponent_score=$3,round_no=$4,turn_player_id=$5,status=CASE WHEN $6 THEN 'completed' ELSE 'active' END,winner_id=$7,resolved_at=CASE WHEN $6 THEN now() END WHERE id=$1",cid,cs,os,round_no,next_player,done,winner)
  if done and winner:
   await conn.execute("UPDATE players SET reputation=reputation+1 WHERE id=$1",winner)
  return {"score":score,"done":done,"challenger_score":cs,"opponent_score":os,"winner_id":winner}

async def report(actor:int,target:int,category:str):
 if category not in CATEGORIES:raise ValueError("invalid_category")
 async with db.transaction() as conn:
  country=await require_peers(conn,actor,target)
  recent=await conn.fetchval("SELECT 1 FROM citizen_reports WHERE reporter_id=$1 AND target_id=$2 AND created_at>now()-interval '24 hours'",actor,target)
  if recent:raise ValueError("report_rate_limit")
  return await conn.fetchrow("INSERT INTO citizen_reports(country_id,reporter_id,target_id,category) VALUES($1,$2,$3,$4) RETURNING *",country,actor,target,category)

async def open_case(actor:int,target:int,category:str,summary:str):
 if category not in CATEGORIES:raise ValueError("invalid_category")
 summary=" ".join(summary.split())
 if not 10<=len(summary)<=500:raise ValueError("invalid_case_summary")
 async with db.transaction() as conn:
  country=await require_peers(conn,actor,target)
  if int(await conn.fetchval("SELECT count(*) FROM citizen_cases WHERE plaintiff_id=$1 AND opened_at>now()-interval '7 days'",actor) or 0)>=2:raise ValueError("case_rate_limit")
  return await conn.fetchrow("INSERT INTO citizen_cases(country_id,plaintiff_id,defendant_id,category,summary,status,voting_ends_at) VALUES($1,$2,$3,$4,$5,'voting',now()+interval '24 hours') RETURNING *",country,actor,target,category,summary)

async def cases(country_id:int):
 return await db.fetch("""SELECT c.*,a.first_name plaintiff_name,b.first_name defendant_name FROM citizen_cases c JOIN players a ON a.id=c.plaintiff_id JOIN players b ON b.id=c.defendant_id WHERE c.country_id=$1 AND c.status='voting' AND c.voting_ends_at>now() ORDER BY c.opened_at DESC LIMIT 10""",country_id)

async def vote(case_id:int,voter:int,vote_value:str):
 if vote_value not in {"guilty","not_guilty"}:raise ValueError("invalid_vote")
 async with db.transaction() as conn:
  case=await conn.fetchrow("SELECT * FROM citizen_cases WHERE id=$1 AND status='voting' AND voting_ends_at>now() FOR UPDATE",case_id)
  if not case:raise ValueError("case_not_found")
  if not await conn.fetchval("SELECT 1 FROM citizenships WHERE player_id=$1 AND country_id=$2 AND is_active",voter,case["country_id"]):raise PermissionError("citizen_required")
  if voter in {case["plaintiff_id"],case["defendant_id"]}:raise PermissionError("case_party_cannot_vote")
  try:await conn.execute("INSERT INTO citizen_case_votes(case_id,voter_id,vote) VALUES($1,$2,$3)",case_id,voter,vote_value)
  except Exception as exc:
   if "citizen_case_votes_pkey" in str(exc):raise ValueError("already_voted") from exc
   raise
  field="guilty_votes" if vote_value=="guilty" else "not_guilty_votes"
  await conn.execute(f"UPDATE citizen_cases SET {field}={field}+1 WHERE id=$1",case_id)
  return True


async def resolve_due()->dict[str,int]:
 """Expire stale invitations/competitions and close court votes deterministically."""
 expired_comp=await db.execute("UPDATE social_competitions SET status='expired',resolved_at=now() WHERE status IN ('pending','active') AND expires_at<=now()")
 expired_rel=await db.execute("UPDATE social_relationships SET status='cancelled',ended_at=now() WHERE status='pending' AND created_at<=now()-interval '7 days'")
 rows=await db.fetch("SELECT id,guilty_votes,not_guilty_votes,defendant_id FROM citizen_cases WHERE status='voting' AND voting_ends_at<=now() ORDER BY id LIMIT 200")
 resolved=0
 for row in rows:
  total=int(row['guilty_votes'])+int(row['not_guilty_votes'])
  guilty=total>=3 and int(row['guilty_votes'])>int(row['not_guilty_votes'])
  verdict='guilty' if guilty else 'not_guilty'
  async with db.transaction() as conn:
   changed=await conn.fetchval("UPDATE citizen_cases SET status='resolved',verdict=$2,resolved_at=now() WHERE id=$1 AND status='voting' RETURNING id",row['id'],verdict)
   if changed and guilty:
    await conn.execute("UPDATE players SET reputation=GREATEST(-1000,reputation-3) WHERE id=$1",row['defendant_id'])
   if changed:resolved+=1
 def count(tag:str)->int:return int(tag.rsplit(' ',1)[-1])
 return {'competitions_expired':count(expired_comp),'relationships_expired':count(expired_rel),'cases_resolved':resolved}

async def admin_reports(limit:int=100):
 return await db.fetch("""SELECT r.id,r.category,r.status,r.created_at,c.name country_name,
  a.first_name reporter_name,b.first_name target_name FROM citizen_reports r
  JOIN countries c ON c.id=r.country_id JOIN players a ON a.id=r.reporter_id JOIN players b ON b.id=r.target_id
  ORDER BY CASE r.status WHEN 'open' THEN 0 ELSE 1 END,r.created_at DESC LIMIT $1""",limit)

async def review_report(report_id:int,status:str):
 if status not in {'reviewed','closed'}:raise ValueError('invalid_report_status')
 return await db.fetchrow("UPDATE citizen_reports SET status=$2 WHERE id=$1 RETURNING *",report_id,status)