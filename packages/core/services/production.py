"""Capacity-capped lazy production with proportional anti-farm XP."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import UTC,datetime
from math import floor
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo,production_repo
from packages.core.services import xp
@dataclass(frozen=True,slots=True)
class Accrual:stored:int;capacity:int;rate:float

def accrue(row,at:datetime)->Accrual:
 cfg=get_config();job=cfg.section(f"jobs.jobs.{row['job_code']}");rate=float(job['base_rate_per_hour'])*(1+(int(row['production_level'])-1)*cfg.float_('jobs.production.production_multiplier_per_level'))
 hours=max(0.0,(at-row['production_updated_at']).total_seconds()/cfg.int_('jobs.production.time_unit_seconds'));cap=floor(rate*cfg.int_(f"jobs.storage.levels.{row['storage_level']}.capacity_hours"));stored=min(cap,int(row['stored_amount'])+floor(rate*hours));return Accrual(stored,cap,rate)
async def choose(player_id:int,job:str)->bool:
 jobs=get_config().section('jobs.jobs');
 if job not in jobs:raise ValueError('invalid_job')
 return await production_repo.choose(player_id,job,str(jobs[job]['output_asset']))
async def collect(player_id:int,key:str,at:datetime|None=None)->tuple[int,int]:
 now=at or datetime.now(UTC)
 async with db.transaction() as conn:
  row=await production_repo.lock(conn,player_id)
  if not row:raise ValueError('job_not_found')
  a=accrue(row,now);amount=a.stored
  if amount<get_config().int_('jobs.production.minimum_collection_amount'):return 0,0
  if await ledger_repo.idempotency_exists(conn,key):return 0,0
  balance=await ledger_repo.change_player(conn,player_id,row['output_asset_code'],amount)
  if not await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason='production_collect',asset=row['output_asset_code'],account='wallet' if row['output_asset_code']=='IRT' else 'inventory',amount=amount,balance=balance):return 0,0
  await production_repo.clear(conn,player_id,now)
 fraction=amount/a.capacity if a.capacity else 0;minimum=get_config().float_('jobs.production.minimum_collection_fraction_for_xp');award=floor(get_config().int_('jobs.production.collection_xp_at_full_capacity')*fraction) if fraction>=minimum else 0
 if award:await xp.grant(player_id,'production_collect',idempotency_key=key+':xp',amount=award)
 return amount,award
async def upgrade(player_id:int,kind:str,key:str,at:datetime|None=None)->int:
 if kind not in {'storage','production'}:raise ValueError('invalid_upgrade')
 now=at or datetime.now(UTC);cfg=get_config()
 async with db.transaction() as conn:
  row=await production_repo.lock(conn,player_id)
  if not row:raise ValueError('job_not_found')
  a=accrue(row,now);await production_repo.checkpoint(conn,player_id,a.stored,now)
  current=int(row[f'{kind}_level']);target=current+1;cost=cfg.int_(f"jobs.{kind if kind=='storage' else 'production_levels'}.upgrade_cost_toman.{target}")
  if await ledger_repo.idempotency_exists(conn,key):return current
  balance=await ledger_repo.change_player(conn,player_id,'IRT',-cost);await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason=f'{kind}_upgrade',asset='IRT',account='wallet',amount=-cost,balance=balance)
  await production_repo.level_up(conn,player_id,kind);return target
