"""Authenticated command-center APIs with audited mutations."""
from __future__ import annotations

from typing import Annotated, Literal
from uuid import uuid4
from fastapi import APIRouter, Depends, Form, HTTPException, Query
from pydantic import BaseModel, Field

from apps.admin.auth import require_admin
from packages.core.repositories import admin_repo
from packages.core.services import admin
from packages.core.settings import get_settings

AdminActor = Annotated[str, Depends(require_admin)]
router = APIRouter(prefix="/api/admin", dependencies=[Depends(require_admin)])

class BanBody(BaseModel):
    enabled: bool
    reason: str | None = Field(default=None, max_length=500)
class XPBody(BaseModel):
    amount: int = Field(gt=0, le=1_000_000)
class PriceBody(BaseModel):
    price: int = Field(gt=0, le=10_000_000_000)
class CountryAssetBody(BaseModel):
    asset: Literal["IRT", "oil", "food", "minerals", "energy", "technology"]
    delta: int = Field(ge=-1_000_000_000, le=1_000_000_000)
class PresidentBody(BaseModel):
    player_id: int | None = Field(default=None, gt=0)
class NewsBody(BaseModel):
    text: str = Field(min_length=3, max_length=4000)
    destination: int | None = None

def fail(exc: ValueError) -> HTTPException:
    messages = {
        "player_not_found": "بازیکن پیدا نشد.",
        "country_not_found": "کشور پیدا نشد.",
        "asset_not_found": "دارایی معتبر نیست.",
        "insufficient_balance": "موجودی برای این کاهش کافی نیست.",
        "president_must_be_citizen": "رئیس‌جمهور باید شهروند همین کشور باشد.",
    }
    return HTTPException(400, messages.get(str(exc), "عملیات انجام نشد."))

@router.get("/overview")
async def overview() -> dict[str, object]:
    row = await admin_repo.dashboard_stats()
    return dict(row) if row else {}

@router.get("/stats")
async def stats() -> dict[str, object]:
    row = await admin_repo.stats()
    return dict(row) if row else {}

@router.get("/users")
async def users(limit: Annotated[int, Query(ge=1, le=500)] = 100,
                q: Annotated[str, Query(max_length=100)] = "") -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.users(limit, q)]

@router.get("/countries")
async def countries(limit: Annotated[int, Query(ge=1, le=500)] = 100) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.countries(limit)]

@router.get("/audit")
async def audit(limit: Annotated[int, Query(ge=1, le=500)] = 100) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.audits(limit)]

@router.get("/news")
async def news(limit: Annotated[int, Query(ge=1, le=500)] = 100) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.news_rows(limit)]

@router.get("/market")
async def market(hours: Annotated[int, Query(ge=1, le=720)] = 24) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.market_history(hours)]

@router.post("/users/{player_id}/ban")
async def ban_json(player_id: int, body: BanBody, actor: AdminActor) -> dict[str, bool]:
    try:
        return {"applied": await admin.ban(actor, player_id, body.enabled, body.reason, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/users/{player_id}/xp")
async def xp_json(player_id: int, body: XPBody, actor: AdminActor) -> dict[str, int]:
    result = await admin.grant_xp(actor, player_id, body.amount, str(uuid4()))
    return {"granted": result.granted if result else 0}

@router.post("/market/{asset}")
async def price(asset: str, body: PriceBody, actor: AdminActor) -> dict[str, bool]:
    try:
        return {"applied": await admin.set_market_price(actor, asset, body.price, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/countries/{country_id}/asset")
async def country_asset(country_id: int, body: CountryAssetBody,
                        actor: AdminActor) -> dict[str, int]:
    try:
        return {"balance": await admin.adjust_country_asset(
            actor, country_id, body.asset, body.delta, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/countries/{country_id}/president")
async def president(country_id: int, body: PresidentBody,
                    actor: AdminActor) -> dict[str, bool]:
    try:
        return {"applied": await admin.set_president(
            actor, country_id, body.player_id, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/news")
async def enqueue_news(body: NewsBody, actor: AdminActor) -> dict[str, bool]:
    destination = body.destination or get_settings().global_news_chat_id
    if destination is None:
        raise HTTPException(400, "GLOBAL_NEWS_CHAT_ID تنظیم نشده است.")
    return {"queued": await admin.enqueue_news(
        actor, body.text, destination, str(uuid4()))}

# Backward-compatible form routes.
@router.post("/ban/{player_id}")
async def ban_form(player_id: int, actor: AdminActor,
                   enabled: Annotated[bool, Form()],
                   reason: Annotated[str | None, Form()] = None) -> dict[str, bool]:
    return {"applied": await admin.ban(actor, player_id, enabled, reason, str(uuid4()))}

@router.post("/grant-xp/{player_id}")
async def grant_form(player_id: int, actor: AdminActor,
                     amount: Annotated[int, Form(gt=0, le=1_000_000)]) -> dict[str, int]:
    result = await admin.grant_xp(actor, player_id, amount, str(uuid4()))
    return {"granted": result.granted if result else 0}

@router.post("/feature/{key}")
async def feature(key: str, actor: AdminActor,
                  enabled: Annotated[bool, Form()]) -> dict[str, bool]:
    return {"applied": await admin.feature(actor, key, enabled, str(uuid4()))}
