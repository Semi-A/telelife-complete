from pathlib import Path

def text(path): return Path(path).read_text(encoding='utf-8')

def test_start_is_fresh_and_retires_old_panel():
    life=text('apps/telelife_bot/handlers/life.py')
    panel=text('apps/telelife_bot/handlers/panel.py')
    assert 'force_new=True' in life
    assert 'edit_message_reply_markup' in panel
    assert 'force_new' in panel

def test_stale_callbacks_are_rejected():
    life=text('apps/telelife_bot/handlers/life.py')
    assert "active_id!=clicked_id" in life
    assert 'retire_message' in life

def test_life_country_and_confirmed_migration_exist():
    life=text('apps/telelife_bot/handlers/life.py')
    keys=text('apps/telelife_bot/keyboards/main.py')
    assert 'async def country_page' in life
    assert "a=='migconfirm'" in life
    assert 'migration.quote' in life and 'migration.request' in life
    assert 'ورود به گروه کشور من' in keys
    assert 'url_button' in keys


def test_world_start_is_fresh_and_retires_old_panel():
    world=text('apps/teleworld_bot/handlers/world.py')
    assert 'edit_message_reply_markup' in world
    assert 'clear_world' in world
