from pathlib import Path


def test_economy_has_usd_and_resource_entries():
    source=Path("apps/telelife_bot/keyboards/main.py").read_text()
    assert '"market"' in source[source.index("def economy"):source.index("def savings")]
    assert '"resources"' in source[source.index("def economy"):source.index("def savings")]


def test_resource_sale_is_two_step_and_has_handler():
    keys=Path("apps/telelife_bot/keyboards/main.py").read_text()
    life=Path("apps/telelife_bot/handlers/life.py").read_text()
    assert '"rpick"' in keys and "if a=='rpick':" in life
    assert "resource_amounts" in keys


def test_social_mutations_are_covered_by_access_gate():
    source=Path("apps/teleworld_bot/handlers/world.py").read_text()
    gate=source[source.index("MUTATING ="):source.index("async def access_page")]
    for action in ('"socperson:"','"rgiftpick:"','"rdonatepick:"','"resourcegift"','"resourcedonate"','"socmarriage"'):
        assert action in gate


def test_daily_resource_limits_are_serialized():
    source=Path("packages/core/services/resource_economy.py").read_text()
    assert "lock_player(conn,player_id)" in source
    assert "lock_player(conn,actor)" in source


def test_onboarding_does_not_capture_every_world_callback():
    source=Path("apps/teleworld_bot/handlers/onboarding.py").read_text()
    register=source[source.index("def register"):]
    assert 'pattern=r"^tw:"' not in register
