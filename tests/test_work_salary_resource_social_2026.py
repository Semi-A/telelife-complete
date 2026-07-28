"""Contracts for wages, resource sales and group resource interaction."""
from datetime import UTC,datetime,timedelta
from pathlib import Path
from packages.core.config import get_config
from packages.core.services.production import accrue
from packages.core.services.resource_economy import ASSETS,spec

class R(dict):
 __getattr__=dict.__getitem__

def test_every_resource_job_has_a_cash_wage():
 jobs=get_config().section("jobs.jobs")
 for job in jobs.values():
  asset=str(job["output_asset"])
  if asset!="IRT":assert int(spec(asset)["wage_toman_per_unit"])>0

def test_resource_sale_price_is_below_wage_and_positive():
 for asset in ASSETS:
  item=spec(asset)
  assert 0<int(item["sell_toman_per_unit"])<int(item["wage_toman_per_unit"])

def test_resource_jobs_still_accrue_resources():
 now=datetime.now(UTC);row=R(job_code="farmer",production_level=1,storage_level=1,stored_amount=0,production_updated_at=now-timedelta(hours=2))
 assert accrue(row,now).stored==20

def test_salary_and_resource_ledger_legs_are_atomic_in_service():
 source=Path("packages/core/services/production.py").read_text()
 assert 'reason="work_cash_salary"' in source
 assert 'salary_net_toman' in source
 assert 'asset!=\'IRT\'' in source

def test_social_resource_schema_and_routes_exist():
 sql=Path("migrations/0024_work_salary_resource_social.sql").read_text()
 world=Path("apps/teleworld_bot/handlers/world.py").read_text()
 service=Path("packages/core/services/resource_economy.py").read_text()
 for table in ("citizen_resource_transfers","player_resource_sales"):assert table in sql
 for action in ("rgift:","rdonate:"):assert action in world
 assert "same_country_required" in service
 assert "daily_gift_units" in service

def test_life_explains_cash_and_resources_separately():
 source=Path("apps/telelife_bot/handlers/life.py").read_text()
 assert "حقوق نقدی" in source
 assert "منبع ذخیره‌شده" in source
 assert "منابع و فروش" in Path("apps/telelife_bot/keyboards/main.py").read_text()