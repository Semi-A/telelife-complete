from datetime import UTC,datetime,timedelta
from packages.core.services.production import accrue
class R(dict):
 __getattr__=dict.__getitem__
def row(at,level=1,storage=1,stored=0):return R(job_code='farmer',production_level=level,storage_level=storage,stored_amount=stored,production_updated_at=at)
def test_lazy_accrual_is_capacity_capped():
 now=datetime.now(UTC);a=accrue(row(now-timedelta(days=5)),now);assert a.stored==a.capacity
def test_old_level_accrual_can_be_checkpointed_before_upgrade():
 now=datetime.now(UTC);old=accrue(row(now-timedelta(hours=3),level=1),now);new=accrue(row(now,level=2,stored=old.stored),now);assert old.stored==30;assert new.stored==30