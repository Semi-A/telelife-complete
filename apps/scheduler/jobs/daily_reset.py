"""Nightly maintenance: prune stale mission rows, break dead streaks.

Both operations are ranged and index-backed, so cost stays flat as the player
base grows.
"""

from __future__ import annotations

import logging

from packages.core import db
from packages.core.config import get_config

logger = logging.getLogger(__name__)

MISSION_RETENTION_DAYS = 7
XP_EVENT_RETENTION_DAYS = 90


async def prune_missions() -> int:
    result = await db.execute(
        "DELETE FROM daily_missions WHERE mission_date < current_date - $1::int",
        MISSION_RETENTION_DAYS,
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def prune_xp_events() -> int:
    result = await db.execute(
        "DELETE FROM xp_events WHERE created_at < now() - ($1 || ' days')::interval",
        str(XP_EVENT_RETENTION_DAYS),
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def break_streaks() -> int:
    """Drop streaks for players who missed more than the grace window."""
    cfg = get_config()
    reset_to = cfg.int_("daily.streak.grace_reset_to")
    break_after = cfg.int_("daily.streak.break_after_days")
    result = await db.execute(
        """
        UPDATE daily_state
        SET streak = $1
        WHERE last_claim_date IS NOT NULL
          AND last_claim_date < current_date - ($2::int + 1)
          AND streak > $1
        """,
        reset_to,
        break_after,
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def run() -> dict[str, int]:
    stats = {
        "missions_pruned": await prune_missions(),
        "xp_events_pruned": await prune_xp_events(),
        "streaks_broken": await break_streaks(),
    }
    logger.info("daily reset complete: %s", stats)
    return stats
