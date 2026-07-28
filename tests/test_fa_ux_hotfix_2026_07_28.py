"""Regression contracts for the Persian UX hotfix."""
from pathlib import Path

from packages.core.services.news import daily_event_text
from packages.core.utils.fa_labels import GOVERNMENT_NAMES, government_name


def test_all_government_codes_have_persian_labels():
    codes = {
        line.strip()[2:]
        for line in Path("packages/core/config/data/country.yaml").read_text().splitlines()
        if line.startswith("  - ")
    }
    assert codes <= GOVERNMENT_NAMES.keys()
    assert government_name("monarchy") == "پادشاهی مطلقه"
    assert not any(value.isascii() for value in GOVERNMENT_NAMES.values())


def test_market_day_is_a_clear_persian_news_message():
    text = daily_event_text("market_day")
    assert "market_day" not in text
    assert "روز پررونق بازار" in text
    assert "۱۰٪" in text and "۲۴ ساعت" in text


def test_closed_panels_change_the_message_text():
    shared = Path("packages/core/ui/panels.py").read_text()
    life = Path("apps/telelife_bot/handlers/panel.py").read_text()
    world = Path("apps/teleworld_bot/handlers/world.py").read_text()
    assert 'text="🔒 بسته شد"' in shared
    assert 'text="🔒 بسته شد"' in life
    assert 'text="🔒 بسته شد"' in world


def test_world_has_slash_free_explicit_group_triggers():
    world = Path("apps/teleworld_bot/handlers/world.py").read_text()
    for trigger in ("تله ورلد", "تله‌ورلد", "پنل جهان"):
        assert trigger in world


def test_today_keyboard_avoids_duplicate_primary_styles():
    source = Path("apps/telelife_bot/keyboards/main.py").read_text()
    assert "primary_used=False" in source
    assert "elif not primary_used" in source