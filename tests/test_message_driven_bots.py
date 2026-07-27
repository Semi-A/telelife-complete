from pathlib import Path

def test_both_active_bots_are_message_and_button_driven():
    life=Path('apps/telelife_bot/handlers/life.py').read_text()
    world=Path('apps/teleworld_bot/handlers/world.py').read_text()
    assert 'CommandHandler' not in life
    assert 'CommandHandler' not in world
    assert 'MessageHandler' in life and 'CallbackQueryHandler' in life
    assert 'MessageHandler' in world and 'CallbackQueryHandler' in world

def test_only_one_active_controller_per_bot():
    assert sorted(p.name for p in Path('apps/telelife_bot/handlers').glob('*.py')) == ['__init__.py','common.py','life.py','panel.py']
    assert sorted(p.name for p in Path('apps/teleworld_bot/handlers').glob('*.py')) == ['__init__.py','world.py']