from packages.core.db import migrator


def test_migrations_discovered_and_ordered():
    names = [path.name for path in migrator.discover()]
    assert names and names == sorted(names)
    assert names[0].startswith("0001")
    assert names[-1].startswith("0027")


def test_checksum_is_stable():
    assert migrator._checksum("SELECT 1;") == migrator._checksum("SELECT 1;")
    assert len(migrator._checksum("SELECT 1;")) == 16


def test_recovered_history_ends_before_new_strict_migrations():
    assert migrator.RECOVERED_BASELINE_END == "0026_referral_growth"
    assert migrator.STRICT_CHECKSUM_FROM == "0027_"
    assert migrator._is_recovered_history("0023_country_social_life")
    assert not migrator._is_recovered_history("0027_production_integrity_hardening")


def test_applied_new_migrations_remain_immutable():
    source = migrator.Path(migrator.__file__).read_text(encoding="utf-8")
    assert "Create a new migration instead of editing history" in source
    assert "await conn.execute(sql)" in source
