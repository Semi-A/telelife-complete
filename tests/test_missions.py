from datetime import date, timedelta

from packages.core.services.missions import select_for

DAY = date(2026, 7, 25)


def test_selection_is_deterministic():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(12345, 5, DAY)]
    assert a == b, "a restart must never reshuffle a player's missions"


def test_different_players_get_different_missions():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(99999, 5, DAY)]
    assert a != b


def test_missions_rotate_daily():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(12345, 5, DAY + timedelta(days=1))]
    assert a != b


def test_level_gating_limits_the_pool():
    low = select_for(12345, 1, DAY)
    high = select_for(12345, 10, DAY)
    assert len(low) <= len(high)
    assert all(int(m.get("min_level", 1)) <= 1 for m in low)