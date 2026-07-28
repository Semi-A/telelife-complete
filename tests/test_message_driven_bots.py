from pathlib import Path

def test_both_active_bots_are_message_and_button_driven():
    life=Path('apps/telelife_bot/handlers/life.py').read_text()
    world=Path('apps/teleworld_bot/handlers/world.py').read_text()
    # /start is intentionally retained; all product navigation remains button-driven.
    assert "CommandHandler('start',start)" in life
    assert 'CommandHandler("start", start)' in world
    assert 'MessageHandler' in life and 'CallbackQueryHandler' in life
    assert 'MessageHandler' in world and 'CallbackQueryHandler' in world

def test_only_one_active_controller_per_bot():
    assert Path('apps/telelife_bot/handlers/life.py').is_file()
    assert Path('apps/teleworld_bot/handlers/world.py').is_file()
