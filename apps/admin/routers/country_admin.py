"""Authenticated country administration API with audited mutations."""

from __future__ import annotations

from typing import Annotated
from uuid import uuid4

from fastapi import APIRouter, Depends, Form, Query

from apps.admin.auth import require_admin
from packages.core.repositories import admin_repo
from packages.core.services import admin

AdminActor = Annotated[str, Depends(require_admin)]
router = APIRouter(prefix="/api/admin", dependencies=[Depends(require_admin)])


@router.get("/stats")
async def stats() -> dict[str, object]:
    row = await admin_repo.stats()
    return dict(row) if row else {}


@router.get("/users")
async def users(limit: Annotated[int, Query(ge=1, le=500)] = 100) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.users(limit)]


@router.get("/countries")
async def countries(
    limit: Annotated[int, Query(ge=1, le=500)] = 100,
) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.countries(limit)]


@router.get("/audit")
async def audit(limit: Annotated[int, Query(ge=1, le=500)] = 100) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.audits(limit)]


@router.post("/ban/{player_id}")
async def ban(
    player_id: int,
    actor: AdminActor,
    enabled: Annotated[bool, Form()],
    reason: Annotated[str | None, Form()] = None,
) -> dict[str, bool]:
    return {
        "applied": await admin.ban(actor, player_id, enabled, reason, str(uuid4()))
    }


@router.post("/grant-xp/{player_id}")
async def grant(
    player_id: int,
    actor: AdminActor,
    amount: Annotated[int, Form(gt=0, le=1_000_000)],
) -> dict[str, int]:
    result = await admin.grant_xp(actor, player_id, amount, str(uuid4()))
    return {"granted": result.granted if result else 0}


@router.post("/feature/{key}")
async def feature(
    key: str,
    actor: AdminActor,
    enabled: Annotated[bool, Form()],
) -> dict[str, bool]:
    return {"applied": await admin.feature(actor, key, enabled, str(uuid4()))}
