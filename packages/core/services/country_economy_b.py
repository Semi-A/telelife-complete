"""Release B country economy rules: deterministic, bounded and retry-safe."""
from __future__ import annotations
from datetime import date, timedelta
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

SECTORS=("welfare","production","technology","defense","intelligence","diplomacy","emergency")
ROLES={"economy_minister","industry_minister","foreign_minister","army_commander","intelligence_chief"}

from packages.core.services.country_economy_rules import DailyPlan, calculate_daily, shortage_bp

async def _budget(conn,country_id:int):
 row=await conn.fetchrow("SELECT * FROM country_budget_allocations WHERE country_id=$1",country_id)
 if row:return {s:int(row[f"{s}_bp"]) for s in SECTORS}
 spec=get_config().section("country_economy_b.budget.presets.balanced")
 await conn.execute("INSERT INTO country_budget_allocations(country_id) VALUES($1) ON CONFLICT DO NOTHING",country_id)
 return {s:int(spec[s]) for s in SECTORS}

async def _resource(conn,country_id:int,asset:str)->int:
 return int(await conn.fetchval("SELECT quantity FROM country_resources WHERE country_id=$1 AND asset_code=$2 FOR UPDATE",country_id,asset) or 0)

async def settle_day(country_id:int,day:date)->bool:
 key=f"country-release-b:{country_id}:{day}"
 async with db.transaction() as conn:
  country=await ledger_repo.lock_country(conn,country_id)
  if not country:return False
  if await conn.fetchval("SELECT 1 FROM country_resource_daily WHERE country_id=$1 AND economy_date=$2",country_id,day):return False
  state=await conn.fetchrow("SELECT * FROM country_economy_state WHERE country_id=$1 FOR UPDATE",country_id)
  if not state:
   await conn.execute("INSERT INTO country_economy_state(country_id) VALUES($1) ON CONFLICT DO NOTHING",country_id)
   state=await conn.fetchrow("SELECT * FROM country_economy_state WHERE country_id=$1 FOR UPDATE",country_id)
  budget=await _budget(conn,country_id)
  citizens=int(await conn.fetchval("SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active",country_id) or 0)
  food=await _resource(conn,country_id,"food");energy=await _resource(conn,country_id,"energy")
  projects=int(await conn.fetchval("SELECT count(*) FROM national_projects WHERE country_id=$1 AND status='completed'",country_id) or 0)
  plan=calculate_daily(citizens=citizens,food=food,energy=energy,treasury=int(country["treasury_toman"]),satisfaction=int(state["satisfaction"]),budget=budget,completed_projects=projects)
  # The daily row is the idempotency claim. Insert it first so a retry can never
  # spend resources twice; a concurrent loser rolls back without side effects.
  claimed=await conn.fetchval("""INSERT INTO country_resource_daily(country_id,economy_date,citizens,food_needed,food_consumed,energy_needed,energy_consumed,budget_spent_toman,satisfaction_before,satisfaction_after,production_modifier_bp,ledger_key,details) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13) ON CONFLICT(country_id,economy_date) DO NOTHING RETURNING country_id""",country_id,day,citizens,plan.food_needed,plan.food_used,plan.energy_needed,plan.energy_used,plan.budget_spend,int(state["satisfaction"]),plan.satisfaction,plan.production_modifier_bp,key,{"budget":budget})
  if not claimed:return False
  for asset,amount in (("food",plan.food_used),("energy",plan.energy_used)):
   if amount:
    balance=await ledger_repo.change_country(conn,country_id,asset,-amount)
    await ledger_repo.insert(conn,player_id=None,country_id=country_id,key=f"{key}:{asset}",reason="country_daily_consumption",asset=asset,account=ledger_repo.country_account(asset),amount=-amount,balance=balance,metadata={"date":str(day)})
  if plan.budget_spend:
   balance=await ledger_repo.change_country(conn,country_id,"IRT",-plan.budget_spend)
   await ledger_repo.insert(conn,player_id=None,country_id=country_id,key=f"{key}:budget",reason="country_daily_budget",asset="IRT",account="treasury",amount=-plan.budget_spend,balance=balance,metadata={"date":str(day),"allocations":budget})
  await conn.execute("""UPDATE country_economy_state SET satisfaction=$2,food_shortage_bp=$3,energy_shortage_bp=$4,production_modifier_bp=$5,welfare_level=$6,defense_readiness=$7,last_settled_date=$8,updated_at=now() WHERE country_id=$1""",country_id,plan.satisfaction,plan.food_shortage_bp,plan.energy_shortage_bp,plan.production_modifier_bp,plan.welfare,plan.defense,day)
  trigger=get_config().int_("country_economy_b.crisis.shortage_trigger_bp");resolve=get_config().int_("country_economy_b.crisis.shortage_resolve_bp")
  for code,severity in (("food_shortage",plan.food_shortage_bp),("energy_shortage",plan.energy_shortage_bp)):
   if severity>=trigger:
    await conn.execute("""INSERT INTO country_crises(country_id,crisis_code,severity,started_on,details) VALUES($1,$2,$3,$4,$5) ON CONFLICT(country_id,crisis_code) WHERE status='active' DO UPDATE SET severity=EXCLUDED.severity,details=EXCLUDED.details,updated_at=now()""",country_id,code,max(1,severity//100),day,{"shortage_bp":severity})
   elif severity<=resolve:
    await conn.execute("UPDATE country_crises SET status='resolved',resolved_on=$3,updated_at=now() WHERE country_id=$1 AND crisis_code=$2 AND status='active'",country_id,code,day)
  return True

async def catch_up(today:date|None=None)->int:
 end=today or clock.game_today();days=get_config().int_("economy.country.catch_up_days");rows=await db.fetch("SELECT id FROM countries ORDER BY id");done=0
 for row in rows:
  for offset in range(days-1,-1,-1):done+=bool(await settle_day(int(row["id"]),end-timedelta(days=offset)))
 return done

async def view(country_id:int):
 return await db.fetchrow("""SELECT c.treasury_toman,s.*,b.*,
 (SELECT count(*) FROM country_crises x WHERE x.country_id=c.id AND x.status='active') active_crises
 FROM countries c LEFT JOIN country_economy_state s ON s.country_id=c.id LEFT JOIN country_budget_allocations b ON b.country_id=c.id WHERE c.id=$1""",country_id)

async def set_budget_preset(country_id:int,actor_id:int,preset:str,key:str)->bool:
 presets=get_config().section("country_economy_b.budget.presets")
 if preset not in presets:raise ValueError("invalid_budget_preset")
 spec=presets[preset]
 async with db.transaction() as conn:
  country=await ledger_repo.lock_country(conn,country_id)
  allowed=country and (int(country["president_player_id"] or 0)==actor_id or await conn.fetchval("SELECT 1 FROM country_offices WHERE country_id=$1 AND player_id=$2 AND role_code='economy_minister'",country_id,actor_id))
  if not allowed:raise PermissionError("budget_permission_required")
  inserted=await conn.fetchval("INSERT INTO country_governance_audit(country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,'budget_preset',$3,$4) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",country_id,actor_id,key,{"preset":preset})
  if not inserted:return False
  await conn.execute("""INSERT INTO country_budget_allocations(country_id,welfare_bp,production_bp,technology_bp,defense_bp,intelligence_bp,diplomacy_bp,emergency_bp,updated_by_player_id) VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9) ON CONFLICT(country_id) DO UPDATE SET welfare_bp=EXCLUDED.welfare_bp,production_bp=EXCLUDED.production_bp,technology_bp=EXCLUDED.technology_bp,defense_bp=EXCLUDED.defense_bp,intelligence_bp=EXCLUDED.intelligence_bp,diplomacy_bp=EXCLUDED.diplomacy_bp,emergency_bp=EXCLUDED.emergency_bp,version=country_budget_allocations.version+1,updated_by_player_id=EXCLUDED.updated_by_player_id,updated_at=now()""",country_id,*[int(spec[s]) for s in SECTORS],actor_id)
  return True

async def appoint(country_id:int,president_id:int,role:str,player_id:int,key:str)->bool:
 if role not in ROLES:raise ValueError("invalid_role")
 async with db.transaction() as conn:
  country=await ledger_repo.lock_country(conn,country_id)
  if not country or int(country["president_player_id"] or 0)!=president_id:raise PermissionError("president_required")
  if not await conn.fetchval("SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2 AND is_active",country_id,player_id):raise ValueError("citizen_required")
  inserted=await conn.fetchval("INSERT INTO country_governance_audit(country_id,actor_player_id,action_code,idempotency_key,payload) VALUES($1,$2,'appoint_office',$3,$4) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id",country_id,president_id,key,{"role":role,"player_id":player_id})
  if not inserted:return False
  await conn.execute("DELETE FROM country_offices WHERE country_id=$1 AND player_id=$2",country_id,player_id)
  await conn.execute("""INSERT INTO country_offices(country_id,role_code,player_id,appointed_by_player_id) VALUES($1,$2,$3,$4) ON CONFLICT(country_id,role_code) DO UPDATE SET player_id=EXCLUDED.player_id,appointed_by_player_id=EXCLUDED.appointed_by_player_id,updated_at=now()""",country_id,role,player_id,president_id)
  return True
