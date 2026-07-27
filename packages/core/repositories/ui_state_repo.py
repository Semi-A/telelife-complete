"""Persistent panel locations and onboarding state."""
from __future__ import annotations
from packages.core import db

async def life(player_id:int):
 return await db.fetchrow("SELECT * FROM player_ui_state WHERE player_id=$1",player_id)
async def ensure_life(player_id:int):
 await db.execute("INSERT INTO player_ui_state(player_id) VALUES($1) ON CONFLICT DO NOTHING",player_id)
 return await life(player_id)
async def set_life_panel(player_id:int,chat_id:int,message_id:int)->None:
 await db.execute("""INSERT INTO player_ui_state(player_id,life_chat_id,life_message_id,life_expires_at) VALUES($1,$2,$3,now()+interval '60 seconds')
 ON CONFLICT(player_id) DO UPDATE SET life_chat_id=$2,life_message_id=$3,life_expires_at=now()+interval '60 seconds',updated_at=now()""",player_id,chat_id,message_id)
async def set_step(player_id:int,step:int)->None:
 await db.execute("""UPDATE player_ui_state SET onboarding_step=GREATEST(onboarding_step,$2),
 onboarding_completed_at=CASE WHEN $2>=4 THEN COALESCE(onboarding_completed_at,now()) ELSE onboarding_completed_at END,updated_at=now() WHERE player_id=$1""",player_id,step)
async def world(chat_id:int):return await db.fetchrow("SELECT * FROM world_ui_state WHERE chat_id=$1",chat_id)
async def set_world(chat_id:int,message_id:int)->None:
 await db.execute("""INSERT INTO world_ui_state(chat_id,message_id,expires_at) VALUES($1,$2,now()+interval '60 seconds')
 ON CONFLICT(chat_id) DO UPDATE SET message_id=$2,expires_at=now()+interval '60 seconds',updated_at=now()""",chat_id,message_id)
