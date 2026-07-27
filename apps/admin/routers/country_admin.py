"""Authenticated command-center APIs with audited mutations."""
from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
import asyncio, json
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from apps.admin.auth import AdminPrincipal, require_admin
from packages.core.repositories import admin_repo
from packages.core.services import admin, admin_accounts, admin_security, commerce, live_market, scheduler_ops, engagement
from packages.core.settings import get_settings

AdminActor = Annotated[AdminPrincipal, Depends(require_admin)]
async def enforce_admin_request(request: Request, actor: AdminActor) -> None:
    await admin_security.verify_request(request, actor.username, actor.role)

router = APIRouter(prefix="/api/admin", dependencies=[Depends(require_admin),Depends(enforce_admin_request)])

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

class AdBody(BaseModel):
    title: str = Field(min_length=3,max_length=120)
    text: str = Field(min_length=3,max_length=4000)
    destination: int
    scheduled_at: datetime | None = None
    repeat_minutes: int | None = Field(default=None,ge=15,le=525600)

class AdReviewBody(BaseModel):
    note: str | None = Field(default=None,max_length=1000)
class AdEditBody(BaseModel):
    title: str = Field(min_length=3,max_length=120)
    description: str = Field(min_length=10,max_length=2000)
    target_url: str = Field(min_length=8,max_length=1000)
    requested_start_at: datetime | None = None
class AdRejectBody(BaseModel):
    reason: str = Field(min_length=3,max_length=1000)

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


class FreezeBody(BaseModel):
    enabled: bool

class FeatureBody(BaseModel):
    enabled: bool


class PreviewBody(BaseModel):
    method: Literal["POST","PUT","PATCH","DELETE"]
    path: str = Field(min_length=12,max_length=500)
    payload: dict[str,object] = Field(default_factory=dict)
class IncidentBody(BaseModel):
    status: Literal["acknowledged","investigating","resolved"]
    note: str | None = Field(default=None,max_length=1000)

class AdminCreateBody(BaseModel):
    username: str = Field(min_length=3,max_length=64,pattern=r"^[A-Za-z0-9_.-]+$")
    password: str = Field(min_length=12,max_length=256)
    role: Literal["viewer","support","content","economy","operator","superadmin"]

class AdminUpdateBody(BaseModel):
    role: Literal["viewer","support","content","economy","operator","superadmin"] | None = None
    enabled: bool | None = None
    password: str | None = Field(default=None,min_length=12,max_length=256)

@router.post("/action-preview")
async def action_preview(body:PreviewBody,actor:AdminActor)->dict[str,object]:
    return await admin_security.issue_preview(actor.username,actor.role,body.method,body.path,body.payload)

@router.get("/me")
async def me(actor:AdminActor)->dict[str,str]:
    return {"username":actor.username,"role":actor.role,"source":actor.source}

@router.get("/admins")
async def admin_identities(actor:AdminActor)->list[dict[str,object]]:
    return await admin_accounts.list_identities()

@router.post("/admins",status_code=201)
async def create_admin(body:AdminCreateBody,actor:AdminActor)->dict[str,object]:
    try:
        return await admin_accounts.create_identity(actor.username,body.username,body.password,body.role)
    except ValueError as exc:
        messages={
            "admin_exists":"این نام کاربری از قبل وجود دارد.",
            "admin_reserved":"این نام کاربری در تنظیمات اصلی رزرو شده است.",
            "invalid_admin_username":"نام کاربری معتبر نیست.",
            "invalid_admin_password":"گذرواژه باید حداقل ۱۲ نویسه باشد.",
            "invalid_admin_role":"نقش معتبر نیست.",
        }
        raise HTTPException(409 if str(exc)=="admin_exists" else 400,messages.get(str(exc),"ساخت مدیر انجام نشد.")) from exc

@router.patch("/admins/{username}")
async def update_admin(username:str,body:AdminUpdateBody,actor:AdminActor)->dict[str,object]:
    if body.role is None and body.enabled is None and body.password is None:
        raise HTTPException(400,"حداقل یک تغییر لازم است.")
    try:
        return await admin_accounts.update_identity(
            actor.username,username,role=body.role,enabled=body.enabled,password=body.password
        )
    except ValueError as exc:
        messages={
            "admin_not_found":"مدیر پیدا نشد.",
            "admin_environment_managed":"حساب اصلی از متغیرهای محیطی مدیریت می‌شود.",
            "admin_cannot_disable_self":"نمی‌توانی حساب خودت را غیرفعال کنی.",
            "last_superadmin":"حداقل یک مدیر ارشد فعال باید باقی بماند.",
            "invalid_admin_username":"نام کاربری معتبر نیست.",
            "invalid_admin_password":"گذرواژه باید حداقل ۱۲ نویسه باشد.",
        }
        code=404 if str(exc)=="admin_not_found" else 409
        raise HTTPException(code,messages.get(str(exc),"ویرایش مدیر انجام نشد.")) from exc

@router.get("/search")
async def global_search(q:Annotated[str,Query(min_length=2,max_length=100)]) -> dict[str,list[dict[str,object]]]:
    return await admin_repo.global_search(q)

@router.get("/incidents")
async def incidents(limit:Annotated[int,Query(ge=1,le=500)]=100)->list[dict[str,object]]:
    return [dict(x) for x in await admin_repo.incident_rows(limit)]

@router.patch("/incidents/{incident_id}")
async def incident_update(incident_id:int,body:IncidentBody,actor:AdminActor)->dict[str,object]:
    row=await admin_repo.update_incident(incident_id,body.status,actor.username,body.note)
    if not row:raise HTTPException(404,"رخداد پیدا نشد.")
    return dict(row)

@router.get("/anomalies")
async def anomalies(limit:Annotated[int,Query(ge=1,le=500)]=100)->list[dict[str,object]]:
    return await admin_repo.anomaly_rows(limit)

@router.post("/undo/{action_id}")
async def undo(action_id:int,actor:AdminActor)->dict[str,bool]:
    try:return {"undone":await admin_repo.undo_action(action_id,actor.username)}
    except ValueError as exc:raise HTTPException(409,"عملیات دیگر قابل بازگردانی نیست.") from exc

@router.get("/undos")
async def undos(limit:Annotated[int,Query(ge=1,le=100)]=50)->list[dict[str,object]]:
    return [dict(x) for x in await admin_repo.available_undos(limit)]

@router.get("/events")
async def admin_events(request:Request):
    async def stream():
        last=""
        while not await request.is_disconnected():
            rows=[dict(x) for x in await admin_repo.incident_rows(30)]
            payload=json.dumps(rows,default=str,ensure_ascii=False,separators=(",",":"))
            if payload!=last:
                yield f"event: incidents\ndata: {payload}\n\n";last=payload
            else:yield ": keepalive\n\n"
            await asyncio.sleep(8)
    return StreamingResponse(stream(),media_type="text/event-stream",headers={"Cache-Control":"no-store","X-Accel-Buffering":"no"})

@router.get("/engagement")
async def engagement_overview() -> dict[str, object]:
    return await admin_repo.engagement_overview()

@router.get("/feature-flags")
async def feature_flags() -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.feature_flags()]

@router.put("/feature-flags/{key}")
async def set_feature_flag(key: str, body: FeatureBody, actor: AdminActor) -> dict[str, bool]:
    allowed = {"economy_frozen", "usd_market_frozen", "ads_frozen", "registrations_frozen"}
    if key not in allowed:
        raise HTTPException(400, "این کلید مدیریتی مجاز نیست.")
    return {"applied": await admin.feature(actor.username, key, body.enabled, str(uuid4()))}

@router.get("/ledger")
async def ledger(limit: Annotated[int, Query(ge=1, le=500)] = 100,
                 player_id: Annotated[int | None, Query(gt=0)] = None) -> list[dict[str, object]]:
    return [dict(row) for row in await admin_repo.ledger_rows(limit, player_id)]

@router.get("/economy-integrity")
async def economy_integrity() -> dict[str, object]:
    return await admin_repo.economy_integrity()

@router.get("/operations")
async def operations() -> dict[str, object]:
    return await admin_repo.operations_status()

@router.post("/operations/market/sync")
async def sync_market(actor: AdminActor) -> dict[str, object]:
    try:
        result=await live_market.sync()
    except Exception as exc:
        raise HTTPException(502,"منبع Zipodo پاسخ معتبر نداد؛ آخرین نرخ معتبر حفظ شد.") from exc
    return result

@router.post("/operations/market/freeze")
async def freeze_market(body: FreezeBody, actor: AdminActor) -> dict[str, bool]:
    return {"applied":await admin.feature(actor.username,"usd_market_frozen",body.enabled,str(uuid4()))}

@router.post("/operations/jobs/{job_name}/run")
async def run_job(job_name: str, actor: AdminActor) -> dict[str, bool]:
    allowed={"zipodo_rate":live_market.sync,"engagement":engagement.minute_tick,"market_snapshot":admin_repo.capture_market_snapshot}
    if job_name not in allowed:raise HTTPException(400,"این Job برای اجرای دستی مجاز نیست.")
    result=await scheduler_ops.run(f"manual:{job_name}",allowed[job_name])
    if result is None:raise HTTPException(502,"Job اجرا نشد؛ جزئیات خطا در عملیات زنده ثبت شد.")
    return {"completed":True}

@router.get("/command-center")
async def command_center() -> dict[str, object]:
    return await admin_repo.command_center()

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
        return {"applied": await admin.ban(actor.username, player_id, body.enabled, body.reason, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/users/{player_id}/xp")
async def xp_json(player_id: int, body: XPBody, actor: AdminActor) -> dict[str, int]:
    result = await admin.grant_xp(actor.username, player_id, body.amount, str(uuid4()))
    return {"granted": result.granted if result else 0}

@router.post("/market/{asset}")
async def price(asset: str, body: PriceBody, actor: AdminActor) -> dict[str, bool]:
    try:
        return {"applied": await admin.set_market_price(actor.username, asset, body.price, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/countries/{country_id}/asset")
async def country_asset(country_id: int, body: CountryAssetBody,
                        actor: AdminActor) -> dict[str, int]:
    try:
        return {"balance": await admin.adjust_country_asset(
            actor.username, country_id, body.asset, body.delta, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/countries/{country_id}/president")
async def president(country_id: int, body: PresidentBody,
                    actor: AdminActor) -> dict[str, bool]:
    try:
        return {"applied": await admin.set_president(
            actor.username, country_id, body.player_id, str(uuid4()))}
    except ValueError as exc:
        raise fail(exc) from exc

@router.post("/news")
async def enqueue_news(body: NewsBody, actor: AdminActor) -> dict[str, bool]:
    destination = body.destination or get_settings().global_news_chat_id
    if destination is None:
        raise HTTPException(400, "GLOBAL_NEWS_CHAT_ID تنظیم نشده است.")
    return {"queued": await admin.enqueue_news(
        actor.username, body.text, destination, str(uuid4()))}

# State-changing admin routes intentionally accept JSON only.
@router.get("/ads")
async def ads(limit: Annotated[int,Query(ge=1,le=500)]=100)->list[dict[str,object]]:
    return [dict(row) for row in await admin_repo.ads(limit)]

@router.post("/ads")
async def create_ad(body:AdBody,actor:AdminActor)->dict[str,int]:
    try:return {"id":await admin.create_ad(actor.username,body.title,body.text,body.destination,body.scheduled_at,body.repeat_minutes,str(uuid4()))}
    except ValueError as exc:raise fail(exc) from exc

@router.post("/ads/{ad_id}/queue")
async def queue_ad(ad_id:int,actor:AdminActor)->dict[str,bool]:
    try:return {"queued":await admin.queue_ad(actor.username,ad_id,str(uuid4()))}
    except ValueError as exc:raise fail(exc) from exc

@router.get("/ad-requests")
async def ad_requests(limit:Annotated[int,Query(ge=1,le=500)]=100)->list[dict[str,object]]:
 return [dict(x) for x in await commerce.list_ads(limit)]
@router.get("/ad-requests/{ad_id}/image")
async def ad_request_image(ad_id:int):
 from fastapi.responses import Response
 row=await commerce.ad_image(ad_id)
 if not row or not row["image_bytes"]:raise HTTPException(404,"تصویری وجود ندارد.")
 return Response(content=bytes(row["image_bytes"]),media_type=row["image_mime"] or "image/jpeg",headers={"Cache-Control":"private, no-store"})
@router.put("/ad-requests/{ad_id}")
async def edit_ad_request(ad_id:int,body:AdEditBody,actor:AdminActor)->dict[str,bool]:
 return {"updated":bool(await commerce.edit_ad(ad_id,body.title,body.description,body.target_url,body.requested_start_at))}
@router.post("/ad-requests/{ad_id}/approve")
async def approve_ad_request(ad_id:int,body:AdReviewBody,actor:AdminActor)->dict[str,bool]:
 row=await commerce.approve_ad(ad_id,actor.username,body.note)
 if not row:raise HTTPException(409,"وضعیت درخواست قابل تأیید نیست.")
 return {"approved":True}
@router.post("/ad-requests/{ad_id}/reject")
async def reject_ad_request(ad_id:int,body:AdRejectBody,actor:AdminActor)->dict[str,bool]:
 row=await commerce.reject_ad(ad_id,actor.username,body.reason)
 return {"rejected":bool(row)}
@router.post("/ad-requests/{ad_id}/pause")
async def pause_ad_request(ad_id:int,actor:AdminActor)->dict[str,bool]:return {"paused":bool(await commerce.pause_ad(ad_id))}
@router.post("/ad-requests/{ad_id}/refund")
async def refund_ad_request(ad_id:int,actor:AdminActor)->dict[str,bool]:
 row=await commerce.refundable(ad_id)
 if not row:raise HTTPException(409,"پس از نخستین پخش، بازپرداخت خودکار مجاز نیست.")
 from telegram import Bot
 async with Bot(get_settings().telelife_bot_token) as bot:ok=await bot.refund_star_payment(user_id=row["telegram_id"],telegram_payment_charge_id=row["telegram_charge_id"])
 if ok:await commerce.mark_refunded(ad_id)
 return {"refunded":bool(ok)}
