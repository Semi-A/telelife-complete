from packages.core.db import migrator


def test_migrations_discovered_and_ordered():
    names = [path.name for path in migrator.discover()]
    assert names and names == sorted(names)
    assert names[0].startswith("0001")
    assert names[-1].startswith("0028")


def test_checksum_is_stable():
    assert migrator._checksum("SELECT 1;") == migrator._checksum("SELECT 1;")
    assert len(migrator._checksum("SELECT 1;")) == 16


def test_recovered_history_ends_before_new_strict_migrations():
    assert migrator.RECOVERED_BASELINE_END == "0027_production_integrity_hardening"
    assert migrator.STRICT_CHECKSUM_FROM == "0028_"
    assert migrator._is_recovered_history("0023_country_social_life")
    assert migrator._is_recovered_history("0027_production_integrity_hardening")
    assert not migrator._is_recovered_history("0028_ui_release_hardening")


def test_line_endings_do_not_change_a_checksum():
    assert migrator._checksum("SELECT 1;\r\nSELECT 2;\r\n") == migrator._checksum(
        "SELECT 1;\nSELECT 2;\n"
    )


def test_applied_new_migrations_remain_immutable():
    source = migrator.Path(migrator.__file__).read_text(encoding="utf-8")
    assert "Create a new migration instead of editing history" in source
    assert "await conn.execute(sql)" in source
