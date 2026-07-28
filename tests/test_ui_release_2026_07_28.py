"""Contracts for the 2026-07-28 UI and copy release."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_every_fa_key_used_by_the_bot_exists():
    import re

    fa = read("apps/telelife_bot/texts/fa.py")
    defined = set(re.findall(r"^(\w+)\s*=", fa, re.M))
    for path in (ROOT / "apps/telelife_bot").rglob("*.py"):
        for key in re.findall(r"fa\.([A-Z_0-9]+)", path.read_text(encoding="utf-8")):
            assert key in defined, f"{key} missing for {path}"


def test_dead_legacy_handlers_are_gone():
    for name in ("start.py", "progression.py", "economy_ui.py", "profile.py"):
        assert not (ROOT / "apps/telelife_bot/handlers" / name).exists()
    assert not (ROOT / "apps/telelife_bot/views").exists()


def test_copy_uses_the_shared_visual_rhythm():
    fa = read("apps/telelife_bot/texts/fa.py")
    assert "RULE = " in fa and "SOFT = " in fa
    for key in ("HOME", "PROFILE", "ECONOMY", "MISSIONS", "UNLOCKS"):
        assert key in fa


def test_keyboards_use_one_colour_language():
    kbd = read("apps/telelife_bot/keyboards/main.py")
    for token in ("NAV =", "MONEY =", "SPEND =", "GROW =", "def _footer("):
        assert token in kbd
    assert "HOME_LABEL" in kbd


def test_migrator_ignores_line_ending_noise():
    from packages.core.db import migrator

    assert migrator._checksum("A;\r\nB;\r\n") == migrator._checksum("A;\nB;\n")
    assert migrator.RECOVERED_BASELINE_END == "0027_production_integrity_hardening"


def test_migration_0028_is_additive_and_repeatable():
    sql = read("migrations/0028_ui_release_hardening.sql").upper()
    assert "DROP " not in sql and "TRUNCATE" not in sql
    assert sql.count("CREATE INDEX IF NOT EXISTS") == 4
