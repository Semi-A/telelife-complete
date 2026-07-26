"""Idempotent daily country income/expense settlement."""
from __future__ import annotations
from datetime import UTC,date,datetime,timedelta
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
async def settle_day(country_id:int,day:date)->bool:
 key=f"country-economy:{country_id}:{day}"
 async with db.transaction() as conn:
  if await ledger_repo.idempotency_exists(conn,key):return False
  row=await ledger_repo.lock_country(conn,country_id)
  if not row:return False
  cfg=get_config();income=int(row["daily_income_toman"])+cfg.int_("economy.country.daily_base_income_toman");expense=int(row["daily_expense_toman"])+cfg.int_("economy.country.daily_base_expense_toman");delta=income-expense
  if delta<0:delta=max(delta,-int(row["treasury_toman"]))
  balance=await ledger_repo.change_country(conn,country_id,"IRT",delta)
  await ledger_repo.insert(conn,player_id=None,country_id=country_id,key=key,reason="country_daily_economy",asset="IRT",account="treasury",amount=delta,balance=balance,metadata={"date":str(day),"income":income,"expense":expense})
  await conn.execute("INSERT INTO country_economy_daily(country_id,economy_date,income_toman,expense_toman,closing_treasury,ledger_key) VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING",country_id,day,income,expense,balance,key);return True
async def catch_up(today:date|None=None)->int:
 end=today or datetime.now(UTC).date();days=get_config().int_("economy.country.catch_up_days");rows=await db.fetch("SELECT id FROM countries");done=0
 for row in rows:
  for offset in range(days-1,-1,-1):done+=int(await settle_day(int(row["id"]),end-timedelta(days=offset)))
 return done
