"""Source contracts for the no-cost hardening release."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def text(path:str)->str:return (ROOT/path).read_text(encoding="utf-8")

def test_recovered_history_ends_at_0014_and_0015_is_strict():
    source=text("packages/core/db/migrator.py")
    legacy=source.split("LEGACY_CHECKSUM_VERSIONS = frozenset({",1)[1].split("})",1)[0]
    assert '"0013_country_identity_candles_realism"' in legacy
    assert '"0014_free_tier_hardening"' in legacy
    assert '"0015_purposeful_work_loop"' not in legacy
    assert "Create a new migration instead of editing history" in source

def test_admin_telegram_calls_use_transactional_outbox():
    router=text("apps/admin/routers/country_admin.py")
    commerce=text("packages/core/services/commerce.py")
    assert "send_invoice(" not in router
    assert "send_message(" not in router
    assert "action_outbox_repo.enqueue" in commerce
    assert "async with db.transaction() as conn" in commerce

def test_admin_mutations_are_json_only():
    app=text("apps/admin/main.py")
    router=text("apps/admin/routers/country_admin.py")
    assert 'content_type != "application/json"' in app
    assert "Form(" not in router

def test_free_tier_jobs_are_bounded():
    maintenance=text("packages/core/services/maintenance.py")
    assert "LIMIT 200" in maintenance
    assert "interval '30 days'" in maintenance
    scheduler=text("apps/scheduler/main.py")
    assert '"telegram_actions"' in scheduler and '"maintenance"' in scheduler
