"""Controlled country migration with escrowed exit fee and destination approval."""
from __future__ import annotations
from datetime import UTC,datetime,timedelta
from packages.core import db

def exit_fee(wealth:int)->int:return min(50_000_000,max(500_000,wealth*5//100))
async def political_hold(player_id:int)->bool:
 return bool(await db.fetchval("SELECT political_hold_until>now() FROM citizenships WHERE player_id=$1 AND is_active",player_id))
async def quote(player_id:int,destination_country_id:int):
 return await db.fetchrow("""SELECT cs.country_id origin_country_id,o.name origin_name,d.id destination_country_id,d.name destination_name,d.president_player_id,p.wallet_toman,p.savings_toman,cs.last_migrated_at
 FROM citizenships cs JOIN countries o ON o.id=cs.country_id JOIN countries d ON d.id=$2 JOIN players p ON p.id=cs.player_id WHERE cs.player_id=$1 AND cs.is_active AND cs.country_id<>d.id""",player_id,destination_country_id)
async def request(player_id:int,destination_country_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("""SELECT cs.country_id origin_country_id,d.president_player_id,p.wallet_toman,p.savings_toman,cs.last_migrated_at FROM citizenships cs JOIN countries d ON d.id=$2 JOIN players p ON p.id=cs.player_id WHERE cs.player_id=$1 AND cs.is_active AND cs.country_id<>d.id FOR UPDATE OF cs,p,d""",player_id,destination_country_id)
  if not row:raise ValueError("migration_not_available")
  if row["last_migrated_at"] and row["last_migrated_at"]>datetime.now(UTC)-timedelta(days=30):raise ValueError("migration_cooldown")
  if await conn.fetchval("SELECT 1 FROM migration_requests WHERE player_id=$1 AND status='pending'",player_id):raise ValueError("migration_pending")
  if await conn.fetchval("SELECT president_player_id=$2 FROM countries WHERE id=$1",row["origin_country_id"],player_id):raise ValueError("leader_must_transfer_power")
  fee=exit_fee(int(row["wallet_toman"])+int(row["savings_toman"]))
  if int(row["wallet_toman"])+int(row["savings_toman"])<fee:raise ValueError("insufficient_balance")
  # Fee is charged only on completion. Approval requests cannot lock funds forever.
  req=await conn.fetchrow("INSERT INTO migration_requests(player_id,origin_country_id,destination_country_id,exit_fee_toman) VALUES($1,$2,$3,$4) RETURNING *",player_id,row["origin_country_id"],destination_country_id,fee)
  if row["president_player_id"] is None:return await _complete(conn,req["id"],None)
  return req
async def _complete(conn,request_id:int,reviewer:int|None):
 req=await conn.fetchrow("SELECT * FROM migration_requests WHERE id=$1 AND status='pending' FOR UPDATE",request_id)
 if not req or req["expires_at"]<=datetime.now(UTC):raise ValueError("migration_expired")
 p=await conn.fetchrow("SELECT wallet_toman,savings_toman FROM players WHERE id=$1 FOR UPDATE",req["player_id"]);fee=int(req["exit_fee_toman"])
 wallet_take=min(int(p["wallet_toman"]),fee);saving_take=fee-wallet_take
 if int(p["wallet_toman"])+int(p["savings_toman"])<fee:raise ValueError("insufficient_balance")
 await conn.execute("UPDATE players SET wallet_toman=wallet_toman-$2,savings_toman=savings_toman-$3 WHERE id=$1",req["player_id"],wallet_take,saving_take)
 await conn.execute("UPDATE countries SET treasury_toman=treasury_toman+$2 WHERE id=$1",req["origin_country_id"],fee)
 await conn.execute("UPDATE citizenships SET country_id=$2,joined_at=now(),left_at=NULL,is_active=TRUE,migrant_until=now()+interval '30 days',political_hold_until=now()+interval '14 days',last_migrated_at=now() WHERE player_id=$1",req["player_id"],req["destination_country_id"])
 await conn.execute("UPDATE migration_requests SET status='approved',reviewed_by_player_id=$2,resolved_at=now() WHERE id=$1",request_id,reviewer)
 return await conn.fetchrow("SELECT * FROM migration_requests WHERE id=$1",request_id)
async def approve(request_id:int,president_id:int):
 async with db.transaction() as conn:
  allowed=await conn.fetchval("SELECT 1 FROM migration_requests r JOIN countries c ON c.id=r.destination_country_id WHERE r.id=$1 AND c.president_player_id=$2 AND r.status='pending'",request_id,president_id)
  if not allowed:raise PermissionError("president_required")
  return await _complete(conn,request_id,president_id)
async def reject(request_id:int,president_id:int,note:str|None=None):
 return bool(await db.fetchval("""UPDATE migration_requests r SET status='rejected',reviewed_by_player_id=$2,review_note=$3,resolved_at=now() FROM countries c WHERE r.id=$1 AND c.id=r.destination_country_id AND c.president_player_id=$2 AND r.status='pending' RETURNING r.id""",request_id,president_id,note))
async def pending_for_country(country_id:int):
 return await db.fetch("""SELECT r.id,r.player_id,r.exit_fee_toman,r.expires_at,p.first_name,o.name origin_name FROM migration_requests r JOIN players p ON p.id=r.player_id JOIN countries o ON o.id=r.origin_country_id WHERE r.destination_country_id=$1 AND r.status='pending' AND r.expires_at>now() ORDER BY r.created_at""",country_id)
async def expire()->int:
 result=await db.execute("UPDATE migration_requests SET status='expired',resolved_at=now() WHERE status='pending' AND expires_at<=now()");return int(result.rsplit(' ',1)[-1])