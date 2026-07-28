from pathlib import Path


def test_vote_threshold_stays_simple_for_all_group_sizes():
    source=Path("packages/core/services/intergroup_council.py").read_text()
    assert "return 1 if citizens<=2 else 2 if citizens<=6 else 3" in source


def test_only_clear_safe_actions_are_offered():
    source=Path("packages/core/services/intergroup_council.py").read_text()
    for action in ("friend","trade_partner","defensive_ally","aid_food","aid_energy","aid_irt"):
        assert f'"{action}"' in source


def test_schema_prevents_duplicate_votes_and_open_duplicates():
    sql=Path("migrations/0025_intergroup_council.sql").read_text()
    assert "PRIMARY KEY(proposal_id,country_id,player_id)" in sql
    assert "uq_country_council_one_open_pair_action" in sql


def test_world_routes_every_council_button():
    keys=Path("apps/teleworld_bot/keyboards.py").read_text()
    world=Path("apps/teleworld_bot/handlers/world.py").read_text()
    for action in ("council","councilnew","councilto:","councilmake:","councilview:","councilvote:"):
        assert action in keys and action in world


def test_execution_uses_existing_atomic_trade_service():
    source=Path("packages/core/services/intergroup_council.py").read_text()
    assert "country_trade.propose_relation" in source
    assert "country_trade.accept_relation" in source
    assert "country_trade.send_aid" in source
    assert "\"execute\":True" in source