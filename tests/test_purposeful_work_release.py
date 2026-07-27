from datetime import UTC,datetime,timedelta
from pathlib import Path
from packages.core.config import get_config
from packages.core.services.production import accrue,shift_modes

class R(dict):
    __getattr__=dict.__getitem__

def test_jobs_are_available_at_level_one_by_policy():
    assert get_config().int_("jobs.purpose_loop.available_from_level")==1

def test_shift_modes_are_balanced_and_bounded():
    modes=shift_modes();assert set(modes)=={"safe","balanced","national","private"}
    for spec in modes.values():
        assert 0<int(spec["player_percent"])<=100
        assert 0<=int(spec["country_percent"])<=100
        assert 0<int(spec["xp_percent"])<=200

def test_national_shift_contributes_more_than_private():
    modes=shift_modes();assert int(modes["national"]["country_percent"])>int(modes["private"]["country_percent"])
    assert int(modes["national"]["player_percent"])<int(modes["private"]["player_percent"])

def test_existing_accrual_behavior_is_preserved():
    now=datetime.now(UTC);row=R(job_code="farmer",production_level=1,storage_level=1,stored_amount=0,production_updated_at=now-timedelta(hours=2))
    result=accrue(row,now);assert result.stored==20 and result.capacity==60

def test_release_is_declared_done_and_migration_is_additive():
    assert Path("RELEASE_PURPOSEFUL_WORK_FA.md").exists()
    sql=Path("migrations/0015_purposeful_work_loop.sql").read_text()
    assert "DROP TABLE" not in sql and "work_claims" in sql and "IF NOT EXISTS" in sql
