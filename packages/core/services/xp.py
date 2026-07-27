"""XP granting with idempotency, daily cap and level-up cascade.

One entry point: `grant()`. Everything else in the codebase calls it.
That single funnel is what makes the daily cap and anti-farm enforceable.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.services import progression
from packages.core.utils import clock

logger = logging.getLogger(__name__)


@dataclass(slots=True, frozen=True)
class XPResult:
    granted: int
    duplicate: bool
    capped: bool
    level_before: int
    level_after: int
    reward_toman: int = 0

    @property
    def leveled_up(self) -> bool:
        return self.level_after > self.level_before


async def _today_total(conn: asyncpg.Connection, player_id: int) -> int:
    """XP already granted today, in the game timezone, not the server's."""
    value = await conn.fetchval(
        """
        SELECT COALESCE(sum(amount), 0) FROM xp_events
        WHERE player_id = $1
          AND (created_at AT TIME ZONE $2)::date = $3::date
        """,
        player_id,
        str(clock.game_timezone().key),
        clock.game_today(),
    )
    return int(value or 0)


def _apply_levels(level: int, xp: int) -> tuple[int, int]:
    """Consume XP into levels. Returns (new_level, remaining_xp)."""
    top = progression.max_level()
    while level < top:
        needed = progression.xp_required(level)
        if xp < needed:
            break
        xp -= needed
        level += 1
    return level, xp


async def grant(
    player_id: int,
    source: str,
    *,
    idempotency_key: str,
    amount: int | None = None,
    conn: asyncpg.Connection | None = None,
) -> XPResult:
    """Grant XP exactly once; optionally participate in a caller transaction."""
    if conn is None:
        async with db.transaction() as owned_conn:
            return await grant(
                player_id, source, idempotency_key=idempotency_key,
                amount=amount, conn=owned_conn,
            )

    cfg = get_config()
    requested = amount if amount is not None else cfg.int_(f"xp.sources.{source}")
    if requested < 0:
        raise ValueError("negative_xp")
    daily_cap = cfg.int_("xp.anti_farm.daily_cap")

    row = await conn.fetchrow(
        "SELECT level, xp FROM players WHERE id = $1 FOR UPDATE", player_id
    )
    if row is None:
        raise ValueError(f"player {player_id} not found")
    level_before, current_xp = int(row["level"]), int(row["xp"])

    inserted = await conn.fetchval(
        """INSERT INTO xp_events (player_id,idempotency_key,source,amount,level_after)
        VALUES ($1,$2,$3,0,$4) ON CONFLICT (idempotency_key) DO NOTHING
        RETURNING id""",
        player_id, idempotency_key, source, level_before,
    )
    if inserted is None:
        return XPResult(0, True, False, level_before, level_before)

    used = await _today_total(conn, player_id)
    allowed = max(0, min(requested, daily_cap - used))
    capped = allowed < requested
    if allowed == 0:
        return XPResult(0, False, capped, level_before, level_before)

    level_after, remaining = _apply_levels(level_before, current_xp + allowed)
    gained = level_after - level_before
    reward = gained * cfg.int_("xp.level_up.reward_toman_per_level")
    happiness_bonus = gained * cfg.int_("xp.level_up.happiness_bonus")
    await conn.execute("UPDATE xp_events SET amount=$2,level_after=$3 WHERE id=$1", inserted, allowed, level_after)
    balance = await conn.fetchval(
        """UPDATE players SET level=$2,xp=$3,wallet_toman=wallet_toman+$4,
        happiness=LEAST(100,happiness+$5) WHERE id=$1 RETURNING wallet_toman""",
        player_id, level_after, remaining, reward, happiness_bonus,
    )
    if reward:
        await conn.execute(
            """INSERT INTO ledger(player_id,idempotency_key,reason,currency,asset_code,account,amount,balance_after)
            VALUES($1,$2,'level_up','IRT','IRT','wallet',$3,$4)
            ON CONFLICT(idempotency_key) DO NOTHING""",
            player_id, f"levelup:{player_id}:{level_after}", reward, int(balance or 0),
        )
    if gained:
        await _record_unlocks(conn, player_id, level_before, level_after)
    return XPResult(allowed, False, capped, level_before, level_after, reward)


async def _record_unlocks(
    conn: asyncpg.Connection, player_id: int, from_level: int, to_level: int
) -> None:
    levels = get_config().section("unlocks.levels")
    keys = [
        str(spec["key"])
        for lvl, spec in levels.items()
        if from_level < int(lvl) <= to_level
    ]
    if not keys:
        return
    await conn.executemany(
        """
        INSERT INTO player_unlocks (player_id, unlock_key) VALUES ($1, $2)
        ON CONFLICT DO NOTHING
        """,
        [(player_id, key) for key in keys],
    )


def day_key(prefix: str, player_id: int) -> str:
    """Idempotency key that rotates once per game day."""
    return f"{prefix}:{player_id}:{clock.day_stamp()}"
