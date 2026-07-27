"""Persistence for TeleWorld membership, permission snapshots and warning dedupe."""
from __future__ import annotations
from collections.abc import Mapping
from typing import Any
from packages.core import db

async def get(chat_id: int):
    return await db.fetchrow("SELECT * FROM world_group_access WHERE chat_id=$1", chat_id)

async def membership(chat_id: int, title: str, status: str, active: bool) -> None:
    await db.execute(
        """INSERT INTO world_group_access(chat_id,chat_title,membership_status,is_active)
        VALUES($1,$2,$3,$4)
        ON CONFLICT(chat_id) DO UPDATE SET chat_title=$2,membership_status=$3,
        is_active=$4,updated_at=now()""", chat_id, title[:128], status, active,
    )

async def claim_welcome(chat_id: int) -> bool:
    """Atomically claim the one lifetime welcome for a chat."""
    claimed = await db.fetchval(
        """UPDATE world_group_access SET welcomed_at=now(),updated_at=now()
        WHERE chat_id=$1 AND welcomed_at IS NULL RETURNING chat_id""", chat_id
    )
    return claimed is not None

async def set_welcome_message(chat_id: int, message_id: int) -> None:
    await db.execute(
        "UPDATE world_group_access SET welcome_message_id=$2,status_message_id=$2,updated_at=now() WHERE chat_id=$1",
        chat_id, message_id,
    )

async def save_access(chat_id: int, administrator: bool, can_delete: bool,
                      missing: list[str]) -> None:
    await db.execute(
        """INSERT INTO world_group_access(chat_id,is_administrator,can_delete_messages,
        missing_permissions,last_checked_at) VALUES($1,$2,$3,$4,now())
        ON CONFLICT(chat_id) DO UPDATE SET is_administrator=$2,can_delete_messages=$3,
        missing_permissions=$4,last_checked_at=now(),updated_at=now()""",
        chat_id, administrator, can_delete, missing,
    )

async def claim_warning(chat_id: int, fingerprint: str, cooldown_minutes: int = 30) -> bool:
    claimed = await db.fetchval(
        """UPDATE world_group_access SET last_warning_at=now(),last_warning_fingerprint=$2,
        updated_at=now() WHERE chat_id=$1 AND (last_warning_fingerprint IS DISTINCT FROM $2
        OR last_warning_at IS NULL OR last_warning_at < now()-($3::int*interval '1 minute'))
        RETURNING chat_id""", chat_id, fingerprint, cooldown_minutes,
    )
    return claimed is not None

async def audit(event_key: str, event_type: str, *, chat_id: int | None = None,
                player_id: int | None = None, country_id: int | None = None,
                details: Mapping[str, Any] | None = None) -> bool:
    value = await db.fetchval(
        """INSERT INTO product_audit_log(event_key,event_type,chat_id,player_id,country_id,details)
        VALUES($1,$2,$3,$4,$5,$6::jsonb) ON CONFLICT(event_key) DO NOTHING RETURNING id""",
        event_key, event_type, chat_id, player_id, country_id, dict(details or {}),
    )
    return value is not None