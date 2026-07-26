"""Read models for progression panels. One query per panel, never N+1."""

from __future__ import annotations

from packages.core import db


async def unlocked_keys(player_id: int) -> set[str]:
    rows = await db.fetch(
        "SELECT unlock_key FROM player_unlocks WHERE player_id = $1", player_id
    )
    return {r["unlock_key"] for r in rows}


async def xp_today(player_id: int) -> int:
    value = await db.fetchval(
        """
        SELECT COALESCE(sum(amount), 0) FROM xp_events
        WHERE player_id = $1 AND created_at >= date_trunc('day', now())
        """,
        player_id,
    )
    return int(value or 0)


async def rank_by_level(player_id: int) -> int:
    value = await db.fetchval(
        """
        SELECT count(*) + 1 FROM players p
        WHERE NOT p.is_banned
          AND (p.level, p.xp) > (
              SELECT level, xp FROM players WHERE id = $1
          )
        """,
        player_id,
    )
    return int(value or 1)