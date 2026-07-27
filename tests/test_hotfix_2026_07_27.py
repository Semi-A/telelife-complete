from pathlib import Path

from packages.core.config.loader import GameConfig
from packages.core.services.country_identity import masthead


def test_game_config_has_existing_and_missing_paths():
    cfg = GameConfig({"jobs": {"levels": {2: 100}}})
    assert cfg.has("jobs.levels.2")
    assert not cfg.has("jobs.levels.3")


def test_news_masthead_has_balanced_html_and_requested_titles():
    text = masthead("خاخام", "متن خبر")
    assert text.startswith("🏛 <b>خبرگزاری حکومت خاخام</b>")
    assert "📊 <b>خلاصه امروز حکومت خاخام</b>" in text
    assert text.count("<b>") == text.count("</b>") == 2
    assert "b><" not in text


def test_start_limit_and_panel_timeout_are_wired():
    life = Path("apps/telelife_bot/handlers/life.py").read_text()
    world = Path("apps/teleworld_bot/handlers/world.py").read_text()
    config = Path("packages/core/config/data/core.yaml").read_text()
    assert "CommandHandler('start',start)" in life
    assert 'CommandHandler("start", start)' in world
    assert "allow_start" in life and "allow_start" in world
    assert "default_timeout_seconds: 60" in config
    assert "schedule_cleanup" in Path("apps/telelife_bot/handlers/panel.py").read_text()
    assert "schedule_cleanup" in world


def test_existing_citizen_gets_actionable_panel():
    world = Path("apps/teleworld_bot/handlers/world.py").read_text()
    keyboard = Path("apps/teleworld_bot/keyboards.py").read_text()
    assert "kb.citizenship_elsewhere()" in world
    assert 'action == "citizenship_cancel_confirm"' in world
    assert "def citizenship_cancel_confirm" in keyboard