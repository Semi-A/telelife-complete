from datetime import date, timedelta

from packages.core.services.daily import (
    _milestone,
    _next_milestone,
    _next_streak,
    _reward_for,
    preview,
)

TODAY = date(2026, 7, 25)


def test_reward_grows_then_caps():
    rewards = [_reward_for(d)[0] for d in range(1, 20)]
    assert rewards == sorted(rewards)
    assert rewards[-1] == rewards[-2], "multiplier must cap"


def test_missing_a_day_does_not_wipe_the_streak():
    """The mercy rule: one bad day costs the streak, not the player."""
    mode, _ = _next_streak(TODAY - timedelta(days=5), TODAY)
    assert mode == 1, "reset must land on 1, never 0"


def test_consecutive_day_continues():
    assert _next_streak(TODAY - timedelta(days=1), TODAY)[0] == -1


def test_same_day_is_blocked():
    assert _next_streak(TODAY, TODAY)[0] == 0


def test_first_ever_claim_starts_at_one():
    assert _next_streak(None, TODAY)[0] == 1


def test_milestones_exist_and_advance():
    assert _milestone(7) is not None
    assert _milestone(8) is None
    assert _next_milestone(7) == 14
    assert _next_milestone(100) is None


def test_preview_matches_ladder():
    assert preview(5) == _reward_for(5)[0]