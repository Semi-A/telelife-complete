"""Audited privileged operations.

Every privileged action writes an audit row and its side effect inside the
same transaction, so an audit trail can never disagree with reality.
"""

from __future__ import annotations

from packages.core import db
from packages.core.repositories import admin_repo
from packages.core.services import xp
from packages.core.services.xp import XPResult


async def ban(
    actor: str,
    player_id: int,
    banned: bool,
    reason: str | None,
    request_id: str,
) -> bool:
    """Ban or unban a player. Returns False when the request_id was replayed."""
    action = "ban" if banned else "unban"
    async with db.transaction() as conn:
        recorded = await admin_repo.audit(
            conn, actor, action, request_id, {"reason": reason}, player_id
        )
        if not recorded:
            return False
        await admin_repo.set_ban(conn, player_id, banned, reason)
        return True


async def feature(actor: str, key: str, enabled: bool, request_id: str) -> bool:
    """Toggle a feature flag. Returns False when the request_id was replayed."""
    async with db.transaction() as conn:
        recorded = await admin_repo.audit(
            conn, actor, "feature_toggle", request_id, {"key": key, "enabled": enabled}
        )
        if not recorded:
            return False
        await admin_repo.set_flag(conn, key, enabled, actor)
        return True


async def grant_xp(
    actor: str,
    player_id: int,
    amount: int,
    request_id: str,
) -> XPResult | None:
    """Grant XP by hand. Returns None when the request_id was replayed.

    The audit row and the XP grant share one transaction: the original code
    committed the audit, then granted outside it, so a crash in between left
    an audited grant that never happened.
    """
    async with db.transaction() as conn:
        recorded = await admin_repo.audit(
            conn, actor, "grant_xp", request_id, {"amount": amount}, player_id
        )
        if not recorded:
            return None
        return await xp.grant(
            player_id,
            "admin_grant",
            idempotency_key=f"admin-xp:{request_id}",
            amount=amount,
            conn=conn,
        )