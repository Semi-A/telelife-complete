"""Admin mutations and append-only audit writes."""
from __future__ import annotations
from typing import Any
import asyncpg
from packages.core import db
async def audit(conn:asyncpg.Connection,actor:str,action:str,request_id:str,details:dict[str,Any],player_id:int|None=None,country_id:int|None=None)->bool:
 return await conn.fetchval("INSERT INTO admin_audit_log(admin_actor,action,target_player_id,target_country_id,request_id,details) VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING id",actor,action,player_id,country_id,request_id,details) is not None
async def set_ban(conn:asyncpg.Connection,player_id:int,banned:bool,reason:str|None)->None:await conn.execute("UPDATE players SET is_banned=$2,ban_reason=$3 WHERE id=$1",player_id,banned,reason)
async def set_flag(conn:asyncpg.Connection,key:str,enabled:bool,actor:str)->None:await conn.execute("INSERT INTO feature_flags(key,enabled,updated_by) VALUES($1,$2,$3) ON CONFLICT(key) DO UPDATE SET enabled=$2,updated_by=$3,updated_at=now()",key,enabled,actor)
async def stats()->asyncpg.Record|None:return await db.fetchrow("SELECT (SELECT count(*) FROM players) players,(SELECT count(*) FROM countries) countries,(SELECT count(*) FROM citizenships) citizens")
async def users(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT id,telegram_id,first_name,level,xp,is_banned FROM players ORDER BY created_at DESC LIMIT $1",limit)
async def countries(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT id,name,government_type,treasury_toman,created_at FROM countries ORDER BY created_at DESC LIMIT $1",limit)
async def audits(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT * FROM admin_audit_log ORDER BY created_at DESC LIMIT $1",limit)
