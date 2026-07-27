"""Action-based career skills and useful personal assets for TeleLife."""
from __future__ import annotations
from dataclasses import dataclass
from math import floor
from typing import Any
import asyncpg
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo

@dataclass(frozen=True, slots=True)
class SkillProgress:
    code: str; level: int; xp: int; needed: int; total_xp: int; actions: int; title: str

@dataclass(frozen=True, slots=True)
class AssetView:
    code: str; title: str; owned: bool; available: bool; reason: str; cost: int
    maintenance: int; opportunity: str

def skill_required(level:int)->int:
    cfg=get_config()
    return max(1,int(cfg.int_("life_progression.skills.base_xp")*(level**cfg.float_("life_progression.skills.exponent"))))

def skill_title(level:int)->str:
    titles=get_config().section("life_progression.skills.titles")
    eligible=[(int(k),str(v)) for k,v in titles.items() if int(k)<=level]
    return max(eligible,key=lambda item:item[0])[1] if eligible else "تازه‌کار"

def skill_for_job(job_code:str)->str:
    return str(get_config().get(f"life_progression.skills.jobs.{job_code}"))

def apply_skill_levels(level:int,xp:int)->tuple[int,int]:
    top=get_config().int_("life_progression.skills.max_level")
    while level<top and xp>=skill_required(level):
        xp-=skill_required(level);level+=1
    return level,xp

async def record_work(conn:asyncpg.Connection,player_id:int,job_code:str,key:str,fraction:float)->SkillProgress:
    code=skill_for_job(job_code)
    await conn.execute("""INSERT INTO player_skills(player_id,skill_code) VALUES($1,$2)
      ON CONFLICT DO NOTHING""",player_id,code)
    row=await conn.fetchrow("SELECT * FROM player_skills WHERE player_id=$1 AND skill_code=$2 FOR UPDATE",player_id,code)
    duplicate=await conn.fetchval("SELECT 1 FROM skill_events WHERE idempotency_key=$1",key)
    level=int(row["level"]);current=int(row["xp"])
    if duplicate:return SkillProgress(code,level,current,skill_required(level),int(row["total_xp"]),int(row["actions_count"]),skill_title(level))
    # Asset configuration is application-owned; only owned codes are read from DB.
    owned=[str(r["asset_code"]) for r in await conn.fetch("SELECT asset_code FROM player_assets WHERE player_id=$1",player_id)]
    specs=get_config().section("life_progression.assets")
    bonus=sum(int(specs[c].get("skill_xp_bonus_bp",0)) for c in owned if c in specs)
    base=get_config().int_("life_progression.skills.work_xp_at_full_capacity")
    amount=max(1,floor(base*max(0.05,min(1.5,fraction))*(10000+min(2500,bonus))/10000))
    after,remaining=apply_skill_levels(level,current+amount)
    await conn.execute("""UPDATE player_skills SET level=$3,xp=$4,total_xp=total_xp+$5,
      actions_count=actions_count+1,updated_at=now() WHERE player_id=$1 AND skill_code=$2""",player_id,code,after,remaining,amount)
    await conn.execute("""INSERT INTO skill_events(idempotency_key,player_id,skill_code,amount,level_after,source)
      VALUES($1,$2,$3,$4,$5,'work_claim')""",key,player_id,code,amount,after)
    return SkillProgress(code,after,remaining,skill_required(after),int(row["total_xp"])+amount,int(row["actions_count"])+1,skill_title(after))

async def primary_skill(player_id:int)->SkillProgress|None:
    row=await db.fetchrow("""SELECT * FROM player_skills WHERE player_id=$1
      ORDER BY level DESC,total_xp DESC,skill_code LIMIT 1""",player_id)
    if not row:return None
    level=int(row["level"])
    return SkillProgress(str(row["skill_code"]),level,int(row["xp"]),skill_required(level),int(row["total_xp"]),int(row["actions_count"]),skill_title(level))

async def asset_bonus_bp(conn:asyncpg.Connection,player_id:int,field:str)->int:
    if field not in {"work_bonus_bp","skill_xp_bonus_bp"}:raise ValueError("invalid_asset_bonus")
    owned=[str(r["asset_code"]) for r in await conn.fetch("SELECT asset_code FROM player_assets WHERE player_id=$1",player_id)]
    specs=get_config().section("life_progression.assets")
    return min(2500,sum(int(specs[c].get(field,0)) for c in owned if c in specs))

async def assets_view(player_id:int)->list[AssetView]:
    player=await db.fetchrow("SELECT level FROM players WHERE id=$1",player_id)
    if not player:raise ValueError("player_not_found")
    owned={str(r["asset_code"]) for r in await db.fetch("SELECT asset_code FROM player_assets WHERE player_id=$1",player_id)}
    skill=await primary_skill(player_id);skill_level=skill.level if skill else 1
    result=[]
    for code,spec in get_config().section("life_progression.assets").items():
        min_level=int(spec["min_level"]);min_skill=int(spec.get("min_skill_level",1));is_owned=str(code) in owned
        available=int(player["level"])>=min_level and skill_level>=min_skill
        reason="خریده شده" if is_owned else "آماده خرید" if available else f"نیازمند سطح {min_level}"+(f" و مهارت {min_skill}" if min_skill>1 else "")
        result.append(AssetView(str(code),str(spec["title"]),is_owned,available,reason,int(spec["cost_toman"]),int(spec["maintenance_daily_toman"]),str(spec["opportunity"])))
    return result

async def buy_asset(player_id:int,code:str,key:str)->bool:
    specs=get_config().section("life_progression.assets")
    if code not in specs:raise ValueError("invalid_asset")
    spec=specs[code]
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if not player:raise ValueError("player_not_found")
        if await conn.fetchval("SELECT 1 FROM player_assets WHERE player_id=$1 AND asset_code=$2",player_id,code):raise ValueError("asset_owned")
        skill=await conn.fetchrow("SELECT level FROM player_skills WHERE player_id=$1 ORDER BY level DESC LIMIT 1",player_id)
        if int(player["level"])<int(spec["min_level"]) or int(skill["level"] if skill else 1)<int(spec.get("min_skill_level",1)):raise ValueError("asset_locked")
        cost=int(spec["cost_toman"]);balance=await ledger_repo.change_player(conn,player_id,"IRT",-cost)
        await conn.execute("INSERT INTO player_assets(player_id,asset_code,purchase_price_toman) VALUES($1,$2,$3)",player_id,code,cost)
        ok=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason="personal_asset_purchase",asset="IRT",account="wallet",amount=-cost,balance=balance,metadata={"asset":code})
        if not ok:raise RuntimeError("asset_ledger_conflict")
        rep=int(spec.get("reputation_bonus",0));happy=int(spec.get("happiness_bonus",0))
        await conn.execute("UPDATE players SET reputation=reputation+$2,happiness=LEAST(100,happiness+$3) WHERE id=$1",player_id,rep,happy)
        return True