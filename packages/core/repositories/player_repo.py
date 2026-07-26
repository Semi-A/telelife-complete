"""All player SQL lives here. Handlers never write SQL."""

from __future__ import annotations

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.models import Player

_COLUMNS = """
    id, telegram_id, username, first_name, language_code,
    level, xp, reputation, happiness, prestige,
    wallet_toman, savings_toman, usd_cents,
    is_banned, is_frozen, ban_reason,
    created_at, updated_at, last_seen_at
"""

_UPSERT = f"""
INSERT INTO players (
    telegram_id, username, first_name, language_code,
    level, xp, reputation, happiness,
    wallet_toman, savings_toman, usd_cents
)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
ON CONFLICT (telegram_id) DO UPDATE SET
    username     = EXCLUDED.username,
    first_name   = EXCLUDED.first_name,
    last_seen_at = now()
RETURNING {_COLUMNS}
"""


async def get_by_telegram_id(telegram_id: int) -> Player | None:
    row = await db.fetchrow(
        f"SELECT {_COLUMNS} FROM players WHERE telegram_id = $1", telegram_id
    )
    return Player.from_record(row) if row else None


async def get_or_create(
    telegram_id: int,
    *,
    username: str | None,
    first_name: str,
    language_code: str = "fa",
    conn: asyncpg.Connection | None = None,
) -> Player:
    """Idempotent registration - safe under concurrent first messages."""
    cfg = get_config()
    args = (
        telegram_id,
        username,
        first_name[:64],
        language_code,
        cfg.int_("progression.starting_state.level"),
        cfg.int_("progression.starting_state.xp"),
        cfg.int_("progression.starting_state.reputation"),
        cfg.int_("progression.starting_state.happiness"),
        cfg.int_("economy.starting_balance.wallet_toman"),
        cfg.int_("economy.starting_balance.savings_toman"),
        cfg.int_("economy.starting_balance.usd_cents"),
    )
    if conn is not None:
        row = await conn.fetchrow(_UPSERT, *args)
    else:
        row = await db.fetchrow(_UPSERT, *args)
    return Player.from_record(row)


async def touch_last_seen(player_id: int) -> None:
    await db.execute("UPDATE players SET last_seen_at = now() WHERE id = $1", player_id)


async def count_total() -> int:
    return int(await db.fetchval("SELECT count(*) FROM players") or 0)


async def count_active(days: int = 7) -> int:
    return int(
        await db.fetchval(
            "SELECT count(*) FROM players WHERE last_seen_at > now() - ($1 || ' days')::interval",
            str(days),
        )
        or 0
    )
