"""Level curve maths. Pure functions - trivially testable, zero I/O."""

from __future__ import annotations

from functools import lru_cache

from packages.core.config import get_config


@lru_cache(maxsize=512)
def xp_required(level: int) -> int:
    """Total XP needed to advance FROM `level` to `level + 1`."""
    cfg = get_config()
    base = cfg.int_("progression.xp_curve.base")
    exponent = cfg.float_("progression.xp_curve.exponent")
    return max(1, int(base * (level**exponent)))


def max_level() -> int:
    return get_config().int_("progression.xp_curve.max_level")


def level_progress(level: int, xp: int) -> tuple[int, int]:
    """Return (current_xp_in_level, xp_needed_for_next).

    At max level there is no next threshold; we report the bar as full instead
    of dividing by a meaningless target.
    """
    if level >= max_level():
        return xp, max(xp, 1)
    return xp, xp_required(level)