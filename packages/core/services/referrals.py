"""Referral growth with delayed qualification and idempotent milestone rewards."""
from __future__ import annotations
import base64
from packages.core import db
from packages.core.repositories import ledger_repo

MILESTONES={1:100_000,3:250_000,5:500_000,10:1_000_000,20:2_000_000,50:5_000_000}

def code(player_id:int)->str:
 raw=int(player_id).to_bytes(8,"big");return base64.urlsafe_b64encode(raw).decode().rstrip("=")

def decode(value:str)->int|None:
 try:
  raw=base64.urlsafe_b64decode(value+"="*((4-len(value)%4)%4));number=int.from_bytes(raw,"big")
  return number if number>0 else None
 except (ValueError,TypeError):return None

def start_payload(player_id:int)->str:return "ref_"+code(player_id)

async def register(invited_player_id:int,payload:str|None)->bool:
 if not payload or not payload.startswith("ref_"):return False
 inviter=decode(payload[4:])
 if not inviter or inviter==invited_player_id:return False
 async with db.transaction() as conn:
  # Referral is accepted only for a genuinely new account (10-minute grace for first /start retries).
  invited=await conn.fetchrow("SELECT created_at FROM players WHERE id=$1 FOR UPDATE",invited_player_id)
  if not invited or not await conn.fetchval("SELECT 1 FROM players WHERE id=$1 AND NOT is_banned",inviter):return False
  is_new=bool(await conn.fetchval("SELECT $1::timestamptz >= now()-interval '10 minutes'",invited['created_at']))
  if not is_new:return False
  row=await conn.fetchval("""INSERT INTO player_referrals(inviter_player_id,invited_player_id,referral_code)
   VALUES($1,$2,$3) ON CONFLICT(invited_player_id) DO NOTHING RETURNING id""",inviter,invited_player_id,payload[4:])
  return bool(row)

async def _qualifies(conn,player_id:int)->bool:
 # Real activation: completed onboarding plus activity on two distinct game days.
 step=int(await conn.fetchval("SELECT onboarding_step FROM player_ui_state WHERE player_id=$1",player_id) or 0)
 days=int(await conn.fetchval("SELECT count(DISTINCT created_at::date) FROM ledger WHERE player_id=$1",player_id) or 0)
 return step>=4 and days>=2

async def qualify_for_player(player_id:int)->bool:
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM player_referrals WHERE invited_player_id=$1 AND status='pending' FOR UPDATE",player_id)
  if not row or not await _qualifies(conn,player_id):return False
  await conn.execute("UPDATE player_referrals SET status='qualified',qualified_at=now() WHERE id=$1",row['id'])
  return True

async def claim(inviter_id:int)->dict[str,int]:
 async with db.transaction() as conn:
  if await ledger_repo.lock_player(conn,inviter_id) is None:raise ValueError("player_not_found")
  # Lock referrals so concurrent clicks cannot claim the same friend or milestone twice.
  rows=await conn.fetch("SELECT id FROM player_referrals WHERE inviter_player_id=$1 AND status='qualified' ORDER BY id FOR UPDATE",inviter_id)
  qualified_total=int(await conn.fetchval("SELECT count(*) FROM player_referrals WHERE inviter_player_id=$1 AND status IN('qualified','rewarded')",inviter_id) or 0)
  paid=0;milestones=[]
  for milestone,reward in MILESTONES.items():
   if qualified_total<milestone:continue
   if await conn.fetchval("SELECT 1 FROM referral_milestone_rewards WHERE player_id=$1 AND milestone=$2",inviter_id,milestone):continue
   balance=await ledger_repo.change_player(conn,inviter_id,"IRT",reward)
   await ledger_repo.insert(conn,player_id=inviter_id,country_id=None,key=f"referral:{inviter_id}:{milestone}",reason="referral_milestone",asset="IRT",account="wallet",amount=reward,balance=balance,metadata={"milestone":milestone})
   await conn.execute("INSERT INTO referral_milestone_rewards(player_id,milestone,reward_toman) VALUES($1,$2,$3)",inviter_id,milestone,reward)
   paid+=reward;milestones.append(milestone)
  if rows:await conn.execute("UPDATE player_referrals SET status='rewarded',rewarded_at=now() WHERE inviter_player_id=$1 AND status='qualified'",inviter_id)
  return {"qualified":qualified_total,"paid":paid,"milestones":len(milestones)}

async def overview(player_id:int)->dict[str,int]:
 row=await db.fetchrow("""SELECT count(*) total,count(*) FILTER(WHERE status='pending') pending,
  count(*) FILTER(WHERE status IN('qualified','rewarded')) qualified FROM player_referrals WHERE inviter_player_id=$1""",player_id)
 claimed=int(await db.fetchval("SELECT COALESCE(max(milestone),0) FROM referral_milestone_rewards WHERE player_id=$1",player_id) or 0)
 q=int(row['qualified'] or 0);next_milestone=next((x for x in MILESTONES if x>q),50)
 claimable=bool(await db.fetchval("SELECT 1 FROM (SELECT unnest($2::int[]) milestone) m WHERE milestone<=$1 AND NOT EXISTS(SELECT 1 FROM referral_milestone_rewards r WHERE r.player_id=$3 AND r.milestone=m.milestone) LIMIT 1",q,list(MILESTONES),player_id))
 return {"total":int(row['total'] or 0),"pending":int(row['pending'] or 0),"qualified":q,"claimed":claimed,"next":next_milestone,"claimable":int(claimable)}
