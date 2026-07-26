"""Country mission and effect persistence."""

from __future__ import annotations

from datetime import date

import asyncpg

from packages.core import db


async def ensure(
    conn: asyncpg.Connection,
    country_id: int,
    day: date,
    key: str,
    metric: str,
    target: int,
    reward_asset: str,
    reward: int,
) -> asyncpg.Record:
    """Create today's mission or return the existing one untouched."""
    row = await conn.fetchrow(
        """
        INSERT INTO country_missions
            (country_id, mission_date, mission_key, metric_key,
             target_amount, reward_asset_code, reward_amount)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        ON CONFLICT (country_id, mission_date, mission_key)
        DO UPDATE SET mission_key = country_missions.mission_key
        RETURNING *
        """,
        country_id,
        day,
        key,
        metric,
        target,
        reward_asset,
        reward,
    )
    if row is None:
        raise RuntimeError("country_mission_upsert_returned_nothing")
    return row


async def add(
    conn: asyncpg.Connection,
    country_id: int,
    day: date,
    metric: str,
    amount: int,
) -> asyncpg.Record | None:
    """Advance progress, clamped at the target, stamping completion once."""
    return await conn.fetchrow(
        """
        UPDATE country_missions SET
            progress_amount = LEAST(target_amount, progress_amount + $4),
            completed_at = CASE
                WHEN progress_amount + $4 >= target_amount
                THEN COALESCE(completed_at, now())
                ELSE completed_at END
        WHERE country_id = $1 AND mission_date = $2 AND metric_key = $3
        RETURNING *
        """,
        country_id,
        day,
        metric,
        amount,
    )


async def reward_once(
    conn: asyncpg.Connection, country_id: int, day: date, key: str
) -> bool:
    """Claim the reward slot. False means it was already paid out."""
    claimed = await conn.fetchval(
        """
        UPDATE country_missions SET rewarded_at = now()
        WHERE country_id = $1 AND mission_date = $2 AND mission_key = $3
          AND completed_at IS NOT NULL AND rewarded_at IS NULL
        RETURNING country_id
        """,
        country_id,
        day,
        key,
    )
    return claimed is not None


async def effect(
    conn: asyncpg.Connection,
    country_id: int,
    code: str,
    magnitude: int,
    source_key: str,
    hours: int,
) -> None:
    await conn.execute(
        """
        INSERT INTO country_effects
            (country_id, effect_code, magnitude, starts_at, ends_at,
             source_type, source_key)
        VALUES ($1, $2, $3, now(), now() + ($5::double precision * interval '1 hour'),
                'country_mission', $4)
        ON CONFLICT DO NOTHING
        """,
        country_id,
        code,
        magnitude,
        source_key,
        hours,
    )


async def list_today(country_id: int, day: date) -> list[asyncpg.Record]:
    """Today's missions. The day is passed in so the game clock decides it,
    not the database server's local `current_date`."""
    return await db.fetch(
        "SELECT * FROM country_missions "
        "WHERE country_id = $1 AND mission_date = $2 ORDER BY mission_key",
        country_id,
        day,
    )