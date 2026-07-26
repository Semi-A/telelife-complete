from packages.core.config import get_config
from packages.core.services.xp import _apply_levels, day_key


def test_partial_xp_does_not_level():
    assert _apply_levels(1, 50) == (1, 50)


def test_exact_threshold_levels_once():
    from packages.core.services import progression

    needed = progression.xp_required(1)
    assert _apply_levels(1, needed) == (2, 0)


def test_large_grant_cascades_multiple_levels():
    level, remainder = _apply_levels(1, 5000)
    assert level > 5
    assert remainder >= 0


def test_cascade_never_exceeds_max_level():
    from packages.core.services import progression

    top = progression.max_level()
    level, _ = _apply_levels(top - 1, 10**9)
    assert level == top


def test_daily_cap_exceeds_a_perfect_day():
    """The cap must punish abuse, never a legitimately active player."""
    cfg = get_config()
    perfect_day = (
        cfg.int_("xp.sources.daily_claim")
        + 3 * cfg.int_("xp.sources.mission_complete")
        + cfg.int_("xp.sources.profile_view")
    )
    assert cfg.int_("xp.anti_farm.daily_cap") > perfect_day * 3


def test_day_key_rotates_daily():
    assert day_key("daily", 1).count(":") == 2
    assert day_key("daily", 1) == day_key("daily", 1)
    assert day_key("daily", 1) != day_key("daily", 2)