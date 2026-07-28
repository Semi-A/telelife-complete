"""Every dynamic keyboard state must build and respect Telegram limits."""
from apps.telelife_bot.keyboards import main as life
from apps.teleworld_bot import keyboards as world

def validate(markup):
    rows=markup.inline_keyboard
    assert rows
    primary=0
    for row in rows:
        assert 1 <= len(row) <= 8
        for button in row:
            data=getattr(button,"callback_data",None)
            if data is not None: assert len(data.encode("utf-8")) <= 64
            if getattr(button,"style",None)=="primary": primary+=1
    assert primary <= 1

def test_every_life_keyboard_state_builds():
    cases=[]
    for daily in (False,True):
        for step in range(5): cases.append(life.home(123456789,daily,step))
    for step in range(6): cases.append(life.journey(123456789,step))
    for ready in (False,True): cases.append(life.daily(123456789,ready))
    for keys in ([],["a"],["a","b","c"]): cases.append(life.missions(123456789,keys))
    for has in (False,True):
        for unlocked in (False,True): cases.append(life.jobs(123456789,has,unlocked))
    for unlocked in (False,True): cases.append(life.market(123456789,unlocked))
    cases += [life.back(123456789),life.economy(123456789),life.savings(123456789),life.housing(123456789)]
    for case in cases: validate(case)

def test_every_world_keyboard_state_builds():
    rows=[{"first_name":"علی","player_id":1},{"first_name":"سارا","player_id":2}]
    cases=[world.private("sample_bot"),world.governments(),world.country(),world.back(),world.cancel(),world.candidates(rows)]
    for country in (False,True):
        for admin in (False,True):
            for citizen in (False,True): cases.append(world.home(country,admin,citizen))
    for status in (None,"nominations","voting"): cases.append(world.politics(status))
    for active in (False,True): cases.append(world.project(active))
    for case in cases: validate(case)
