from pathlib import Path

def test_onboarding_has_welcome_wizard_and_navigation() -> None:
    code=Path("apps/teleworld_bot/handlers/onboarding.py").read_text()
    assert "ChatMemberHandler" in code
    assert 'FLOW_KEY="tw_country_flow"' in code
    assert 'action=="create"' in code
    assert 'flow["step"]="government"' in code
    assert 'flow["step"]="description"' in code
    assert 'CommandHandler("menu",start)' in code

def test_world_keyboard_has_glass_navigation() -> None:
    code=Path("apps/teleworld_bot/keyboards.py").read_text()
    assert "InlineKeyboardMarkup" in code
    assert "ساخت کشور" in code
    assert "شغل و تولید" in code
    assert "سیاست" in code
