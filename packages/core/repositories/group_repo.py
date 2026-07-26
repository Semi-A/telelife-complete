"""Group persistence for TeleWorld."""

from __future__ import annotations

from packages.core import db
from packages.core.models import Group

_COLUMNS = "id, telegram_id, title, is_active, member_count, settings, created_at, last_active_at"

_UPSERT = f"""
INSERT INTO groups (telegram_id, title)
VALUES ($1, $2)
ON CONFLICT (telegram_id) DO UPDATE SET
    title          = EXCLUDED.title,
    is_active      = TRUE,
    last_active_at = now()
RETURNING {_COLUMNS}
"""


async def get_or_create(telegram_id: int, title: str) -> Group:
    row = await db.fetchrow(_UPSERT, telegram_id, title[:128])
    return Group.from_record(row)


async def link_member(group_id: int, player_id: int) -> None:
    await db.execute(
        """
        INSERT INTO group_members (group_id, player_id)
        VALUES ($1, $2)
        ON CONFLICT (group_id, player_id)
        DO UPDATE SET last_active_at = now()
        """,
        group_id,
        player_id,
    )


async def count_total() -> int:
    return int(await db.fetchval("SELECT count(*) FROM groups WHERE is_active") or 0)