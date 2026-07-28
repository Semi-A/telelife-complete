from pathlib import Path
from packages.core.config import get_config
from packages.core.services.life_progression import apply_skill_levels,skill_required


def test_skill_curve_is_monotonic_and_bounded():
    values=[skill_required(i) for i in range(1,20)]
    assert values==sorted(values) and all(v>0 for v in values)
    level,xp=apply_skill_levels(1,10**9)
    assert level==get_config().int_("life_progression.skills.max_level") and xp>=0


def test_every_job_maps_to_one_skill():
    cfg=get_config()
    assert set(cfg.section("jobs.jobs"))==set(cfg.section("life_progression.skills.jobs"))


def test_assets_have_real_cost_effect_and_gate():
    for spec in get_config().section("life_progression.assets").values():
        assert int(spec["cost_toman"])>0
        assert int(spec["maintenance_daily_toman"])>=0
        assert int(spec["min_level"])>=1
        assert str(spec["opportunity"]).strip()
        assert int(spec["work_bonus_bp"]) or int(spec["skill_xp_bonus_bp"])


def test_work_unlock_matches_runtime_policy():
    cfg=get_config()
    unlock=cfg.section("unlocks.levels")[1]
    assert unlock["key"]=="jobs_basic"
    assert cfg.int_("jobs.purpose_loop.available_from_level")==1


def test_migration_is_additive():
    sql=Path("migrations/0019_life_progression_system.sql").read_text()
    assert "DROP TABLE" not in sql and "IF NOT EXISTS" in sql
    assert "player_skills" in sql and "player_assets" in sql and "skill_events" in sql