from pathlib import Path


def test_recovered_history_ends_at_0026_and_0027_is_strict():
    source = Path("packages/core/db/migrator.py").read_text(encoding="utf-8")
    assert 'RECOVERED_BASELINE_END = "0026_referral_growth"' in source
    assert 'STRICT_CHECKSUM_FROM = "0027_"' in source
    assert "Create a new migration instead of editing history" in source


def test_free_tier_migration_still_exists():
    assert Path("migrations/0014_free_tier_hardening.sql").is_file()
