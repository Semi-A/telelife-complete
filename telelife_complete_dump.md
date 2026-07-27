# دامپ پروژه: telelife_complete

مسیر مبدا: `D:\PRojects\telelife_complete`

تعداد کل فایل‌ها: 217


## ساختار پوشه‌ها و فایل‌ها

```
telelife_complete/
├── apps/
│   ├── admin/
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── country_admin.py
│   │   ├── static/
│   │   │   ├── admin.css
│   │   │   └── admin.js
│   │   ├── templates/
│   │   │   ├── partials/
│   │   │   │   └── stats.html
│   │   │   ├── base.html
│   │   │   └── dashboard.html
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── main.py
│   ├── scheduler/
│   │   ├── jobs/
│   │   │   ├── __init__.py
│   │   │   ├── country_jobs.py
│   │   │   └── daily_reset.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── telelife_bot/
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── advertising.py
│   │   │   ├── common.py
│   │   │   ├── economy_ui.py
│   │   │   ├── life.py
│   │   │   ├── panel.py
│   │   │   ├── profile.py
│   │   │   ├── progression.py
│   │   │   └── start.py
│   │   ├── keyboards/
│   │   │   ├── __init__.py
│   │   │   └── main.py
│   │   ├── texts/
│   │   │   ├── __init__.py
│   │   │   └── fa.py
│   │   ├── views/
│   │   │   ├── __init__.py
│   │   │   └── render.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── teleworld_bot/
│   │   ├── handlers/
│   │   │   ├── __init__.py
│   │   │   ├── access.py
│   │   │   ├── country.py
│   │   │   ├── onboarding.py
│   │   │   ├── politics.py
│   │   │   ├── production.py
│   │   │   ├── status.py
│   │   │   └── world.py
│   │   ├── texts/
│   │   │   ├── __init__.py
│   │   │   └── fa.py
│   │   ├── __init__.py
│   │   ├── keyboards.py
│   │   └── main.py
│   └── __init__.py
├── docs/
│   ├── CONVENTIONS.md
│   ├── DEPLOYMENT.md
│   ├── DEPLOYMENT_FA.md
│   ├── FOR_AI_AGENTS.md
│   ├── PHASE_1.md
│   ├── PHASE_2.md
│   ├── PHASE_3.md
│   ├── PHASE_4.md
│   └── PHASE_5.md
├── migrations/
│   ├── 0001_core_schema.sql
│   ├── 0002_progression.sql
│   ├── 0003_country_layer.sql
│   ├── 0004_admin_command_center.sql
│   ├── 0005_life_world_hardening.sql
│   ├── 0006_phase3_phase4_complete.sql
│   ├── 0007_unified_ui_onboarding.sql
│   ├── 0008_world_access_lifecycle.sql
│   ├── 0009_ads_governance_moderation.sql
│   ├── 0010_stars_subscriptions_ad_marketplace.sql
│   ├── 0011_population_channels_migration.sql
│   ├── 0012_reliability_live_market_engagement.sql
│   └── 0013_country_identity_candles_realism.sql
├── packages/
│   ├── core/
│   │   ├── bot/
│   │   │   ├── __init__.py
│   │   │   ├── errors.py
│   │   │   └── runtime.py
│   │   ├── config/
│   │   │   ├── data/
│   │   │   │   ├── commerce.yaml
│   │   │   │   ├── core.yaml
│   │   │   │   ├── country.yaml
│   │   │   │   ├── country_missions.yaml
│   │   │   │   ├── daily.yaml
│   │   │   │   ├── daily_events.yaml
│   │   │   │   ├── economy.yaml
│   │   │   │   ├── elections.yaml
│   │   │   │   ├── jobs.yaml
│   │   │   │   ├── market.yaml
│   │   │   │   ├── migration.yaml
│   │   │   │   ├── missions.yaml
│   │   │   │   ├── national_project.yaml
│   │   │   │   ├── news.yaml
│   │   │   │   ├── phase3.yaml
│   │   │   │   ├── progression.yaml
│   │   │   │   ├── unlocks.yaml
│   │   │   │   └── xp.yaml
│   │   │   ├── __init__.py
│   │   │   └── loader.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── migrator.py
│   │   │   └── pool.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── player.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── admin_repo.py
│   │   │   ├── country_repo.py
│   │   │   ├── election_repo.py
│   │   │   ├── group_repo.py
│   │   │   ├── ledger_repo.py
│   │   │   ├── mission_repo.py
│   │   │   ├── outbox_repo.py
│   │   │   ├── player_repo.py
│   │   │   ├── production_repo.py
│   │   │   ├── progression_repo.py
│   │   │   ├── project_repo.py
│   │   │   ├── ui_state_repo.py
│   │   │   └── world_access_repo.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── commerce.py
│   │   │   ├── content_filter.py
│   │   │   ├── country.py
│   │   │   ├── country_economy.py
│   │   │   ├── country_identity.py
│   │   │   ├── country_missions.py
│   │   │   ├── country_realism.py
│   │   │   ├── daily.py
│   │   │   ├── economy.py
│   │   │   ├── elections.py
│   │   │   ├── engagement.py
│   │   │   ├── governance.py
│   │   │   ├── live_market.py
│   │   │   ├── market_chart.py
│   │   │   ├── migration.py
│   │   │   ├── missions.py
│   │   │   ├── national_project.py
│   │   │   ├── news.py
│   │   │   ├── personal_economy.py
│   │   │   ├── production.py
│   │   │   ├── progression.py
│   │   │   ├── scheduler_ops.py
│   │   │   ├── unlocks.py
│   │   │   ├── usd_market.py
│   │   │   ├── world_access.py
│   │   │   └── xp.py
│   │   ├── ui/
│   │   │   ├── __init__.py
│   │   │   ├── buttons.py
│   │   │   ├── callbacks.py
│   │   │   └── panels.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── clock.py
│   │   │   └── fmt.py
│   │   ├── __init__.py
│   │   ├── logging.py
│   │   ├── runtime_status.py
│   │   ├── settings.py
│   │   └── supervisor.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_admin_2026_hardening.py
│   ├── test_all_keyboard_states.py
│   ├── test_callbacks.py
│   ├── test_clock.py
│   ├── test_commerce.py
│   ├── test_commerce_regressions.py
│   ├── test_config.py
│   ├── test_content_filter.py
│   ├── test_country_realism_contracts.py
│   ├── test_daily.py
│   ├── test_fmt.py
│   ├── test_glass_buttons.py
│   ├── test_governance.py
│   ├── test_hardening_contracts.py
│   ├── test_interval_bindings.py
│   ├── test_live_market.py
│   ├── test_market_chart_contracts.py
│   ├── test_message_driven_bots.py
│   ├── test_migrator.py
│   ├── test_missions.py
│   ├── test_outbox_repo.py
│   ├── test_panel_edit.py
│   ├── test_persian_button_contracts.py
│   ├── test_phase3_phase4_contracts.py
│   ├── test_phase5_config.py
│   ├── test_production_security.py
│   ├── test_progression.py
│   ├── test_project_integrity.py
│   ├── test_scaling_migration.py
│   ├── test_supervisor.py
│   ├── test_teleworld_onboarding.py
│   ├── test_teleworld_start.py
│   ├── test_token_isolation.py
│   ├── test_unlocks.py
│   ├── test_world_access_contracts.py
│   └── test_xp.py
├── .dockerignore
├── .env.example
├── .gitignore
├── AUDIT_AND_DEPLOY_FA_2026-07-27.md
├── AUDIT_FINAL_FA_2026-07-27.md
├── AUDIT_STATUS.md
├── CHANGELOG_FA.md
├── CHANGELOG_FA_2026-07-27.md
├── CHANGELOG_FA_2026-07-27_V2.md
├── DELIVERY.md
├── Dockerfile
├── dump.py
├── MANIFEST.sha256
├── pyproject.toml
├── README.md
├── README_FA.md
├── RELEASE_2026_07_27_FA.md
├── RELEASE_AUDIT_FA.md
├── RELEASE_AUDIT_FA_2026-07-27.md
├── RELEASE_COMMERCE_FA.md
├── RELEASE_NOTES_FA.md
├── RELEASE_SCALING_MIGRATION_FA.md
├── RELEASE_V2_FA.md
├── render.yaml
├── requirements.txt
├── run.py
├── telelife_complete_dump.md
├── TeleLife_Master_Plan.md
├── TEST_RESULTS_FA_2026-07-27.md
└── UI_REDESIGN_FA.md
```

## محتوای فایل‌ها


### `.dockerignore`

_[این فایل باینری/غیرمتنی تشخیص داده شد و محتوایش درج نشد]_


### `.env.example`

```
ENVIRONMENT=development
LOG_LEVEL=INFO
DEBUG=false
DATABASE_URL=postgresql://postgres.PROJECT_REF:PASSWORD@POOLER_HOST:6543/postgres?sslmode=require
DB_POOL_MIN=1
DB_POOL_MAX=4
DB_COMMAND_TIMEOUT=15
DB_STATEMENT_CACHE_SIZE=0
DB_MAX_INACTIVE_SECONDS=60
TELELIFE_BOT_TOKEN=
TELEWORLD_BOT_TOKEN=
GLOBAL_NEWS_CHAT_ID=
RUN_MODE=polling
PORT=8000
HOST=0.0.0.0
ADMIN_USERNAME=
ADMIN_PASSWORD=
MEMORY_WARNING_MB=450
# Telegram Stars uses currency XTR and an empty provider token.
AD_REVIEW_NOTIFICATION_CHAT_ID=

# Live USDT/IRT source (validated server-side; last good value is retained on failure).
USDT_RATE_URL=https://api.zipodo.ir/usdt/
```

### `.gitignore`

```
__pycache__/
*.py[cod]
.env
.venv/
venv/
.pytest_cache/
.mypy_cache/
.ruff_cache/
*.log
```

### `apps\__init__.py`

```python
"""Package apps."""
```

### `apps\admin\__init__.py`

```python
"""Package apps.admin."""
```

### `apps\admin\auth.py`

```python
"""Authentication dependencies shared by the admin application and routers."""

from __future__ import annotations

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from packages.core.settings import get_settings

security = HTTPBasic(auto_error=False)


def require_admin(
    credentials: Annotated[HTTPBasicCredentials | None, Depends(security)],
) -> str:
    """Authenticate an admin with constant-time credential comparisons."""
    settings = get_settings()
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized", headers={"WWW-Authenticate": "Basic"})
    username_ok = secrets.compare_digest(credentials.username, settings.admin_username)
    password_ok = secrets.compare_digest(credentials.password, settings.admin_password)
    if not (username_ok and password_ok):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
```

### `apps\admin\main.py`

```python
"""Authenticated, lightweight administration command center."""
from __future__ import annotations
from pathlib import Path
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from apps.admin.auth import require_admin
from apps.admin.routers.country_admin import router as country_admin_router
from packages.core import db
from packages.core.repositories import admin_repo
from packages.core.runtime_status import snapshot

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app = FastAPI(title="TeleLife Admin", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.include_router(country_admin_router)

@app.middleware("http")
async def security_headers(request: Request, call_next):  # type: ignore[no-untyped-def]
    # JSON APIs already trigger CORS preflight; this also protects legacy form routes.
    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        origin = request.headers.get("origin")
        host = request.headers.get("host")
        if origin and host and origin.split("://", 1)[-1] != host:
            return JSONResponse({"detail": "درخواست از مبدأ نامعتبر رد شد."}, status_code=403)
    response: Response = await call_next(request)
    response.headers.update({
        "X-Content-Type-Options": "nosniff", "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer", "Cache-Control": "no-store",
        "Content-Security-Policy": "default-src 'self'; style-src 'self' 'unsafe-inline'; "
          "script-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'",
    })
    return response

@app.get("/healthz")
async def healthz() -> JSONResponse:
    db_ok = await db.healthcheck(); services = snapshot()
    admin_ok = services.get("admin", {}).get("status") in {"starting", "healthy"}
    code = status.HTTP_200_OK if db_ok and admin_ok else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse({"ok": db_ok and admin_ok, "database": db_ok, "services": services}, code)

@app.get("/readyz")
async def readyz() -> JSONResponse:
    db_ok = await db.healthcheck()
    return JSONResponse({"ready": db_ok}, status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, _: str = Depends(require_admin)) -> HTMLResponse:
    row = await admin_repo.dashboard_stats()
    return templates.TemplateResponse(request, "dashboard.html", {"stats": dict(row) if row else {}})
```

### `apps\admin\routers\__init__.py`

```python
"""Package apps.admin.routers."""
```

### `apps\admin\routers\country_admin.py`

```python
"""Authenticated command-center APIs with audited mutations."""
from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Depends, Form, HTTPException, Query
from pydantic import BaseModel, Field

from apps.admin.auth import require_admin
from packages.core.repositories import admin_repo
from packages.core.services import admin, commerce, live_market, scheduler_ops, engagement
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
    return {"applied": await admin.feature(actor, key, body.enabled, str(uuid4()))}

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
    return {"applied":await admin.feature(actor,"usd_market_frozen",body.enabled,str(uuid4()))}

@router.post("/operations/jobs/{job_name}/run")
async def run_job(job_name: str, actor: AdminActor) -> dict[str, bool]:
    allowed={"zipodo_rate":live_market.sync,"engagement":engagement.minute_tick,"market_snapshot":admin_repo.capture_market_snapshot}
    if job_name not in allowed:raise HTTPException(400,"این Job برای اجرای دستی مجاز نیست.")
    result=await scheduler_ops.run(f"manual:{job_name}",allowed[job_name])
    if result is None:raise HTTPException(502,"Job اجرا نشد؛ جزئیات خطا در عملیات زنده ثبت شد.")
    return {"completed":True}

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

@router.get("/ads")
async def ads(limit: Annotated[int,Query(ge=1,le=500)]=100)->list[dict[str,object]]:
    return [dict(row) for row in await admin_repo.ads(limit)]

@router.post("/ads")
async def create_ad(body:AdBody,actor:AdminActor)->dict[str,int]:
    try:return {"id":await admin.create_ad(actor,body.title,body.text,body.destination,body.scheduled_at,body.repeat_minutes,str(uuid4()))}
    except ValueError as exc:raise fail(exc) from exc

@router.post("/ads/{ad_id}/queue")
async def queue_ad(ad_id:int,actor:AdminActor)->dict[str,bool]:
    try:return {"queued":await admin.queue_ad(actor,ad_id,str(uuid4()))}
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
 row=await commerce.approve_ad(ad_id,actor,body.note)
 if not row:raise HTTPException(409,"وضعیت درخواست قابل تأیید نیست.")
 owner=await admin_repo.ad_owner(ad_id);payload,stars,title=await commerce.ad_invoice(ad_id,int(owner["telegram_id"]))
 from telegram import Bot,LabeledPrice
 async with Bot(get_settings().telelife_bot_token) as bot:
  await bot.send_invoice(chat_id=owner["telegram_id"],title=f"پرداخت تبلیغ: {title}",description="درخواست تأیید شد. این صورتحساب ۴۸ ساعت اعتبار دارد.",payload=payload,currency="XTR",prices=[LabeledPrice("بسته تبلیغ",stars)],provider_token="")
 return {"approved":True}
@router.post("/ad-requests/{ad_id}/reject")
async def reject_ad_request(ad_id:int,body:AdRejectBody,actor:AdminActor)->dict[str,bool]:
 row=await commerce.reject_ad(ad_id,actor,body.reason)
 if row:
  from telegram import Bot
  owner=await admin_repo.ad_owner(ad_id)
  async with Bot(get_settings().telelife_bot_token) as bot:await bot.send_message(owner["telegram_id"],f"✏️ درخواست تبلیغ #{ad_id} نیاز به اصلاح دارد:\n\n{body.reason}\n\nبرای اصلاح، درخواست تازه‌ای از بخش تبلیغات ثبت کن.")
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
```

### `apps\admin\static\admin.css`

```css
@font-face{font-family:TL;src:local("Vazirmatn"),local("Tahoma")}*{box-sizing:border-box}html{scroll-behavior:smooth}:root{color-scheme:dark;--ink:#eaf5ff;--muted:#7e99ad;--dim:#496477;--cyan:#3ee6d0;--blue:#4ba3ff;--violet:#8c7cff;--rose:#ff6685;--bg:#06111d;--panel:rgba(11,29,45,.72);--line:rgba(151,208,239,.13);--shadow:0 24px 80px rgba(0,0,0,.28)}body{margin:0;background:radial-gradient(circle at 72% -20%,#123c55 0,transparent 38%),radial-gradient(circle at 12% 92%,#151f4a 0,transparent 34%),var(--bg);color:var(--ink);font-family:TL,"Segoe UI",sans-serif;min-height:100vh}.noise{position:fixed;inset:0;pointer-events:none;opacity:.12;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.16'/%3E%3C/svg%3E")}.rail{position:fixed;right:0;top:0;bottom:0;width:248px;border-left:1px solid var(--line);background:rgba(4,15,25,.78);backdrop-filter:blur(24px);padding:28px 18px;display:flex;flex-direction:column;z-index:10}.brand{display:flex;align-items:center;gap:12px;color:var(--ink);text-decoration:none;padding:0 10px 32px}.brand-mark{width:43px;height:43px;border:1px solid #5ce6dc66;border-radius:14px;display:grid;place-items:center;background:linear-gradient(145deg,#1d4f63,#0a2535);box-shadow:inset 0 1px #ffffff22,0 10px 30px #00b8ab18;color:var(--cyan);font:800 22px Georgia}.brand b{display:block;font-size:17px;letter-spacing:.4px}.brand small{color:var(--dim);letter-spacing:3px;font-size:8px}nav{display:grid;gap:7px}.nav{appearance:none;border:0;background:transparent;color:var(--muted);display:flex;align-items:center;gap:14px;border-radius:13px;padding:12px 14px;font:600 14px TL;cursor:pointer;text-align:right;transition:.2s}.nav span{font-size:19px;color:#6289a2;width:22px}.nav em{font-style:normal}.nav:hover,.nav.active{color:var(--ink);background:linear-gradient(90deg,rgba(62,230,208,.13),rgba(75,163,255,.04));box-shadow:inset -2px 0 var(--cyan)}.nav.active span{color:var(--cyan)}.rail-foot{margin-top:auto;border-top:1px solid var(--line);padding:20px 10px 0;display:grid;grid-template-columns:10px 1fr;align-items:center;gap:3px 9px;color:var(--muted);font-size:12px}.rail-foot small{grid-column:2;color:var(--dim);direction:ltr;text-align:right}.pulse,.live i{width:8px;height:8px;border-radius:50%;background:var(--cyan);box-shadow:0 0 14px var(--cyan);animation:pulse 2s infinite}@keyframes pulse{50%{opacity:.35;transform:scale(.75)}}.shell{margin-right:248px;min-height:100vh;padding:0 38px 60px}.topbar{height:112px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);margin-bottom:30px}.eyebrow{color:var(--cyan);font-size:10px;letter-spacing:1.6px;margin:0 0 8px;font-weight:700}.topbar h1,.section-lead h2{margin:0;font-size:27px;letter-spacing:-.8px}.top-actions{display:flex;gap:10px}.live,.icon-btn,select{border:1px solid var(--line);background:#0a1d2b99;color:var(--muted);border-radius:11px;height:38px;display:flex;align-items:center;gap:9px;padding:0 13px}.live{font:700 9px monospace;letter-spacing:2px}.live i{width:6px;height:6px}.icon-btn{font-size:20px;cursor:pointer}.view{display:none;animation:rise .35s ease}.view.active{display:block}@keyframes rise{from{opacity:0;transform:translateY(8px)}}.hero-grid{display:grid;grid-template-columns:minmax(0,1.8fr) minmax(260px,.8fr);gap:18px}.hero-card,.signal-card,.panel,.metric-grid article,.country-card,.market-cards article{border:1px solid var(--line);background:linear-gradient(145deg,rgba(14,39,57,.8),rgba(7,21,34,.72));backdrop-filter:blur(18px);box-shadow:var(--shadow);border-radius:20px}.hero-card{min-height:230px;padding:34px;display:flex;align-items:center;justify-content:space-between;overflow:hidden;position:relative}.hero-card:before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,transparent 40%,rgba(62,230,208,.06));pointer-events:none}.hero-card strong{display:block;font:300 clamp(38px,6vw,75px) TL;margin:8px 0;letter-spacing:-4px}.hero-card span{color:var(--muted);font-size:12px}.orbit{width:170px;height:170px;border:1px solid #68e8dc28;border-radius:50%;display:grid;place-items:center;position:relative;background:radial-gradient(circle,#39d8ca18,transparent 62%)}.orbit:before,.orbit:after{content:"";position:absolute;border:1px solid #75bfff1c;border-radius:50%;inset:18px}.orbit:after{inset:42px}.orbit b{font:700 24px Georgia;color:var(--cyan);text-shadow:0 0 25px #34e6d1}.orbit i{position:absolute;width:6px;height:6px;background:var(--cyan);border-radius:50%;box-shadow:0 0 12px var(--cyan)}.orbit i:nth-of-type(1){top:13px}.orbit i:nth-of-type(2){bottom:25px;left:17px;background:var(--blue)}.orbit i:nth-of-type(3){right:0;background:var(--violet)}.signal-card{padding:27px}.signal-card>p{font-size:12px;color:var(--muted);margin:0 0 20px}.service-radar{display:grid;gap:11px}.service-radar span{display:flex;justify-content:space-between;align-items:center;padding:10px 12px;background:#061623;border:1px solid var(--line);border-radius:10px;font-size:11px}.service-radar i{font-style:normal;color:var(--cyan)}.metric-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:16px 0}.metric-grid article{padding:21px}.metric-grid span,.metric-grid small{display:block;color:var(--muted);font-size:11px}.metric-grid strong{display:block;font-size:28px;font-weight:500;margin:8px 0}.metric-grid small{color:var(--dim)}.split{display:grid;grid-template-columns:1.55fr 1fr;gap:16px}.panel{padding:24px}.panel-head,.section-lead{display:flex;align-items:center;justify-content:space-between;gap:20px}.panel-head{margin-bottom:18px}.panel-head h2{font-size:17px;margin:0}.text-btn{border:0;background:transparent;color:var(--cyan);cursor:pointer;font:11px TL}.quick-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.quick-grid button{background:#081c2b;border:1px solid var(--line);border-radius:13px;padding:16px;color:var(--ink);font:700 12px TL;text-align:right;cursor:pointer}.quick-grid small{display:block;color:var(--dim);margin-top:7px;font-weight:400}.chart-wrap{height:250px;position:relative;direction:ltr}.chart-wrap.large{height:390px}.chart-wrap svg{width:100%;height:100%;overflow:visible}.chart-wrap .gridline{stroke:#bde4ff12}.chart-wrap .area{fill:url(#areaGradient)}.chart-wrap .line{fill:none;stroke:var(--cyan);stroke-width:2.4;filter:drop-shadow(0 0 7px #3ee6d077)}.chart-wrap .dot{fill:var(--cyan);stroke:#06111d;stroke-width:2}.chart-label{position:absolute;direction:rtl;color:var(--muted);font-size:10px}.empty{height:100%;display:grid;place-items:center;color:var(--dim);font-size:12px;border:1px dashed var(--line);border-radius:14px}.section-lead{margin-bottom:22px}.section-lead p:not(.eyebrow){color:var(--muted);margin:7px 0 0;font-size:12px}.section-lead select{font:12px TL}.market-stage{margin-bottom:16px}.asset-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}.asset-tabs button{border:1px solid var(--line);background:#081b29;color:var(--muted);border-radius:10px;padding:9px 13px;font:11px TL;cursor:pointer}.asset-tabs button.active{background:#0e3c46;color:var(--cyan);border-color:#3ee6d044}.market-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}.market-cards article{padding:19px;display:grid;gap:7px}.market-cards strong{font-size:23px;font-weight:500}.market-cards span,.market-cards small{color:var(--muted);font-size:11px}.market-cards button{margin-top:6px}.search{display:flex;align-items:center;border:1px solid var(--line);background:#081b29;border-radius:12px;padding:0 13px;width:min(340px,100%)}input,textarea{width:100%;border:1px solid var(--line);background:#071824;color:var(--ink);border-radius:11px;padding:11px 13px;font:12px TL;outline:none}input:focus,textarea:focus{border-color:#3ee6d066;box-shadow:0 0 0 3px #3ee6d00c}.search input{border:0;background:transparent}.table-panel{padding:0;overflow:hidden}.table-scroll{overflow:auto}table{width:100%;border-collapse:collapse;min-width:870px}th{color:var(--dim);font-size:10px;text-align:right;padding:16px;border-bottom:1px solid var(--line);font-weight:600}td{padding:16px;border-bottom:1px solid #bfe5ff0b;color:var(--muted);font-size:11px}td b{color:var(--ink);display:block;font-size:12px;margin-bottom:4px}.badge{display:inline-flex;padding:5px 8px;border-radius:20px;background:#29d6bd16;color:var(--cyan)}.badge.danger{background:#ff668518;color:var(--rose)}.row-actions{display:flex;gap:6px}.small-btn,.primary,.secondary{border:1px solid var(--line);border-radius:9px;background:#0b2433;color:var(--ink);padding:8px 11px;font:10px TL;cursor:pointer}.small-btn.danger{color:var(--rose)}.primary{background:linear-gradient(135deg,#2bc8b7,#268cd3);border:0;color:#02131d;font-weight:800;padding:11px 17px}.secondary{color:var(--muted)}.country-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}.country-card{padding:22px}.country-top{display:flex;justify-content:space-between;align-items:start}.country-card h3{margin:0;font-size:19px}.country-card p{color:var(--muted);font-size:11px}.treasury{font-size:24px;margin:20px 0 5px}.resource-row{display:flex;gap:7px;flex-wrap:wrap;margin:15px 0}.resource-row span{background:#071a28;border:1px solid var(--line);border-radius:8px;padding:7px 9px;font-size:10px;color:var(--muted)}.country-actions{display:flex;gap:7px;flex-wrap:wrap}.news-layout{grid-template-columns:.85fr 1.4fr}.composer{display:grid;gap:15px}.composer label{font-size:11px;color:var(--muted)}.composer label small{color:var(--dim);margin-right:5px}.composer textarea{height:180px;resize:vertical;margin-top:8px}.news-list{display:grid;gap:8px;max-height:440px;overflow:auto}.news-item{padding:12px;border:1px solid var(--line);border-radius:11px;background:#071824;display:grid;grid-template-columns:1fr auto;gap:6px}.news-item p{margin:0;color:var(--ink);font-size:11px}.news-item small{color:var(--dim);font-size:9px}dialog{border:1px solid var(--line);border-radius:20px;background:#081b29;color:var(--ink);box-shadow:0 30px 100px #000b;max-width:430px;width:calc(100% - 30px);padding:0}dialog::backdrop{background:#020a10cc;backdrop-filter:blur(6px)}dialog form{padding:27px;position:relative}dialog h2{margin:0 0 22px}.dialog-close{position:absolute;left:16px;top:14px;background:transparent;border:0;color:var(--muted);font-size:25px;cursor:pointer}.dialog-actions{display:flex;justify-content:flex-end;gap:8px;margin-top:20px}#dialog-fields{display:grid;gap:11px}#dialog-fields label{color:var(--muted);font-size:11px;display:grid;gap:7px}#toast{position:fixed;left:25px;bottom:25px;z-index:50;background:#0c2836;border:1px solid #3ee6d044;border-radius:12px;padding:12px 18px;color:var(--ink);font-size:11px;box-shadow:var(--shadow);opacity:0;transform:translateY(12px);pointer-events:none;transition:.25s}#toast.show{opacity:1;transform:none}#toast.error{border-color:#ff668566;color:#ff9eb2}@media(max-width:1050px){.rail{width:82px;padding:25px 11px}.brand span:last-child,.nav em,.rail-foot span,.rail-foot small{display:none}.brand{padding:0 8px 28px}.nav{justify-content:center}.shell{margin-right:82px;padding:0 24px 50px}.hero-grid,.split{grid-template-columns:1fr}.metric-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:650px){.rail{right:0;left:0;top:auto;height:70px;width:auto;border-left:0;border-top:1px solid var(--line);padding:8px 10px;flex-direction:row}.brand,.rail-foot{display:none}.rail nav{display:flex;width:100%;justify-content:space-around}.nav{padding:8px 10px;display:grid;gap:2px;justify-items:center}.nav em{display:block;font-size:8px}.nav.active{box-shadow:inset 0 -2px var(--cyan)}.shell{margin:0;padding:0 15px 92px}.topbar{height:88px}.topbar h1{font-size:21px}.hero-card{padding:24px;min-height:190px}.orbit{width:95px;height:95px}.hero-card strong{font-size:36px;letter-spacing:-2px}.metric-grid{grid-template-columns:1fr 1fr}.metric-grid article{padding:16px}.market-cards,.country-grid{grid-template-columns:1fr}.section-lead{align-items:flex-start;flex-direction:column}.search{width:100%}.chart-wrap.large{height:300px}.panel{padding:18px}}
/* Advertising workspace: denser editorial rhythm and clearer focus feedback. */
#view-ads .composer{border-top:2px solid var(--violet)}
#view-ads .news-item{transition:transform .18s ease,border-color .18s ease}
#view-ads .news-item:hover{transform:translateY(-2px);border-color:#8c7cff55}
button:focus-visible,input:focus-visible,textarea:focus-visible,select:focus-visible{outline:2px solid var(--cyan);outline-offset:3px}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
.request-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:16px}.request-card{padding:0;overflow:hidden}.request-card>img{width:100%;height:190px;object-fit:cover;background:#061623}.request-card>div{padding:20px}.request-card h3{margin:4px 0 10px}.request-card p{color:var(--muted);font-size:12px;line-height:1.8}.request-card a{display:block;color:var(--cyan);font-size:11px;direction:ltr;text-align:left;overflow-wrap:anywhere;margin:10px 0}.request-card small{display:block;color:var(--dim);margin:12px 0}
/* Operations room — inspired by an exchange tape, not a generic KPI dashboard. */
.rate-ticker{position:relative;overflow:hidden;display:flex;justify-content:space-between;align-items:center;gap:24px;padding:28px 32px;margin-bottom:16px;border-radius:6px;background:linear-gradient(100deg,#071824 0 62%,#0b2630 100%)}
.rate-ticker:after{content:"";position:absolute;inset:auto 0 0;height:2px;background:linear-gradient(90deg,transparent,var(--cyan),var(--blue),transparent);animation:tape 4s linear infinite}.rate-ticker strong{display:block;font:500 clamp(32px,5vw,64px) JetBrains Mono,monospace;letter-spacing:-3px}.rate-ticker small{color:var(--muted)}.source-seal{font:700 10px JetBrains Mono,monospace;color:var(--cyan);letter-spacing:2px}.ticker-actions{display:flex;gap:8px;flex-wrap:wrap}.sparkline{position:absolute;inset:0 43% 0 0;opacity:.16;pointer-events:none}.ops-head{padding:22px 24px 0}.legend{font-size:10px;color:var(--muted);display:flex;gap:7px;align-items:center}.legend i{width:7px;height:7px;border-radius:50%}.legend .ok{background:var(--cyan)}.legend .bad{background:var(--rose)}.job-error{max-width:320px;white-space:normal;color:#ff9eb2}.source-stale{color:#ffbd70!important}.source-live{color:var(--cyan)!important}@keyframes tape{from{transform:translateX(100%)}to{transform:translateX(-100%)}}@media(max-width:650px){.rate-ticker{align-items:flex-start;flex-direction:column;padding:22px}.rate-ticker strong{letter-spacing:-2px}.sparkline{inset:0;opacity:.08}}/* 2026 Command Atlas — redesigned around retention, auditability and calm density. */
:root{--bg:#071017;--panel:#0b1821;--panel-2:#0f212c;--ink:#eaf3f5;--muted:#8aa1aa;--dim:#58707a;--cyan:#43d6c5;--blue:#72a7ff;--violet:#b394ff;--rose:#ff718d;--amber:#f4bd68;--line:rgba(145,187,198,.15);--shadow:0 22px 60px rgba(0,0,0,.26)}
body{background:linear-gradient(125deg,#071017 0 57%,#08151e 57% 100%);font-family:TL,"Segoe UI",sans-serif}.noise{opacity:.055}.rail{width:264px;background:rgba(5,14,20,.94);border-left-color:rgba(91,214,198,.16);padding:24px 16px}.shell{margin-right:264px;max-width:1800px}.brand-mark{border-radius:7px;transform:rotate(-7deg);background:#102b31}.brand small{color:var(--cyan)}nav{gap:3px;overflow:auto}.nav{border-radius:8px;padding:10px 13px}.nav:hover,.nav.active{background:#10232c;box-shadow:inset -3px 0 var(--cyan)}.topbar{height:96px}.hero-card,.signal-card,.panel,.metric-grid article,.country-card,.market-cards article{border-radius:10px;background:linear-gradient(145deg,rgba(14,31,40,.94),rgba(8,21,29,.95));box-shadow:0 14px 42px rgba(0,0,0,.2)}.hero-card{border-top:3px solid var(--cyan)}.orbit{border-radius:8px;transform:rotate(8deg)}.orbit:before,.orbit:after{border-radius:8px}.primary,.small-btn,.secondary,.quick-grid button,.asset-tabs button{border-radius:7px}.metric-grid-five{grid-template-columns:repeat(5,1fr)}.metric-grid article{position:relative;overflow:hidden}.metric-grid article:after{content:"";position:absolute;right:0;bottom:0;width:35%;height:2px;background:var(--cyan)}
.funnel{display:grid;gap:12px}.funnel-row{display:grid;grid-template-columns:140px 1fr 58px;gap:12px;align-items:center}.funnel-row span{font-size:11px;color:var(--muted)}.funnel-track{height:13px;background:#071219;border:1px solid var(--line);overflow:hidden}.funnel-fill{height:100%;background:linear-gradient(90deg,var(--cyan),var(--blue));transform-origin:right}.funnel-row b{font:600 12px "JetBrains Mono",monospace;text-align:left}.insight-list{display:grid;gap:10px}.insight{display:grid;grid-template-columns:9px 1fr;gap:12px;padding:13px;background:#08171f;border:1px solid var(--line)}.insight i{width:7px;height:7px;margin-top:7px;border-radius:50%;background:var(--cyan)}.insight.warn i{background:var(--amber)}.insight strong{font-size:12px}.insight p{margin:4px 0 0;color:var(--muted);font-size:11px;line-height:1.8}
.control-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.control-card{border:1px solid var(--line);background:var(--panel);padding:22px;display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center}.control-card h3{margin:0 0 6px}.control-card p{margin:0;color:var(--muted);font-size:11px}.toggle{width:52px;height:28px;border:1px solid var(--line);background:#061219;padding:3px;cursor:pointer}.toggle i{display:block;width:20px;height:20px;background:var(--dim);transition:.2s}.toggle.on{background:#173b39;border-color:#43d6c566}.toggle.on i{transform:translateX(-24px);background:var(--cyan)}.safety-note{display:flex;gap:16px;align-items:center;margin-top:16px}.safety-mark{font:700 28px Georgia;color:var(--amber);border:1px solid #f4bd6844;width:46px;height:46px;display:grid;place-items:center}.safety-note h3,.safety-note p{margin:0}.safety-note p{color:var(--muted);font-size:11px;margin-top:5px}.amount-positive{color:var(--cyan)}.amount-negative{color:var(--rose)}.mono{font-family:"JetBrains Mono",monospace;direction:ltr;text-align:right}.danger-zone{border-color:#ff718d55!important}.danger-zone h3{color:#ff9aae}
@media(max-width:1200px){.metric-grid-five{grid-template-columns:repeat(3,1fr)}}@media(max-width:1050px){.rail{width:82px}.shell{margin-right:82px}.control-grid{grid-template-columns:1fr}}@media(max-width:650px){.rail{width:auto}.shell{margin:0}.metric-grid-five{grid-template-columns:1fr 1fr}.funnel-row{grid-template-columns:92px 1fr 48px}.control-card{padding:16px}}
```

### `apps\admin\static\admin.js`

```javascript
"use strict";
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const fa=new Intl.NumberFormat("fa-IR"), money=n=>`${fa.format(Number(n||0))} تومان`;
const state={market:[],asset:"USD",ops:null,opsTimer:null};
function toast(message,error=false){const el=$("#toast");el.textContent=message;el.className=error?"show error":"show";clearTimeout(el._t);el._t=setTimeout(()=>el.className="",3500)}
async function api(url,options={}){const res=await fetch(url,{headers:{"Content-Type":"application/json",...(options.headers||{})},...options});if(res.status===401){location.reload();throw Error("ورود منقضی شده است")};const data=await res.json().catch(()=>({}));if(!res.ok)throw Error(typeof data.detail==="string"?data.detail:"خطا در ارتباط با سرور");return data}
function esc(v){return String(v??"").replace(/[&<>'"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[c]))}
function date(v){if(!v)return "—";return new Intl.DateTimeFormat("fa-IR",{dateStyle:"short",timeStyle:"short"}).format(new Date(v))}
function go(name){$$('.view').forEach(v=>v.classList.toggle('active',v.id===`view-${name}`));$$('.nav').forEach(v=>v.classList.toggle('active',v.dataset.view===name));$("#view-title").textContent={overview:"مرکز فرماندهی",market:"بازار دارایی‌ها",players:"مدیریت بازیکنان",countries:"مدیریت کشورها",news:"اتاق خبر",ads:"مرکز تبلیغات",requests:"بازبینی تبلیغات",operations:"عملیات زنده",engagement:"ماندگاری کاربران",ledger:"دفتر اقتصاد",audit:"گزارش حسابرسی",controls:"کنترل سامانه"}[name];history.replaceState(null,"",`#${name}`);load(name)}
$$('.nav').forEach(b=>b.onclick=()=>go(b.dataset.view));$$('[data-go]').forEach(b=>b.onclick=()=>go(b.dataset.go));
async function overview(){const [o,h]=await Promise.all([api('/api/admin/overview'),api('/healthz')]);$$('[data-stat]').forEach(el=>el.textContent=fa.format(o[el.dataset.stat]||0));const names={admin:'پنل مدیریت',scheduler:'زمان‌بند',telelife:'TeleLife',teleworld:'TeleWorld'};$("#service-radar").innerHTML=Object.entries(h.services||{}).map(([k,v])=>`<span>${names[k]||esc(k)}<i>${v.status==='healthy'?'سالم':esc(v.status)}</i></span>`).join('')||'<span>اطلاعات سرویس موجود نیست</span>';await market(true)}
function chart(target,points){const el=$(target);if(!points?.length){el.innerHTML='<div class="empty">هنوز نقطه تاریخی ثبت نشده است</div>';return}const w=900,h=310,p=28,vals=points.map(x=>Number(x.price)),min=Math.min(...vals),max=Math.max(...vals),spread=Math.max(max-min,1);const xy=points.map((x,i)=>[p+i*(w-2*p)/Math.max(points.length-1,1),h-p-(Number(x.price)-min)*(h-2*p)/spread]);const path=xy.map((v,i)=>`${i?'L':'M'}${v[0].toFixed(1)},${v[1].toFixed(1)}`).join(' ');const area=`${path} L${xy.at(-1)[0]},${h-p} L${xy[0][0]},${h-p} Z`;el.innerHTML=`<svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="none" role="img" aria-label="نمودار قیمت"><defs><linearGradient id="areaGradient" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3ee6d0" stop-opacity=".22"/><stop offset="1" stop-color="#3ee6d0" stop-opacity="0"/></linearGradient></defs>${[.2,.4,.6,.8].map(v=>`<line class="gridline" x1="${p}" x2="${w-p}" y1="${h*v}" y2="${h*v}"/>`).join('')}<path class="area" d="${area}"/><path class="line" d="${path}"/>${xy.map(v=>`<circle class="dot" cx="${v[0]}" cy="${v[1]}" r="3.5"/>`).join('')}</svg><span class="chart-label" style="top:6px;right:8px">${money(max)}</span><span class="chart-label" style="bottom:6px;right:8px">${money(min)}</span>`}
async function market(mini=false){state.market=await api(`/api/admin/market?hours=${$("#market-range")?.value||24}`);if(!state.market.length)return;let selected=state.market.find(x=>x.asset_code===state.asset)||state.market[0];state.asset=selected.asset_code;chart(mini?'#mini-chart':'#market-chart',selected.points?.length?selected.points:[{price:selected.current_price_toman,time:selected.updated_at}]);if(mini)return;$("#market-tabs").innerHTML=state.market.map(x=>`<button class="${x.asset_code===state.asset?'active':''}" data-asset="${esc(x.asset_code)}">${esc(x.title_fa)}</button>`).join('');$("#market-cards").innerHTML=state.market.map(x=>`<article><span>${esc(x.title_fa)} · ${esc(x.asset_code)}</span><strong>${money(x.current_price_toman)}</strong><small>آخرین تغییر: ${date(x.updated_at)}</small><button class="small-btn" data-price="${esc(x.asset_code)}">ثبت قیمت جدید</button></article>`).join('');$$('[data-asset]').forEach(b=>b.onclick=()=>{state.asset=b.dataset.asset;market()});$$('[data-price]').forEach(b=>b.onclick=()=>priceDialog(b.dataset.price))}
function openDialog(title,kicker,fields,confirm){$("#dialog-title").textContent=title;$("#dialog-kicker").textContent=kicker;$("#dialog-fields").innerHTML=fields;$("#dialog-confirm").onclick=confirm;$("#action-dialog").showModal()}
function priceDialog(asset){const row=state.market.find(x=>x.asset_code===asset);openDialog(`قیمت ${row?.title_fa||asset}`,"ثبت نقطه بازار",`<label>قیمت جدید به تومان<input id="f-price" type="number" min="1" value="${row?.current_price_toman||1}"></label>`,async()=>{try{await api(`/api/admin/market/${encodeURIComponent(asset)}`,{method:'POST',body:JSON.stringify({price:Number($("#f-price").value)})});$("#action-dialog").close();toast("قیمت ثبت شد");await market()}catch(e){toast(e.message,true)}})}
async function players(){const q=encodeURIComponent($("#player-search").value.trim()),rows=await api(`/api/admin/users?limit=150&q=${q}`);$("#players-body").innerHTML=rows.map(x=>`<tr><td><b>${esc(x.first_name)}</b>@${esc(x.username||'—')} · #${x.id}<br><small>TG ${x.telegram_id}</small></td><td><b>سطح ${fa.format(x.level)}</b>${fa.format(x.xp)} XP</td><td><b>${money(Number(x.wallet_toman)+Number(x.savings_toman))}</b>${fa.format(x.usd_cents)} سنت</td><td>${date(x.last_seen_at)}</td><td><span class="badge ${x.is_banned?'danger':''}">${x.is_banned?'مسدود':'فعال'}</span></td><td><div class="row-actions"><button class="small-btn" data-xp="${x.id}">XP</button><button class="small-btn ${x.is_banned?'':'danger'}" data-ban="${x.id}" data-banned="${x.is_banned}">${x.is_banned?'رفع مسدودی':'مسدود'}</button></div></td></tr>`).join('')||'<tr><td colspan="6">بازیکنی پیدا نشد.</td></tr>';$$('[data-xp]').forEach(b=>b.onclick=()=>xpDialog(Number(b.dataset.xp)));$$('[data-ban]').forEach(b=>b.onclick=()=>banDialog(Number(b.dataset.ban),b.dataset.banned==='true'))}
function xpDialog(id){openDialog(`اعطای XP به #${id}`,"پیشرفت بازیکن",'<label>مقدار XP<input id="f-xp" type="number" min="1" max="1000000" value="1000"></label>',async()=>{try{const r=await api(`/api/admin/users/${id}/xp`,{method:'POST',body:JSON.stringify({amount:Number($("#f-xp").value)})});$("#action-dialog").close();toast(`${fa.format(r.granted)} XP اعمال شد`);players()}catch(e){toast(e.message,true)}})}
function banDialog(id,banned){openDialog(banned?`رفع مسدودی #${id}`:`مسدود کردن #${id}`,"کنترل دسترسی",banned?'': '<label>دلیل مسدودی<input id="f-reason" maxlength="500" placeholder="دلیل روشن و قابل پیگیری"></label>',async()=>{try{await api(`/api/admin/users/${id}/ban`,{method:'POST',body:JSON.stringify({enabled:!banned,reason:$("#f-reason")?.value||null})});$("#action-dialog").close();toast(banned?'دسترسی باز شد':'بازیکن مسدود شد');players()}catch(e){toast(e.message,true)}})}
const assetFa={IRT:'خزانه',oil:'نفت',food:'غذا',minerals:'معدن',energy:'انرژی',technology:'فناوری'};
async function countries(){const rows=await api('/api/admin/countries?limit=100');$("#country-grid").innerHTML=rows.map(x=>`<article class="country-card"><div class="country-top"><div><p class="eyebrow">${esc(x.government_type)}</p><h3>${esc(x.name)}</h3></div><span class="badge">${fa.format(x.citizens)} شهروند</span></div><div class="treasury">${money(x.treasury_toman)}</div><p>رئیس‌جمهور: ${esc(x.president_name||'تعیین نشده')} ${x.president_player_id?`(#${x.president_player_id})`:''}</p><div class="resource-row">${Object.entries(x.resources||{}).map(([k,v])=>`<span>${assetFa[k]||esc(k)}: ${fa.format(v)}</span>`).join('')}</div><div class="country-actions"><button class="small-btn" data-country-asset="${x.id}">تنظیم دارایی</button><button class="small-btn" data-president="${x.id}">تعیین رئیس‌جمهور</button></div></article>`).join('')||'<div class="empty">هنوز کشوری ساخته نشده است</div>';$$('[data-country-asset]').forEach(b=>b.onclick=()=>assetDialog(Number(b.dataset.countryAsset)));$$('[data-president]').forEach(b=>b.onclick=()=>presidentDialog(Number(b.dataset.president)))}
function assetDialog(id){openDialog(`دارایی کشور #${id}`,"تنظیم حسابرسی‌شده",`<label>نوع دارایی<select id="f-asset">${Object.entries(assetFa).map(([k,v])=>`<option value="${k}">${v}</option>`).join('')}</select></label><label>مقدار تغییر (منفی برای کاهش)<input id="f-delta" type="number" value="1000"></label>`,async()=>{try{await api(`/api/admin/countries/${id}/asset`,{method:'POST',body:JSON.stringify({asset:$("#f-asset").value,delta:Number($("#f-delta").value)})});$("#action-dialog").close();toast("دارایی کشور اصلاح شد");countries()}catch(e){toast(e.message,true)}})}
function presidentDialog(id){openDialog(`ریاست کشور #${id}`,"مدیریت حاکمیت",'<label>شناسه داخلی بازیکن<input id="f-president" type="number" min="1" placeholder="مثلاً 42"></label><small>برای خالی‌کردن سمت، فیلد را خالی بگذارید. بازیکن انتخابی باید شهروند همین کشور باشد.</small>',async()=>{try{const v=$("#f-president").value;await api(`/api/admin/countries/${id}/president`,{method:'POST',body:JSON.stringify({player_id:v?Number(v):null})});$("#action-dialog").close();toast("ریاست‌جمهوری به‌روزرسانی شد");countries()}catch(e){toast(e.message,true)}})}
async function news(){const rows=await api('/api/admin/news?limit=100');$("#news-list").innerHTML=rows.map(x=>`<div class="news-item"><div><p>${esc(x.payload?.text||x.payload?.event_code||x.event_type)}</p><small>${esc(x.event_type)} · ${date(x.created_at)}</small></div><span class="badge ${x.last_error_code?'danger':''}">${x.published_at?'منتشر شد':x.last_error_code?'خطا':'در صف'}</span></div>`).join('')||'<div class="empty">صف خبر خالی است</div>'}
$("#send-news").onclick=async()=>{const text=$("#news-text").value.trim(),d=$("#news-destination").value.trim();if(text.length<3)return toast("متن خبر کوتاه است",true);try{await api('/api/admin/news',{method:'POST',body:JSON.stringify({text,destination:d?Number(d):null})});$("#news-text").value='';toast("خبر وارد صف انتشار شد");news()}catch(e){toast(e.message,true)}};
let searchTimer;$("#player-search").oninput=()=>{clearTimeout(searchTimer);searchTimer=setTimeout(players,300)};$("#market-range").onchange=()=>market();$("#refresh").onclick=()=>load(location.hash.slice(1)||'overview');


async function requests(){const rows=await api('/api/admin/ad-requests?limit=100');$("#ad-requests").innerHTML=rows.map(x=>`<article class="panel request-card">${x.image_mime?`<img src="/api/admin/ad-requests/${x.id}/image" alt="تصویر تبلیغ">`:''}<div><p class="eyebrow">#${x.id} · ${esc(x.package_code)} · ${esc(x.channel)} · ${fa.format(x.price_stars)} ⭐</p><h3>${esc(x.title)}</h3><p>${esc(x.description)}</p><a href="${esc(x.target_url)}" target="_blank" rel="noopener">${esc(x.target_url)}</a><small>${esc(x.first_name)} · ${date(x.created_at)} · ${esc(x.status)} · ارسال‌شده ${fa.format(x.delivered||0)} · در انتظار ${fa.format(x.pending||0)}</small><div class="country-actions"><button class="small-btn" data-editrequest="${x.id}" data-title="${esc(x.title)}" data-description="${esc(x.description)}" data-url="${esc(x.target_url)}">ویرایش</button><button class="small-btn" data-approve="${x.id}">تأیید و صدور پرداخت</button><button class="small-btn danger" data-reject="${x.id}">درخواست اصلاح</button><button class="small-btn" data-pause="${x.id}">توقف</button><button class="small-btn" data-refund="${x.id}">بازپرداخت</button></div></div></article>`).join('')||'<div class="empty">درخواستی وجود ندارد</div>';$$('[data-editrequest]').forEach(b=>b.onclick=()=>editRequest(b));$$('[data-approve]').forEach(b=>b.onclick=()=>reviewAction(b.dataset.approve,'approve'));$$('[data-reject]').forEach(b=>b.onclick=()=>reviewAction(b.dataset.reject,'reject'));$$('[data-pause]').forEach(b=>b.onclick=()=>reviewAction(b.dataset.pause,'pause'));$$('[data-refund]').forEach(b=>b.onclick=()=>reviewAction(b.dataset.refund,'refund'))}

function editRequest(b){openDialog(`ویرایش درخواست #${b.dataset.editrequest}`,"بازبینی محتوای تبلیغ",`<label>عنوان<input id="f-ad-title" maxlength="120" value="${esc(b.dataset.title)}"></label><label>توضیحات<textarea id="f-ad-description" maxlength="2000">${esc(b.dataset.description)}</textarea></label><label>نشانی مقصد<input id="f-ad-url" maxlength="1000" dir="ltr" value="${esc(b.dataset.url)}"></label>`,async()=>{try{await api(`/api/admin/ad-requests/${b.dataset.editrequest}`,{method:'PUT',body:JSON.stringify({title:$("#f-ad-title").value.trim(),description:$("#f-ad-description").value.trim(),target_url:$("#f-ad-url").value.trim(),requested_start_at:null})});$("#action-dialog").close();toast('درخواست ویرایش شد');requests()}catch(e){toast(e.message,true)}})}

function reviewAction(id,action){const labels={approve:'تأیید و صدور صورتحساب',reject:'درخواست اصلاح',pause:'توقف پخش',refund:'بازپرداخت'};const dangerous=['pause','refund','reject'].includes(action);const fields=action==='reject'?'<label>دلیل روشن برای اصلاح<textarea id="f-review-reason" maxlength="1000"></textarea></label>':`<p class="confirm-copy">عملیات <b>${labels[action]}</b> روی درخواست #${id} انجام می‌شود.${dangerous?' این تغییر حساس است و در گزارش ثبت خواهد شد.':''}</p>`;openDialog(labels[action],dangerous?'عملیات حساس':'بازبینی نهایی',fields,async()=>{const body=action==='reject'?{reason:$("#f-review-reason").value.trim()}:action==='approve'?{note:null}:{};if(action==='reject'&&body.reason.length<3)return toast('دلیل اصلاح را کامل بنویس',true);try{await api(`/api/admin/ad-requests/${id}/${action}`,{method:'POST',body:JSON.stringify(body)});$("#action-dialog").close();toast('وضعیت درخواست به‌روزرسانی شد');requests()}catch(e){toast(e.message,true)}})}

async function ads(){const rows=await api('/api/admin/ads?limit=100');$("#ad-list").innerHTML=rows.map(x=>`<div class="news-item"><div><p><b>${esc(x.title)}</b></p><small>${esc(x.status)} · مقصد ${esc(x.destination_chat_id)} · ${date(x.scheduled_at||x.created_at)}</small></div><button class="small-btn" data-adqueue="${x.id}">ارسال حالا</button></div>`).join('')||'<div class="empty">هنوز کمپینی ساخته نشده است</div>';$$('[data-adqueue]').forEach(b=>b.onclick=async()=>{try{await api(`/api/admin/ads/${b.dataset.adqueue}/queue`,{method:'POST',body:'{}'});toast("تبلیغ وارد صف شد");ads()}catch(e){toast(e.message,true)}})}
$("#save-ad").onclick=async()=>{const title=$("#ad-title").value.trim(),text=$("#ad-text").value.trim(),destination=Number($("#ad-destination").value),raw=$("#ad-scheduled").value,repeat=$("#ad-repeat").value;if(title.length<3||text.length<3||!destination)return toast("عنوان، متن و گروه مقصد را کامل کن",true);try{await api('/api/admin/ads',{method:'POST',body:JSON.stringify({title,text,destination,scheduled_at:raw?new Date(raw).toISOString():null,repeat_minutes:repeat?Number(repeat):null})});$("#ad-title").value=$("#ad-text").value='';toast("کمپین ذخیره شد");ads()}catch(e){toast(e.message,true)}};


function jobLabel(name){return ({commerce:'تجارت و تحویل تبلیغ',zipodo_rate:'همگام‌سازی نرخ Zipodo',publish_news:'انتشار Outbox',engagement:'تعامل گروه‌ها',market_snapshot:'ثبت تاریخچه بازار',elections:'انتخابات',legacy_ads:'کمپین‌های مستقیم',cooldown_cleanup:'پاک‌سازی محدودیت‌ها'})[name]||name}
function relativeAge(value){if(!value)return 'نامشخص';const sec=Math.max(0,(Date.now()-new Date(value).getTime())/1000);if(sec<90)return `${Math.round(sec)} ثانیه پیش`;if(sec<5400)return `${Math.round(sec/60)} دقیقه پیش`;return date(value)}
async function operations(){
 const data=await api('/api/admin/operations');state.ops=data;
 const m=data.market||{},stale=!m.source_checked_at||(Date.now()-new Date(m.source_checked_at).getTime()>180000)||m.source_error;
 $('#live-rate').textContent=m.current_price_toman?money(m.current_price_toman):'—';
 const source=$('#rate-source');source.textContent=m.source_error?`آخرین نرخ معتبر · خطای منبع: ${m.source_error}`:`Zipodo · دریافت ${relativeAge(m.source_checked_at)}`;source.className=stale?'source-stale':'source-live';
 $('#freeze-market').textContent=data.market_frozen?'بازکردن بازار':'توقف اضطراری بازار';
 const q=data.queues||{};$('#queue-metrics').innerHTML=[['صف انتشار',q.outbox_pending],['خطای انتشار',q.outbox_failed],['تبلیغ زمان‌بندی‌شده',q.ads_scheduled],['خطای تبلیغ',q.ads_failed],['رویداد زنده',q.live_events]].map(([k,v])=>`<article><span>${k}</span><strong>${fa.format(v||0)}</strong><small>وضعیت همین لحظه</small></article>`).join('');
 $('#jobs-body').innerHTML=(data.jobs||[]).map(j=>`<tr><td><b>${esc(jobLabel(j.job_name))}</b><small>${esc(j.job_name)}</small></td><td><span class="badge ${j.status==='failed'?'danger':''}">${j.status==='succeeded'?'سالم':j.status==='failed'?'خطا':'در حال اجرا'}</span></td><td>${relativeAge(j.finished_at||j.started_at)}</td><td>${fa.format(j.duration_ms||0)} ms</td><td class="${j.error_message?'job-error':''}">${esc(j.error_message||JSON.stringify(j.result||{}))}</td><td>${['zipodo_rate','engagement','market_snapshot'].includes(j.job_name)?`<button class="small-btn" data-runjob="${j.job_name}">اجرای مجدد</button>`:'—'}</td></tr>`).join('')||'<tr><td colspan="6">هنوز Job ثبت‌شده‌ای وجود ندارد.</td></tr>';
 $$('[data-runjob]').forEach(b=>b.onclick=async()=>{try{await api(`/api/admin/operations/jobs/${b.dataset.runjob}/run`,{method:'POST',body:'{}'});toast('Job اجرا شد');operations()}catch(e){toast(e.message,true)}});
 await market(true).catch(()=>{});
}
$('#ops-refresh').onclick=()=>operations().catch(e=>toast(e.message,true));
$('#sync-rate').onclick=async()=>{try{await api('/api/admin/operations/market/sync',{method:'POST',body:'{}'});toast('نرخ معتبر Zipodo ثبت شد');operations()}catch(e){toast(e.message,true)}};
$('#freeze-market').onclick=async()=>{try{await api('/api/admin/operations/market/freeze',{method:'POST',body:JSON.stringify({enabled:!state.ops?.market_frozen})});toast(state.ops?.market_frozen?'بازار باز شد':'بازار متوقف شد');operations()}catch(e){toast(e.message,true)}};
document.addEventListener('visibilitychange',()=>{clearInterval(state.opsTimer);if(!document.hidden)state.opsTimer=setInterval(()=>{if(location.hash==='#operations')operations().catch(()=>{})},30000)});state.opsTimer=setInterval(()=>{if(!document.hidden&&location.hash==='#operations')operations().catch(()=>{})},30000);
async function engagement(){
 const d=await api('/api/admin/engagement'),a=d.activity||{},dy=d.daily||{},m=d.missions||{},o=d.onboarding||{};
 const metrics=[['فعال امروز',a.active_24h,'بازیکن یکتا'],['فعال ۷ روز',a.active_7d,'هفته جاری'],['هدیه امروز',dy.claimed_today,'دریافت موفق'],['زنجیره ۷+',dy.streak_7,'کاربر وفادار'],['شروع کامل',o.completed,'چهار قدم']];
 $('#engagement-metrics').innerHTML=metrics.map(([k,v,s])=>`<article><span>${k}</span><strong>${fa.format(v||0)}</strong><small>${s}</small></article>`).join('');
 const total=Math.max(Number(a.total||0),1),f=[['کل بازیکنان',a.total],['فعال ۳۰ روز',a.active_30d],['شروع کامل',o.completed],['رسیده به شغل',a.reached_jobs],['رسیده به بازار',a.reached_market]];
 $('#retention-funnel').innerHTML=f.map(([k,v])=>{const pct=Math.min(100,Math.round(Number(v||0)*100/total));return `<div class="funnel-row"><span>${k}</span><div class="funnel-track"><div class="funnel-fill" style="width:${pct}%"></div></div><b>${fa.format(pct)}٪</b></div>`}).join('');
 const claimRate=Math.round(Number(dy.claimed_today||0)*100/Math.max(Number(a.active_24h||0),1)),completeRate=Math.round(Number(o.completed||0)*100/Math.max(Number(o.completed||0)+Number(o.incomplete||0),1)),missionRate=Math.round(Number(m.completed_today||0)*100/Math.max(Number(m.assigned_today||0),1));
 const insights=[[completeRate<70,'مسیر شروع',completeRate<70?`فقط ${fa.format(completeRate)}٪ مسیر چهارمرحله‌ای را کامل کرده‌اند؛ متن یا قدم پرت‌ریزش را کوتاه کن.`:'مسیر شروع سالم است؛ تغییر بزرگ نده.'],[claimRate<45,'هدیه روزانه',claimRate<45?`نرخ دریافت میان فعال‌های امروز ${fa.format(claimRate)}٪ است؛ دکمه هدیه را در خانه پررنگ‌تر نگه دار.`:'هدیه روزانه به‌خوبی دیده می‌شود.'],[missionRate<35,'کارهای امروز',missionRate<35?`تکمیل کارها ${fa.format(missionRate)}٪ است؛ هدف‌ها احتمالاً سخت یا نامشخص‌اند.`:'سختی کارهای روزانه متعادل است.']];
 $('#engagement-insights').innerHTML=insights.map(([warn,t,b])=>`<div class="insight ${warn?'warn':''}"><i></i><div><strong>${t}</strong><p>${b}</p></div></div>`).join('');
}
async function ledger(){const raw=$('#ledger-player').value.trim(),[rows,integrity]=await Promise.all([api(`/api/admin/ledger?limit=200${raw?`&player_id=${encodeURIComponent(raw)}`:''}`),api('/api/admin/economy-integrity')]);$('#integrity-metrics').innerHTML=[['موجودی منفی بازیکن',integrity.negative_players],['خزانه منفی',integrity.negative_countries],['ردیف منفی غیرمجاز',integrity.negative_ledger_rows],['تراکنش ۲۴ ساعت',integrity.ledger_24h]].map(([k,v])=>`<article><span>${k}</span><strong>${fa.format(v||0)}</strong><small>${Number(v||0)===0?'وضعیت سالم':'نیازمند بررسی'}</small></article>`).join('');$('#ledger-body').innerHTML=rows.map(x=>`<tr><td><b>${date(x.created_at)}</b><small>#${x.id}</small></td><td><b>${esc(x.first_name||'کشور')}</b><small>${x.player_id?'بازیکن #'+x.player_id:'کشور #'+x.country_id}</small></td><td>${esc(x.reason)}</td><td><span class="badge">${esc(x.asset_code)}</span><br><small>${esc(x.account)}</small></td><td class="mono ${Number(x.amount)>=0?'amount-positive':'amount-negative'}">${Number(x.amount)>=0?'+':''}${fa.format(x.amount)}</td><td class="mono">${fa.format(x.balance_after)}</td></tr>`).join('')||'<tr><td colspan="6">تراکنشی پیدا نشد.</td></tr>'}
async function audit(){const rows=await api('/api/admin/audit?limit=200');$('#audit-body').innerHTML=rows.map(x=>`<tr><td>${date(x.created_at)}</td><td><b>${esc(x.admin_actor)}</b></td><td><span class="badge">${esc(x.action)}</span></td><td>${x.target_player_id?'بازیکن #'+x.target_player_id:x.target_country_id?'کشور #'+x.target_country_id:'سامانه'}</td><td><small>${esc(JSON.stringify(x.details||{}))}</small></td><td class="mono"><small>${esc(x.request_id)}</small></td></tr>`).join('')||'<tr><td colspan="6">هنوز عملیاتی ثبت نشده است.</td></tr>'}
const flagMeta={economy_frozen:['توقف کامل اقتصاد','تراکنش‌های اقتصادی کاربران متوقف می‌شود.'],usd_market_frozen:['توقف بازار ارز','خرید و فروش ارز متوقف می‌شود.'],ads_frozen:['توقف تبلیغات','پخش تبلیغات متوقف می‌شود.'],registrations_frozen:['توقف ثبت‌نام','ورود کاربران تازه متوقف می‌شود.']};
async function controls(){const rows=await api('/api/admin/feature-flags'),map=Object.fromEntries(rows.map(x=>[x.key,x]));$('#flag-grid').innerHTML=Object.entries(flagMeta).map(([key,[title,desc]])=>{const on=Boolean(map[key]?.enabled);return `<article class="control-card ${on?'danger-zone':''}"><div><h3>${title}</h3><p>${desc} · ${map[key]?`آخرین تغییر ${date(map[key].updated_at)}`:'هنوز تنظیم نشده'}</p></div><button class="toggle ${on?'on':''}" data-flag="${key}" data-enabled="${on}" aria-label="${title}"><i></i></button></article>`}).join('');$$('[data-flag]').forEach(b=>b.onclick=()=>confirmFlag(b.dataset.flag,b.dataset.enabled==='true'))}
function confirmFlag(key,on){const [title,desc]=flagMeta[key];openDialog(on?`غیرفعال‌کردن: ${title}`:`فعال‌کردن: ${title}`,"تأیید عملیات حساس",`<p class="confirm-copy">${desc}</p><label>برای تأیید بنویس «تأیید»<input id="f-confirm-word" autocomplete="off"></label>`,async()=>{if($('#f-confirm-word').value.trim()!=='تأیید')return toast('واژه تأیید درست وارد نشده است',true);try{await api(`/api/admin/feature-flags/${key}`,{method:'PUT',body:JSON.stringify({enabled:!on})});$('#action-dialog').close();toast('کنترل سامانه به‌روزرسانی شد');controls()}catch(e){toast(e.message,true)}})}
$$('[data-reload]').forEach(b=>b.onclick=()=>load(b.dataset.reload));let ledgerTimer;$('#ledger-player').oninput=()=>{clearTimeout(ledgerTimer);ledgerTimer=setTimeout(ledger,350)};
function load(name){({overview,market,operations,engagement,players,countries,news,ads,requests,ledger,audit,controls}[name]||overview)().catch(e=>toast(e.message,true))}
setInterval(()=>$("#clock").textContent=new Date().toLocaleTimeString('fa-IR'),1000);go(location.hash.slice(1)||'overview');
```

### `apps\admin\templates\base.html`

```html
<!doctype html><html lang="fa" dir="rtl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#06111d"><title>{% block title %}مرکز فرماندهی TeleLife{% endblock %}</title>
<link rel="stylesheet" href="{{ url_for('static', path='/admin.css') }}">
</head><body><div class="noise"></div>{% block content %}{% endblock %}
<script src="{{ url_for('static', path='/admin.js') }}" defer></script></body></html>
```

### `apps\admin\templates\dashboard.html`

```html
{% extends "base.html" %}{% block content %}
<aside class="rail" aria-label="منوی مدیریت">
  <a class="brand" href="#overview" aria-label="TeleLife"><span class="brand-mark">T</span><span><b>TeleLife</b><small>COMMAND</small></span></a>
  <nav>
    <button class="nav active" data-view="overview"><span>◈</span><em>نمای کلی</em></button>
    <button class="nav" data-view="market"><span>⌁</span><em>بازار</em></button>
    <button class="nav" data-view="operations"><span>≋</span><em>عملیات زنده</em></button>
    <button class="nav" data-view="engagement"><span>↗</span><em>ماندگاری</em></button>
    <button class="nav" data-view="players"><span>◎</span><em>بازیکنان</em></button>
    <button class="nav" data-view="countries"><span>◇</span><em>کشورها</em></button>
    <button class="nav" data-view="news"><span>◉</span><em>اتاق خبر</em></button>
    <button class="nav" data-view="ads"><span>✦</span><em>تبلیغات</em></button>
    <button class="nav" data-view="requests"><span>▣</span><em>درخواست‌ها</em></button>
    <button class="nav" data-view="ledger"><span>≜</span><em>دفتر اقتصاد</em></button>
    <button class="nav" data-view="audit"><span>⌾</span><em>حسابرسی</em></button>
    <button class="nav" data-view="controls"><span>⏻</span><em>کنترل سامانه</em></button>
  </nav>
  <div class="rail-foot"><i class="pulse"></i><span>سامانه برخط</span><small id="clock">—</small></div>
</aside>
<main class="shell">
<header class="topbar"><div><p class="eyebrow">شبکه اقتصادی تله‌لایف</p><h1 id="view-title">مرکز فرماندهی</h1></div><div class="top-actions"><div class="live"><i></i><span>LIVE</span></div><button id="refresh" class="icon-btn" title="تازه‌سازی">↻</button></div></header>
<div id="toast" role="status" aria-live="polite"></div>
<section class="view active" id="view-overview">
  <div class="hero-grid">
    <article class="hero-card"><div><p class="eyebrow">حجم اقتصاد بازیکنان</p><strong data-stat="player_liquidity">{{ stats.get('player_liquidity',0) }}</strong><span>تومان نقدینگی ثبت‌شده</span></div><div class="orbit"><b>TL</b><i></i><i></i><i></i></div></article>
    <article class="signal-card"><p>وضعیت شبکه</p><div id="service-radar" class="service-radar"><span>در حال دریافت…</span></div></article>
  </div>
  <div class="metric-grid">
    <article><span>بازیکن</span><strong data-stat="players_total">{{ stats.get('players_total',0) }}</strong><small>کل حساب‌ها</small></article>
    <article><span>فعال</span><strong data-stat="players_active">{{ stats.get('players_active',0) }}</strong><small>هفت روز اخیر</small></article>
    <article><span>کشور</span><strong data-stat="countries_total">{{ stats.get('countries_total',0) }}</strong><small>جهان فعال</small></article>
    <article><span>صف خبر</span><strong data-stat="news_pending">{{ stats.get('news_pending',0) }}</strong><small>در انتظار انتشار</small></article>
  </div>
  <div class="split">
    <article class="panel chart-panel"><div class="panel-head"><div><p class="eyebrow">نبض بازار</p><h2>حرکت دارایی‌های اصلی</h2></div><button class="text-btn" data-go="market">مشاهده بازار ←</button></div><div id="mini-chart" class="chart-wrap"><div class="empty">داده بازار در حال بارگذاری است</div></div></article>
    <article class="panel"><div class="panel-head"><div><p class="eyebrow">کنترل سریع</p><h2>عملیات پرتکرار</h2></div></div><div class="quick-grid"><button data-go="players">اعطای XP<small>مدیریت پیشرفت</small></button><button data-go="countries">تنظیم منابع<small>اقتصاد کشور</small></button><button data-go="news">ارسال خبر<small>صف انتشار</small></button><button data-go="market">قیمت بازار<small>ثبت نقطه جدید</small></button></div></article>
  </div>
</section>
<section class="view" id="view-engagement">
  <div class="section-lead"><div><p class="eyebrow">چرخه بازگشت کاربر</p><h2>ماندگاری و مسیر شروع</h2><p>به‌جای عددهای تزئینی، گلوگاه‌های واقعی ورود، هدیه و کارهای روزانه را ببین.</p></div><button class="secondary" data-reload="engagement">تازه‌سازی</button></div>
  <div id="engagement-metrics" class="metric-grid metric-grid-five"></div>
  <div class="split"><article class="panel"><div class="panel-head"><div><p class="eyebrow">قیف امروز</p><h2>از ورود تا عادت روزانه</h2></div></div><div id="retention-funnel" class="funnel"></div></article><article class="panel"><div class="panel-head"><div><p class="eyebrow">راهنمای اقدام</p><h2>چه چیزی را بهتر کنیم؟</h2></div></div><div id="engagement-insights" class="insight-list"></div></article></div>
</section>
<section class="view" id="view-market">
  <div class="section-lead"><div><p class="eyebrow">دفتر رسمی قیمت</p><h2>بازار و نرخ دارایی‌ها</h2><p>هر تغییر قیمت ثبت و وارد تاریخچه نمودار می‌شود.</p></div><select id="market-range"><option value="24">۲۴ ساعت</option><option value="168">۷ روز</option><option value="720">۳۰ روز</option></select></div>
  <article class="panel market-stage"><div id="market-tabs" class="asset-tabs"></div><div id="market-chart" class="chart-wrap large"><div class="empty">در حال دریافت قیمت‌ها…</div></div></article>
  <div id="market-cards" class="market-cards"></div>
</section>

<section class="view" id="view-operations">
  <div class="section-lead"><div><p class="eyebrow">اتاق کنترل زیرساخت</p><h2>عملیات زنده</h2><p>منبع نرخ، صف‌ها و آخرین اجرای هر Job؛ بدون حدس و بدون عدد ساختگی.</p></div><button id="ops-refresh" class="secondary">تازه‌سازی وضعیت</button></div>
  <article class="rate-ticker panel"><div><span class="source-seal">USDT / IRT</span><strong id="live-rate">—</strong><small id="rate-source">در حال بررسی منبع…</small></div><div class="ticker-actions"><button id="sync-rate" class="primary">دریافت نرخ Zipodo</button><button id="freeze-market" class="secondary">توقف بازار</button></div><div id="sparkline" class="sparkline" aria-label="روند نرخ تتر"></div></article>
  <div id="queue-metrics" class="metric-grid"></div>
  <article class="panel table-panel"><div class="panel-head ops-head"><div><p class="eyebrow">اجرای زمان‌بند</p><h2>آخرین وضعیت Jobها</h2></div><span class="legend"><i class="ok"></i> سالم <i class="bad"></i> خطا</span></div><div class="table-scroll"><table><thead><tr><th>Job</th><th>وضعیت</th><th>آخرین اجرا</th><th>زمان اجرا</th><th>جزئیات</th><th>عملیات</th></tr></thead><tbody id="jobs-body"></tbody></table></div></article>
</section>

<section class="view" id="view-players">
  <div class="section-lead"><div><p class="eyebrow">مدیریت هویت</p><h2>بازیکنان</h2><p>جست‌وجو، اعطای XP و کنترل دسترسی.</p></div><label class="search"><span>⌕</span><input id="player-search" placeholder="نام، نام کاربری یا شناسه…"></label></div>
  <article class="panel table-panel"><div class="table-scroll"><table><thead><tr><th>بازیکن</th><th>سطح / XP</th><th>دارایی</th><th>آخرین حضور</th><th>وضعیت</th><th>عملیات</th></tr></thead><tbody id="players-body"></tbody></table></div></article>
</section>
<section class="view" id="view-countries">
  <div class="section-lead"><div><p class="eyebrow">ژئو‌اقتصاد</p><h2>کشورها</h2><p>خزانه، منابع و ریاست‌جمهوری در یک قاب.</p></div></div><div id="country-grid" class="country-grid"></div>
</section>
<section class="view" id="view-news">
  <div class="section-lead"><div><p class="eyebrow">انتشار سراسری</p><h2>اتاق خبر</h2><p>پیام را مستقیم وارد صف مطمئن Outbox کنید.</p></div></div>
  <div class="split news-layout"><article class="panel composer"><label>متن اطلاعیه<textarea id="news-text" maxlength="4000" placeholder="پیام رسمی شبکه را بنویسید…"></textarea></label><label>Chat ID مقصد <small>خالی = GLOBAL_NEWS_CHAT_ID</small><input id="news-destination" inputmode="numeric" placeholder="-1001234567890"></label><button id="send-news" class="primary">قرار دادن در صف انتشار</button></article><article class="panel"><div class="panel-head"><div><p class="eyebrow">تاریخچه</p><h2>صف پیام‌ها</h2></div></div><div id="news-list" class="news-list"></div></article></div>
</section>
<section class="view" id="view-ads">
  <div class="section-lead"><div><p class="eyebrow">کمپین و انتشار</p><h2>مرکز تبلیغات</h2><p>تبلیغ را برای گروه مشخص، فوری یا زمان‌بندی‌شده وارد صف امن انتشار کنید.</p></div></div>
  <div class="split news-layout"><article class="panel composer">
    <label>عنوان کمپین<input id="ad-title" maxlength="120" placeholder="مثلاً معرفی فصل تازه"></label>
    <label>متن تبلیغ<textarea id="ad-text" maxlength="4000" placeholder="متن نهایی تبلیغ…"></textarea></label>
    <label>Chat ID گروه مقصد<input id="ad-destination" inputmode="numeric" placeholder="-1001234567890"></label>
    <label>زمان انتشار <small>اختیاری؛ خالی یعنی پیش‌نویس</small><input id="ad-scheduled" type="datetime-local"></label>
    <label>تکرار هر چند دقیقه <small>اختیاری، حداقل ۱۵</small><input id="ad-repeat" type="number" min="15"></label>
    <button id="save-ad" class="primary">ذخیره کمپین</button>
  </article><article class="panel"><div class="panel-head"><div><p class="eyebrow">کمپین‌ها</p><h2>صف تبلیغات</h2></div></div><div id="ad-list" class="news-list"></div></article></div>
</section>
<section class="view" id="view-requests"><div class="section-lead"><div><p class="eyebrow">بازبینی پیش از پرداخت</p><h2>درخواست‌های تبلیغ</h2><p>جزئیات، تصویر و لینک را بررسی و ویرایش کن؛ فقط پس از تأیید، مهلت پرداخت ۴۸ساعته آغاز می‌شود.</p></div></div><div id="ad-requests" class="request-grid"></div></section>
<section class="view" id="view-ledger">
  <div class="section-lead"><div><p class="eyebrow">منبع حقیقت اقتصاد</p><h2>دفتر تراکنش‌ها</h2><p>گردش دارایی، موجودی پس از عملیات و کلیدهای قابل پیگیری.</p></div><label class="search"><span>⌕</span><input id="ledger-player" inputmode="numeric" placeholder="فیلتر با شناسه بازیکن…"></label></div>
  <div id="integrity-metrics" class="metric-grid"></div>
  <article class="panel table-panel"><div class="table-scroll"><table><thead><tr><th>زمان / شناسه</th><th>مالک</th><th>علت</th><th>دارایی</th><th>تغییر</th><th>مانده</th></tr></thead><tbody id="ledger-body"></tbody></table></div></article>
</section>
<section class="view" id="view-audit">
  <div class="section-lead"><div><p class="eyebrow">ردپای تغییرات حساس</p><h2>گزارش حسابرسی مدیران</h2><p>چه کسی، چه زمانی و روی کدام بازیکن یا کشور تغییر اعمال کرده است.</p></div><button class="secondary" data-reload="audit">تازه‌سازی</button></div>
  <article class="panel table-panel"><div class="table-scroll"><table><thead><tr><th>زمان</th><th>مدیر</th><th>عملیات</th><th>هدف</th><th>جزئیات</th><th>شناسه درخواست</th></tr></thead><tbody id="audit-body"></tbody></table></div></article>
</section>
<section class="view" id="view-controls">
  <div class="section-lead"><div><p class="eyebrow">کلیدهای توقف امن</p><h2>کنترل سامانه</h2><p>هر تغییر ثبت حسابرسی می‌شود. توقف اضطراری را فقط هنگام رخداد واقعی فعال کن.</p></div></div>
  <div id="flag-grid" class="control-grid"></div>
  <article class="panel safety-note"><div class="safety-mark">!</div><div><h3>قاعده دو مرحله‌ای</h3><p>برای هر تغییر مخرب، پنجره تأیید نام عملیات و اثر آن را دوباره نشان می‌دهد. این اصطکاک کوچک جلوی کلیک‌های گران‌قیمت را می‌گیرد.</p></div></article>
</section>
</main>
<dialog id="action-dialog"><form method="dialog"><button class="dialog-close" value="cancel">×</button><p class="eyebrow" id="dialog-kicker">عملیات مدیریت</p><h2 id="dialog-title">—</h2><div id="dialog-fields"></div><div class="dialog-actions"><button value="cancel" class="secondary">انصراف</button><button type="button" id="dialog-confirm" class="primary">اعمال تغییر</button></div></form></dialog>
{% endblock %}
```

### `apps\admin\templates\partials\stats.html`

```html
<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
  <div class="panel rounded-xl p-5">
    <div class="text-xs text-slate-500 mb-2">کل بازیکنان</div>
    <div class="text-3xl font-extrabold text-white">{{ fmt.number(stats.players_total) }}</div>
  </div>
  <div class="panel rounded-xl p-5">
    <div class="text-xs text-slate-500 mb-2">فعال (۷ روز)</div>
    <div class="text-3xl font-extrabold text-emerald-400">{{ fmt.number(stats.players_active) }}</div>
  </div>
  <div class="panel rounded-xl p-5">
    <div class="text-xs text-slate-500 mb-2">گروه‌های فعال</div>
    <div class="text-3xl font-extrabold text-white">{{ fmt.number(stats.groups_total) }}</div>
  </div>
  <div class="panel rounded-xl p-5">
    <div class="text-xs text-slate-500 mb-2">دیتابیس</div>
    <div class="text-3xl font-extrabold {{ 'text-emerald-400' if stats.db_ok else 'text-rose-500' }}">
      {{ 'سالم' if stats.db_ok else 'قطع' }}
    </div>
  </div>
</div>
```

### `apps\scheduler\__init__.py`

```python
"""Package apps.scheduler."""
```

### `apps\scheduler\jobs\__init__.py`

```python
"""Scheduler job modules; imported lazily to avoid startup side effects."""

__all__ = ["country_jobs", "daily_reset"]
```

### `apps\scheduler\jobs\country_jobs.py`

```python
"""Country minute/daily jobs; all operations are retry-safe."""
from __future__ import annotations
from telegram import Bot
from packages.core.services import country_economy,elections,news,commerce,country_identity
async def resolve_due()->dict[str,int]:return await elections.resolve_due()
async def daily_events()->int:
 await country_economy.catch_up()
 return await news.ensure_daily_events()
async def publish_news(bot:Bot,life_bot:Bot|None=None)->dict[str,int]:
 async def sender(chat_id,event_type,payload):
  if chat_id is None:return
  if event_type=="marketplace_ad":
   from packages.core import db
   ad=await db.fetchrow("SELECT * FROM ad_requests WHERE id=$1",payload["ad_id"])
   if not ad:return
   if payload.get("destination_type")=="world":
    protected=await db.fetchval("SELECT ad_free_until>now() FROM groups WHERE telegram_id=$1",chat_id)
    if protected:
     await db.execute("UPDATE ad_deliveries SET status='cancelled' WHERE id=$1",payload["delivery_id"]);return
   text=f"📣 <b>{ad['title']}</b>\n\n{ad['description']}\n\n🔗 {ad['target_url']}"
   if ad["image_bytes"] and len(text)>1000:text=text[:960]+"…\n\n🔗 "+str(ad['target_url'])[:45]
   sender_bot=life_bot if payload.get("destination_type")=="life" and life_bot is not None else bot
   if ad["image_bytes"]:await sender_bot.send_photo(chat_id=chat_id,photo=bytes(ad["image_bytes"]),caption=text)
   else:await sender_bot.send_message(chat_id=chat_id,text=text)
   await db.execute("UPDATE ad_deliveries SET status='sent',sent_at=now() WHERE id=$1",payload["delivery_id"])
   await db.execute("UPDATE ad_requests SET first_delivery_at=COALESCE(first_delivery_at,now()),updated_at=now() WHERE id=$1",payload["ad_id"])
   await db.execute("UPDATE ad_requests SET status='completed',updated_at=now() WHERE id=$1 AND NOT EXISTS(SELECT 1 FROM ad_deliveries WHERE ad_request_id=$1 AND status IN ('scheduled','queued'))",payload["ad_id"])
   return
  text=str(payload.get('text') or payload.get('event_code') or payload.get('mission_key') or event_type)
  destination=await country_identity.destination(chat_id)
  if destination:
   if not destination['country_id']:
    if await country_identity.should_send_setup_notice(chat_id):await bot.send_message(chat_id=chat_id,text=country_identity.SETUP_TEXT)
    return
   text=country_identity.masthead(str(destination['country_name']),text)
  await bot.send_message(chat_id=chat_id,text=text)
 return await news.publish_batch(sender)

async def queue_due_ads()->int:
 from packages.core import db
 from packages.core.repositories import outbox_repo
 count=0
 async with db.transaction() as conn:
  rows=await conn.fetch("SELECT * FROM ad_campaigns WHERE status='scheduled' AND scheduled_at<=now() FOR UPDATE SKIP LOCKED LIMIT 50")
  for row in rows:
   key=f"ad-scheduled:{row['id']}:{row['scheduled_at'].isoformat()}"
   if await outbox_repo.enqueue(conn,key,"advertisement",{"text":row["body"],"ad_id":row["id"]},row["destination_chat_id"]):count+=1
   if row["repeat_minutes"]:
    await conn.execute("UPDATE ad_campaigns SET scheduled_at=now()+($2::int*interval '1 minute'),last_queued_at=now(),updated_at=now() WHERE id=$1",row["id"],row["repeat_minutes"])
   else: await conn.execute("UPDATE ad_campaigns SET status='queued',last_queued_at=now(),updated_at=now() WHERE id=$1",row["id"])
 return count

async def run_commerce()->dict[str,int]:
 await __import__("packages.core.services.migration",fromlist=["expire"]).expire();expired=await commerce.expire_commerce();planned=await commerce.plan_paid_ads();queued=await commerce.queue_due_deliveries();return {**expired,"planned":planned,"queued":queued}
```

### `apps\scheduler\jobs\daily_reset.py`

```python
"""Nightly maintenance: prune stale mission rows, break dead streaks.

Both operations are ranged and index-backed, so cost stays flat as the player
base grows.
"""

from __future__ import annotations

import logging

from packages.core import db
from packages.core.config import get_config

logger = logging.getLogger(__name__)

MISSION_RETENTION_DAYS = 7
XP_EVENT_RETENTION_DAYS = 90


async def prune_missions() -> int:
    result = await db.execute(
        "DELETE FROM daily_missions WHERE mission_date < current_date - $1::int",
        MISSION_RETENTION_DAYS,
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def prune_xp_events() -> int:
    result = await db.execute(
        "DELETE FROM xp_events WHERE created_at < now() - ($1::double precision * interval '1 day')",
        XP_EVENT_RETENTION_DAYS,
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def break_streaks() -> int:
    """Drop streaks for players who missed more than the grace window."""
    cfg = get_config()
    reset_to = cfg.int_("daily.streak.grace_reset_to")
    break_after = cfg.int_("daily.streak.break_after_days")
    result = await db.execute(
        """
        UPDATE daily_state
        SET streak = $1
        WHERE last_claim_date IS NOT NULL
          AND last_claim_date < current_date - ($2::int + 1)
          AND streak > $1
        """,
        reset_to,
        break_after,
    )
    return int(result.rsplit(" ", 1)[-1] or 0)


async def run() -> dict[str, int]:
    stats = {
        "missions_pruned": await prune_missions(),
        "xp_events_pruned": await prune_xp_events(),
        "streaks_broken": await break_streaks(),
    }
    logger.info("daily reset complete: %s", stats)
    return stats
```

### `apps\scheduler\main.py`

```python
"""Supervised scheduler with isolated minute and daily background jobs."""
from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime, timedelta

from telegram import Bot

from apps.scheduler.jobs import country_jobs, daily_reset
from packages.core import db
from packages.core.repositories import admin_repo
from packages.core.settings import Settings
from packages.core.services import usd_market, live_market, scheduler_ops, engagement, country_realism

logger = logging.getLogger(__name__)


def seconds_until_daily() -> float:
    now = datetime.now(UTC)
    target = (now + timedelta(days=1)).replace(hour=0, minute=10, second=0, microsecond=0)
    return max(1.0, (target - now).total_seconds())


async def _sleep_or_stop(stop: asyncio.Event, seconds: float) -> bool:
    try:
        await asyncio.wait_for(stop.wait(), timeout=seconds)
        return True
    except TimeoutError:
        return False


class SchedulerService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._running = False
        self._heartbeat = 0.0

    def healthy(self) -> bool:
        return self._running

    async def minute_loop(self, stop: asyncio.Event, bot: Bot, life_bot: Bot) -> None:
        while not stop.is_set():
            try:
                jobs = (
                    ("cooldown_cleanup", lambda: db.execute("DELETE FROM cooldowns WHERE expires_at < now()")),
                    ("elections", country_jobs.resolve_due),
                    ("legacy_ads", country_jobs.queue_due_ads),
                    ("commerce", country_jobs.run_commerce),
                    ("publish_news", lambda: country_jobs.publish_news(bot, life_bot)),
                    ("zipodo_rate", live_market.sync),
                    ("engagement", engagement.minute_tick),
                    ("market_snapshot", admin_repo.capture_market_snapshot),
                )
                for name, job in jobs:
                    if stop.is_set(): break
                    await scheduler_ops.run(name, job)
                self._heartbeat = asyncio.get_running_loop().time()
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("minute loop infrastructure failed; next cycle remains scheduled")
            await _sleep_or_stop(stop, 60)

    async def daily_loop(self, stop: asyncio.Event) -> None:
        while not stop.is_set():
            if await _sleep_or_stop(stop, seconds_until_daily()):
                return
            try:
                await daily_reset.run()
                await usd_market.daily_rollover()
                await country_jobs.daily_events()
                await scheduler_ops.run("country_realism", country_realism.daily_tick)
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("daily jobs failed; scheduler remains active")

    async def run(self, stop: asyncio.Event) -> None:
        self._running = True
        try:
            async with Bot(self.settings.teleworld_bot_token) as bot, Bot(self.settings.telelife_bot_token) as life_bot:
                minute = asyncio.create_task(self.minute_loop(stop, bot, life_bot), name="scheduler:minute")
                daily = asyncio.create_task(self.daily_loop(stop), name="scheduler:daily")
                stop_waiter = asyncio.create_task(stop.wait(), name="scheduler:stop")
                done, _ = await asyncio.wait(
                    {minute, daily, stop_waiter}, return_when=asyncio.FIRST_COMPLETED
                )
                if stop_waiter not in done:
                    for task in done:
                        if task is not stop_waiter:
                            exc = task.exception()
                            if exc:
                                raise exc
                            raise RuntimeError(f"{task.get_name()} exited unexpectedly")
                for task in (minute, daily, stop_waiter):
                    if not task.done():
                        task.cancel()
                await asyncio.gather(minute, daily, stop_waiter, return_exceptions=True)
        finally:
            self._running = False
```

### `apps\telelife_bot\__init__.py`

```python
"""Package apps.telelife_bot."""
```

### `apps\telelife_bot\handlers\__init__.py`

```python
"""Package apps.telelife_bot.handlers."""
```

### `apps\telelife_bot\handlers\advertising.py`

```python
"""Guided private ad request flow and Telegram Stars settlement."""
from __future__ import annotations
from datetime import UTC,datetime
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,LabeledPrice,Update
from telegram.ext import CallbackQueryHandler,ContextTypes,MessageHandler,PreCheckoutQueryHandler,filters
from packages.core.repositories import player_repo
from packages.core.services import commerce
from packages.core.services.content_filter import inspect
FLOW="ad_request_flow"
PACK={"economy":"اقتصادی · پایه ۲۵ ⭐ · یک پخش","standard":"استاندارد · پایه ۶۰ ⭐ · ۳ پخش / ۲۴ ساعت","campaign":"کمپین · پایه ۱۲۰ ⭐ · ۶ پخش / ۳ روز","featured":"ویژه · پایه ۲۰۰ ⭐ · ۸ پخش / ۷ روز"}
CHANNEL={"life":"فقط Life · کاربران فعال ۳۰ روز · ×۱","world":"فقط World · گروه‌های فعال غیرمشترک · ×۱٫۵","both":"Life + World · ×۲٫۲"}
def keyboard(rows):return InlineKeyboardMarkup(rows)
def menu():return keyboard([[InlineKeyboardButton(v,callback_data=f"ad:pkg:{k}")] for k,v in PACK.items()]+[[InlineKeyboardButton("📂 درخواست‌های من",callback_data="ad:mine")],[InlineKeyboardButton("لغو",callback_data="ad:cancel")]])
def channels(package):
 return keyboard([[InlineKeyboardButton(label+f" · {commerce.ad_price(package,code)} ⭐",callback_data=f"ad:channel:{package}:{code}")] for code,label in CHANNEL.items()]+[[InlineKeyboardButton("بازگشت",callback_data="ad:new")]])
async def begin(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.callback_query
 if q:await q.answer();await q.edit_message_text("📣 <b>درخواست تبلیغ</b>\n\nبسته را انتخاب کن. تبلیغ پیش از پرداخت کامل در پنل مدیریت بررسی می‌شود.",reply_markup=menu())
async def callback(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.callback_query;action=(q.data or "").split(":")
 if action[1]=="cancel":context.user_data.pop(FLOW,None);await q.answer();await q.edit_message_text("درخواست لغو شد.");return
 if action[1]=="mine":
  p=await player_repo.get_by_telegram_id(q.from_user.id);rows=await commerce.player_ads(p.id) if p else []
  buttons=[];lines=["📂 <b>درخواست‌های من</b>"]
  for row in rows:
   lines.append(f"#{row['id']} · {row['title']} · {row['status']}"+(f"\nیادداشت: {row['admin_note']}" if row['admin_note'] else ""))
   if row['status']=='changes_requested':buttons.append([InlineKeyboardButton(f"✏️ اصلاح #{row['id']}",callback_data=f"ad:revise:{row['id']}")])
  buttons.append([InlineKeyboardButton("درخواست تازه",callback_data="ad:new")]);await q.answer();await q.edit_message_text("\n\n".join(lines) if rows else "درخواستی نداری.",reply_markup=keyboard(buttons));return
 if action[1]=="new":await q.answer();await q.edit_message_text("بسته را انتخاب کن.",reply_markup=menu());return
 if action[1]=="revise":
  p=await player_repo.get_by_telegram_id(q.from_user.id);row=await commerce.revision_source(int(action[2]),p.id) if p else None
  if not row:await q.answer("این درخواست قابل اصلاح نیست.",show_alert=True);return
  context.user_data[FLOW]={"step":"title","package":row['package_code'],"channel":row['channel'],"revision_id":row['id']};await q.answer();await q.edit_message_text(f"عنوان اصلاح‌شده را بفرست.\nعنوان فعلی: {row['title']}");return
 if action[1]=="pkg":await q.answer();await q.edit_message_text("محل نمایش تبلیغ را انتخاب کن. قیمت نهایی بر اساس کانال محاسبه می‌شود.",reply_markup=channels(action[2]));return
 if action[1]=="channel":context.user_data[FLOW]={"step":"title","package":action[2],"channel":action[3]};await q.answer();await q.edit_message_text(f"قیمت نهایی: {commerce.ad_price(action[2],action[3])} ⭐\n\nعنوان کوتاه تبلیغ را بفرست (۳ تا ۱۲۰ نویسه).")
async def text(update:Update,context:ContextTypes.DEFAULT_TYPE):
 flow=context.user_data.get(FLOW);msg=update.effective_message
 if not flow or not msg:return
 value=(msg.text or "").strip();step=flow["step"]
 if step in {"title","description"} and not inspect(value).allowed:await msg.reply_text("⚠️ متن شامل عبارت غیرمجاز است؛ آن را اصلاح کن و دوباره بفرست.");return
 if step=="title":
  if not 3<=len(value)<=120:await msg.reply_text("عنوان باید بین ۳ تا ۱۲۰ نویسه باشد.");return
  flow.update(title=value,step="description");await msg.reply_text("توضیح کامل تبلیغ را بفرست (۱۰ تا ۲۰۰۰ نویسه).");return
 if step=="description":
  if not 10<=len(value)<=2000:await msg.reply_text("توضیح باید بین ۱۰ تا ۲۰۰۰ نویسه باشد.");return
  flow.update(description=value,step="url");await msg.reply_text("لینک مقصد را با https:// بفرست.");return
 if step=="url":
  if not commerce.valid_url(value):await msg.reply_text("لینک معتبر نیست؛ یک لینک کامل http یا https بفرست.");return
  flow.update(url=value,step="image");await msg.reply_text("حالا تصویر تبلیغ را بفرست (JPG/PNG/WebP، حداکثر ۵ مگابایت). اگر تصویر نمی‌خواهی «بدون عکس» بنویس.");return
 if step=="image" and value=="بدون عکس":flow.update(image=None,mime=None,step="start");await msg.reply_text("زمان شروع دلخواه را به شکل 2026-07-30 18:30 UTC بفرست یا «اولین زمان ممکن» بنویس.");return
 if step=="start":
  start=None
  if value!="اولین زمان ممکن":
   try:start=datetime.strptime(value,"%Y-%m-%d %H:%M").replace(tzinfo=UTC)
   except ValueError:await msg.reply_text("قالب زمان درست نیست؛ نمونه: 2026-07-30 18:30 یا «اولین زمان ممکن».");return
  user=update.effective_user;p=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "کاربر",language_code=user.language_code or "fa")
  if flow.get("revision_id"):
   ad_id=int(flow["revision_id"]);ok=await commerce.submit_revision(ad_id,p.id,flow["title"],flow["description"],flow["url"],flow.get("image"),flow.get("mime"),start)
   if not ok:raise ValueError("revision_closed")
  else:ad_id=await commerce.create_ad_request(p.id,flow["package"],flow["channel"],flow["title"],flow["description"],flow["url"],flow.get("image"),flow.get("mime"),start)
  context.user_data.pop(FLOW,None);await msg.reply_text(f"✅ درخواست #{ad_id} برای بررسی مدیر ثبت شد.\n\nدر صورت تأیید، صورتحساب استارز با اعتبار ۴۸ ساعت همین‌جا ارسال می‌شود. تا پیش از تأیید هیچ پرداختی انجام نمی‌دهی.")
async def photo(update:Update,context:ContextTypes.DEFAULT_TYPE):
 flow=context.user_data.get(FLOW);msg=update.effective_message
 if not flow or flow.get("step")!="image" or not msg.photo:return
 photo=msg.photo[-1]
 if photo.file_size and photo.file_size>5_000_000:await msg.reply_text("حجم تصویر بیشتر از ۵ مگابایت است.");return
 f=await photo.get_file();data=bytes(await f.download_as_bytearray());flow.update(image=data,mime="image/jpeg",step="start");await msg.reply_text("زمان شروع دلخواه را به شکل 2026-07-30 18:30 UTC بفرست یا «اولین زمان ممکن» بنویس.")
async def precheckout(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.pre_checkout_query;ok=await commerce.precheckout(q.invoice_payload,q.from_user.id,q.total_amount);await q.answer(ok=ok,error_message=None if ok else "صورتحساب نامعتبر یا منقضی شده است.")
async def paid(update:Update,context:ContextTypes.DEFAULT_TYPE):
 p=update.effective_message.successful_payment
 if not p:return
 purpose=await commerce.settle(p.invoice_payload,update.effective_user.id,p.total_amount,p.telegram_payment_charge_id,p.provider_payment_charge_id or None)
 await update.effective_message.reply_text("✅ پرداخت ثبت شد. کمپین به‌صورت خودکار در گروه‌های واجد شرایط برنامه‌ریزی می‌شود." if purpose=="advertisement" else "✅ سهم استارز ثبت شد؛ با تکمیل ۱۰ استار اشتراک گروه فعال می‌شود.")
def register(app):
 app.add_handler(CallbackQueryHandler(callback,pattern=r"^ad:"),group=0)
 app.add_handler(PreCheckoutQueryHandler(precheckout),group=0)
 app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT,paid),group=0)
 app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.PHOTO,photo),group=1)
 app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT & ~filters.COMMAND,text),group=2)
```

### `apps\telelife_bot\handlers\common.py`

```python
"""Shared handler plumbing: player resolution, guards, panel sending."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

from telegram import Message, Update
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from apps.telelife_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import player_repo
from packages.core.ui import Callback, schedule_cleanup


@dataclass(slots=True, frozen=True)
class Ctx:
    player: Player
    message: Message
    telegram_id: int


async def resolve(update: Update) -> Ctx | None:
    """Fetch-or-create the player and reject unplayable accounts."""
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return None

    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "رفیق",
        language_code=user.language_code or "fa",
    )

    if not player.playable:
        text = (
            fa.BANNED.format(reason=escape(player.ban_reason or fa.NO_REASON))
            if player.is_banned
            else fa.FROZEN
        )
        await message.reply_text(text)
        return None

    return Ctx(player=player, message=message, telegram_id=user.id)


async def guard_callback(update: Update) -> Callback | None:
    """Reject taps on someone else's panel without touching the database."""
    query = update.callback_query
    if query is None or query.data is None:
        return None
    parsed = Callback.parse(query.data)
    if parsed is None:
        await query.answer(fa.PANEL_EXPIRED, show_alert=True)
        return None
    if not parsed.owned_by(query.from_user.id):
        await query.answer(fa.NOT_YOUR_PANEL, show_alert=True)
        return None
    return parsed


async def send_panel(
    context: ContextTypes.DEFAULT_TYPE,
    message: Message,
    text: str,
    markup,  # type: ignore[no-untyped-def]
    panel: str,
    *,
    edit: bool = False,
) -> None:
    """Send or edit a panel and arm its auto-cleanup timer."""
    if edit:
        try:
            sent = await message.edit_text(text, reply_markup=markup)
        except BadRequest as exc:
            # Double taps and refreshes can legitimately produce an identical panel.
            # Telegram rejects that no-op with HTTP 400; it is not an application error.
            if "message is not modified" not in str(exc).lower():
                raise
            target = message
        else:
            target = sent if isinstance(sent, Message) else message
    else:
        target = await message.reply_text(text, reply_markup=markup)
    schedule_cleanup(context, target, panel)
```

### `apps\telelife_bot\handlers\economy_ui.py`

```python
"""Button-only Phase 3/4 UI. All navigation edits one owned glass panel."""
from __future__ import annotations
from uuid import uuid4
from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes
from apps.telelife_bot.handlers.common import guard_callback,resolve,send_panel
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.repositories import player_repo,production_repo
from packages.core.services import personal_economy,production,usd_market
from packages.core.utils import fmt

ERRORS={
 "insufficient_balance":"موجودی کافی نیست.","amount_out_of_bounds":"مبلغ خارج از محدوده مجاز است.",
 "job_locked":"مشاغل از سطح ۵ باز می‌شوند.","job_not_found":"هنوز شغلی انتخاب نکرده‌ای.",
 "housing_locked":"سطحت برای این خانه کافی نیست.","market_locked":"بازار دلار از سطح ۱۰ باز می‌شود.",
 "market_frozen":"بازار فعلاً برای حفاظت از اقتصاد متوقف است.","economy_frozen":"اقتصاد فعلاً متوقف است.",
 "daily_limit":"سقف معامله امروزت پر شده است.","invalid_housing":"انتخاب خانه معتبر نیست.",
 "invalid_job":"این شغل معتبر نیست.","max_level_reached":"به آخرین سطح ارتقا رسیده‌ای.",
}
def err(exc:Exception)->str:return ERRORS.get(str(exc),"عملیات انجام نشد؛ کمی بعد دوباره تلاش کن.")
def key(prefix:str,pid:int)->str:return f"ui:{prefix}:{pid}:{uuid4().hex[:16]}"

async def economy_panel(ctx,context):
 v=await personal_economy.view(ctx.player.id); title="بدون خانه"
 if v.housing:
  spec=get_config().section(f"phase3.housing.options.{v.housing['housing_code']}");title=str(spec['title'])
 text=fa.ECONOMY_PANEL.format(wallet=fmt.toman(v.wallet),savings=fmt.toman(v.savings),housing=title,living=fmt.toman(v.living_due))
 await send_panel(context,ctx.message,text,kb.economy_panel(ctx.telegram_id),"profile",edit=True)
async def savings(ctx,context):
 v=await personal_economy.view(ctx.player.id)
 await send_panel(context,ctx.message,f"🏦 <b>پس‌انداز امن</b>\n\nکیف پول: <b>{fmt.toman(v.wallet)}</b>\nپس‌انداز: <b>{fmt.toman(v.savings)}</b>\n\nمبلغ را انتخاب کن.",kb.savings_panel(ctx.telegram_id),"profile",edit=True)
async def housing(ctx,context):
 await send_panel(context,ctx.message,"🏠 <b>خانه و زندگی</b>\n\nخانه بهتر هزینه زندگی بیشتری دارد، اما مسیر رشد شخصیتت را کامل می‌کند. اجاره هفت‌روزه است؛ خرید دائمی.",kb.housing_panel(ctx.telegram_id),"profile",edit=True)
async def jobs(ctx,context):
 row=await production_repo.get(ctx.player.id)
 if row:
  a=production.accrue(row,__import__('datetime').datetime.now(__import__('datetime').UTC)); body=f"شغل: <b>{row['job_code']}</b>\nتولید ذخیره‌شده: <b>{fmt.number(a.stored)} / {fmt.number(a.capacity)}</b>\nنرخ: <b>{a.rate:.1f}</b> در ساعت\nسطح تولید: <b>{fmt.number(row['production_level'])}</b> · انبار: <b>{fmt.number(row['storage_level'])}</b>"
 else: body="هنوز شغلی نداری. شغل را با توجه به هدف اقتصادی‌ات انتخاب کن؛ انتخاب اولیه دائمی است."
 await send_panel(context,ctx.message,fa.JOBS_PANEL.format(body=body),kb.jobs_panel(ctx.telegram_id,bool(row)),"profile",edit=True)
async def market(ctx,context):
 v=await usd_market.view();p=await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player
 status="متوقف" if v.frozen else "سالم" if v.health>=75 else "نیازمند توجه" if v.health>=45 else "پرنوسان"
 text=fa.MARKET_PANEL.format(buy=fmt.toman(v.buy_price),sell=fmt.toman(v.sell_price),health=fmt.number(v.health),volume=fmt.usd(v.volume_cents),status=status,usd=fmt.usd(p.usd_cents))
 await send_panel(context,ctx.message,text,kb.market_panel(ctx.telegram_id),"profile",edit=True)

async def callback(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 parsed=await guard_callback(update);q=update.callback_query
 if parsed is None or q is None:return
 if parsed.action not in {"economy","savings","housing","living","deposit","withdraw","jobs","jchoose","jcollect","jupgrade","market","mbuy","msell","hrent","hbuy"}:return
 ctx=await resolve(update)
 if ctx is None:await q.answer();return
 try:
  a=parsed.action
  if a=="economy":await q.answer();await economy_panel(ctx,context)
  elif a=="savings":await q.answer();await savings(ctx,context)
  elif a=="housing":await q.answer();await housing(ctx,context)
  elif a=="jobs":await q.answer();await jobs(ctx,context)
  elif a=="market":await q.answer();await market(ctx,context)
  elif a in {"deposit","withdraw"}:
   await personal_economy.savings_transfer(ctx.player.id,int(parsed.arg),a,key(a,ctx.player.id));await q.answer(fa.ACTION_DONE);await savings(ctx,context)
  elif a=="living":
   paid,_=await personal_economy.pay_living(ctx.player.id,key(a,ctx.player.id));await q.answer("هزینه‌ای باقی نمانده." if not paid else f"{fmt.toman(paid)} پرداخت شد.",show_alert=True);await economy_panel(ctx,context)
  elif a in {"hrent","hbuy"}:
   await personal_economy.acquire_housing(ctx.player.id,parsed.arg,"rent" if a=="hrent" else "owned",key(a,ctx.player.id));await q.answer(fa.ACTION_DONE,show_alert=True);await economy_panel(ctx,context)
  elif a=="jchoose":
   if not await production.choose(ctx.player.id,parsed.arg):raise ValueError("job_already_selected")
   await q.answer("شغلت ثبت شد!",show_alert=True);await jobs(ctx,context)
  elif a=="jcollect":
   amount,xp=await production.collect(ctx.player.id,key(a,ctx.player.id));await q.answer(f"{fmt.number(amount)} واحد و {fmt.number(xp)} XP دریافت شد.",show_alert=True);await jobs(ctx,context)
  elif a=="jupgrade":
   lvl=await production.upgrade(ctx.player.id,parsed.arg,key(a,ctx.player.id));await q.answer(f"به سطح {fmt.number(lvl)} ارتقا یافت.",show_alert=True);await jobs(ctx,context)
  elif a in {"mbuy","msell"}:
   r=await usd_market.trade(ctx.player.id,"buy" if a=="mbuy" else "sell",int(parsed.arg),key(a,ctx.player.id));await q.answer(f"معامله انجام شد؛ کارمزد {fmt.toman(r.fee)}",show_alert=True);await market(ctx,context)
 except (ValueError,PermissionError) as exc:await q.answer(err(exc),show_alert=True)

def register(app)->None:app.add_handler(CallbackQueryHandler(callback,pattern=r"^tl:(economy|savings|housing|living|deposit|withdraw|jobs|jchoose|jcollect|jupgrade|market|mbuy|msell|hrent|hbuy):"),group=-1)
```

### `apps\telelife_bot\handlers\life.py`

```python
"""Unified, Persian, single-message TeleLife experience."""
from __future__ import annotations
from datetime import UTC,datetime
from uuid import uuid4
from html import escape
from telegram import Update, InputFile
from telegram.ext import CallbackQueryHandler,ContextTypes,MessageHandler,filters
from apps.telelife_bot.handlers.common import guard_callback,resolve
from apps.telelife_bot.handlers.panel import show
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.repositories import player_repo,progression_repo,production_repo,ui_state_repo
from packages.core.services import daily,missions,personal_economy,production,progression,unlocks,usd_market,xp,market_chart
from packages.core.utils import fmt

JOB_FA={"farmer":"کشاورز","miner":"معدن‌کار","trader":"بازرگان","journalist":"روزنامه‌نگار","doctor":"پزشک","programmer":"برنامه‌نویس","engineer":"مهندس"}
ASSET_FA={"IRT":"تومان","USD":"دلار","food":"محصول کشاورزی","minerals":"مواد معدنی","technology":"فناوری","energy":"انرژی"}
ERR={"amount_out_of_bounds":"مبلغ خارج از محدوده مجاز است.","invalid_housing":"این خانه معتبر نیست.","market_not_initialized":"بازار هنوز راه‌اندازی نشده است.","invalid_upgrade":"نوع ارتقا معتبر نیست.","player_not_found":"بازیکن پیدا نشد.","insufficient_balance":"موجودی کافی نیست.","job_locked":"شغل‌ها از سطح ۵ باز می‌شوند.","market_locked":"بازار دلار از سطح ۱۰ باز می‌شود.","housing_locked":"سطحت برای این خانه کافی نیست.","daily_limit":"سقف معامله امروزت پر شده است.","market_frozen":"بازار فعلاً متوقف است.","economy_frozen":"اقتصاد فعلاً متوقف است.","max_level_reached":"این بخش به آخرین سطح رسیده است.","job_not_found":"ابتدا یک شغل انتخاب کن.","invalid_job":"این شغل معتبر نیست.","insufficient_player_balance":"موجودی کافی نیست."}
def why(e):return ERR.get(str(e),"این کار انجام نشد؛ شرایط را دوباره بررسی کن.")
def ik(a,p):return f"life:{a}:{p}:{uuid4().hex[:12]}"
async def answer(q,text=None,show_alert=False):
 try:await q.answer(text,show_alert=show_alert)
 except Exception:return
async def panel(ctx,c,text,mark):return await show(c,ctx.player.id,ctx.message.chat_id,text,mark,message=ctx.message if getattr(ctx.message,'reply_markup',None) is not None else None)
async def fresh(ctx):return await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player
async def home(ctx,c):
 p=await fresh(ctx);st=await ui_state_repo.ensure_life(p.id);_,_,last=await daily.state(p.id);cur,need=progression.level_progress(p.level,p.xp);left=max(0,need-cur)
 step=int(st['onboarding_step']);goal=("چهار قدم شروع را کامل کن" if step<4 else "کارهای امروز را انجام بده و به سطح ۵ برس" if p.level<5 else "شغلت را انتخاب کن، کار کن و درآمدت را رشد بده")
 hint="🚀 مسیر شروع آماده ادامه است." if step<4 else "🎯 کارهای امروز بهترین راه رشد هستند."
 text=fa.HOME.format(name=escape(p.first_name),level=fmt.number(p.level),bar=fmt.progress_bar(cur,need,width=10),left=fmt.number(left),wallet=fmt.toman(p.wallet_toman),happy=fmt.number(p.happiness),goal=goal,hint=hint)
 await panel(ctx,c,text,kb.home(ctx.telegram_id,daily.claimable(last),step))
async def journey(ctx,c):
 st=await ui_state_repo.ensure_life(ctx.player.id);step=int(st['onboarding_step']);bodies=["هدف نخست را ثبت کن تا نوار پیشرفت و مسیر رشدت فعال شود.","سرمایه آغازین را بگیر؛ بلافاصله بعد از آن کارهای روزانه منتظرت هستند.","نخستین کار روزانه را باز کن؛ پاداش آغاز فقط شروع بازی است، نه پایان آن.","وارد زندگی اصلی شو؛ تا سطح ۵ با کارهای روزانه رشد کن، سپس شغل انتخاب کن و درآمد بساز.","مسیر شروع کامل شده است؛ هدیه روزانه، کارها، شغل، بانک و خانه چرخه ادامه بازی را می‌سازند."]
 await panel(ctx,c,fa.JOURNEY.format(body=bodies[min(step,4)],done=fmt.number(step),bar=fmt.progress_bar(step,4,width=8)),kb.journey(ctx.telegram_id,step))
async def profile(ctx,c):
 p=await fresh(ctx);cur,need=progression.level_progress(p.level,p.xp);rank=await progression_repo.rank_by_level(p.id);streak,_,_=await daily.state(p.id)
 text=fa.PROFILE.format(name=escape(p.first_name),level=fmt.number(p.level),rank=fmt.number(rank),bar=fmt.progress_bar(cur,need),xp=fmt.number(cur),need=fmt.number(need),wallet=fmt.toman(p.wallet_toman),savings=fmt.toman(p.savings_toman),usd=fmt.usd(p.usd_cents),happy=fmt.number(p.happiness),rep=fmt.number(p.reputation),streak=fmt.number(streak))
 from packages.core import db
 mig=await db.fetchrow("SELECT migrant_until,political_hold_until FROM citizenships WHERE player_id=$1 AND is_active",p.id)
 if mig and mig["migrant_until"] and mig["migrant_until"]>datetime.now(UTC):text+="\n\n🧳 <b>وضعیت: مهاجر</b>"
 if mig and mig["political_hold_until"] and mig["political_hold_until"]>datetime.now(UTC):text+="\nمحدودیت فعالیت سیاسی تا: "+mig["political_hold_until"].strftime('%Y-%m-%d')
 await panel(ctx,c,text,kb.back(ctx.telegram_id))
async def daily_page(ctx,c):
 streak,best,last=await daily.state(ctx.player.id);ready=daily.claimable(last)
 text=fa.DAILY_READY.format(streak=fmt.number(streak),amount=fmt.toman(daily.preview(streak+1))) if ready else fa.DAILY_WAIT.format(streak=fmt.number(streak),amount=fmt.toman(daily.tomorrow_preview(streak)))
 await panel(ctx,c,text,kb.daily(ctx.telegram_id,ready))
async def missions_page(ctx,c):
 p=await fresh(ctx);items=await missions.ensure_today(p.id,max(1,p.level));ready=[m.key for m in items if m.done and not m.claimed];rows=[]
 for m in items:rows.append(("✅" if m.claimed else "🎁" if m.done else "▫️")+f" {m.title} — {fmt.number(m.progress)}/{fmt.number(m.target)} · {fmt.toman(m.reward_toman)}")
 await panel(ctx,c,fa.MISSIONS.format(rows="\n".join(rows) or "امروز کاری ثبت نشده است."),kb.missions(ctx.telegram_id,ready))
async def economy(ctx,c):
 v=await personal_economy.view(ctx.player.id);house="نداری" if not v.housing else str(get_config().get(f"phase3.housing.options.{v.housing['housing_code']}.title"));await panel(ctx,c,fa.ECONOMY.format(wallet=fmt.toman(v.wallet),savings=fmt.toman(v.savings),house=house,due=fmt.toman(v.living_due)),kb.economy(ctx.telegram_id))
async def savings_page(ctx,c):
 v=await personal_economy.view(ctx.player.id);await panel(ctx,c,f"🏦 <b>مدیریت پس‌انداز</b>\n\nکیف پول: <b>{fmt.toman(v.wallet)}</b>\nپس‌انداز: <b>{fmt.toman(v.savings)}</b>\n\nواریز، پول را از کیف پول به پس‌انداز منتقل می‌کند؛ برداشت برعکس آن است. مبلغ را انتخاب کن.",kb.savings(ctx.telegram_id))
async def housing_page(ctx,c):
 p=await fresh(ctx);v=await personal_economy.view(p.id);current="نداری" if not v.housing else str(get_config().get(f"phase3.housing.options.{v.housing['housing_code']}.title"));await panel(ctx,c,f"🏠 <b>خانه و زندگی</b>\n\nخانه فعلی: <b>{current}</b>\n\nاتاق از سطح ۳، آپارتمان از سطح ۸ و ویلا از سطح ۲۰ باز می‌شود. اجاره هفت‌روزه است و خرید دائمی. خانه بهتر هزینه روزانه بیشتری دارد؛ پیش از انتخاب، موجودی و سطح خودت را بررسی کن.",kb.housing(ctx.telegram_id))
async def jobs(ctx,c):
 p=await fresh(ctx);row=await production_repo.get(p.id)
 if row:
  a=production.accrue(row,datetime.now(UTC));job=JOB_FA.get(str(row['job_code']),'شغل');asset=ASSET_FA.get(str(row['output_asset_code']),'درآمد');body=f"شغل: <b>{job}</b>\nدرآمد آماده: <b>{fmt.number(a.stored)} از {fmt.number(a.capacity)} {asset}</b>\nسرعت کار: <b>{fmt.number(round(a.rate,1))} {asset} در ساعت</b>\n\nهر وقت مقداری آماده شد، «کار کن و درآمد بگیر» را بزن. اگر ظرفیت پر شود، تولید بیشتر متوقف می‌شود."
 else:body=("هنوز شغلی نداری. یکی را بر اساس نوع درآمدش انتخاب کن؛ انتخاب اولیه قابل تعویض نیست." if p.level>=5 else f"شغل از سطح ۵ باز می‌شود. اکنون سطح {fmt.number(p.level)} هستی؛ با کارهای امروز تجربه بگیر.")
 await panel(ctx,c,fa.JOBS.format(body=body),kb.jobs(ctx.telegram_id,bool(row),p.level>=5))
async def market(ctx,c):
 v=await usd_market.view();p=await fresh(ctx);status="متوقف" if v.frozen else "سالم" if v.health>=75 else "پرنوسان"
 extra="\n\nبازار از سطح ۱۰ باز می‌شود؛ با کارهای امروز سطح بگیر." if p.level<10 else ""
 rows=await market_chart.candles(24)
 previous=c.user_data.get("market_chart_message_id")
 if previous:
  try:await c.bot.delete_message(chat_id=ctx.message.chat_id,message_id=previous)
  except Exception:pass
 chart_message=await c.bot.send_photo(chat_id=ctx.message.chat_id,photo=InputFile(market_chart.render(rows),filename="usdt_30m.png"),caption="نمودار واقعی USDT/IRT · کندل ۳۰ دقیقه‌ای · ۲۴ ساعت اخیر\nمنبع نرخ: Zipodo · فاصله‌های بدون داده پر نمی‌شوند.")
 c.user_data["market_chart_message_id"]=chart_message.message_id
 await panel(ctx,c,fa.MARKET.format(buy=fmt.toman(v.buy_price),sell=fmt.toman(v.sell_price),health=fmt.number(v.health),status=status,usd=fmt.usd(p.usd_cents))+extra,kb.market(ctx.telegram_id,p.level>=10))
async def unlock_page(ctx,c):
 p=await fresh(ctx);rows=[]
 for level,spec in get_config().section('unlocks.levels').items():rows.append(("✅" if p.level>=int(level) else "🔒")+f" سطح {fmt.number(level)} — {spec['title']}")
 await panel(ctx,c,fa.UNLOCKS.format(rows="\n".join(rows)),kb.back(ctx.telegram_id))
async def start(update,c):
 ctx=await resolve(update)
 if ctx:await home(ctx,c)
async def text_start(update,c):
 if c.user_data.get('ad_request_flow'):return
 if update.effective_chat and update.effective_chat.type=='private':
  ctx=await resolve(update)
  if ctx:await home(ctx,c)
async def callback(update,c):
 parsed=await guard_callback(update);q=update.callback_query
 if not parsed or not q:return
 ctx=await resolve(update)
 if not ctx:await answer(q,);return
 a=parsed.action
 if a=='advertise':
  from apps.telelife_bot.handlers.advertising import begin
  await begin(update,c);return
 try:
  if a in {'home','profile','daily','missions','economy','jobs','market','unlocks','journey','housing','savings'}:
   await answer(q,);fn={'home':home,'profile':profile,'daily':daily_page,'missions':missions_page,'economy':economy,'jobs':jobs,'market':market,'unlocks':unlock_page,'journey':journey,'housing':housing_page,'savings':savings_page}[a];await fn(ctx,c);return
  if a=='jstep':
   step=int(parsed.arg);state=await ui_state_repo.ensure_life(ctx.player.id);expected=int(state['onboarding_step'])
   if step!=expected:await answer(q,'این قدم قبلاً انجام شده یا هنوز نوبتش نرسیده است.',show_alert=True);await journey(ctx,c);return
   result=await xp.grant(ctx.player.id,'onboarding_step',idempotency_key=f'onboarding:{ctx.player.id}:{step}',amount=35 if step<3 else 80);await ui_state_repo.set_step(ctx.player.id,min(4,step+1));await answer(q,f"+{fmt.number(result.granted)} تجربه؛ قدم بعد باز شد.",show_alert=True)
   if step==1:await missions_page(ctx,c)
   elif step==3:await home(ctx,c)
   else:await journey(ctx,c)
   return
  if a=='claim':
   r=await daily.claim(ctx.player.id)
   if r.already_claimed:await answer(q,"امروز گرفته‌ای.");await daily_page(ctx,c);return
   await xp.grant(ctx.player.id,'daily_claim',idempotency_key=xp.day_key('daily',ctx.player.id),amount=r.reward_xp);await missions.report_progress(ctx.player.id,'claim_daily');await answer(q,"پاداش دریافت شد.",show_alert=True);await panel(ctx,c,fa.DAILY_DONE.format(amount=fmt.toman(r.reward_toman),xp=fmt.number(r.reward_xp),streak=fmt.number(r.streak)),kb.daily(ctx.telegram_id,False));return
  if a=='mclaim':
   m=await missions.claim(ctx.player.id,parsed.arg)
   if not m:await answer(q,"هنوز کامل نشده است.",show_alert=True);return
   await xp.grant(ctx.player.id,'mission_complete',idempotency_key=f"mission-xp:{ctx.player.id}:{parsed.arg}:{xp.day_key('d',0)}",amount=m.reward_xp);await answer(q,"پاداش مأموریت دریافت شد.",show_alert=True);await missions_page(ctx,c);return
  if a in {'deposit','withdraw'}:await personal_economy.savings_transfer(ctx.player.id,int(parsed.arg),a,ik(a,ctx.player.id));await answer(q,"انتقال انجام شد.",show_alert=True);await savings_page(ctx,c);return
  if a=='living':paid,_=await personal_economy.pay_living(ctx.player.id,ik(a,ctx.player.id));await answer(q,"تسویه شد." if paid else "بدهی نداری.",show_alert=True);await economy(ctx,c);return
  if a in {'hrent','hbuy'}:await personal_economy.acquire_housing(ctx.player.id,parsed.arg,'rent' if a=='hrent' else 'owned',ik(a,ctx.player.id));await answer(q,"خانه ثبت شد.",show_alert=True);await housing_page(ctx,c);return
  if a=='jchoose':await production.choose(ctx.player.id,parsed.arg);await answer(q,"شغل انتخاب شد.",show_alert=True);await jobs(ctx,c);return
  if a=='jcollect':
   amount,gain=await production.collect(ctx.player.id,ik(a,ctx.player.id));msg=(f"{fmt.number(amount)} واحد درآمد و {fmt.number(gain)} تجربه گرفتی." if amount else "هنوز درآمد قابل دریافت آماده نشده است؛ کمی بعد دوباره تلاش کن.");await answer(q,msg,show_alert=True);await jobs(ctx,c);return
  if a=='jupgrade':lvl=await production.upgrade(ctx.player.id,parsed.arg,ik(a,ctx.player.id));await answer(q,f"ارتقا به سطح {fmt.number(lvl)}",show_alert=True);await jobs(ctx,c);return
  if a in {'mbuy','msell'}:r=await usd_market.trade(ctx.player.id,'buy' if a=='mbuy' else 'sell',int(parsed.arg),ik(a,ctx.player.id));await answer(q,f"معامله انجام شد؛ کارمزد {fmt.toman(r.fee)}",show_alert=True);await market(ctx,c);return
  await answer(q,)
 except (ValueError,PermissionError) as e:await answer(q,why(e),show_alert=True)
def register(app):
 app.add_handler(CallbackQueryHandler(callback,pattern=r'^tl:'));app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT,text_start))
```

### `apps\telelife_bot\handlers\panel.py`

```python
"""One persistent TeleLife panel: edit first, send only when no editable panel exists."""
from __future__ import annotations
from telegram import Message
from telegram.error import BadRequest,Forbidden
from telegram.ext import ContextTypes
from packages.core.repositories import ui_state_repo

async def show(context:ContextTypes.DEFAULT_TYPE,player_id:int,chat_id:int,text:str,markup,*,message:Message|None=None):
 state=await ui_state_repo.ensure_life(player_id); target=None
 # A callback's own message is always the freshest valid panel.
 if message is not None and getattr(message,"message_id",None):
  try:
   result=await message.edit_text(text,reply_markup=markup);target=result if isinstance(result,Message) else message
  except BadRequest as exc:
   if "message is not modified" in str(exc).lower():target=message
   elif "message to edit not found" not in str(exc).lower() and "message can't be edited" not in str(exc).lower():raise
 # On /start, edit the remembered panel instead of producing another one.
 if target is None and state and state["life_message_id"]:
  try:
   result=await context.bot.edit_message_text(chat_id=int(state["life_chat_id"] or chat_id),message_id=int(state["life_message_id"]),text=text,reply_markup=markup)
   target=result if isinstance(result,Message) else None
  except (BadRequest,Forbidden):target=None
 if target is None:
  target=await context.bot.send_message(chat_id=chat_id,text=text,reply_markup=markup)
 await ui_state_repo.set_life_panel(player_id,chat_id,target.message_id if target else int(state["life_message_id"]))
 return target
```

### `apps\telelife_bot\handlers\profile.py`

```python
"""/profile - the first screen that must feel premium."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from apps.telelife_bot.texts import fa
from packages.core.repositories import player_repo
from packages.core.services import progression
from packages.core.utils import fmt


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return

    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "رفیق",
        language_code=user.language_code or "fa",
    )

    if not player.playable:
        text = (
            fa.BANNED.format(reason=player.ban_reason or fa.NO_REASON)
            if player.is_banned
            else fa.FROZEN
        )
        await message.reply_text(text)
        return

    current_xp, needed = progression.level_progress(player.level, player.xp)

    await message.reply_text(
        fa.PROFILE.format(
            name=player.first_name,
            level=fmt.number(player.level),
            prestige=fmt.number(player.prestige),
            xp_bar=fmt.progress_bar(current_xp, needed),
            xp=fmt.number(current_xp),
            xp_needed=fmt.number(needed),
            wallet=fmt.toman(player.wallet_toman),
            savings=fmt.toman(player.savings_toman),
            usd=fmt.usd(player.usd_cents),
            happiness=fmt.number(player.happiness),
            reputation=fmt.number(player.reputation),
            net_worth=fmt.toman(player.net_worth_toman),
        )
    )


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
```

### `apps\telelife_bot\handlers\progression.py`

```python
"""Profile, daily, missions and the unlock map - commands plus glass callbacks."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from apps.telelife_bot.handlers.common import Ctx, guard_callback, resolve, send_panel
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from apps.telelife_bot.views import render
from packages.core.repositories import player_repo, progression_repo
from packages.core.services import daily, missions, progression, xp
from packages.core.utils import fmt

MISSIONS_UNLOCK_LEVEL = 2


async def _announce_level_up(ctx: Ctx, result: xp.XPResult) -> None:
    # Level state is rendered inside the persistent panel; no extra message.
    return


async def _render_profile(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    result = await xp.grant(
        ctx.player.id, "profile_view", idempotency_key=xp.day_key("profile", ctx.player.id)
    )
    player = await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player

    streak, _, last_claim = await daily.state(player.id)
    rank = await progression_repo.rank_by_level(player.id)
    _, needed = progression.level_progress(player.level, player.xp)

    text = render.profile(player, rank=rank, streak=streak, xp_needed=needed)
    markup = kb.profile_panel(
        ctx.telegram_id,
        daily_ready=daily.claimable(last_claim),
        missions_unlocked=player.level >= MISSIONS_UNLOCK_LEVEL,
    )
    await send_panel(context, ctx.message, text, markup, "profile", edit=edit)
    await missions.report_progress(player.id, "check_profile")
    await _announce_level_up(ctx, result)


async def _render_daily(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    streak, best, last_claim = await daily.state(ctx.player.id)
    can_claim = daily.claimable(last_claim)
    if can_claim:
        text = render.daily_ready(streak, best)
    else:
        text = render.daily_already(streak, daily.tomorrow_preview(streak))
    await send_panel(
        context,
        ctx.message,
        text,
        kb.daily_panel(ctx.telegram_id, claimable=can_claim),
        "profile",
        edit=edit,
    )


async def _render_missions(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    if ctx.player.level < MISSIONS_UNLOCK_LEVEL:
        await ctx.message.reply_text(fa.MISSIONS_LOCKED)
        return
    items = await missions.ensure_today(ctx.player.id, ctx.player.level)
    ready = [m.key for m in items if m.done and not m.claimed]
    await send_panel(
        context, ctx.message, render.missions(items),
        kb.missions_panel(ctx.telegram_id, ready), "profile", edit=edit,
    )


async def _render_unlocks(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    await send_panel(
        context, ctx.message, render.unlocks_map(ctx.player.level),
        kb.unlocks_panel(ctx.telegram_id), "profile", edit=edit,
    )


# ---------------- commands ----------------

async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_profile(ctx, context, edit=False)


async def cmd_daily(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_daily(ctx, context, edit=False)


async def cmd_missions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_missions(ctx, context, edit=False)


async def cmd_unlocks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_unlocks(ctx, context, edit=False)


# ---------------- callbacks ----------------

async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parsed = await guard_callback(update)
    query = update.callback_query
    if parsed is None or query is None:
        return
    ctx = await resolve(update)
    if ctx is None:
        await query.answer()
        return

    action = parsed.action
    if action == "profile":
        await query.answer()
        await _render_profile(ctx, context, edit=True)
    elif action == "daily":
        await query.answer()
        await _render_daily(ctx, context, edit=True)
    elif action == "missions":
        await query.answer()
        await _render_missions(ctx, context, edit=True)
    elif action == "unlocks":
        await query.answer()
        await _render_unlocks(ctx, context, edit=True)
    elif action == "claim":
        await _do_claim(ctx, context, update)
    elif action == "mclaim":
        await _do_mission_claim(ctx, context, update, parsed.arg)
    else:
        await query.answer()


async def _do_claim(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, update: Update) -> None:
    query = update.callback_query
    assert query is not None

    result = await daily.claim(ctx.player.id)
    if result.already_claimed:
        await query.answer(fa.MISSION_NOT_READY, show_alert=False)
        await _render_daily(ctx, context, edit=True)
        return

    xp_result = await xp.grant(
        ctx.player.id,
        "daily_claim",
        idempotency_key=xp.day_key("daily", ctx.player.id),
        amount=result.reward_xp,
    )
    await missions.report_progress(ctx.player.id, "claim_daily")
    await missions.report_progress(ctx.player.id, "streak_keeper")

    text = render.daily_claimed(result)
    if xp_result.capped:
        text += fa.XP_CAPPED

    await query.answer()
    await send_panel(
        context, ctx.message, text,
        kb.daily_panel(ctx.telegram_id, claimable=False), "profile", edit=True,
    )
    await _announce_level_up(ctx, xp_result)


async def _do_mission_claim(
    ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, update: Update, mission_key: str
) -> None:
    query = update.callback_query
    assert query is not None

    claimed = await missions.claim(ctx.player.id, mission_key)
    if claimed is None:
        await query.answer(fa.MISSION_NOT_READY, show_alert=True)
        return

    xp_result = await xp.grant(
        ctx.player.id,
        "mission_complete",
        idempotency_key=f"mission:{ctx.player.id}:{mission_key}:{xp.day_key('d', 0)}",
        amount=claimed.reward_xp,
    )
    await query.answer(
        fa.MISSION_CLAIMED.format(
            title=claimed.title,
            reward=fmt.toman(claimed.reward_toman),
            xp=fmt.number(claimed.reward_xp),
        ).replace("<b>", "").replace("</b>", "").replace("\n", " "),
        show_alert=True,
    )
    await _render_missions(ctx, context, edit=True)
    await _announce_level_up(ctx, xp_result)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CallbackQueryHandler(on_callback, pattern=r"^tl:"))
```

### `apps\telelife_bot\handlers\start.py`

```python
"""/start and /help for TeleLife."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from apps.telelife_bot.handlers.common import resolve
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.repositories import player_repo
from packages.core.services import daily
from packages.core.utils import fmt


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if user is None:
        return
    existing = await player_repo.get_by_telegram_id(user.id)

    ctx = await resolve(update)
    if ctx is None:
        return

    if existing is None:
        cfg = get_config()
        text = fa.WELCOME_NEW.format(
            name=ctx.player.first_name,
            wallet=fmt.toman(cfg.int_("economy.starting_balance.wallet_toman")),
        )
    else:
        text = fa.WELCOME_BACK.format(
            name=ctx.player.first_name,
            level=fmt.number(ctx.player.level),
            wallet=fmt.toman(ctx.player.wallet_toman),
        )

    _, _, last_claim = await daily.state(ctx.player.id)
    await ctx.message.reply_text(
        text,
        reply_markup=kb.profile_panel(
            ctx.telegram_id,
            daily_ready=daily.claimable(last_claim),
            missions_unlocked=ctx.player.level >= 2,
        ),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(fa.HELP)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("start", start))
```

### `apps\telelife_bot\keyboards\__init__.py`

```python
from apps.telelife_bot.keyboards import main

__all__ = ["main"]
```

### `apps\telelife_bot\keyboards\main.py`

```python
"""صفحه‌کلیدهای فارسی بات زندگی؛ در هر صفحه فقط یک اقدام اصلی داریم."""
from telegram import InlineKeyboardMarkup
from packages.core.ui import Keyboard, Style, button, cb

NS = "tl"

def B(text, action, owner, arg="", style=Style.GLASS):
    return button(text, cb(NS, action, owner, arg), style=style)

def home(owner: int, daily_ready: bool, onboarding: int = 4) -> InlineKeyboardMarkup:
    k = Keyboard()
    if onboarding < 4:
        k.row(B("🚀 ادامه مسیر شروع", "journey", owner, style=Style.PRIMARY))
    else:
        k.row(B("🎯 کارهای امروز", "missions", owner, style=Style.PRIMARY),
              B("🎁 هدیه روزانه", "daily", owner, style=Style.SUCCESS if daily_ready else Style.GLASS))
    if onboarding < 4:
        k.row(B("🎯 کارهای امروز", "missions", owner),
              B("🎁 هدیه روزانه", "daily", owner, style=Style.SUCCESS if daily_ready else Style.GLASS))
    k.row(B("💼 کار و دریافت درآمد", "jobs", owner), B("💳 دارایی و بانک", "economy", owner))
    k.row(B("💵 بازار ارز", "market", owner), B("🏠 خانه و زندگی", "housing", owner))
    k.row(B("🪪 شخصیت من", "profile", owner), B("🗺 مسیر پیشرفت", "unlocks", owner))
    k.row(B("📣 درخواست تبلیغ", "advertise", owner))
    return k.build()

def journey(owner, step):
    labels = {0:"✨ تعیین هدف نخست", 1:"🎁 دریافت سرمایه آغازین", 2:"🎯 بازکردن نخستین کار روزانه", 3:"🏁 ورود به زندگی اصلی"}
    k = Keyboard()
    if 0 <= step < 4:
        k.row(B(labels[step], "jstep", owner, str(step), Style.PRIMARY))
    k.row(B("🏠 خانه", "home", owner))
    return k.build()

def back(owner, action="home"):
    return Keyboard().row(B("🏠 خانه", action, owner, style=Style.PRIMARY)).build()

def daily(owner, ready):
    k = Keyboard()
    if ready:
        k.row(B("🎁 دریافت هدیه", "claim", owner, style=Style.SUCCESS))
    k.row(B("🎯 ادامه با کارهای امروز", "missions", owner, style=Style.PRIMARY), B("🏠 خانه", "home", owner))
    return k.build()

def missions(owner, keys):
    k = Keyboard()
    for i, key in enumerate(keys):
        k.row(B(f"🎁 دریافت پاداش کار {i + 1}", "mclaim", owner, key, Style.SUCCESS))
    k.row(B("🔄 تازه‌سازی", "missions", owner, style=Style.PRIMARY), B("🏠 خانه", "home", owner))
    return k.build()

def economy(owner):
    return (Keyboard().row(B("🏦 مدیریت پس‌انداز", "savings", owner, style=Style.PRIMARY), B("🧾 پرداخت هزینه زندگی", "living", owner, style=Style.SUCCESS))
            .row(B("🏠 انتخاب خانه", "housing", owner), B("🏠 منوی اصلی", "home", owner)).build())

def savings(owner):
    return (Keyboard().row(B("واریز ۵۰ هزار", "deposit", owner, "50000", Style.PRIMARY), B("برداشت ۵۰ هزار", "withdraw", owner, "50000"))
            .row(B("واریز ۲۰۰ هزار", "deposit", owner, "200000"), B("برداشت ۲۰۰ هزار", "withdraw", owner, "200000"))
            .row(B("↩️ بازگشت", "economy", owner)).build())

def housing(owner):
    return (Keyboard().row(B("اجاره اتاق", "hrent", owner, "room", Style.PRIMARY), B("خرید اتاق", "hbuy", owner, "room"))
            .row(B("اجاره آپارتمان", "hrent", owner, "apartment"), B("خرید آپارتمان", "hbuy", owner, "apartment"))
            .row(B("خرید ویلا", "hbuy", owner, "villa"), B("↩️ بازگشت", "economy", owner)).build())

def jobs(owner, has_job, unlocked=True):
    k = Keyboard()
    if not unlocked:
        return k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY)).row(B("🏠 خانه", "home", owner)).build()
    if has_job:
        k.row(B("🛠 کار کن و درآمد بگیر", "jcollect", owner, style=Style.SUCCESS))
        k.row(B("⚙️ ارتقای مهارت", "jupgrade", owner, "production", Style.PRIMARY), B("🗄 افزایش ظرفیت", "jupgrade", owner, "storage"))
    else:
        k.row(B("🌾 کشاورز", "jchoose", owner, "farmer", Style.PRIMARY), B("⛏ معدن‌کار", "jchoose", owner, "miner"))
        k.row(B("💻 برنامه‌نویس", "jchoose", owner, "programmer"), B("📈 بازرگان", "jchoose", owner, "trader"))
        k.row(B("⚡ مهندس", "jchoose", owner, "engineer"), B("🩺 پزشک", "jchoose", owner, "doctor"))
        k.row(B("📰 روزنامه‌نگار", "jchoose", owner, "journalist"))
    k.row(B("🏠 منوی اصلی", "home", owner))
    return k.build()

def market(owner, unlocked=True):
    k = Keyboard()
    if not unlocked:
        return k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY)).row(B("🏠 خانه", "home", owner)).build()
    return (k.row(B("خرید ۱۰ دلار", "mbuy", owner, "1000", Style.PRIMARY), B("فروش ۱۰ دلار", "msell", owner, "1000"))
            .row(B("خرید ۵۰ دلار", "mbuy", owner, "5000"), B("فروش ۵۰ دلار", "msell", owner, "5000"))
            .row(B("🔄 تازه‌سازی", "market", owner), B("🏠 خانه", "home", owner)).build())
```

### `apps\telelife_bot\main.py`

```python
from telegram import BotCommandScopeAllGroupChats,BotCommandScopeAllPrivateChats
from telegram.ext import Application
from apps.telelife_bot.handlers import life,advertising
from apps.telelife_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service

async def post_init(application:Application)->None:
 await application.bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
 await application.bot.delete_my_commands(scope=BotCommandScopeAllGroupChats())
def register(application:Application)->None:life.register(application);advertising.register(application);application.post_init=post_init;application.add_error_handler(make_error_handler(fa.ERROR))
def main()->None:run_bot(Service.TELELIFE,register)
if __name__=='__main__':main()
```

### `apps\telelife_bot\texts\__init__.py`

```python
"""Package apps.telelife_bot.texts."""
```

### `apps\telelife_bot\texts\fa.py`

```python
BANNED="دسترسی حساب محدود شده است. دلیل: {reason}";NO_REASON="ثبت نشده";FROZEN="حساب موقتاً متوقف است."
PANEL_EXPIRED="این صفحه قدیمی شده است؛ پیام «خانه» را بفرست.";NOT_YOUR_PANEL="این صفحه برای بازیکن دیگری است.";ERROR="مشکلی پیش آمد؛ دوباره امتحان کن."
HOME="""🌆 <b>زندگیِ {name}</b>

🎚 سطح <b>{level}</b>  ·  {bar}
✨ تا سطح بعد: <b>{left} تجربه</b>
👛 پول نقد: <b>{wallet}</b>
😊 حال شخصیت: <b>{happy}٪</b>

🎯 <b>هدف بعدی:</b> {goal}
{hint}

از دکمه‌ها انتخاب کن؛ لازم نیست هیچ فرمانی حفظ کنی."""
JOURNEY="""🚀 <b>شروع زندگی تازه</b>

{body}

پیشرفت شروع: <b>{done} از ۴</b>
{bar}

هر قدم تو را مستقیم به فعالیت بعدی می‌برد تا بعد از نخستین پاداش، بازی رها نشود."""
PROFILE="""🪪 <b>شخصیت من</b>

نام: <b>{name}</b>
سطح: <b>{level}</b> · رتبه: <b>{rank}</b>
تجربه: {bar}  <b>{xp}/{need}</b>

👛 کیف پول: <b>{wallet}</b>
🏦 پس‌انداز: <b>{savings}</b>
💵 دلار: <b>{usd}</b>
😊 شادی: <b>{happy}٪</b> · ⭐ شهرت: <b>{rep}</b>
🔥 حضور پیوسته: <b>{streak} روز</b>"""
DAILY_READY="🎁 <b>هدیه امروز آماده است</b>\n\n🔥 حضور پیوسته: {streak} روز\n💰 هدیه امروز: <b>{amount}</b>\n\nبعد از دریافت، دکمه «ادامه با کارهای امروز» تو را وارد چرخه اصلی بازی می‌کند."
DAILY_DONE="✅ <b>هدیه امروز دریافت شد</b>\n\n💰 +{amount}\n✨ +{xp} تجربه\n🔥 حضور پیوسته: {streak} روز\n\nاین آغاز امروز توست؛ حالا یکی از کارهای امروز را کامل کن."
DAILY_WAIT="⏳ هدیه امروز را گرفته‌ای.\n\n🔥 حضور پیوسته: {streak} روز\nهدیه فردا: <b>{amount}</b>\n\nتا فردا می‌توانی کارهای روزانه، شغل، بانک و خانه را ادامه بدهی."
MISSIONS="🎯 <b>کارهای امروز</b>\n\n{rows}\n\n▫️ یعنی در حال انجام، 🎁 یعنی آماده دریافت و ✅ یعنی کامل‌شده. کارها هر روز تازه می‌شوند."
ECONOMY="💳 <b>دارایی و بانک</b>\n\n👛 کیف پول: <b>{wallet}</b>\n🏦 پس‌انداز: <b>{savings}</b>\n🏠 خانه: <b>{house}</b>\n🧾 هزینه زندگی: <b>{due}</b>\n\nپس‌انداز پولت را جدا نگه می‌دارد؛ هزینه زندگی و خانه نیز بر وضعیت شخصیت اثر می‌گذارند."
JOBS="💼 <b>کار و دریافت درآمد</b>\n\n{body}\n\nشغل شخصی فقط در همین بات مدیریت می‌شود. از سطح ۵ شغل انتخاب کن، با گذر زمان کار انجام می‌شود و درآمد آماده را دریافت کن."
MARKET="💵 <b>بازار ارز</b>\n\nقیمت خرید: <b>{buy}</b>\nقیمت فروش: <b>{sell}</b>\nسلامت بازار: <b>{health}٪</b> · {status}\nدارایی دلاری تو: <b>{usd}</b>\n\nاختلاف خرید و فروش و کارمزد را پیش از معامله در نظر بگیر."
UNLOCKS="🗺 <b>مسیر پیشرفت</b>\n\n{rows}\n\nبخش‌های قفل‌شده با رشد سطح باز می‌شوند؛ کارهای امروز مطمئن‌ترین مسیر پیشرفت‌اند."
```

### `apps\telelife_bot\views\__init__.py`

```python
from apps.telelife_bot.views import render

__all__ = ["render"]
```

### `apps\telelife_bot\views\render.py`

```python
"""Pure text builders. No Telegram, no I/O - just data in, string out."""

from __future__ import annotations

from apps.telelife_bot.texts import fa
from packages.core.models import Player
from packages.core.services import unlocks as unlock_svc
from packages.core.services.daily import DailyResult
from packages.core.services.missions import Mission
from packages.core.services.xp import XPResult
from packages.core.utils import fmt


def profile(player: Player, *, rank: int, streak: int, xp_needed: int) -> str:
    prestige_tag = (
        fa.PRESTIGE_TAG.format(prestige=fmt.number(player.prestige))
        if player.prestige
        else ""
    )
    return fa.PROFILE.format(
        name=player.first_name,
        level=fmt.number(player.level),
        prestige_tag=prestige_tag,
        rank=fmt.number(rank),
        xp_bar=fmt.progress_bar(player.xp, xp_needed, width=14),
        xp=fmt.number(player.xp),
        xp_needed=fmt.number(xp_needed),
        wallet=fmt.toman(player.wallet_toman),
        savings=fmt.toman(player.savings_toman),
        usd=fmt.usd(player.usd_cents),
        happiness=fmt.number(player.happiness),
        reputation=fmt.number(player.reputation),
        streak=fmt.number(streak),
        net_worth=fmt.toman(player.net_worth_toman),
    )


def daily_claimed(result: DailyResult) -> str:
    if result.next_milestone:
        remaining = result.next_milestone - result.streak
        next_line = fa.DAILY_NEXT_MILESTONE.format(days=fmt.number(remaining))
    else:
        next_line = ""

    text = fa.DAILY_CLAIMED.format(
        reward=fmt.toman(result.reward_toman),
        xp=fmt.number(result.reward_xp),
        streak=fmt.number(result.streak),
        next_line=next_line,
    )
    if result.milestone_label:
        text += fa.DAILY_MILESTONE.format(
            label=result.milestone_label, bonus=fmt.toman(result.milestone_toman)
        )
    return text


def daily_ready(streak: int, best: int) -> str:
    from packages.core.services import daily as daily_svc  # noqa: PLC0415

    today_amount = daily_svc.preview(streak + 1)
    tomorrow_amount = daily_svc.preview(streak + 2)
    return fa.DAILY_READY.format(
        streak=fmt.number(streak),
        best=fmt.number(best),
        amount=fmt.toman(today_amount),
        next_line=fa.DAILY_READY_NEXT.format(amount=fmt.toman(tomorrow_amount)),
    )


def daily_already(streak: int, tomorrow: int) -> str:
    return fa.DAILY_ALREADY.format(
        streak=fmt.number(streak), tomorrow=fmt.toman(tomorrow)
    )


def missions(items: list[Mission]) -> str:
    if not items:
        return fa.MISSIONS_EMPTY
    rows: list[str] = []
    for m in items:
        reward = fmt.toman(m.reward_toman)
        if m.claimed:
            rows.append(fa.MISSION_ROW_DONE.format(title=m.title, reward=reward))
        elif m.done:
            rows.append(
                fa.MISSION_ROW_READY.format(
                    title=m.title,
                    progress=fmt.number(m.progress),
                    target=fmt.number(m.target),
                    reward=reward,
                )
            )
        else:
            rows.append(
                fa.MISSION_ROW_OPEN.format(
                    title=m.title,
                    progress=fmt.number(m.progress),
                    target=fmt.number(m.target),
                    reward=reward,
                )
            )
    return fa.MISSIONS_HEADER.format(body="\n".join(rows))


def unlocks_map(level: int) -> str:
    catalogue = unlock_svc.catalogue()
    nxt = unlock_svc.next_unlock(level)
    rows: list[str] = []
    for u in catalogue:
        if u.level <= level:
            rows.append(fa.UNLOCK_ROW_OPEN.format(icon=u.icon, title=u.title))
        elif nxt and u.key == nxt.key:
            rows.append(
                fa.UNLOCK_ROW_NEXT.format(
                    icon=u.icon, title=u.title, level=fmt.number(u.level)
                )
            )
        else:
            rows.append(
                fa.UNLOCK_ROW_LOCKED.format(
                    icon=u.icon, title=u.title, level=fmt.number(u.level)
                )
            )
    return fa.UNLOCKS_HEADER.format(
        body="\n".join(rows),
        level=fmt.number(level),
        next_level=fmt.number(nxt.level) if nxt else fmt.number(level),
    )


def level_up(result: XPResult) -> str:
    opened = unlock_svc.unlocked_at(result.level_after)
    if opened:
        unlock_line = "\n".join(
            fa.LEVEL_UP_UNLOCK.format(icon=u.icon, title=u.title) for u in opened
        )
    else:
        nxt = unlock_svc.next_unlock(result.level_after)
        unlock_line = (
            fa.LEVEL_UP_NEXT.format(
                level=fmt.number(nxt.level), icon=nxt.icon, title=nxt.title
            )
            if nxt
            else ""
        )
    return fa.LEVEL_UP.format(
        level=fmt.number(result.level_after),
        reward=fmt.toman(result.reward_toman),
        unlock_line=unlock_line,
    )
```

### `apps\teleworld_bot\__init__.py`

```python
"""Package apps.teleworld_bot."""
```

### `apps\teleworld_bot\handlers\__init__.py`

```python
"""TeleWorld handler modules; imported explicitly by the application."""

__all__ = ["country", "onboarding", "politics", "production", "status"]
```

### `apps\teleworld_bot\handlers\access.py`

```python
"""Telegram my_chat_member lifecycle and the TeleWorld permission gate."""
from __future__ import annotations
from html import escape
from telegram import Update
from telegram.constants import ChatMemberStatus, ChatType
from telegram.error import BadRequest, Forbidden
from telegram.ext import ChatMemberHandler, ContextTypes
from apps.teleworld_bot import keyboards as kb
from packages.core.repositories import group_repo, world_access_repo
from packages.core.services import world_access

GROUPS = {ChatType.GROUP, ChatType.SUPERGROUP}
ACTIVE = {ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}
INACTIVE = {ChatMemberStatus.LEFT, ChatMemberStatus.BANNED}

async def lifecycle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    change = update.my_chat_member
    if not change or change.chat.type not in GROUPS:
        return
    chat = change.chat
    old_status = change.old_chat_member.status
    new_status = change.new_chat_member.status
    active = new_status in ACTIVE
    await world_access_repo.membership(chat.id, chat.title or "سرزمین بی‌نام", new_status, active)
    world_access.invalidate(chat.id)
    if not active:
        await world_access_repo.audit(
            f"bot-membership:{chat.id}:{change.date.isoformat()}:{new_status}", "bot_removed",
            chat_id=chat.id, details={"status": new_status},
        )
        return
    await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    access = await world_access.check(context.bot, chat.id, force=True)
    await world_access_repo.audit(
        f"bot-membership:{chat.id}:{change.date.isoformat()}:{new_status}",
        "bot_added" if old_status in INACTIVE else "bot_access_changed",
        chat_id=chat.id, details={"ready": access.ready, "missing": list(access.missing)},
    )
    if old_status in INACTIVE and await world_access_repo.claim_welcome(chat.id):
        state = "✅ دسترسی لازم کامل است." if access.ready else f"⚠️ دسترسی ناقص: {access.missing_fa()}"
        text = (
            f"🌍 <b>به {escape(chat.title or 'این گروه')} خوش آمدم</b>\n\n"
            "اینجا می‌توانید کشور، شهروندی، اقتصاد عمومی، انتخابات و پروژه ملی بسازید.\n\n"
            f"{state}"
        )
        sent = await context.bot.send_message(chat.id, text, reply_markup=kb.access(access.ready))
        await world_access_repo.set_welcome_message(chat.id, sent.message_id)
    elif not access.ready and await world_access_repo.claim_warning(chat.id, access.fingerprint):
        try:
            await context.bot.send_message(
                chat.id, f"🔒 دسترسی بات تغییر کرده و عملیات کشور قفل شد.\nکمبود: {access.missing_fa()}",
                reply_markup=kb.access(False),
            )
        except (BadRequest, Forbidden):
            return

def register(app) -> None:
    app.add_handler(ChatMemberHandler(lifecycle, ChatMemberHandler.MY_CHAT_MEMBER), group=-10)
```

### `apps\teleworld_bot\handlers\country.py`

```python
"""Telegram adapters for country and economy commands."""

from __future__ import annotations

from dataclasses import dataclass

from telegram import Chat, Message, Update, User
from telegram.constants import ChatMemberStatus, ChatType
from telegram.ext import CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import country_repo, player_repo
from packages.core.services import country as country_service
from packages.core.services import country_missions, economy

_GROUP_TYPES = {ChatType.GROUP, ChatType.SUPERGROUP}


@dataclass(frozen=True, slots=True)
class GroupContext:
    chat: Chat
    user: User
    message: Message
    player: Player


async def resolve_group(update: Update) -> GroupContext | None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    if chat is None or user is None or message is None or chat.type not in _GROUP_TYPES:
        if message is not None:
            await message.reply_text(fa.PRIVATE_ONLY)
        return None
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    return GroupContext(chat, user, message, player)


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    member = await context.bot.get_chat_member(ctx.chat.id, ctx.user.id)
    if member.status not in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}:
        await ctx.message.reply_text(fa.ADMIN_REQUIRED)
        return
    parts = [part.strip() for part in " ".join(context.args).split("|")]
    if len(parts) != 3:
        await ctx.message.reply_text(fa.CREATE_USAGE)
        return
    try:
        row = await country_service.create_country(
            chat_id=ctx.chat.id,
            chat_title=ctx.chat.title or "",
            player_id=ctx.player.id,
            name=parts[0],
            government=parts[1].lower(),
            description=parts[2],
        )
    except ValueError as exc:
        await ctx.message.reply_text(fa.INVALID_INPUT.format(reason=fa.ERROR_NAMES.get(str(exc), str(exc))))
        return
    await ctx.message.reply_text(fa.COUNTRY_CREATED.format(name=row["name"]))


async def join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    await country_service.join_country(chat_id=ctx.chat.id, player_id=ctx.player.id)
    await ctx.message.reply_text(fa.COUNTRY_JOINED)


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    row = await country_repo.by_chat(ctx.chat.id)
    if row is None:
        await ctx.message.reply_text(fa.COUNTRY_MISSING)
        return
    await ctx.message.reply_text(
        fa.COUNTRY_STATUS.format(
            name=row["name"],
            description=row["description"],
            government=row["government_type"],
            treasury=row["treasury_toman"],
        )
    )


async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    if len(context.args) != 2:
        await ctx.message.reply_text(fa.DONATE_USAGE)
        return
    try:
        amount = int(context.args[1])
    except ValueError:
        await ctx.message.reply_text(fa.INVALID_AMOUNT)
        return
    asset = context.args[0]
    country = await country_repo.by_chat(ctx.chat.id)
    if country is None:
        await ctx.message.reply_text(fa.COUNTRY_MISSING)
        return
    await economy.transfer(
        player_id=ctx.player.id,
        country_id=country["id"],
        asset=asset,
        amount=amount,
        reason="country_donation",
        idempotency_key=f"donate:{ctx.message.message_id}:{ctx.player.id}",
    )
    await country_missions.report(country["id"], "donate", asset, amount)
    await ctx.message.reply_text(fa.DONATED.format(amount=amount, asset=asset))


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 1:
        message = update.effective_message
        if message is not None:
            await message.reply_text(fa.TAX_USAGE)
        return
    context.args = ["IRT", context.args[0]]
    await donate(update, context)


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
```

### `apps\teleworld_bot\handlers\onboarding.py`

```python
"""Welcoming lifecycle, guided menu and country-creation conversation."""
from __future__ import annotations
from telegram import Update
from telegram.error import BadRequest
from telegram.constants import ChatMemberStatus, ChatType
from telegram.ext import CallbackQueryHandler, ChatMemberHandler, CommandHandler, ContextTypes, MessageHandler, filters
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core.repositories import country_repo, group_repo, player_repo
from packages.core.services import country as country_service
from packages.core.services import economy, elections, production
from packages.core.repositories import production_repo
from packages.core.utils import fmt
from uuid import uuid4

_GROUPS={ChatType.GROUP,ChatType.SUPERGROUP}
FLOW_KEY="tw_country_flow"

async def _is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
 chat=update.effective_chat; user=update.effective_user
 if not chat or not user:return False
 member=await context.bot.get_chat_member(chat.id,user.id)
 return member.status in {ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER}

async def _home(update: Update, context: ContextTypes.DEFAULT_TYPE, *, edit: bool=False) -> None:
 chat=update.effective_chat; msg=update.effective_message
 if not chat or not msg:return
 if chat.type not in _GROUPS:
  username=context.bot.username or ""
  await msg.reply_text(fa.WORLD_PRIVATE,reply_markup=kb.private(username) if username else None)
  return
 await group_repo.get_or_create(chat.id,chat.title or "سرزمین بی‌نام")
 country=await country_repo.by_chat(chat.id); admin=await _is_admin(update,context)
 text=fa.WORLD_HOME_COUNTRY.format(name=country["name"]) if country else fa.WORLD_HOME_EMPTY_ADMIN if admin else fa.WORLD_HOME_EMPTY_MEMBER
 markup=kb.home(bool(country),admin)
 if edit and update.callback_query:
  try: await update.callback_query.edit_message_text(text,reply_markup=markup)
  except BadRequest as exc:
   if "message is not modified" not in str(exc).lower(): raise
 else: await msg.reply_text(text,reply_markup=markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None: await _home(update,context)

async def welcomed(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 change=update.my_chat_member
 if not change or change.chat.type not in _GROUPS:return
 old,new=change.old_chat_member.status,change.new_chat_member.status
 if old in {ChatMemberStatus.LEFT,ChatMemberStatus.BANNED} and new in {ChatMemberStatus.MEMBER,ChatMemberStatus.ADMINISTRATOR}:
  await group_repo.get_or_create(change.chat.id,change.chat.title or "سرزمین بی‌نام")
  await context.bot.send_message(change.chat.id,fa.WORLD_ADDED,reply_markup=kb.home(False,False))

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 q=update.callback_query
 if not q:return
 action=(q.data or "").removeprefix("tw:")
 if action in {"home","cancel"}:
  await q.answer();context.chat_data.pop(FLOW_KEY,None);await _home(update,context,edit=True);return
 if action=="guide":await q.answer();await q.edit_message_text(fa.WORLD_GUIDE,reply_markup=kb.back());return
 if action=="create":
  if not await _is_admin(update,context):await q.answer(fa.ADMIN_REQUIRED,show_alert=True);return
  if await country_repo.by_chat(q.message.chat.id):await q.answer(fa.COUNTRY_EXISTS,show_alert=True);return
  await q.answer();context.chat_data[FLOW_KEY]={"step":"name","owner_id":q.from_user.id}
  await q.edit_message_text(fa.WIZARD_NAME,reply_markup=kb.cancel());return
 if action.startswith("gov:"):
  flow=context.chat_data.get(FLOW_KEY)
  if not flow or flow.get("owner_id")!=q.from_user.id or flow.get("step")!="government":return
  await q.answer();flow["government"]=action.split(":",1)[1];flow["step"]="description"
  await q.edit_message_text(fa.WIZARD_DESCRIPTION.format(name=flow["name"]),reply_markup=kb.cancel());return
 if action=="join":
  user=q.from_user; player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try: joined=await country_service.join_country(chat_id=q.message.chat.id,player_id=player.id)
  except ValueError:await q.answer(fa.COUNTRY_MISSING,show_alert=True);return
  await q.answer();await q.edit_message_text(fa.COUNTRY_JOINED if joined else fa.ALREADY_CITIZEN,reply_markup=kb.back());return
 if action=="country":
  row=await country_repo.by_chat(q.message.chat.id)
  await q.answer()
  if row:await q.edit_message_text(fa.COUNTRY_STATUS.format(name=row['name'],description=row['description'],government=fa.GOVERNMENT_NAMES.get(row['government_type'],row['government_type']),treasury=row['treasury_toman']),reply_markup=kb.country_actions())
  return
 if action=="jobs":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  row=await production_repo.get(player.id);await q.answer();await q.edit_message_text(fa.JOBS_GUIDE,reply_markup=kb.jobs_actions(bool(row)));return
 if action.startswith("donate:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");country=await country_repo.by_chat(q.message.chat.id)
  try: await economy.transfer(player.id,int(country["id"]),"IRT",int(action.split(":")[1]),reason="donation",idempotency_key=f"ui-donate:{player.id}:{uuid4().hex}");await q.answer("کمک مالی ثبت شد.",show_alert=True)
  except ValueError as exc: await q.answer("موجودی کافی نیست یا اقتصاد متوقف است.",show_alert=True)
  return
 if action=="leave":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");ok=await country_service.leave_country(chat_id=q.message.chat.id,player_id=player.id);await q.answer("از کشور خارج شدی." if ok else "عضویت فعالی نداشتی.",show_alert=True);return
 if action=="election":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");country=await country_repo.by_chat(q.message.chat.id)
  try: await elections.start(int(country["id"]),player.id);await q.answer("انتخابات آغاز شد.",show_alert=True)
  except (ValueError,PermissionError):await q.answer("شروع انتخابات برایت مجاز نیست یا انتخابات دیگری باز است.",show_alert=True)
  return
 if action.startswith("job:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:ok=await production.choose(player.id,action.split(":")[1]);await q.answer("شغل ثبت شد." if ok else "قبلاً شغل انتخاب کرده‌ای.",show_alert=True)
  except ValueError:await q.answer("شغل از سطح ۵ باز می‌شود.",show_alert=True)
  return
 if action=="jcollect" or action.startswith("jup:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:
   if action=="jcollect":amount,xp=await production.collect(player.id,f"ui-collect:{player.id}:{uuid4().hex}");text=f"{fmt.number(amount)} واحد و {fmt.number(xp)} XP دریافت شد."
   else:lvl=await production.upgrade(player.id,action.split(":")[1],f"ui-up:{player.id}:{uuid4().hex}");text=f"ارتقا به سطح {fmt.number(lvl)} انجام شد."
   await q.answer(text,show_alert=True)
  except ValueError:await q.answer("عملیات شغلی انجام نشد؛ موجودی یا شرایط را بررسی کن.",show_alert=True)
  return
 if action=="politics":await q.answer();await q.edit_message_text(fa.POLITICS_GUIDE,reply_markup=kb.back());return
 if action=="donate_help":await q.answer();await q.edit_message_text(fa.DONATE_GUIDE,reply_markup=kb.back());return

async def wizard_text(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 flow=context.chat_data.get(FLOW_KEY);msg=update.effective_message;user=update.effective_user;chat=update.effective_chat
 if not flow or not msg or not user or not chat or user.id!=flow.get("owner_id"):return
 text=(msg.text or "").strip()
 if flow["step"]=="name":
  if not 3<=len(text)<=80:await msg.reply_text(fa.WIZARD_NAME_ERROR);return
  flow["name"]=text;flow["step"]="government";await msg.reply_text(fa.WIZARD_GOVERNMENT,reply_markup=kb.governments());return
 if flow["step"]=="description":
  if not 10<=len(text)<=500:await msg.reply_text(fa.WIZARD_DESCRIPTION_ERROR);return
  player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:row=await country_service.create_country(chat_id=chat.id,chat_title=chat.title or "",player_id=player.id,name=flow["name"],government=flow["government"],description=text)
  except ValueError as exc:context.chat_data.pop(FLOW_KEY,None);await msg.reply_text(fa.INVALID_INPUT.format(reason=fa.ERROR_NAMES.get(str(exc),str(exc))),reply_markup=kb.home(False,True));return
  context.chat_data.pop(FLOW_KEY,None);await msg.reply_text(fa.COUNTRY_CREATED_GUIDED.format(name=row["name"]),reply_markup=kb.home(True,True))

def register(app)->None:
 app.add_handler(CommandHandler("start",start),group=0)
 app.add_handler(ChatMemberHandler(welcomed,ChatMemberHandler.MY_CHAT_MEMBER),group=0)
 app.add_handler(CallbackQueryHandler(callback,pattern=r"^tw:"),group=0)
 app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,wizard_text),group=1)
```

### `apps\teleworld_bot\handlers\politics.py`

```python
"""Thin election, project, poll and presidential adapters."""
from __future__ import annotations
from telegram import Update
from telegram.ext import CommandHandler,ContextTypes
from apps.teleworld_bot.texts import fa
from packages.core import db
from packages.core.repositories import country_repo,election_repo,player_repo,project_repo,outbox_repo
from packages.core.services import elections,national_project
async def ctx(update:Update):
 chat=update.effective_chat;u=update.effective_user;m=update.effective_message
 if not chat or not u or not m:return None
 p=await player_repo.get_or_create(u.id,username=u.username,first_name=u.first_name or '',language_code=u.language_code or 'fa');c=await country_repo.by_chat(chat.id)
 return chat,m,p,c
async def start_election(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:await elections.start(x[3]['id'],x[2].id);await x[1].reply_text(fa.ELECTION_STARTED)
async def nominate(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:
  e=await election_repo.open_for_country(x[3]['id']);await elections.nominate(e['id'],x[2].id,x[0].id,x[1].message_id);await x[1].reply_text(fa.NOMINATED)
async def vote(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and x[1].reply_to_message:
  e=await election_repo.open_for_country(x[3]['id']);candidate=await db.fetchval('SELECT player_id FROM election_candidates WHERE election_id=$1 AND message_id=$2',e['id'],x[1].reply_to_message.message_id)
  ok=await elections.vote(e['id'],x[2].id,candidate);await x[1].reply_text(fa.VOTED if ok else fa.DUPLICATE_VOTE)
async def start_project(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:await national_project.start(x[3]['id'],x[2].id);await x[1].reply_text(fa.PROJECT_STARTED)
async def contribute(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and len(context.args)==2:
  p=await project_repo.active(x[3]['id']);used,_=await national_project.contribute(p['id'],x[2].id,context.args[0],int(context.args[1]),f'project:{x[1].message_id}:{x[2].id}');await x[1].reply_text(fa.CONTRIBUTED.format(amount=used))
async def poll(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update);parts=[v.strip() for v in ' '.join(context.args).split('|')]
 if x and x[3] and len(parts)>=3:await elections.create_poll(x[3]['id'],x[2].id,parts[0],parts[1:]);await x[1].reply_text(fa.POLL_STARTED)
async def polls(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:
  rows=await election_repo.polls(x[3]["id"])
  text="\n".join(f"{v['id']}: {v['question']}" for v in rows) or fa.COUNTRY_MISSING
  await x[1].reply_text(text)
async def pollvote(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and len(context.args)==2:ok=await election_repo.poll_vote(int(context.args[0]),x[2].id,int(context.args[1]));await x[1].reply_text(fa.VOTED if ok else fa.DUPLICATE_VOTE)
async def setflag(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and x[1].photo and x[1].caption:
  photo=x[1].photo[-1];ok=await country_repo.set_flag(x[3]['id'],x[2].id,photo.file_id,photo.file_unique_id);await x[1].reply_text(fa.FLAG_SET if ok else fa.PRESIDENT_REQUIRED)
async def announce(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and await country_repo.is_president(x[3]['id'],x[2].id):
  async with db.transaction() as conn:await outbox_repo.enqueue(conn,f'announce:{x[1].message_id}','country_announcement',{'text':' '.join(context.args)},x[0].id)
  await x[1].reply_text(fa.ANNOUNCED)
def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
```

### `apps\teleworld_bot\handlers\production.py`

```python
"""Telegram adapters for jobs and lazy production."""

from __future__ import annotations

from telegram import Message, Update
from telegram.ext import CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import player_repo
from packages.core.services import production


async def resolve(update: Update) -> tuple[Player, Message] | None:
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return None
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    return player, message


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is not None:
        await message.reply_text(fa.JOBS)


async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    if len(context.args) != 1:
        await message.reply_text(fa.CHOOSE_JOB_USAGE)
        return
    try:
        await production.choose(player.id, context.args[0])
    except ValueError as exc:
        await message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
        return
    await message.reply_text(fa.JOB_CHOSEN)


async def collect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    amount, earned_xp = await production.collect(
        player.id, f"collect:{player.id}:{message.message_id}"
    )
    await message.reply_text(fa.COLLECTED.format(amount=amount, xp=earned_xp))


async def upgrade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    if len(context.args) != 1:
        await message.reply_text(fa.UPGRADE_USAGE)
        return
    kind = context.args[0]
    try:
        level = await production.upgrade(
            player.id, kind, f"upgrade:{player.id}:{message.message_id}"
        )
    except ValueError as exc:
        await message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
        return
    await message.reply_text(fa.UPGRADED.format(kind=kind, level=level))


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
```

### `apps\teleworld_bot\handlers\status.py`

```python
"""TeleWorld onboarding, group activation and status commands."""

from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatType
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.repositories import group_repo, player_repo
from packages.core.utils import fmt

_GROUP_TYPES = {ChatType.GROUP, ChatType.SUPERGROUP}


async def _sync(update: Update) -> tuple[int, str] | None:
    chat = update.effective_chat
    user = update.effective_user
    if chat is None or user is None or chat.type not in _GROUP_TYPES:
        return None
    group = await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    await group_repo.link_member(group.id, player.id)
    return group.id, group.title


def _private_menu(bot_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "➕ افزودن TeleWorld به گروه",
            url=f"https://t.me/{bot_username}?startgroup=true",
            style="primary",
        )],
        [InlineKeyboardButton("📚 مشاهده راهنما", callback_data="tw:help")],
    ])


def _group_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌍 وضعیت گروه", callback_data="tw:status", style="primary"),
            InlineKeyboardButton("💼 فهرست شغل‌ها", callback_data="tw:jobs"),
        ],
        [InlineKeyboardButton("📚 راهنمای دستورات", callback_data="tw:help")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Always acknowledge /start and direct users to the correct game context."""
    message = update.effective_message
    chat = update.effective_chat
    if message is None or chat is None:
        return

    if chat.type in _GROUP_TYPES:
        await _sync(update)
        await message.reply_text(fa.START_GROUP, reply_markup=_group_menu())
        return

    username = context.bot.username or ""
    markup = _private_menu(username) if username else None
    await message.reply_text(fa.START_PRIVATE, reply_markup=markup)


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None:
        return
    synced = await _sync(update)
    if synced is None:
        await message.reply_text(fa.PRIVATE_ONLY)
        return
    group_id, title = synced
    from packages.core import db

    members = await db.fetchval(
        "SELECT count(*) FROM group_members WHERE group_id = $1", group_id
    )
    await message.reply_text(
        fa.STATUS.format(title=title, members=fmt.number(int(members or 0))),
        reply_markup=_group_menu(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(
            fa.HELP,
            reply_markup=_group_menu()
            if update.effective_chat and update.effective_chat.type in _GROUP_TYPES
            else None,
        )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query is None:
        return
    await query.answer()
    action = (query.data or "").removeprefix("tw:")
    if action == "status":
        await status(update, context)
    elif action == "jobs":
        await query.message.reply_text(fa.JOBS, reply_markup=_group_menu())
    elif action == "help":
        await query.message.reply_text(fa.HELP)


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
```

### `apps\teleworld_bot\handlers\world.py`

```python
"""کنترل‌گر یک‌پیامی، فارسی و دکمه‌محور جهان گروهی."""
from __future__ import annotations
from uuid import uuid4
from datetime import UTC,datetime
from html import escape
from telegram.constants import ChatMemberStatus, ChatType
from telegram.error import BadRequest, Forbidden
from telegram.ext import CallbackQueryHandler, MessageHandler, PreCheckoutQueryHandler, filters
from telegram import LabeledPrice
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core import db
from packages.core.repositories import country_repo, election_repo, group_repo, player_repo, project_repo, ui_state_repo, world_access_repo
from packages.core.services import country as countries, economy, elections, national_project, commerce, migration, country_realism
from packages.core.services import world_access
from packages.core.utils import fmt

GROUPS = {ChatType.GROUP, ChatType.SUPERGROUP}
FLOW = "world_creation"
STATUS = {"forming":"در حال ساخت", "temporary":"موقت", "official":"رسمی"}
GOV = {code: item[0] for code, item in fa.GOVERNMENT_DETAILS.items()}
ASSET = {"IRT":"تومان", "food":"غذا", "minerals":"مواد معدنی", "oil":"نفت", "energy":"انرژی", "technology":"فناوری"}
ERRORS = {
    "citizen_required":"ابتدا شهروند این کشور شو.", "president_required":"فقط رهبر کشور می‌تواند این کار را انجام دهد.",
    "already_citizen_elsewhere":"اکنون شهروند کشور دیگری هستی؛ ابتدا از آن خارج شو.",
    "election_already_open":"یک انتخابات فعال وجود دارد.", "project_not_active":"پروژه فعالی وجود ندارد.",
    "country_already_exists":"این گروه از قبل کشور دارد.", "insufficient_balance":"موجودی کافی نیست.",
    "insufficient_player_balance":"موجودی کیف پولت کافی نیست.", "country_not_found":"کشوری پیدا نشد.",
    "asset_not_required":"این دارایی برای پروژه لازم نیست.", "project_exists":"از قبل پروژه فعالی وجود دارد.",
}

async def answer(query, text=None, show_alert=False):
    try:
        await query.answer(text, show_alert=show_alert)
    except BadRequest:
        return

async def is_admin(update, context) -> bool:
    member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
    return member.status in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}

async def player(update):
    user = update.effective_user
    return await player_repo.get_or_create(user.id, username=user.username, first_name=user.first_name or "شهروند", language_code=user.language_code or "fa")

async def show(update, context, text, markup):
    chat = update.effective_chat
    query = update.callback_query
    state = await ui_state_repo.world(chat.id)
    message_id = query.message.message_id if query and query.message else int(state["message_id"]) if state else None
    if message_id:
        try:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=message_id, text=text, reply_markup=markup)
            await ui_state_repo.set_world(chat.id, message_id)
            return
        except BadRequest as exc:
            if "message is not modified" in str(exc).lower():
                return
        except Forbidden:
            pass
    sent = await context.bot.send_message(chat.id, text, reply_markup=markup)
    await ui_state_repo.set_world(chat.id, sent.message_id)

async def facts(chat_id):
    row = await country_repo.by_chat(chat_id)
    if not row:
        return None, 0, None
    count = int(await db.fetchval("SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active", row["id"]) or 0)
    leader = await db.fetchval("SELECT first_name FROM players WHERE id=$1", row["president_player_id"]) if row["president_player_id"] else None
    return row, count, leader

MUTATING = {"create", "join", "leave", "estart", "nominate", "pstart", "subtreasury", "migration", "rate", "reserve"}

def is_mutating(action: str) -> bool:
    return action in MUTATING or action.startswith(("donate:", "vote:", "pcon:", "gov:", "govok:", "substar:", "migrate:", "migaccept:", "migreject:", "rate:", "reserve:"))

async def access_page(update, context, *, force: bool = False):
    access = await world_access.check(context.bot, update.effective_chat.id, force=force)
    if access.ready:
        await show(update, context, "✅ <b>دسترسی کامل است</b>\n\nبات مدیر است و اجازه حذف پیام‌های مرحله‌ای را دارد. جهان آماده استفاده است.", kb.access(True))
    else:
        await show(update, context, "🔒 <b>جهان در حالت محدود است</b>\n\nکمبود: " + access.missing_fa() + "\n\nاز تنظیمات گروه، بات را مدیر کنید و اجازه «حذف پیام‌ها» را فعال کنید. اجازه افزودن مدیر یا تغییر اطلاعات گروه لازم نیست.", kb.access(False))
    return access

async def health_page(update, context):
    access = await world_access.check(context.bot, update.effective_chat.id, force=True)
    country = await country_repo.by_chat(update.effective_chat.id)
    panel = await ui_state_repo.world(update.effective_chat.id)
    election = await election_repo.open_for_country(country["id"]) if country else None
    project = await project_repo.active(country["id"]) if country else None
    lines = [
        f"• دسترسی بات: {'کامل' if access.ready else 'ناقص — ' + access.missing_fa()}",
        f"• اتصال کشور: {'سالم' if country else 'هنوز کشوری ساخته نشده'}",
        f"• صفحه اصلی: {'ثبت شده' if panel else 'با نخستین نمایش ساخته می‌شود'}",
        f"• انتخابات فعال: {'بله' if election else 'خیر'}",
        f"• پروژه فعال: {'بله' if project else 'خیر'}",
        f"• قابلیت‌های اصلی: {'آماده' if access.ready else 'قفل ایمن'}",
    ]
    await show(update, context, "🩺 <b>بررسی وضعیت جهان</b>\n\n" + "\n".join(lines), kb.access(access.ready))

async def home(update, context):
    chat = update.effective_chat
    if chat.type not in GROUPS:
        await show(update, context, fa.PRIVATE, kb.private(context.bot.username or ""))
        return
    await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    access = await world_access.check(context.bot, chat.id)
    if not access.ready:
        await access_page(update, context)
        return
    row, count, leader = await facts(chat.id)
    p = await player(update)
    citizenship = await country_repo.citizenship(p.id) if row else None
    citizen = bool(citizenship and citizenship["is_active"] and int(citizenship["country_id"]) == int(row["id"]))
    if not row:
        await show(update, context, fa.HOME_EMPTY, kb.home(False, await is_admin(update, context)))
        return
    goal = "شهروند جذب کنید" if row["status"] == "forming" else "انتخابات رهبر را کامل کنید" if not row["president_player_id"] else "پروژه و اقتصاد کشور را رشد دهید"
    text = fa.HOME.format(name=escape(str(row["name"])), status=STATUS.get(row["status"], "نامشخص"), citizens=fmt.number(count), leader=escape(str(leader or "هنوز انتخاب نشده")), treasury=fmt.toman(row["treasury_toman"]), goal=goal)
    await show(update, context, text, kb.home(True, await is_admin(update, context), citizen))

async def country_page(update, context):
    row, count, leader = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    text = fa.COUNTRY.format(name=escape(str(row["name"])), government=GOV.get(row["government_type"], "نامشخص"), status=STATUS.get(row["status"], "نامشخص"), citizens=fmt.number(count), leader=escape(str(leader or "انتخاب نشده")), treasury=fmt.toman(row["treasury_toman"]), description=escape(str(row["description"])))
    await show(update, context, text, kb.country())

async def economy_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    resources = await country_repo.resources(row["id"])
    lines = "\n".join(f"• {ASSET.get(str(x['asset_code']), 'دارایی')}: {fmt.number(x['quantity'])}" for x in resources) or "هنوز منبعی ثبت نشده است."
    from telegram import InlineKeyboardMarkup
    markup=InlineKeyboardMarkup([[kb.b("🏦 بانک مرکزی و شاخص‌ها","centralbank","primary")],[kb.b("🏠 خانه جهان","home")]])
    await show(update, context, fa.ECONOMY.format(treasury=fmt.toman(row["treasury_toman"]), income=fmt.toman(row["daily_income_toman"]), expense=fmt.toman(row["daily_expense_toman"]), resources=lines), markup)

async def central_bank_page(update,context):
    row,_,_=await facts(update.effective_chat.id)
    if not row:raise ValueError("country_not_found")
    v=await country_realism.policy_view(row["id"]);p=await player(update);president=row["president_player_id"]==p.id
    indicators=("هنوز گزارش روزانه محاسبه نشده است." if not v["indicator_date"] else f"تورم: <b>{int(v['inflation_bp'])/100:.1f}٪</b> · بیکاری: <b>{int(v['unemployment_bp'])/100:.1f}٪</b>\nرشد: <b>{int(v['growth_bp'])/100:+.1f}٪</b> · رضایت: <b>{v['satisfaction']}/۱۰۰</b>")
    text=f"🏦 <b>بانک مرکزی {escape(str(row['name']))}</b>\n\nنرخ بهره: <b>{int(v['interest_rate_bp'])/100:.1f}٪</b>\nهدف تورم: <b>{int(v['inflation_target_bp'])/100:.1f}٪</b>\nذخیره ارزی: <b>{fmt.usd(int(v['fx_reserve_cents']))}</b>\n\n{indicators}\n\nافزایش بهره معمولاً تورم را مهار می‌کند اما رشد را کندتر می‌کند. تصمیم امروز در گزارش فردا اثر می‌گذارد."
    await show(update,context,text,kb.central_bank(president))

async def citizens_page(update, context):
    row, count, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    people=await db.fetch("SELECT p.first_name,cs.migrant_until FROM citizenships cs JOIN players p ON p.id=cs.player_id WHERE cs.country_id=$1 AND cs.is_active ORDER BY cs.joined_at LIMIT 25",row["id"])
    names=[f"• {escape(str(x['first_name']))}"+(" · 🧳 مهاجر" if x["migrant_until"] and x["migrant_until"]>datetime.now(UTC) else "") for x in people]
    await show(update, context, fa.CITIZENS.format(count=fmt.number(count), members="\n".join(names) or "هنوز شهروندی ثبت نشده است."), kb.back("country"))

async def politics_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    election = await election_repo.open_for_country(row["id"])
    status = str(election["status"]) if election else None
    from packages.core.services.governance import rules_for
    rules=rules_for(str(row["government_type"]))
    state = "در این نظام، رهبر با انتخابات عمومی تعیین نمی‌شود." if not rules.public_elections else "انتخابات فعالی وجود ندارد." if not election else "مرحله نام‌نویسی نامزدها باز است." if status == "nominations" else "رأی‌گیری باز است."
    await show(update, context, fa.POLITICS.format(state=state), kb.politics(status,allowed=rules.public_elections))

async def project_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    project = await project_repo.active(row["id"])
    latest = project or await db.fetchrow("SELECT * FROM national_projects WHERE country_id=$1 ORDER BY id DESC LIMIT 1", row["id"])
    body = "هنوز پروژه‌ای آغاز نشده است."
    if latest:
        status = await project_repo.status(latest["id"])
        body = "\n".join(f"• {ASSET.get(str(x['asset_code']), 'دارایی')}: {fmt.number(x['contributed_amount'])} از {fmt.number(x['required_amount'])}" for x in status)
        if latest["status"] == "completed": body = "✅ این پروژه ملی تکمیل شده است.\n\n" + body
    markup = kb.project(True) if project else kb.back()
    if latest is None: markup = kb.project(False)
    await show(update, context, "🏗 <b>پروژه ملی</b>\n\n" + body + "\n\nهر شهروند فقط به اندازه نیاز باقی‌مانده کمک می‌کند.", markup)

async def callback(update, context):
    query = update.callback_query
    if not query: return
    action = (query.data or "")[3:]
    try:
        if action == "access:why":
            await answer(query)
            await show(update, context, "📘 <b>چرا مدیر؟</b>\n\nفقط برای حذف پیام‌های مرحله‌ای باید بات مدیر باشد. ویرایش پیام‌های خود بات نیاز به مجوز جداگانه ندارد.\n\nمسیر: اطلاعات گروه ← ویرایش ← مدیران ← افزودن مدیر ← فعال‌کردن «حذف پیام‌ها».\n\nتلگرام پیوند قابل‌اتکایی برای بازکردن مستقیم صفحه ارتقای مدیر ارائه نمی‌کند؛ بنابراین دکمه جعلی نمایش داده نمی‌شود.", kb.access(False))
            return
        if action == "access:check":
            await answer(query)
            access = await access_page(update, context, force=True)
            if access.ready:
                await home(update, context)
            return
        if action == "health":
            await answer(query)
            await health_page(update, context)
            return
        if update.effective_chat.type in GROUPS and is_mutating(action):
            access = await world_access.check(context.bot, update.effective_chat.id)
            if not access.ready:
                await answer(query, "عملیات قفل است: " + access.missing_fa(), show_alert=True)
                await access_page(update, context)
                return
        if action == "home":
            await answer(query, ); context.chat_data.pop(FLOW, None); await home(update, context)
        elif action == "guide":
            await answer(query, ); row, _, _ = await facts(update.effective_chat.id) if update.effective_chat.type in GROUPS else (None, 0, None); await show(update, context, fa.GUIDE if row else fa.GUIDE_EMPTY, kb.back())
        elif action == "country": await answer(query, ); await country_page(update, context)
        elif action == "economy": await answer(query, ); await economy_page(update, context)
        elif action == "centralbank": await answer(query); await central_bank_page(update,context)
        elif action.startswith("rate:"):
            row,_,_=await facts(update.effective_chat.id);p=await player(update);delta=100 if action.endswith("up") else -100
            value=await country_realism.set_interest(row["id"],p.id,delta)
            if value is None:await answer(query,"فقط رهبر کشور می‌تواند نرخ را در محدوده مجاز تغییر دهد.",show_alert=True);return
            await answer(query,f"نرخ بهره به {value/100:.1f}٪ تغییر کرد.",show_alert=True);await central_bank_page(update,context)
        elif action == "reserve:buy":
            row,_,_=await facts(update.effective_chat.id);p=await player(update)
            try:cents=await country_realism.buy_reserve(row["id"],p.id)
            except ValueError:await answer(query,"فقط رهبر و با خزانه کافی می‌تواند ذخیره بخرد.",show_alert=True);return
            await answer(query,f"{fmt.usd(cents)} به ذخیره ارزی افزوده شد.",show_alert=True);await central_bank_page(update,context)
        elif action == "citizens": await answer(query, ); await citizens_page(update, context)
        elif action == "politics": await answer(query, ); await politics_page(update, context)
        elif action == "project": await answer(query, ); await project_page(update, context)
        elif action == "create":
            if update.effective_chat.type not in GROUPS or not await is_admin(update, context):
                await answer(query, "فقط مدیر گروه می‌تواند ساخت را شروع کند.", show_alert=True); return
            if await country_repo.by_chat(update.effective_chat.id):
                await answer(query, "این گروه از قبل کشور دارد.", show_alert=True); return
            await answer(query, ); context.chat_data[FLOW] = {"step":"name", "owner":query.from_user.id, "panel":query.message.message_id}; await show(update, context, fa.WIZARD_NAME, kb.cancel())
        elif action.startswith("gov:"):
            flow = context.chat_data.get(FLOW)
            if not flow or flow.get("owner") != query.from_user.id or flow.get("step") != "government":
                await answer(query, "فرایند ساخت منقضی شده است؛ دوباره آغاز کن.", show_alert=True); return
            code=action.split(":",1)[1]; detail=fa.GOVERNMENT_DETAILS.get(code)
            if not detail: await answer(query,"نوع حکومت معتبر نیست.",show_alert=True);return
            await answer(query); await show(update,context,fa.GOV_CONFIRM.format(title=detail[0],description=detail[1]),kb.government_confirm(code))
        elif action == "govback":
            flow=context.chat_data.get(FLOW)
            if not flow or flow.get("owner") != query.from_user.id: await answer(query,"فرایند ساخت منقضی شده است.",show_alert=True);return
            await answer(query);flow["step"]="government";await show(update,context,fa.WIZARD_GOV,kb.governments())
        elif action.startswith("govok:"):
            flow=context.chat_data.get(FLOW);code=action.split(":",1)[1]
            if not flow or flow.get("owner") != query.from_user.id or flow.get("step") != "government" or code not in fa.GOVERNMENT_DETAILS:
                await answer(query,"فرایند ساخت منقضی شده است؛ دوباره آغاز کن.",show_alert=True);return
            await answer(query);flow["government"]=code;flow["step"]="description";await show(update,context,fa.WIZARD_DESC,kb.cancel())
        elif action == "migration":
            p=await player(update);current=await country_repo.citizenship(p.id)
            if not current:await answer(query,"ابتدا شهروند یک کشور شو.",show_alert=True);return
            rows=await db.fetch("SELECT id,name FROM countries ORDER BY name LIMIT 100");await answer(query)
            await show(update,context,"✈️ <b>تغییر کشور</b>\n\nعوارض هنگام تکمیل مهاجرت: ۵٪ دارایی شخصی، حداقل ۵۰۰ هزار و حداکثر ۵۰ میلیون تومان؛ مبلغ به خزانه کشور مبدأ می‌رود.\n\nمحدودیت تغییر: هر ۳۰ روز. اگر مقصد رهبر داشته باشد، درخواست ۷۲ ساعت برای تأیید اعتبار دارد. پس از مهاجرت، نشان مهاجر ۳۰ روز و محدودیت سیاسی ۱۴ روز فعال است.",kb.migration_countries(rows,current["country_id"]))
        elif action.startswith("migrate:"):
            p=await player(update);dest=int(action.split(":")[1]);qte=await migration.quote(p.id,dest)
            if not qte:await answer(query,"مقصد معتبر نیست.",show_alert=True);return
            fee=migration.exit_fee(int(qte["wallet_toman"])+int(qte["savings_toman"]));row=await migration.request(p.id,dest)
            await answer(query,(f"مهاجرت انجام شد و {fmt.toman(fee)} به خزانه کشور مبدأ رفت." if row["status"]=='approved' else f"درخواست ثبت شد؛ رهبر مقصد تا ۷۲ ساعت فرصت تأیید دارد. عوارض {fmt.toman(fee)} فقط هنگام تأیید کسر می‌شود."),show_alert=True);await home(update,context)
        elif action == "migration_review":
            p=await player(update);row=await country_repo.by_chat(update.effective_chat.id)
            if not row or row["president_player_id"]!=p.id:await answer(query,"فقط رهبر مقصد دسترسی دارد.",show_alert=True);return
            rows=await migration.pending_for_country(row["id"]);await answer(query);await show(update,context,"📥 <b>درخواست‌های مهاجرت</b>\n\n"+("درخواستی وجود ندارد." if not rows else "پذیرش، عوارض را به کشور مبدأ منتقل و مهاجر را وارد کشور می‌کند."),kb.migration_review(rows))
        elif action.startswith("migaccept:"):
            p=await player(update);await migration.approve(int(action.split(":")[1]),p.id);await answer(query,"مهاجر پذیرفته شد.",show_alert=True);await home(update,context)
        elif action.startswith("migreject:"):
            p=await player(update);ok=await migration.reject(int(action.split(":")[1]),p.id);await answer(query,"درخواست رد شد." if ok else "درخواست قابل رد نیست.",show_alert=True);await home(update,context)
        elif action == "subscription":
            await answer(query); view=await commerce.subscription_view(update.effective_chat.id)
            if not view: raise ValueError("group_not_found")
            if view["ad_free_until"] and view["ad_free_until"]>datetime.now(UTC):
                await show(update,context,f"🛡 <b>اشتراک بدون تبلیغ فعال است</b>\n\nاعتبار تا: <b>{view['ad_free_until'].strftime('%Y-%m-%d %H:%M UTC')}</b>\n\nدر این مدت تبلیغ عمومی وارد گروه نمی‌شود.",kb.back());return
            rnd=await commerce.ensure_round(update.effective_chat.id);target=int(rnd["target_stars"]);remaining=target-int(rnd["collected_stars"])
            treasury=int(view["treasury_toman"] or 0);citizens=int(view["citizens"] or 0);price=commerce.treasury_price(treasury,citizens)
            await show(update,context,f"🛡 <b>اشتراک ۳۰روزه بدون تبلیغ</b>\n\nجمعیت: <b>{citizens}</b> شهروند · قیمت: <b>{target} ⭐</b>\nپیشرفت مشارکت: <b>{rnd['collected_stars']} از {target} ⭐</b>\nهر عضو می‌تواند ۱، ۲، ۵، ۱۰، ۲۵ یا ۵۰ استار سهم بگذارد. با تکمیل قیمت جمعیت‌محور، اشتراک خودکار فعال می‌شود.\n\nخرید از خزانه: <b>{fmt.toman(price)}</b> (۲۰٪ خزانه + یک میلیون برای هر شهروند، کف ۲۰ میلیون و سقف یک میلیارد).",kb.subscription(int(rnd["id"]),remaining))
        elif action.startswith("substar:"):
            _,rid,amount=action.split(":");payload,stars=await commerce.subscription_invoice(int(rid),query.from_user.id,int(amount));await answer(query)
            await context.bot.send_invoice(chat_id=update.effective_chat.id,title="مشارکت اشتراک بدون تبلیغ",description=f"{stars} استار برای اشتراک ۳۰روزه گروه",payload=payload,currency="XTR",prices=[LabeledPrice("سهم اشتراک",stars)],provider_token="")
        elif action == "subtreasury":
            p=await player(update);price=await commerce.buy_with_treasury(update.effective_chat.id,p.id);await answer(query,f"اشتراک با {fmt.toman(price)} از خزانه فعال شد.",show_alert=True);await home(update,context)
        elif action == "join":
            p = await player(update); joined = await countries.join_country(chat_id=update.effective_chat.id, player_id=p.id); await answer(query, "شهروند شدی." if joined else "از قبل شهروندی.", show_alert=True); await home(update, context)
        elif action == "leave":
            await answer(query,"برای جلوگیری از دورزدن عوارض و محدودیت زمانی، خروج مستقیم بسته است؛ از بخش «مهاجرت» کشور مقصد را انتخاب کن.",show_alert=True)
        elif action.startswith("donate:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            citizenship = await country_repo.citizenship(p.id)
            if not citizenship or not citizenship["is_active"] or int(citizenship["country_id"]) != int(row["id"]): raise PermissionError("citizen_required")
            await economy.transfer(p.id, row["id"], "IRT", int(action.split(":", 1)[1]), reason="donation", idempotency_key=f"world-donate:{p.id}:{query.id}")
            await answer(query, "کمک مالی ثبت شد.", show_alert=True); await country_page(update, context)
        elif action == "estart":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            await elections.start(row["id"], p.id); await answer(query, "انتخابات آغاز شد.", show_alert=True); await politics_page(update, context)
        elif action == "nominate":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "nominations": await answer(query, "مرحله نام‌نویسی باز نیست.", show_alert=True); return
            accepted = await elections.nominate(election["id"], p.id, update.effective_chat.id, query.message.message_id)
            await answer(query, "نامزدی ثبت شد." if accepted else "قبلاً نامزد شده‌ای.", show_alert=True); await politics_page(update, context)
        elif action == "votehelp":
            row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "voting": await answer(query, "رأی‌گیری هنوز باز نشده است.", show_alert=True); return
            rows = await db.fetch("SELECT ec.player_id,p.first_name FROM election_candidates ec JOIN players p ON p.id=ec.player_id WHERE ec.election_id=$1 ORDER BY ec.created_at", election["id"])
            if not rows: await answer(query, "نامزدی برای رأی‌دادن وجود ندارد.", show_alert=True); return
            await answer(query, ); await show(update, context, "🗳 <b>انتخاب رهبر</b>\n\nنامزد موردنظر را انتخاب کن. رأی فقط یک‌بار ثبت می‌شود.", kb.candidates(rows))
        elif action.startswith("vote:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "voting": await answer(query, "رأی‌گیری باز نیست.", show_alert=True); return
            accepted = await elections.vote(election["id"], p.id, int(action.split(":", 1)[1])); await answer(query, "رأی ثبت شد." if accepted else "قبلاً رأی داده‌ای.", show_alert=True); await politics_page(update, context)
        elif action == "pstart":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            if await db.fetchval("SELECT 1 FROM national_projects WHERE country_id=$1", row["id"]): await answer(query, "پروژه ملی این کشور قبلاً آغاز شده است و تکرارشدنی نیست.", show_alert=True); return
            await national_project.start(row["id"], p.id); await answer(query, "پروژه ملی آغاز شد.", show_alert=True); await project_page(update, context)
        elif action.startswith("pcon:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            project = await project_repo.active(row["id"])
            if not project: await answer(query, "پروژه فعالی وجود ندارد.", show_alert=True); return
            _, asset, amount = action.split(":")
            accepted, done = await national_project.contribute(project["id"], p.id, asset, int(amount), f"world-project:{p.id}:{query.id}")
            await answer(query, (f"{fmt.number(accepted)} واحد ثبت شد." if accepted else "نیاز این بخش قبلاً تکمیل شده است.") + (" پروژه تکمیل شد!" if done else ""), show_alert=True); await project_page(update, context) if not done else await home(update, context)
        elif action == "polls": await answer(query, "هنوز نظرسنجی فعالی نیست.", show_alert=True)
        else: await answer(query, "این دکمه قدیمی شده است؛ صفحه را تازه‌سازی کن.", show_alert=True)
    except (ValueError, PermissionError, TypeError, KeyError, AttributeError) as exc:
        await answer(query, ERRORS.get(str(exc), "شرایط این کار کامل نیست؛ راهنما را بخوان."), show_alert=True)

async def text(update, context):
    message, chat = update.effective_message, update.effective_chat
    if not message or not chat: return
    if chat.type not in GROUPS: await home(update, context); return
    flow = context.chat_data.get(FLOW)
    if not flow or update.effective_user.id != flow.get("owner"):
        await home(update, context); return
    value = (message.text or "").strip()
    access = await world_access.check(context.bot, chat.id)
    if not access.ready:
        context.chat_data.pop(FLOW, None)
        await access_page(update, context)
        return
    try:
        await message.delete()
    except (BadRequest, Forbidden):
        if await world_access_repo.claim_warning(chat.id, "delete-failed"):
            await message.reply_text("پیام مرحله‌ای حذف نشد؛ فرایند ادامه دارد و دسترسی در بررسی بعدی دوباره کنترل می‌شود.")
    if flow["step"] == "name":
        from packages.core.services.content_filter import inspect
        if not inspect(value).allowed:
            await msg.reply_text(fa.CONTENT_REJECTED); return
        if not 3 <= len(value) <= 80:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="نام باید بین ۳ تا ۸۰ نویسه باشد. دوباره نام را بفرست.", reply_markup=kb.cancel()); return
        flow["name"] = value; flow["step"] = "government"
        await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text=fa.WIZARD_GOV, reply_markup=kb.governments()); return
    if flow["step"] == "description":
        from packages.core.services.content_filter import inspect
        if not inspect(value).allowed:
            await msg.reply_text(fa.CONTENT_REJECTED); return
        if not 10 <= len(value) <= 500:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="معرفی باید بین ۱۰ تا ۵۰۰ نویسه باشد. دوباره معرفی را بفرست.", reply_markup=kb.cancel()); return
        p = await player(update)
        try:
            await countries.create_country(chat_id=chat.id, chat_title=chat.title or "", player_id=p.id, name=flow["name"], government=flow["government"], description=value)
        except (ValueError, PermissionError) as exc:
            context.chat_data.pop(FLOW, None)
            await show(update, context, f"ساخت کشور انجام نشد: {ERRORS.get(str(exc), 'اطلاعات معتبر نبود.')}\n\nاز صفحه اصلی دوباره تلاش کن.", kb.back()); return
        context.chat_data.pop(FLOW, None); await home(update, context)

async def precheckout(update,context):
 q=update.pre_checkout_query;ok=await commerce.precheckout(q.invoice_payload,q.from_user.id,q.total_amount);await q.answer(ok=ok,error_message=None if ok else "صورتحساب نامعتبر یا منقضی شده است.")
async def successful_payment(update,context):
 payment=update.effective_message.successful_payment
 if not payment:return
 purpose=await commerce.settle(payment.invoice_payload,update.effective_user.id,payment.total_amount,payment.telegram_payment_charge_id,payment.provider_payment_charge_id or None)
 await update.effective_message.reply_text("✅ سهم شما ثبت شد. با تکمیل هدف جمعیت‌محور، اشتراک ۳۰روزه گروه فعال می‌شود." if purpose=="subscription" else "✅ پرداخت ثبت شد.")
def register(app):
    app.add_handler(CallbackQueryHandler(callback, pattern=r"^tw:"))
    app.add_handler(PreCheckoutQueryHandler(precheckout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))
    app.add_handler(MessageHandler(filters.TEXT, text))
```

### `apps\teleworld_bot\keyboards.py`

```python
"""رابط دکمه‌ای فارسی جهان؛ رنگ فقط برای یک اقدام اصلی در هر صفحه است."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def b(text, action, style=None):
    kwargs = {"text": text, "callback_data": f"tw:{action}"}
    if style:
        kwargs["style"] = style
    return InlineKeyboardButton(**kwargs)

def access(ready=False):
    if ready:
        return InlineKeyboardMarkup([[b("✅ ورود به جهان", "access:check", "primary")],
                                     [b("🩺 بررسی وضعیت", "health")]])
    return InlineKeyboardMarkup([[b("🔄 بررسی دوباره دسترسی", "access:check", "primary")],
                                 [b("📘 چرا دسترسی مدیر لازم است؟", "access:why")],
                                 [b("🩺 وضعیت و علت قفل", "health")]])

def private(username):
    return InlineKeyboardMarkup([[InlineKeyboardButton("➕ افزودن به گروه", url=f"https://t.me/{username}?startgroup=true", style="primary")], [b("📘 راهنمای استفاده", "guide")]])

def home(country, admin, citizen=False):
    if country:
        rows = [[b("🏛 شناسنامه کشور", "country", "primary"), b("👥 شهروندان", "citizens")],
                [b("💰 اقتصاد و منابع", "economy"), b("🗳 سیاست و انتخابات", "politics")], [b("🏗 پروژه ملی", "project")]]
        rows.append([b("🚪 خروج از شهروندی", "leave", "danger")] if citizen else [b("🤝 شهروند این کشور می‌شوم", "join", "success")])
        rows.append([b("🛡 اشتراک بدون تبلیغ", "subscription", "primary"),b("✈️ مهاجرت", "migration")])
        if admin:rows.append([b("📥 درخواست‌های مهاجرت", "migration_review")])
        rows.append([b("📘 راهنمای همین مرحله", "guide"), b("🔄 تازه‌سازی", "home")])
        return InlineKeyboardMarkup(rows)
    if admin:
        return InlineKeyboardMarkup([[b("🏗 ساخت کشور", "create", "primary")], [b("📘 راهنمای ساخت کشور", "guide")], [b("🔄 تازه‌سازی", "home")]])
    return InlineKeyboardMarkup([[b("📘 برای ساخت کشور چه کنیم؟", "guide", "primary")], [b("🔄 تازه‌سازی", "home")]])

def governments():
    items=[("🏛 جمهوری","republic"),("🗳 ریاستی","presidential"),("🏢 پارلمانی","parliamentary"),("⚖️ نیمه‌ریاستی","semi_presidential"),("👑 پادشاهی","monarchy"),("📜 مشروطه","constitutional_monarchy"),("🛡 دیکتاتوری","dictatorship"),("🧭 فدرال","federal"),("🤝 شورایی","council"),("👥 مستقیم","direct_democracy"),("⛪ دینی","theocracy"),("🎖 شورای نظامی","military_junta"),("💠 الیگارشی","oligarchy")]
    rows=[[b(label,f"gov:{code}") for label,code in items[i:i+2]] for i in range(0,len(items),2)]
    rows.append([b("لغو ساخت کشور","home")]);return InlineKeyboardMarkup(rows)

def government_confirm(code):
    return InlineKeyboardMarkup([[b("تأیید این حکومت",f"govok:{code}","primary")],[b("انتخاب نوع دیگر","govback")],[b("لغو ساخت کشور","home")]])

def country():
    return InlineKeyboardMarkup([[b("💰 کمک ۵۰ هزار تومان", "donate:50000", "success"), b("💰 کمک ۲۰۰ هزار تومان", "donate:200000")],
                                 [b("🗳 انتخابات", "politics", "primary"), b("👥 شهروندان", "citizens")], [b("🏠 خانه جهان", "home")]])

def politics(status=None, allowed=True):
    if not allowed: return InlineKeyboardMarkup([[b("🏛 شناسنامه کشور","country","primary")],[b("🏠 خانه جهان","home")]])
    if status == "nominations":
        rows = [[b("🙋 نامزد می‌شوم", "nominate", "primary")], [b("⏳ زمان رأی‌گیری هنوز نرسیده", "politics")]]
    elif status == "voting":
        rows = [[b("🗳 انتخاب نامزد", "votehelp", "primary")]]
    else:
        rows = [[b("🗳 آغاز انتخابات", "estart", "primary")]]
    rows.append([b("📊 نظرسنجی‌ها", "polls"), b("🏠 خانه جهان", "home")])
    return InlineKeyboardMarkup(rows)

def back(action="home"):
    return InlineKeyboardMarkup([[b("🏠 خانه جهان", action, "primary")]])
def cancel(): return back()
def candidates(rows):
    buttons = [[b(f"🗳 رأی به {row['first_name']}", f"vote:{row['player_id']}", "primary" if i == 0 else None)] for i, row in enumerate(rows)]
    buttons.append([b("↩️ بازگشت", "politics")])
    return InlineKeyboardMarkup(buttons)
def project(active):
    if active:
        return InlineKeyboardMarkup([[b("💵 کمک ۵۰ هزار تومان", "pcon:IRT:50000", "success")],
                                     [b("🌾 کمک ۵۰ غذا", "pcon:food:50"), b("⛏ کمک ۵۰ ماده معدنی", "pcon:minerals:50")], [b("🏠 خانه جهان", "home")]])
    return InlineKeyboardMarkup([[b("🏗 آغاز پروژه ملی", "pstart", "primary")], [b("🏠 خانه جهان", "home")]])

def subscription(round_id:int,remaining:int):
 rows=[]
 for amount in (1,2,5,10,25,50):
  if amount<=remaining: rows.append([b(f"⭐ مشارکت {amount} استار",f"substar:{round_id}:{amount}","primary" if amount==min(remaining,50) else None)])
 rows.append([b("💰 خرید از خزانه کشور","subtreasury")]);rows.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(rows)

def migration_countries(rows,owner_country_id):
 buttons=[[b(f"✈️ مهاجرت به {r['name']}",f"migrate:{r['id']}")] for r in rows if int(r['id'])!=int(owner_country_id)]
 buttons.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(buttons)
def migration_review(rows):
 buttons=[]
 for r in rows:buttons.extend([[b(f"✅ پذیرش {r['first_name']}",f"migaccept:{r['id']}","success"),b("رد",f"migreject:{r['id']}","danger")]])
 buttons.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(buttons)

def central_bank(president=False):
    rows=[]
    if president:
        rows.append([b("➕ افزایش بهره ۱٪","rate:up","primary"),b("➖ کاهش بهره ۱٪","rate:down")])
        rows.append([b("💵 خرید ذخیره ارزی ۱۰M","reserve:buy","success")])
    rows.append([b("↩️ اقتصاد کشور","economy"),b("🏠 خانه جهان","home")])
    return InlineKeyboardMarkup(rows)
```

### `apps\teleworld_bot\main.py`

```python
from telegram import BotCommandScopeAllGroupChats,BotCommandScopeAllPrivateChats
from telegram.ext import Application
from apps.teleworld_bot.handlers import access, world
from apps.teleworld_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service

async def post_init(application:Application)->None:
 await application.bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
 await application.bot.delete_my_commands(scope=BotCommandScopeAllGroupChats())
def register(application:Application):access.register(application);world.register(application);application.post_init=post_init;application.add_error_handler(make_error_handler(fa.ERROR))
def main():run_bot(Service.TELEWORLD,register)
if __name__=='__main__':main()
```

### `apps\teleworld_bot\texts\__init__.py`

```python
"""Package apps.teleworld_bot.texts."""
```

### `apps\teleworld_bot\texts\fa.py`

```python
ERROR='مشکلی پیش آمد؛ صفحه را تازه‌سازی کن و دوباره تلاش کن.'
HOME_EMPTY='🌍 <b>جهان این گروه</b>\n\nاین گروه هنوز کشور ندارد. کشور یک بازی گروهی با شهروند، خزانه، منابع، انتخابات و پروژه ملی است.\n\nاگر مدیر گروه هستی، «ساخت کشور» را بزن. در غیر این صورت از مدیر بخواه این کار را آغاز کند. هیچ فرمانی لازم نیست.'
HOME='🌍 <b>{name}</b>\n\nوضعیت: <b>{status}</b> · شهروندان: <b>{citizens}</b>\nرهبر: <b>{leader}</b>\nخزانه: <b>{treasury}</b>\n\n🎯 <b>هدف بعدی:</b> {goal}\n\nهمه کارهای عمومی کشور با دکمه‌های همین پیام انجام می‌شود. شغل و دارایی شخصی در بات زندگی قرار دارد.'
GUIDE_EMPTY='📘 <b>راهنمای ساخت جهان</b>\n\n۱) مدیر گروه «ساخت کشور» را می‌زند.\n۲) نام را به‌صورت یک پیام معمولی می‌فرستد.\n۳) نوع حکومت را با دکمه انتخاب می‌کند.\n۴) معرفی کشور را به‌صورت پیام می‌فرستد.\n۵) اعضا با دکمه شهروند می‌شوند.\n\nپیام‌های نام و معرفی پس از دریافت پاک می‌شوند تا گروه شلوغ نشود.'
GUIDE='📘 <b>راهنمای بازی گروهی</b>\n\n• عضوها با دکمه «شهروند می‌شوم» وارد کشور می‌شوند.\n• شهروندان می‌توانند کمک مالی کنند، نامزد شوند و رأی بدهند.\n• رهبر و جمعیت معتبر، کشور را به مرحله رسمی می‌رسانند.\n• پروژه ملی با همکاری شهروندان کامل می‌شود.\n• کار، حقوق، بانک، خانه و بازار شخصی فقط در بات زندگی انجام می‌شوند.\n\nهر بار یک دکمه را انتخاب کن؛ نتیجه و قدم بعدی روی همین پیام نشان داده می‌شود.'
COUNTRY='🏛 <b>{name}</b>\n\nنوع حکومت: <b>{government}</b>\nوضعیت: <b>{status}</b>\nشهروندان: <b>{citizens}</b>\nرهبر: <b>{leader}</b>\nخزانه: <b>{treasury}</b>\n\n{description}\n\nکمک مالی از کیف پول شخصی کم و به خزانه کشور اضافه می‌شود.'
ECONOMY='💰 <b>اقتصاد کشور</b>\n\nخزانه: <b>{treasury}</b>\nدرآمد روزانه: <b>{income}</b>\nهزینه روزانه: <b>{expense}</b>\n\n<b>منابع کشور</b>\n{resources}\n\nاین دارایی‌ها عمومی‌اند؛ دارایی شخصی هر بازیکن در بات زندگی مدیریت می‌شود.'
CITIZENS='👥 <b>شهروندان کشور</b>\n\nجمعیت رسمی: <b>{count}</b>\n{members}\n\nرسمی‌شدن کشور بر اساس شهروندان ثبت‌شده است، نه تعداد خام اعضای گروه.'
POLITICS='🗳 <b>سیاست و انتخابات</b>\n\n{state}\n\nفقط شهروند معتبر می‌تواند نامزد شود یا رأی بدهد. هر رأی یک‌بار ثبت می‌شود.'
WIZARD_NAME='🏗 <b>ساخت کشور — گام ۱ از ۳</b>\n\nمدیر سازنده، نام کشور را همین حالا در گروه بفرستد.\n\nنام باید بین ۳ تا ۸۰ نویسه باشد. پیام پس از خواندن پاک می‌شود.'
WIZARD_GOV='🏛 <b>ساخت کشور — گام ۲ از ۳</b>\n\nنوع حکومت را با یکی از دکمه‌ها انتخاب کن.'
WIZARD_DESC='📝 <b>ساخت کشور — گام ۳ از ۳</b>\n\nیک معرفی روشن بین ۱۰ تا ۵۰۰ نویسه بفرست. پس از ساخت، صفحه اصلی کشور نمایش داده می‌شود.'
PRIVATE='🌍 <b>جهان گروهی</b>\n\nاین بات برای بازی عمومی داخل گروه است. آن را به گروه اضافه کن؛ سپس در گروه یک پیام معمولی بفرست تا صفحه دکمه‌ای جهان باز شود.\n\nکار و دارایی شخصی در بات زندگی انجام می‌شوند.'
CONTENT_REJECTED='⚠️ این متن شامل واژه‌ای است که در نام یا معرفی کشور مجاز نیست. لطفاً متن محترمانه‌تری بنویس؛ فرصتت برای ادامه ساخت محفوظ است.'
GOVERNMENT_DETAILS={
'republic':('جمهوری','رهبر با رأی شهروندان و برای دوره محدود انتخاب می‌شود. نتیجه رأی قابل تغییر نیست.'),
'presidential':('جمهوری ریاستی','رئیس‌جمهور مستقیماً انتخاب می‌شود و اختیار اجرایی بالایی دارد؛ رأی و انتقال قدرت الزام‌آور است.'),
'parliamentary':('جمهوری پارلمانی','شهروندان نمایندگان را انتخاب می‌کنند و اکثریت پارلمان دولت را می‌سازد.'),
'semi_presidential':('نیمه‌ریاستی','قدرت اجرایی میان رئیس‌جمهور منتخب و نخست‌وزیر متکی به پارلمان تقسیم می‌شود.'),
'monarchy':('پادشاهی مطلقه','جانشینی موروثی است؛ انتخابات سراسری رهبر وجود ندارد و پادشاه اختیار نهایی دارد.'),
'constitutional_monarchy':('پادشاهی مشروطه','پادشاه نماد کشور است و دولت منتخب در چارچوب قانون اساسی اداره می‌کند.'),
'dictatorship':('دیکتاتوری','رهبر اختیار آغاز انتخابات نمایشی، لغو آن و تغییر نتیجه را دارد؛ انتقال قدرت آزاد تضمین‌شده نیست.'),
'federal':('فدرال','قدرت میان دولت مرکزی و ایالت‌ها تقسیم می‌شود؛ رهبر با انتخابات رقابتی تعیین می‌شود.'),
'council':('شورایی','شورا به‌صورت جمعی تصمیم می‌گیرد و رئیس شورا اختیار یک‌جانبه محدود دارد.'),
'direct_democracy':('دموکراسی مستقیم','شهروندان مستقیماً درباره تصمیم‌ها و رهبری رأی می‌دهند؛ نتیجه الزام‌آور است.'),
'theocracy':('حکومت دینی','رهبر بر پایه ساختار مذهبی تعیین می‌شود و صلاحیت نامزدها پیش از رأی‌گیری بررسی می‌شود.'),
'military_junta':('شورای نظامی','شورای فرماندهان رهبر را تعیین می‌کند؛ انتخابات عمومی رهبر برگزار نمی‌شود.'),
'oligarchy':('الیگارشی','شورای نخبگان محدود رهبر را انتخاب می‌کند؛ شهروندان رأی مستقیم ندارند.'),
}
GOV_CONFIRM='<b>{title}</b>\n\n{description}\n\nاین مدل فقط برچسب نیست و قواعد انتخابات و انتقال قدرت را در بازی تغییر می‌دهد. این نوع حکومت را تأیید می‌کنی؟'
```

### `AUDIT_AND_DEPLOY_FA_2026-07-27.md`

```markdown
# ممیزی و استقرار TeleLife — ۲۰۲۶/۰۵/۰۵

## اصلاح‌های بحرانی

1. قفل `FOR UPDATE OF g` از سمت nullable در `LEFT JOIN` حذف شد؛ فقط ردیف‌های `ad_deliveries` با `SKIP LOCKED` رزرو می‌شوند و به‌روزرسانی گروه اتمیک باقی مانده است.
2. محدودیت قیمت تبلیغ از فهرست چهار قیمت پایه به بازه امن ۱ تا ۱۰٬۰۰۰ ستاره تغییر کرد. قیمت‌های کانال World و Both مثل ۱۸۰ و ۴۴۰ اکنون معتبرند.
3. محدودیت قدیمی اشتراک (`target_stars=10`) با منطق فعلی ۱۰ تا ۷۵ ستاره سازگار شد؛ داده‌ای حذف نمی‌شود.
4. Jobهای دقیقه‌ای ایزوله شدند؛ شکست یک Job مانع نرخ، خبر، انتخابات یا Job بعدی نمی‌شود.
5. آخرین نتیجه، مدت اجرا و خطای Jobها در `scheduler_job_runs` ثبت می‌شود.

## نرخ واقعی USDT

- منبع: `https://api.zipodo.ir/usdt/`
- دریافت فقط سمت سرور با timeout، محدودیت حجم، اعتبارسنجی JSON/text و بازه معقول انجام می‌شود.
- نرخ معتبر در `market_prices` و `market_price_snapshots` ذخیره می‌شود.
- در خطای منبع، آخرین نرخ معتبر حفظ و وضعیت stale در پنل نمایش داده می‌شود؛ عدد تصادفی به‌عنوان نرخ واقعی تولید نمی‌شود.

## پنل مدیریت

- اتاق عملیات زنده، وضعیت منبع نرخ و صف‌ها
- تاریخچه واقعی بازار و تازه‌سازی ۳۰ ثانیه‌ای فقط هنگام فعال‌بودن تب
- توقف اضطراری بازار
- مشاهده آخرین اجرای Jobها و اجرای دستی فهرست سفید
- نمایش خطای واقعی به‌جای پنهان‌کردن شکست

## تعامل گروه

- streak روزانه گروه
- تصمیم کوتاه ۴۵ دقیقه‌ای هر ۴۸ ساعت برای گروه فعال
- هشدار بازار در تغییر حداقل ۰٫۵٪
- خلاصه روزانه ساعت ۱۸ UTC
- همه پیام‌ها از Outbox با کلید idempotency عبور می‌کنند.

## ترتیب استقرار

1. از دیتابیس پشتیبان بگیرید.
2. نسخه را Deploy کنید؛ migrator فایل `0012_reliability_live_market_engagement.sql` را افزایشی اجرا می‌کند.
3. در پنل «عملیات زنده»، Job نرخ Zipodo و صف‌ها را کنترل کنید.
4. یک درخواست تبلیغ `campaign/world` با قیمت ۱۸۰ ستاره ثبت کنید.
5. ابتدا بازار را در حالت freeze نگه دارید، نرخ را بررسی و سپس باز کنید.

## اعتبارسنجی انجام‌شده

- Compile تمام ۱۰۳ فایل Python: موفق
- Syntax فایل JavaScript: موفق
- ساختار HTML: ۴۶ شناسه بدون تکرار، ۸ view
- اسکن قفل nullable: مورد خطادار باقی نمانده
- تست‌های رگرسیون قیمت و parser نرخ اضافه شد
- اجرای کامل pytest در محیط تحویل ممکن نبود، چون محیط آفلاین ابزار `pytest` و وابستگی‌های پروژه را نصب نداشت. در CI/محیط پروژه اجرا شود: `python -m pytest -q`.
```

### `AUDIT_FINAL_FA_2026-07-27.md`

```markdown
# ممیزی نهایی TeleLife — ۲۷ ژوئیهٔ ۲۰۲۶

## خلاصه اجرایی
پروژه از دامپ ۲۱۵ بخشی بازسازی شد؛ ۲۱۳ فایل متنی بازیابی شدند و دو فایل غیرمتنی تولیدشدنی (`.dockerignore` و `MANIFEST.sha256`) دوباره ساخته شدند. تمرکز این نسخه بر امنیت و صحت اقتصاد، کاهش گیجی کاربر، مشاهده‌پذیری ماندگاری و بازطراحی کامل پنل مدیریت است.

## ایرادهای مهم اصلاح‌شده

1. **ریسک CSRF روی عملیات مدیریتی:** عملیات POST/PUT قدیمی با Basic Auth می‌توانستند از مبدأ دیگر فراخوانی شوند. Middleware اکنون مبدأ درخواست‌های تغییردهنده را با Host تطبیق می‌دهد.
2. **اعتماد سراسری به Proxy Header:** مقدار `forwarded_allow_ips="*"` به loopback محدود شد تا جعل اطلاعات پراکسی کاهش یابد.
3. **ناسازگاری احتمالی پاداش روزانه و Ledger:** اگر درج ردیف Ledger به‌دلیل برخورد کلید انجام نشود، تراکنش اکنون rollback می‌شود؛ پول بدون سند immutable ثبت نمی‌شود.
4. **کاهش منبع با ردیف ناموجود:** UPSERT منابع اکنون فقط برای delta مثبت ردیف تازه می‌سازد و کاهش نامعتبر را رد می‌کند.
5. **Feature flag دلخواه:** API جدید فقط چهار کلید اضطراری allowlist‌شده را می‌پذیرد.
6. **ویرایش تبلیغ با prompt:** تمام promptهای مرورگر حذف و با Dialog معتبر، قابل‌دسترسی و دارای بازخورد جایگزین شدند.
7. **عملیات حساس بدون اصطکاک:** توقف سامانه و بازپرداخت/رد/توقف تبلیغ تأیید واضح و دومرحله‌ای دارند.
8. **قابلیت‌های پنهان پنل:** Audit و Ledger که داده داشتند ولی UI نداشتند، اکنون صفحه کامل دارند.

## پنل مدیریت تازه

- نمای ماندگاری با فعال روز/هفته/ماه، دریافت هدیه، زنجیره حضور، قیف شروع، رسیدن به شغل/بازار و پیشنهادهای داده‌محور
- دفتر اقتصاد و کنترل سریع موجودی‌های منفی
- گزارش کامل حسابرسی مدیران
- مرکز توقف اضطراری اقتصاد، بازار، تبلیغات و ثبت‌نام
- حفظ همه صفحات قبلی: نمای کلی، بازار، عملیات زنده، بازیکنان، کشورها، خبر، تبلیغات و درخواست‌ها
- واکنش‌گرا، RTL، focus-visible و احترام به reduced-motion

## پیشنهادهای درگیری کاربر

این نسخه عمداً از افزودن هم‌زمان ده سیستم تازه خودداری می‌کند. برای کاربری که نباید گیج شود، بهترین چرخه این است:

1. **خانه فقط یک «قدم بعدی» اصلی نشان دهد.** این ساختار در مسیر چهارمرحله‌ای فعلی حفظ شده است.
2. **هدیه روزانه آغاز جلسه باشد، نه پایان آن.** پس از Claim، کارهای امروز اقدام اصلی باقی می‌ماند.
3. **ماموریت‌ها کوتاه و قابل فهم باشند.** پنل جدید نرخ تکمیل را نشان می‌دهد تا سختی با داده تنظیم شود.
4. **بازشدن شغل در سطح ۵ و بازار در سطح ۱۰** هدف میان‌مدت روشن می‌دهد بدون اینکه همه امکانات روز اول روی کاربر آوار شود.
5. در نسخه بعد، فقط پس از جمع‌شدن داده، یک **رویداد آخرهفته مشارکتی سبک** اضافه شود؛ نه لیگ پیچیده و نه ده ارز تازه.

## محدودیت اعتبارسنجی

- تمام فایل‌های Python با `compileall` و AST بررسی شدند.
- JavaScript پنل با `node --check` بررسی شد.
- تمام YAMLها parse شدند.
- تست‌های Regression تازه اضافه شدند.
- محیط ممیزی Python 3.10 دارد و `pytest`/وابستگی‌های پروژه نصب نیستند؛ اجرای کامل suite نیازمند Python 3.13 و نصب dependencyهای تعریف‌شده در `pyproject.toml` است.
- تست عملی PostgreSQL و Telegram بدون credential و سرویس خارجی انجام نشده است.

## استقرار

1. ZIP را استخراج کنید و `.env` را از `.env.example` بسازید.
2. Python 3.13 و dependencyها را نصب کنید.
3. پیش از production، `python -m pytest -q` را اجرا کنید.
4. روی دیتابیس staging مهاجرت‌ها را اجرا و Snapshot/Backup بگیرید.
5. یک Claim روزانه، یک معامله، یک تغییر Feature Flag و یک گردش تأیید تبلیغ را smoke-test کنید.
6. سپس release را به production ببرید و صفحه عملیات زنده و Ledger را زیر نظر بگیرید.
```

### `AUDIT_STATUS.md`

```markdown
# Production Readiness Audit

## اصلاحات تکمیل‌شده

- ورودی چهار-service قدیمی با یک process supervisor جایگزین شد.
- دو bot در polling mode، scheduler و FastAPI همزمان اجرا می‌شوند.
- فقط Uvicorn/FastAPI روی `PORT` listen می‌کند.
- crash boundary، auto-restart با exponential backoff، health registry، heartbeat، memory watermark و graceful shutdown افزوده شد.
- lifecycle دیتابیس process-level شد تا یک pool مشترک asyncpg با سقف ۴ connection استفاده شود.
- Supabase transaction pooler با statement cache صفر، TLS در DSN نمونه و inactive lifetime محدود پیکربندی شد.
- migration runner با PostgreSQL advisory transaction lock ایمن شد.
- health/readiness endpoints و security headers افزوده شدند.
- Render Blueprint به یک Free Web Service کاهش یافت؛ هیچ feature، route، table یا game service حذف نشد.
- تمام فایل‌های Python با AST و compileall بررسی شدند؛ fragment تولیدی خراب در source پیدا نشد.
- تست crash isolation افزوده شد.

## محدودیت اعتبارسنجی محیط ممیزی

اجرای کامل pytest و integration test زنده با Supabase/Telegram در sandbox آفلاین ممکن نبود، زیرا runtime dependencyهای پروژه و credentialهای واقعی موجود نبودند. Dockerfile نصب dependencyها و compile check را در build انجام می‌دهد. پیش از production، تست‌های integration باید در CI با database آزمایشی و tokenهای اختصاصی اجرا شوند.
```

### `CHANGELOG_FA.md`

```markdown
# گزارش اصلاحات نسخه فارسی دکمه‌محور

- رفع خرابی نحوی فایل تنظیمات تجربه که مانع بارگذاری کل پیکربندی می‌شد.
- انتقال کامل شغل، کارکردن، دریافت درآمد و ارتقا به بات خصوصی زندگی.
- حذف شغل شخصی و همه مسیرهای آن از رابط و کنترل‌گر بات جهان.
- تبدیل بات جهان به رابط پیام‌محور: هر پیام گروه صفحه جهان را نمایش یا تازه‌سازی می‌کند.
- حذف ثبت فرمان از بات جهان و پاک‌سازی منوی فرمان‌های قدیمی در زمان راه‌اندازی.
- فارسی‌سازی نام شغل‌ها و نوع خروجی در صفحه درآمد.
- افزودن معدن‌کار به فهرست انتخاب شغل و هماهنگ‌سازی فهرست با تنظیمات واقعی.
- ایمن‌سازی ترتیب چهار گام شروع؛ گام قدیمی یا خارج از نوبت دیگر پیشرفت ایجاد نمی‌کند.
- هدایت بازیکن پس از سرمایه آغازین به کارهای روزانه و پس از پایان آموزش به خانه اصلی.
- تقویت حلقه ماندگاری: هدیه روزانه به کارهای امروز، سطح ۵، شغل و رشد دارایی متصل شد.
- افزودن توضیح مرحله‌ای، وضعیت‌های روشن و راهنمای فارسی در صفحه‌های اصلی.
- ایمن‌سازی انتخاب حکومت در صورت منقضی‌شدن یا متعلق‌نبودن فرایند ساخت.
- اصلاح پاسخ دوباره به یک دکمه در مسیر ساخت کشور.
- افزودن پیام خطای فارسی برای موجودی ناکافی و وضعیت‌های ناقص.
- افزودن آزمون‌های ایستا برای نحو پایتون، YAML، جداسازی مسئولیت بات‌ها و نبود فرمان در بات جهان.
```

### `CHANGELOG_FA_2026-07-27.md`

```markdown
# گزارش تغییرات نسخه سخت‌سازی جهان گروهی

- مدیریت واقعی `my_chat_member` برای ورود، تغییر دسترسی و حذف بات افزوده شد.
- خوش‌آمدگویی اتمیک و غیرتکراری، ذخیره شناسه پیام و وضعیت عضویت پیاده‌سازی شد.
- سیاست حداقل مجوز شامل مدیر بودن و اجازه حذف پیام‌ها است.
- کش کوتاه‌مدت بررسی دسترسی و بررسی اجباری با دکمه افزوده شد.
- همه عملیات تغییردهنده جهان پشت قفل دسترسی قرار گرفتند.
- صفحه سلامت بدون نمایش اطلاعات محرمانه افزوده شد.
- کلید تکرارناپذیری کمک مالی و پروژه از شناسه ثابت Callback ساخته شد؛ دوبارکلیک پرداخت را تکرار نمی‌کند.
- گزارش حسابرسی محصول با کلید یکتا و جلوگیری از سیل رخداد افزوده شد.
- راهنمای فارسی BotFather، Privacy Mode و مجوز مدیر افزوده شد.
- مهاجرت `0008_world_access_lifecycle.sql` افزوده شد؛ فقط ساخت افزایشی و تکرارپذیر دارد.

- سازگاری checksum برای مهاجرت‌های تاریخی 0001 تا 0007 افزوده شد: رکورد دیتابیس حفظ و SQL قدیمی دوباره اجرا نمی‌شود؛ از 0008 به بعد کنترل checksum همچنان سخت‌گیرانه است.
```

### `CHANGELOG_FA_2026-07-27_V2.md`

```markdown
# تغییرات V2 — هویت کشور و بازار واقعی

- تمام پیام‌های سیستمی گروه در مرز انتشار Outbox با نام کشور سربرگ می‌گیرند.
- برای گروه ثبت‌شده بدون کشور، انتشار سیستمی متوقف و راهنمای ساخت کشور فقط یک بار نمایش داده می‌شود.
- خلاصه، رویداد و هشدار بازار دیگر از عنوان گروه تلگرام استفاده نمی‌کنند.
- نمودار واقعی USDT/IRT با OHLC سی‌دقیقه‌ای و بازه ۲۴ساعته به TeleLife افزوده شد.
- نمودار از snapshotهای Zipodo ساخته می‌شود و فاصله‌های بدون داده را جعل نمی‌کند.
- بانک مرکزی با نرخ بهره و خرید ذخیره ارزی برای رئیس کشور اضافه شد.
- شاخص‌های روزانه تورم، بیکاری، رشد، رضایت و GDP اضافه شدند.
- شوک‌های کمیاب و قطعی بر اساس کشور/تاریخ و روزنامه اختصاصی کشور اضافه شدند.
- ذخیره ارزی شدت شوک منفی را کم می‌کند و نرخ بهره بالا تورم و رشد را تحت تأثیر قرار می‌دهد.
```

### `DELIVERY.md`

```markdown
# TeleLife Phase 5 Delivery

This repository is reconstructed from the supplied TeleLife Phase 2 dump and includes the integrated country/group layer.

## Included

- Forward-only `0003_country_layer.sql`
- YAML-driven country, economy, jobs, elections, projects, missions, news, and daily events
- Repository-only SQL for all new domains
- Atomic shared-ledger service for money/resources
- Lazy production with capacity cap, proportional XP threshold, and checkpoint-before-upgrade
- Country missions instantiated from eligible actions
- Elections, secret one-vote ballots, polls, presidential permissions
- One-time national storage project
- Transactional outbox with retry lease
- Idempotent daily events and country-economy catch-up
- Audited admin APIs
- TeleWorld command handlers and scheduler integration
- Phase 5 documentation and security/config tests

## Run

1. Copy `.env.example` to `.env` and set database/bot/admin secrets.
2. Install dependencies from `requirements.txt` in Python 3.13.
3. Run `pytest`.
4. Start services with `SERVICE=telelife|teleworld|scheduler|admin python run.py`.

Migrations are applied automatically at service startup.
```

### `Dockerfile`

```
FROM python:3.13-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app

WORKDIR /app

RUN addgroup --system --gid 10001 telelife \
    && adduser --system --uid 10001 --ingroup telelife --home /home/telelife telelife

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY --chown=telelife:telelife . .
RUN python -m compileall -q apps packages run.py

USER telelife
CMD ["python", "run.py"]
```

### `docs\CONVENTIONS.md`

```markdown
# Conventions — non-negotiable

## Code
- Python 3.13 target, forward-compatible with 3.14.
- `from __future__ import annotations` at the top of every module.
- Full type hints on every public function.
- Fully async. No blocking I/O in the event loop, ever.
- Max 400 lines per file. Split before exceeding.
- Ruff and mypy strict must pass.

## Money
- Always BIGINT minor units. Never float.
- Every mutation goes through the ledger with an idempotency key.
- Every mutation runs inside `db.transaction()`.
- `CHECK (balance >= 0)` stays on every balance column.

## Database
- Forward-only migrations numbered `0001_`, `0002_`, ...
- Never edit an applied migration; the checksum guard will reject it.
- Index every column used in WHERE, ORDER BY or JOIN on a hot path.
- Use partial indexes for filtered hot queries.

## Persian copy
- Modern, warm, meme-aware. Never robotic, never childish, never cringe.
- Persian digits with `٬` as the thousands separator in all player-facing numbers.
- Second person singular. Short sentences. Emoji as structure, not decoration.

## Telegram
- HTML parse mode everywhere. Escape user input.
- Every callback must be ownership-checked (Phase 6).
- Interactive panels auto-expire per `core.menu_cleanup` (Phase 2+).

## Security
- Secrets only via env. Never committed, never logged.
- Constant-time comparison for every credential check.
- Admin actions write to `audit_log`.
```

### `docs\DEPLOYMENT.md`

```markdown
# راهنمای اجرا | Deployment Guide

---

## ۰. آیا الان آماده انتشار عمومی است؟

**نه هنوز.** کد اجرا می‌شود و پایدار است، اما دو فاز حیاتی هنوز نیامده‌اند.

| موضوع | وضعیت | چرا مهم است |
|---|---|---|
| اجرا می‌شود بدون کرش | ✅ | فاز ۱ و ۲ کامل و تست‌شده |
| بازیکن می‌تواند رشد کند | ✅ | XP، سطح، جایزه، ماموریت، آنلاک |
| **راهی برای خرج‌کردن پول** | ❌ فاز ۳ | پول فقط وارد می‌شود، خارج نمی‌شود → تورم |
| **شغل و درآمد فعال** | ❌ فاز ۳ | بعد از سطح ۱۰ محتوا تمام می‌شود |
| **Rate limit و ضد اسپم** | ❌ فاز ۶ | یک اسکریپت ساده می‌تواند دیتابیس را اشباع کند |
| **تعامل فارسی در گروه** | ❌ فاز ۵ | TeleWorld فعلاً فقط `/status` دارد |
| **ویرایش بازیکن در پنل** | ❌ فاز ۷ | برای رفع مشکل کاربر ابزاری نداری |

### جمع‌بندی صادقانه

- **تست بسته با ۱۰ تا ۵۰ نفر دوست:** ✅ همین الان برو.
- **انتشار عمومی:** ❌ حداقل تا پایان **فاز ۳ و فاز ۶** صبر کن.

دلیل اصلی: اقتصاد فعلاً فقط **ورودی** دارد. هر بازیکن روزانه پول می‌گیرد و هیچ‌جا خرجش نمی‌کند. اگر عمومی منتشر کنی، تا چند هفته همه میلیاردر می‌شوند و وقتی فاز ۳ بیاید، مجبوری یا اقتصاد را ریست کنی (بازیکن‌ها عصبانی می‌شوند) یا با تورمی که هرگز جبران نمی‌شود زندگی کنی.

دلیل دوم: بدون rate limit، یک نفر با یک اسکریپت ساده می‌تواند pool دیتابیس رایگان Supabase را پر کند و بازی برای همه بخوابد.

---

## ۱. پیش‌نیازها

- Python **3.13** (یا Docker)
- یک دیتابیس PostgreSQL (Supabase رایگان کافی است)
- دو توکن ربات از [@BotFather](https://t.me/BotFather)
- **مهم:** کلاینت تلگرام به‌روز برای دیدن دکمه‌های رنگی (Bot API 9.4). کلاینت قدیمی همه را شیشه‌ای می‌بیند و بازی سالم کار می‌کند.

---

## ۲. ساخت ربات‌ها در BotFather
```

### `docs\DEPLOYMENT_FA.md`

```markdown
# راهنمای استقرار فارسی تله‌لایف و جهان گروهی

## پیش‌نیازها

- Python 3.13، PostgreSQL و دو توکن مستقل برای بات «زندگی» و «جهان»
- ساخت `.env` از روی `.env.example`؛ فایل واقعی `.env` را وارد مخزن یا بسته نکنید.
- اجرای برنامه با `python run.py`؛ مهاجرت‌ها هنگام راه‌اندازی زیر قفل PostgreSQL اجرا می‌شوند.

## تنظیم BotFather و حریم خصوصی گروه

1. در BotFather فرمان `/mybots` را باز کنید و بات جهان را انتخاب کنید.
2. به **Bot Settings → Group Privacy** بروید و Privacy Mode را **خاموش** کنید.
3. وضعیت Privacy Mode از Telegram Bot API قابل تشخیص مستقیم نیست؛ برنامه ادعا نمی‌کند آن را تشخیص داده است.
4. منوی فرمان‌های خصوصی و گروهی هنگام راه‌اندازی پاک می‌شود و استفاده عادی دکمه‌محور است.

## حداقل دسترسی مدیر برای بات جهان

در اطلاعات گروه، بخش «مدیران»، بات جهان را مدیر کنید و فقط **حذف پیام‌ها** را فعال کنید. این مجوز برای پاک‌کردن ورودی‌های مرحله‌ای ساخت کشور لازم است. ویرایش پیام‌های خود بات مجوز جداگانه نمی‌خواهد و شهروندی داخل بازی ثبت می‌شود؛ بنابراین افزودن مدیر، تغییر اطلاعات گروه و سایر مجوزهای خطرناک لازم نیست.

Telegram API پیوند قابل‌اتکایی برای بازکردن مستقیم صفحه ارتقای یک بات به مدیر نمی‌دهد؛ رابط به‌جای دکمه جعلی، همین مسیر کوتاه را نشان می‌دهد.

## بررسی پس از استقرار

- بات جهان را به گروه آزمایشی اضافه کنید؛ پیام خوش‌آمد باید بدون فرمان ارسال شود.
- پیش از مدیرشدن، فقط راهنما، بررسی دسترسی و سلامت فعال است.
- پس از اعطای مجوز، «بررسی دوباره دسترسی» باید فوراً خانه جهان را باز کند.
- با گرفتن مجوز حذف پیام، عملیات تغییردهنده باید دوباره قفل شود و داده کشور باقی بماند.
- آزمون کامل: `pytest -q`. آزمون PostgreSQL را با نشانی پایگاه‌داده آزمایشی اجرا کنید؛ هرگز روی پایگاه‌داده تولید اجرا نکنید.
```

### `docs\FOR_AI_AGENTS.md`

```markdown
# Handover guide — read before writing any code

You are continuing an existing project. Follow the plan; do not restart it.

## Read first, in this order
1. `TeleLife_Master_Plan.md` — product definition, stack, phase map
2. `docs/PHASE_1.md` and `docs/PHASE_2.md` — what already exists
3. `docs/CONVENTIONS.md` — non-negotiable rules

## Hard rules from the project owner
- Never remove an existing requirement without asking.
- Never redesign the architecture without asking.
- Never add a major feature without asking.
- Never overengineer. Simpler beats clever.
- If you have a better idea, present it in exactly this format and WAIT for approval:
  current solution / suggested solution / advantages / disadvantages /
  performance impact / scalability impact / security impact / approval required.

## Priority order for trade-offs
Optimization > Scalability > Security > Economy balance > Performance >
Maintainability > UX > Clean architecture.

## Where things go
```

### `docs\PHASE_1.md`

```markdown
# Phase 1 — Core Skeleton (DELIVERED)

**Status:** complete and runnable
**Scope discipline:** everything listed below works. Nothing beyond it exists yet, by design.

## What Phase 1 delivers

| Area | Delivered |
|---|---|
| Settings | env-driven, validated by pydantic-settings, Supabase-pooler safe |
| Logging | structured JSON, one line per event, noisy libraries muted |
| Database | asyncpg pool, jsonb codec, transaction helper, healthcheck |
| Migrations | forward-only SQL runner with checksum tamper detection |
| Schema | players, groups, group_members, ledger, cooldowns, audit_log |
| Game config | YAML-driven, dotted access, zero hardcoded game numbers |
| Bot runtime | shared bootstrap; polling AND webhook from one code path |
| TeleLife | /start, /profile, /help |
| TeleWorld | /status, /help, group + member sync |
| Scheduler | independent worker, cooldown cleanup, graceful shutdown |
| Admin | HTTP Basic auth, dark dashboard, HTMX live refresh, /healthz |
| Deploy | one Dockerfile, four Render services via the SERVICE env var |
| Tests | config, formatting, progression curve, migration runner |

## Running locally
```

### `docs\PHASE_2.md`

```markdown
# Phase 2 — Identity & Progression (DELIVERED)

**Status:** complete, tested, runnable
**New in this phase:** the glass button system (Bot API 9.4 styles)

---

## 1. Glass buttons — what Telegram actually shipped

Bot API **9.4** (9 Feb 2026) added `style` to `InlineKeyboardButton` and
`KeyboardButton`. Supported in python-telegram-bot **22.7+**.

| Value | Colour | Our rule |
|---|---|---|
| *(omitted)* | translucent glass | **default for everything** |
| `primary` | blue | the one action we want tapped — **max one per keyboard** |
| `success` | green | a reward is waiting to be collected |
| `danger` | red | destructive / irreversible only |

`icon_custom_emoji_id` is also available for custom emoji on buttons.

### Colour policy (enforced in code, not by discipline)

`Keyboard.build()` **raises** if a keyboard contains more than one `primary`
button. Colour everywhere means colour nowhere; if every button shouts, the
player's eye has nothing to follow.

Colour is emphasis, never meaning. Old clients silently ignore `style`, so
every layout must read perfectly with zero colour. Button text always stands
on its own.
```

### `docs\PHASE_3.md`

```markdown
# Phase 3 — Economy Core (DELIVERED)

**Status:** complete implementation

Wallet, two-leg savings transfers, append-only ledger, level-gated lazy-production jobs, capped storage, checkpoint-before-upgrade, housing purchase/rent and daily living costs are implemented. User operations are exposed through owned glass-button panels rather than slash commands.
```

### `docs\PHASE_4.md`

```markdown
# Phase 4 — USD Market (DELIVERED)

**Status:** complete implementation

The market includes bounded supply/demand impact, buy/sell spread, fees, per-player daily limits, daily price bands, emergency freeze, health and volume indicators, minute stabilization, daily rollover, snapshots and atomic two-leg IRT/USD ledger entries.
```

### `docs\PHASE_5.md`

```markdown
# Phase 5 — Country and Group Layer

**Status:** integrated implementation

## Delivered
Countries/citizenship, shared economic ledger, five resources, seven lazy-production jobs, proportional collection XP, checkpoint-before-upgrade, country missions and effects, elections, secret one-vote ballots, presidential permissions, one-time national storage project, anti-spam polls, transactional news outbox, deterministic daily events, scheduler resolution, and audited admin operations.

## Security invariants
- Telegram numeric IDs are identity; group-admin API is used only for country registration.
- Every asset mutation is transactional and receives a unique ledger key.
- Collection XP is proportional and suppressed below the configured minimum fraction.
- Upgrade locks and checkpoints the old rate/capacity before changing level.
- Vote, contribution, reward, scheduler, outbox, and daily-event retries are idempotent.
- Admin audit and ledger are append-only.

## Issues found/fixed
| Issue | Fix |
|---|---|
| Fine-grained collection XP farming | Proportional XP plus minimum fraction |
| Retroactive upgrade production | Locked checkpoint before level update |
| Missions appearing only on view | Instantiation during eligible action |
| Duplicate votes/contributions | Database uniqueness and idempotency keys |
| Competing schedulers | `FOR UPDATE SKIP LOCKED` plus outbox leases |
| Untracked privileged changes | Append-only admin audit log |

## Metrics
- Eight Phase 5 YAML config files
- Schema migration remains below 400 lines
- Repository/service files remain below 400 lines
- Seven job definitions and five national resources
```

### `MANIFEST.sha256`

_[این فایل باینری/غیرمتنی تشخیص داده شد و محتوایش درج نشد]_


### `migrations\0001_core_schema.sql`

```sql
-- ============================================================
-- TeleLife / TeleWorld  |  Phase 1 core schema
-- Money is BIGINT minor units. NEVER float.
-- ============================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ---------- players : one identity across both bots ----------
CREATE TABLE IF NOT EXISTS players (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    telegram_id     BIGINT      NOT NULL UNIQUE,
    username        TEXT,
    first_name      TEXT        NOT NULL DEFAULT '',
    language_code   TEXT        NOT NULL DEFAULT 'fa',

    level           INTEGER     NOT NULL DEFAULT 1  CHECK (level >= 1),
    xp              BIGINT      NOT NULL DEFAULT 0  CHECK (xp >= 0),
    reputation      INTEGER     NOT NULL DEFAULT 0,
    happiness       SMALLINT    NOT NULL DEFAULT 70 CHECK (happiness BETWEEN 0 AND 100),
    prestige        SMALLINT    NOT NULL DEFAULT 0  CHECK (prestige >= 0),

    wallet_toman    BIGINT      NOT NULL DEFAULT 0  CHECK (wallet_toman >= 0),
    savings_toman   BIGINT      NOT NULL DEFAULT 0  CHECK (savings_toman >= 0),
    usd_cents       BIGINT      NOT NULL DEFAULT 0  CHECK (usd_cents >= 0),

    is_banned       BOOLEAN     NOT NULL DEFAULT FALSE,
    is_frozen       BOOLEAN     NOT NULL DEFAULT FALSE,
    ban_reason      TEXT,

    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_players_last_seen  ON players (last_seen_at DESC);
CREATE INDEX IF NOT EXISTS idx_players_level_xp   ON players (level DESC, xp DESC);
CREATE INDEX IF NOT EXISTS idx_players_wealth     ON players ((wallet_toman + savings_toman) DESC);
CREATE INDEX IF NOT EXISTS idx_players_active     ON players (id) WHERE NOT is_banned AND NOT is_frozen;

-- ---------- groups : TeleWorld territories ----------
CREATE TABLE IF NOT EXISTS groups (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    telegram_id     BIGINT      NOT NULL UNIQUE,
    title           TEXT        NOT NULL DEFAULT '',
    is_active       BOOLEAN     NOT NULL DEFAULT TRUE,
    member_count    INTEGER     NOT NULL DEFAULT 0,
    settings        JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_active_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_groups_active ON groups (last_active_at DESC) WHERE is_active;

-- ---------- group_members ----------
CREATE TABLE IF NOT EXISTS group_members (
    group_id        BIGINT      NOT NULL REFERENCES groups(id)  ON DELETE CASCADE,
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    joined_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_active_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (group_id, player_id)
);

CREATE INDEX IF NOT EXISTS idx_group_members_player ON group_members (player_id);

-- ---------- ledger : the ONLY source of truth for money movement ----------
CREATE TABLE IF NOT EXISTS ledger (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    idempotency_key TEXT        NOT NULL,
    reason          TEXT        NOT NULL,
    currency        TEXT        NOT NULL CHECK (currency IN ('IRT','USD')),
    account         TEXT        NOT NULL CHECK (account IN ('wallet','savings','usd')),
    amount          BIGINT      NOT NULL,
    balance_after   BIGINT      NOT NULL,
    metadata        JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- The single most important constraint in the project:
-- it makes double-clicks, Telegram retries and races economically harmless.
CREATE UNIQUE INDEX IF NOT EXISTS uq_ledger_idempotency ON ledger (idempotency_key);
CREATE INDEX IF NOT EXISTS idx_ledger_player_time ON ledger (player_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ledger_reason_time ON ledger (reason, created_at DESC);

-- ---------- cooldowns ----------
CREATE TABLE IF NOT EXISTS cooldowns (
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    action          TEXT        NOT NULL,
    expires_at      TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (player_id, action)
);

CREATE INDEX IF NOT EXISTS idx_cooldowns_expiry ON cooldowns (expires_at);

-- ---------- audit_log ----------
CREATE TABLE IF NOT EXISTS audit_log (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    actor       TEXT        NOT NULL,
    action      TEXT        NOT NULL,
    target_id   BIGINT,
    payload     JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_audit_time ON audit_log (created_at DESC);

-- ---------- updated_at trigger ----------
CREATE OR REPLACE FUNCTION touch_updated_at() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_players_touch ON players;
CREATE TRIGGER trg_players_touch
    BEFORE UPDATE ON players
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();
```

### `migrations\0002_progression.sql`

```sql
-- ============================================================
-- Phase 2 | Identity & Progression
-- Daily rewards, streaks, missions, unlocks, XP events.
-- ============================================================

-- ---------- daily claim state (one row per player) ----------
CREATE TABLE IF NOT EXISTS daily_state (
    player_id        BIGINT      PRIMARY KEY REFERENCES players(id) ON DELETE CASCADE,
    streak           INTEGER     NOT NULL DEFAULT 0 CHECK (streak >= 0),
    best_streak      INTEGER     NOT NULL DEFAULT 0 CHECK (best_streak >= 0),
    last_claim_date  DATE,
    total_claims     INTEGER     NOT NULL DEFAULT 0 CHECK (total_claims >= 0),
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- daily missions ----------
-- One row per player per mission per day. The PK makes progress writes
-- idempotent and lets the daily reset be a single ranged DELETE.
CREATE TABLE IF NOT EXISTS daily_missions (
    player_id     BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    mission_date  DATE        NOT NULL,
    mission_key   TEXT        NOT NULL,
    progress      INTEGER     NOT NULL DEFAULT 0 CHECK (progress >= 0),
    target        INTEGER     NOT NULL CHECK (target > 0),
    claimed_at    TIMESTAMPTZ,
    PRIMARY KEY (player_id, mission_date, mission_key)
);

CREATE INDEX IF NOT EXISTS idx_missions_date ON daily_missions (mission_date);
CREATE INDEX IF NOT EXISTS idx_missions_open
    ON daily_missions (player_id, mission_date)
    WHERE claimed_at IS NULL;

-- ---------- unlocks earned by the player ----------
CREATE TABLE IF NOT EXISTS player_unlocks (
    player_id    BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    unlock_key   TEXT        NOT NULL,
    unlocked_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (player_id, unlock_key)
);

-- ---------- xp audit trail ----------
-- Mirrors the ledger philosophy: XP is currency, so it gets the same
-- idempotency guarantee. This is what makes anti-farming enforceable.
CREATE TABLE IF NOT EXISTS xp_events (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id        BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    idempotency_key  TEXT        NOT NULL,
    source           TEXT        NOT NULL,
    amount           INTEGER     NOT NULL,
    level_after      INTEGER     NOT NULL,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_xp_idempotency ON xp_events (idempotency_key);
CREATE INDEX IF NOT EXISTS idx_xp_player_time ON xp_events (player_id, created_at DESC);

-- Daily XP ceiling per player is enforced by this covering index.
CREATE INDEX IF NOT EXISTS idx_xp_daily_cap
    ON xp_events (player_id, created_at) INCLUDE (amount);

DROP TRIGGER IF EXISTS trg_daily_state_touch ON daily_state;
CREATE TRIGGER trg_daily_state_touch
    BEFORE UPDATE ON daily_state
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();
```

### `migrations\0003_country_layer.sql`

```sql
-- ============================================================
-- TeleLife / TeleWorld | Phase 5 country and group layer schema
-- Forward-only. Existing identities, balances, and ledger rows are preserved.
-- Game balance values and durations belong in YAML, not in this migration.
-- ============================================================

-- ---------- extend the shared ledger ----------
-- The Phase 1 ledger only supported player IRT/USD accounts. Phase 5 keeps
-- that table as the single economic journal and expands its ownership/assets.
ALTER TABLE ledger
    ADD COLUMN IF NOT EXISTS country_id BIGINT,
    ADD COLUMN IF NOT EXISTS asset_code TEXT;

UPDATE ledger
SET asset_code = currency
WHERE asset_code IS NULL;

-- Keep legacy Phase 1/2 writers compatible during the expansion window.
-- A trigger copies currency into asset_code when an older writer omits it.
CREATE OR REPLACE FUNCTION ledger_fill_asset_code() RETURNS TRIGGER AS $$
BEGIN
    NEW.asset_code := COALESCE(NEW.asset_code, NEW.currency);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_ledger_fill_asset_code ON ledger;
CREATE TRIGGER trg_ledger_fill_asset_code
    BEFORE INSERT ON ledger
    FOR EACH ROW EXECUTE FUNCTION ledger_fill_asset_code();

ALTER TABLE ledger
    ALTER COLUMN asset_code SET NOT NULL,
    ALTER COLUMN player_id DROP NOT NULL,
    ALTER COLUMN currency DROP NOT NULL;

ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_currency_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_account_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_owner_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_balance_after_check;

ALTER TABLE ledger
    ADD CONSTRAINT ledger_owner_check CHECK (
        (player_id IS NOT NULL AND country_id IS NULL)
        OR (player_id IS NULL AND country_id IS NOT NULL)
    ),
    ADD CONSTRAINT ledger_balance_after_check CHECK (balance_after >= 0),
    ADD CONSTRAINT ledger_asset_code_check CHECK (length(asset_code) BETWEEN 1 AND 64),
    ADD CONSTRAINT ledger_account_check CHECK (length(account) BETWEEN 1 AND 64);

CREATE INDEX IF NOT EXISTS idx_ledger_country_time
    ON ledger (country_id, created_at DESC)
    WHERE country_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_ledger_asset_time
    ON ledger (asset_code, created_at DESC);

COMMENT ON TABLE ledger IS
    'Append-only source of truth for every player and country asset mutation.';
COMMENT ON COLUMN ledger.idempotency_key IS
    'Unique mutation-leg key; multi-leg operations use deterministic leg suffixes.';

-- ---------- countries and citizenship ----------
CREATE TABLE IF NOT EXISTS countries (
    id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    group_id            BIGINT NOT NULL UNIQUE REFERENCES groups(id) ON DELETE RESTRICT,
    name                TEXT NOT NULL UNIQUE,
    government_type     TEXT NOT NULL,
    description         TEXT NOT NULL,
    flag_file_id        TEXT,
    flag_file_unique_id TEXT,
    protection_until    TIMESTAMPTZ NOT NULL,
    president_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
    treasury_toman      BIGINT NOT NULL DEFAULT 0 CHECK (treasury_toman >= 0),
    daily_income_toman  BIGINT NOT NULL DEFAULT 0 CHECK (daily_income_toman >= 0),
    daily_expense_toman BIGINT NOT NULL DEFAULT 0 CHECK (daily_expense_toman >= 0),
    created_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(name) BETWEEN 1 AND 80),
    CHECK (length(government_type) BETWEEN 1 AND 32),
    CHECK (length(description) BETWEEN 1 AND 500)
);

ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_country_id_fkey;
ALTER TABLE ledger
    ADD CONSTRAINT ledger_country_id_fkey
    FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE RESTRICT;

CREATE INDEX IF NOT EXISTS idx_countries_protection
    ON countries (protection_until);
CREATE INDEX IF NOT EXISTS idx_countries_president
    ON countries (president_player_id)
    WHERE president_player_id IS NOT NULL;

CREATE TABLE IF NOT EXISTS citizenships (
    player_id  BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    joined_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_citizenships_country
    ON citizenships (country_id, joined_at);

CREATE TABLE IF NOT EXISTS country_resources (
    country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    asset_code TEXT NOT NULL,
    quantity   BIGINT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (country_id, asset_code),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

-- ---------- player resources and lazy production ----------
CREATE TABLE IF NOT EXISTS player_resources (
    player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    asset_code TEXT NOT NULL,
    quantity   BIGINT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (player_id, asset_code),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS player_jobs (
    player_id             BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    job_code              TEXT NOT NULL,
    output_asset_code     TEXT NOT NULL,
    production_level      INTEGER NOT NULL DEFAULT 1 CHECK (production_level > 0),
    storage_level         INTEGER NOT NULL DEFAULT 1 CHECK (storage_level > 0),
    stored_amount         BIGINT NOT NULL DEFAULT 0 CHECK (stored_amount >= 0),
    production_updated_at TIMESTAMPTZ NOT NULL,
    selected_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at            TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(job_code) BETWEEN 1 AND 32),
    CHECK (length(output_asset_code) BETWEEN 1 AND 64)
);

CREATE INDEX IF NOT EXISTS idx_player_jobs_checkpoint
    ON player_jobs (production_updated_at);

-- ---------- elections ----------
CREATE TABLE IF NOT EXISTS elections (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id         BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    started_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    status             TEXT NOT NULL,
    nominations_end_at TIMESTAMPTZ NOT NULL,
    voting_end_at      TIMESTAMPTZ NOT NULL,
    winner_player_id   BIGINT REFERENCES players(id) ON DELETE SET NULL,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at        TIMESTAMPTZ,
    CHECK (status IN ('nominations', 'voting', 'completed', 'cancelled')),
    CHECK (voting_end_at > nominations_end_at)
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_elections_country_open
    ON elections (country_id)
    WHERE status IN ('nominations', 'voting');
CREATE INDEX IF NOT EXISTS idx_elections_due
    ON elections (status, nominations_end_at, voting_end_at);

CREATE TABLE IF NOT EXISTS election_candidates (
    election_id BIGINT NOT NULL REFERENCES elections(id) ON DELETE RESTRICT,
    player_id   BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    message_chat_id BIGINT,
    message_id  BIGINT,
    nominated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (election_id, player_id)
);

CREATE TABLE IF NOT EXISTS election_votes (
    election_id        BIGINT NOT NULL REFERENCES elections(id) ON DELETE RESTRICT,
    voter_player_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    candidate_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    voted_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (election_id, voter_player_id),
    FOREIGN KEY (election_id, candidate_player_id)
        REFERENCES election_candidates(election_id, player_id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_election_votes_tally
    ON election_votes (election_id, candidate_player_id);

-- ---------- national projects ----------
CREATE TABLE IF NOT EXISTS national_projects (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id           BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    project_key          TEXT NOT NULL,
    started_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    status               TEXT NOT NULL DEFAULT 'active',
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at         TIMESTAMPTZ,
    UNIQUE (country_id, project_key),
    CHECK (status IN ('active', 'completed', 'cancelled')),
    CHECK (length(project_key) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS project_requirements (
    project_id         BIGINT NOT NULL REFERENCES national_projects(id) ON DELETE RESTRICT,
    asset_code         TEXT NOT NULL,
    required_amount    BIGINT NOT NULL CHECK (required_amount > 0),
    contributed_amount BIGINT NOT NULL DEFAULT 0 CHECK (contributed_amount >= 0),
    PRIMARY KEY (project_id, asset_code)
);

CREATE TABLE IF NOT EXISTS project_contributions (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id      BIGINT NOT NULL REFERENCES national_projects(id) ON DELETE RESTRICT,
    player_id       BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    asset_code      TEXT NOT NULL,
    amount          BIGINT NOT NULL CHECK (amount > 0),
    idempotency_key TEXT NOT NULL UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_project_contributions_project
    ON project_contributions (project_id, created_at DESC);

-- ---------- country polls ----------
CREATE TABLE IF NOT EXISTS polls (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id         BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    creator_player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    question           TEXT NOT NULL,
    status             TEXT NOT NULL DEFAULT 'active',
    closes_at          TIMESTAMPTZ NOT NULL,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at        TIMESTAMPTZ,
    CHECK (status IN ('active', 'completed', 'cancelled')),
    CHECK (length(question) BETWEEN 1 AND 200)
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_polls_creator_active
    ON polls (creator_player_id)
    WHERE status = 'active';
CREATE INDEX IF NOT EXISTS idx_polls_due
    ON polls (status, closes_at);

CREATE TABLE IF NOT EXISTS poll_options (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    poll_id     BIGINT NOT NULL REFERENCES polls(id) ON DELETE RESTRICT,
    option_text TEXT NOT NULL,
    UNIQUE (poll_id, id),
    UNIQUE (poll_id, option_text),
    CHECK (length(option_text) BETWEEN 1 AND 100)
);

CREATE TABLE IF NOT EXISTS poll_votes (
    poll_id         BIGINT NOT NULL REFERENCES polls(id) ON DELETE RESTRICT,
    voter_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    option_id       BIGINT NOT NULL,
    voted_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (poll_id, voter_player_id),
    FOREIGN KEY (poll_id, option_id)
        REFERENCES poll_options(poll_id, id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_poll_votes_tally
    ON poll_votes (poll_id, option_id);

-- ---------- country missions and effects ----------
CREATE TABLE IF NOT EXISTS country_missions (
    country_id        BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    mission_date      DATE NOT NULL,
    mission_key       TEXT NOT NULL,
    metric_key        TEXT NOT NULL,
    target_amount     BIGINT NOT NULL CHECK (target_amount > 0),
    progress_amount   BIGINT NOT NULL DEFAULT 0 CHECK (progress_amount >= 0),
    reward_asset_code TEXT NOT NULL,
    reward_amount     BIGINT NOT NULL CHECK (reward_amount > 0),
    completed_at      TIMESTAMPTZ,
    rewarded_at       TIMESTAMPTZ,
    PRIMARY KEY (country_id, mission_date, mission_key)
);

CREATE INDEX IF NOT EXISTS idx_country_missions_open
    ON country_missions (country_id, mission_date)
    WHERE completed_at IS NULL;

CREATE TABLE IF NOT EXISTS country_effects (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id  BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    effect_code TEXT NOT NULL,
    magnitude   BIGINT NOT NULL,
    starts_at   TIMESTAMPTZ NOT NULL,
    ends_at     TIMESTAMPTZ NOT NULL,
    source_type TEXT NOT NULL,
    source_key  TEXT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (country_id, source_type, source_key, effect_code),
    CHECK (ends_at > starts_at)
);

CREATE INDEX IF NOT EXISTS idx_country_effects_active
    ON country_effects (country_id, effect_code, ends_at);

-- ---------- daily economy and events ----------
CREATE TABLE IF NOT EXISTS country_economy_daily (
    country_id       BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    economy_date     DATE NOT NULL,
    income_toman     BIGINT NOT NULL DEFAULT 0 CHECK (income_toman >= 0),
    expense_toman    BIGINT NOT NULL DEFAULT 0 CHECK (expense_toman >= 0),
    closing_treasury BIGINT NOT NULL CHECK (closing_treasury >= 0),
    ledger_key       TEXT NOT NULL UNIQUE,
    processed_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (country_id, economy_date)
);

CREATE TABLE IF NOT EXISTS daily_events (
    event_date      DATE PRIMARY KEY,
    event_code      TEXT NOT NULL,
    effect_payload  JSONB NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    announced_at    TIMESTAMPTZ,
    CHECK (jsonb_typeof(effect_payload) = 'object')
);

-- ---------- transactional news outbox ----------
CREATE TABLE IF NOT EXISTS news_outbox (
    id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    idempotency_key   TEXT NOT NULL UNIQUE,
    event_type        TEXT NOT NULL,
    destination_chat_id BIGINT,
    payload           JSONB NOT NULL,
    attempts          INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    available_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    processing_token  UUID,
    processing_until  TIMESTAMPTZ,
    published_at      TIMESTAMPTZ,
    last_error_code   TEXT,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (jsonb_typeof(payload) = 'object')
);

CREATE INDEX IF NOT EXISTS idx_news_outbox_claim
    ON news_outbox (available_at, created_at)
    WHERE published_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_news_outbox_lease
    ON news_outbox (processing_until)
    WHERE published_at IS NULL AND processing_token IS NOT NULL;

-- ---------- global feature flags and privileged audit ----------
CREATE TABLE IF NOT EXISTS feature_flags (
    key           TEXT PRIMARY KEY,
    enabled       BOOLEAN NOT NULL DEFAULT FALSE,
    updated_by    TEXT NOT NULL,
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(key) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS admin_audit_log (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    admin_actor        TEXT NOT NULL,
    action             TEXT NOT NULL,
    target_player_id   BIGINT REFERENCES players(id) ON DELETE RESTRICT,
    target_country_id  BIGINT REFERENCES countries(id) ON DELETE RESTRICT,
    request_id         TEXT NOT NULL UNIQUE,
    details            JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (jsonb_typeof(details) = 'object')
);

CREATE INDEX IF NOT EXISTS idx_admin_audit_time
    ON admin_audit_log (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_admin_audit_action_time
    ON admin_audit_log (action, created_at DESC);

-- ---------- append-only database guards ----------
CREATE OR REPLACE FUNCTION reject_append_only_mutation() RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'append-only table cannot be updated or deleted';
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_ledger_append_only ON ledger;
CREATE TRIGGER trg_ledger_append_only
    BEFORE UPDATE OR DELETE ON ledger
    FOR EACH ROW EXECUTE FUNCTION reject_append_only_mutation();

DROP TRIGGER IF EXISTS trg_admin_audit_append_only ON admin_audit_log;
CREATE TRIGGER trg_admin_audit_append_only
    BEFORE UPDATE OR DELETE ON admin_audit_log
    FOR EACH ROW EXECUTE FUNCTION reject_append_only_mutation();

DROP TRIGGER IF EXISTS trg_countries_touch ON countries;
CREATE TRIGGER trg_countries_touch
    BEFORE UPDATE ON countries
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();

DROP TRIGGER IF EXISTS trg_player_jobs_touch ON player_jobs;
CREATE TRIGGER trg_player_jobs_touch
    BEFORE UPDATE ON player_jobs
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();
```

### `migrations\0004_admin_command_center.sql`

```sql
-- Admin command center: authoritative market board and historical snapshots.
CREATE TABLE IF NOT EXISTS market_prices (
    asset_code          TEXT PRIMARY KEY,
    title_fa            TEXT NOT NULL,
    current_price_toman BIGINT NOT NULL CHECK (current_price_toman > 0),
    updated_by          TEXT NOT NULL DEFAULT 'system',
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS market_price_snapshots (
    asset_code  TEXT NOT NULL REFERENCES market_prices(asset_code) ON DELETE RESTRICT,
    price_toman BIGINT NOT NULL CHECK (price_toman > 0),
    captured_at TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (asset_code, captured_at)
);

CREATE INDEX IF NOT EXISTS idx_market_snapshots_time
    ON market_price_snapshots (captured_at DESC, asset_code);

INSERT INTO market_prices (asset_code, title_fa, current_price_toman)
VALUES
    ('USD', 'دلار', 85000),
    ('oil', 'نفت', 720000),
    ('food', 'غذا', 85000),
    ('minerals', 'مواد معدنی', 310000),
    ('energy', 'انرژی', 190000),
    ('technology', 'فناوری', 950000)
ON CONFLICT (asset_code) DO NOTHING;

INSERT INTO market_price_snapshots (asset_code, price_toman, captured_at)
SELECT asset_code, current_price_toman, date_trunc('minute', now())
FROM market_prices
ON CONFLICT DO NOTHING;
```

### `migrations\0005_life_world_hardening.sql`

```sql
-- TeleLife/TeleWorld hardening: country lifecycle, membership validity and election safety.
ALTER TABLE countries ADD COLUMN IF NOT EXISTS status TEXT;
ALTER TABLE countries ADD COLUMN IF NOT EXISTS temporary_at TIMESTAMPTZ;
ALTER TABLE countries ADD COLUMN IF NOT EXISTS official_at TIMESTAMPTZ;
UPDATE countries SET status = 'temporary', temporary_at = COALESCE(temporary_at, created_at)
WHERE status IS NULL;
ALTER TABLE countries ALTER COLUMN status SET DEFAULT 'forming';
ALTER TABLE countries ALTER COLUMN status SET NOT NULL;
ALTER TABLE countries DROP CONSTRAINT IF EXISTS countries_status_check;
ALTER TABLE countries ADD CONSTRAINT countries_status_check
    CHECK (status IN ('forming','temporary','official'));

ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS left_at TIMESTAMPTZ;
CREATE INDEX IF NOT EXISTS idx_citizenships_active_country
    ON citizenships(country_id, joined_at) WHERE is_active;

-- Existing primary-key semantics retain one-country-per-player. Only active rows count.
CREATE UNIQUE INDEX IF NOT EXISTS uq_elections_one_open_country
    ON elections(country_id) WHERE status IN ('nominations','voting');

-- A president must be an active citizen of the country. The trigger protects admin
-- tools and future writers in addition to the service layer.
CREATE OR REPLACE FUNCTION validate_country_president() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.president_player_id IS NOT NULL AND NOT EXISTS (
        SELECT 1 FROM citizenships cs
        WHERE cs.player_id = NEW.president_player_id
          AND cs.country_id = NEW.id AND cs.is_active
    ) THEN
        RAISE EXCEPTION 'president_must_be_active_citizen';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS trg_validate_country_president ON countries;
CREATE CONSTRAINT TRIGGER trg_validate_country_president
    AFTER INSERT OR UPDATE OF president_player_id ON countries
    DEFERRABLE INITIALLY DEFERRED
    FOR EACH ROW EXECUTE FUNCTION validate_country_president();
```

### `migrations\0006_phase3_phase4_complete.sql`

```sql
-- Phase 3: personal economy, housing and living costs.
CREATE TABLE IF NOT EXISTS player_housing (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    housing_code TEXT NOT NULL,
    tenure TEXT NOT NULL CHECK (tenure IN ('rent','owned')),
    rent_paid_until DATE,
    purchased_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(housing_code) BETWEEN 1 AND 32)
);

CREATE TABLE IF NOT EXISTS player_life_economy (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    last_living_charge_date DATE,
    total_living_paid BIGINT NOT NULL DEFAULT 0 CHECK (total_living_paid >= 0),
    missed_living_days INTEGER NOT NULL DEFAULT 0 CHECK (missed_living_days >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Phase 4: auditable USD market state and per-player daily limits.
CREATE TABLE IF NOT EXISTS usd_market_state (
    singleton BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (singleton),
    reference_price_toman BIGINT NOT NULL CHECK (reference_price_toman > 0),
    open_price_toman BIGINT NOT NULL CHECK (open_price_toman > 0),
    net_flow_cents BIGINT NOT NULL DEFAULT 0,
    volume_cents BIGINT NOT NULL DEFAULT 0 CHECK (volume_cents >= 0),
    health SMALLINT NOT NULL DEFAULT 100 CHECK (health BETWEEN 0 AND 100),
    market_date DATE NOT NULL DEFAULT current_date,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO usd_market_state(singleton,reference_price_toman,open_price_toman)
SELECT TRUE,current_price_toman,current_price_toman FROM market_prices WHERE asset_code='USD'
ON CONFLICT(singleton) DO NOTHING;

CREATE TABLE IF NOT EXISTS usd_trades (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    idempotency_key TEXT NOT NULL UNIQUE,
    side TEXT NOT NULL CHECK (side IN ('buy','sell')),
    usd_cents BIGINT NOT NULL CHECK (usd_cents > 0),
    gross_toman BIGINT NOT NULL CHECK (gross_toman > 0),
    fee_toman BIGINT NOT NULL CHECK (fee_toman >= 0),
    price_toman BIGINT NOT NULL CHECK (price_toman > 0),
    price_after_toman BIGINT NOT NULL CHECK (price_after_toman > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_usd_trades_player_time ON usd_trades(player_id,created_at DESC);
CREATE INDEX IF NOT EXISTS idx_usd_trades_time ON usd_trades(created_at DESC);

CREATE TABLE IF NOT EXISTS usd_daily_limits (
    player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    trade_date DATE NOT NULL,
    bought_cents BIGINT NOT NULL DEFAULT 0 CHECK (bought_cents >= 0),
    sold_cents BIGINT NOT NULL DEFAULT 0 CHECK (sold_cents >= 0),
    PRIMARY KEY(player_id,trade_date)
);

INSERT INTO feature_flags(key,enabled,updated_by)
VALUES ('usd_market_frozen',FALSE,'migration-0006') ON CONFLICT(key) DO NOTHING;
```

### `migrations\0007_unified_ui_onboarding.sql`

```sql
-- Persistent single-panel navigation and an actionable new-player journey.
CREATE TABLE IF NOT EXISTS player_ui_state (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE CASCADE,
    life_chat_id BIGINT,
    life_message_id BIGINT,
    onboarding_step SMALLINT NOT NULL DEFAULT 0 CHECK (onboarding_step BETWEEN 0 AND 4),
    onboarding_completed_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS world_ui_state (
    chat_id BIGINT PRIMARY KEY,
    message_id BIGINT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

### `migrations\0008_world_access_lifecycle.sql`

```sql
-- TeleWorld group lifecycle, permission gate and deduplicated product audit.
CREATE TABLE IF NOT EXISTS world_group_access (
    chat_id BIGINT PRIMARY KEY,
    chat_title TEXT NOT NULL DEFAULT '',
    membership_status TEXT NOT NULL DEFAULT 'unknown',
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    welcomed_at TIMESTAMPTZ,
    welcome_message_id BIGINT,
    status_message_id BIGINT,
    is_administrator BOOLEAN NOT NULL DEFAULT FALSE,
    can_delete_messages BOOLEAN NOT NULL DEFAULT FALSE,
    missing_permissions TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
    last_checked_at TIMESTAMPTZ,
    last_warning_at TIMESTAMPTZ,
    last_warning_fingerprint TEXT,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_world_group_access_active
    ON world_group_access (is_active, updated_at DESC);

CREATE TABLE IF NOT EXISTS product_audit_log (
    id BIGSERIAL PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    event_type TEXT NOT NULL,
    chat_id BIGINT,
    player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
    country_id BIGINT REFERENCES countries(id) ON DELETE SET NULL,
    details JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_product_audit_time
    ON product_audit_log (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_product_audit_chat_time
    ON product_audit_log (chat_id, created_at DESC);
```

### `migrations\0009_ads_governance_moderation.sql`

```sql
-- Advertising campaigns and governance controls.
CREATE TABLE IF NOT EXISTS ad_campaigns (
 id BIGSERIAL PRIMARY KEY,
 title TEXT NOT NULL CHECK(length(title) BETWEEN 3 AND 120),
 body TEXT NOT NULL CHECK(length(body) BETWEEN 3 AND 4000),
 destination_chat_id BIGINT NOT NULL,
 status TEXT NOT NULL DEFAULT 'draft' CHECK(status IN ('draft','scheduled','queued','cancelled')),
 scheduled_at TIMESTAMPTZ,
 repeat_minutes INTEGER CHECK(repeat_minutes IS NULL OR repeat_minutes >= 15),
 last_queued_at TIMESTAMPTZ,
 created_by TEXT NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_ad_campaign_due ON ad_campaigns(status,scheduled_at) WHERE status='scheduled';
```

### `migrations\0010_stars_subscriptions_ad_marketplace.sql`

```sql
-- Telegram Stars subscriptions, collaborative funding, moderated ad marketplace.
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ad_free_until TIMESTAMPTZ;
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ads_delivered_today INTEGER NOT NULL DEFAULT 0;
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ads_delivery_day DATE;

CREATE TABLE IF NOT EXISTS subscription_rounds (
 id BIGSERIAL PRIMARY KEY, group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
 target_stars INTEGER NOT NULL DEFAULT 10 CHECK(target_stars=10), collected_stars INTEGER NOT NULL DEFAULT 0 CHECK(collected_stars BETWEEN 0 AND 10),
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','completed','expired','cancelled')),
 expires_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '7 days', completed_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_subscription_open_round ON subscription_rounds(group_id) WHERE status='open';
CREATE TABLE IF NOT EXISTS star_payments (
 id BIGSERIAL PRIMARY KEY, purpose TEXT NOT NULL CHECK(purpose IN ('subscription','advertisement')),
 reference_id BIGINT NOT NULL, payer_telegram_id BIGINT NOT NULL, stars INTEGER NOT NULL CHECK(stars>0),
 invoice_payload TEXT NOT NULL UNIQUE, telegram_charge_id TEXT UNIQUE, provider_charge_id TEXT,
 status TEXT NOT NULL DEFAULT 'invoiced' CHECK(status IN ('invoiced','paid','refunded','expired','cancelled')),
 expires_at TIMESTAMPTZ NOT NULL, paid_at TIMESTAMPTZ, refunded_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_star_payment_lookup ON star_payments(invoice_payload,status);
CREATE TABLE IF NOT EXISTS group_subscription_events (
 id BIGSERIAL PRIMARY KEY, group_id BIGINT NOT NULL REFERENCES groups(id), source TEXT NOT NULL CHECK(source IN ('stars','treasury','admin')),
 stars INTEGER, treasury_toman BIGINT, starts_at TIMESTAMPTZ NOT NULL, ends_at TIMESTAMPTZ NOT NULL,
 actor_player_id BIGINT REFERENCES players(id), created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ad_requests (
 id BIGSERIAL PRIMARY KEY, requester_player_id BIGINT NOT NULL REFERENCES players(id),
 package_code TEXT NOT NULL CHECK(package_code IN ('economy','standard','campaign','featured')),
 title TEXT NOT NULL CHECK(length(title) BETWEEN 3 AND 120), description TEXT NOT NULL CHECK(length(description) BETWEEN 10 AND 2000),
 target_url TEXT NOT NULL CHECK(length(target_url) BETWEEN 8 AND 1000), image_bytes BYTEA, image_mime TEXT,
 requested_start_at TIMESTAMPTZ, status TEXT NOT NULL DEFAULT 'pending_review' CHECK(status IN ('draft','pending_review','changes_requested','approved_unpaid','paid','active','paused','completed','rejected','cancelled','refunded','payment_expired')),
 price_stars INTEGER NOT NULL CHECK(price_stars IN (25,60,120,200)), impressions_planned INTEGER NOT NULL,
 campaign_hours INTEGER NOT NULL, priority INTEGER NOT NULL DEFAULT 0, admin_note TEXT, approved_by TEXT,
 approved_at TIMESTAMPTZ, payment_expires_at TIMESTAMPTZ, paid_at TIMESTAMPTZ, first_delivery_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_ad_requests_admin ON ad_requests(status,created_at DESC);
CREATE TABLE IF NOT EXISTS ad_deliveries (
 id BIGSERIAL PRIMARY KEY, ad_request_id BIGINT NOT NULL REFERENCES ad_requests(id) ON DELETE CASCADE,
 group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE, slot_no INTEGER NOT NULL,
 scheduled_at TIMESTAMPTZ NOT NULL, status TEXT NOT NULL DEFAULT 'scheduled' CHECK(status IN ('scheduled','queued','sent','failed','cancelled')),
 outbox_key TEXT UNIQUE, sent_at TIMESTAMPTZ, error_code TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(ad_request_id,group_id,slot_no)
);
CREATE INDEX IF NOT EXISTS idx_ad_delivery_due ON ad_deliveries(status,scheduled_at) WHERE status='scheduled';
```

### `migrations\0011_population_channels_migration.sql`

```sql
-- Population-priced subscriptions, channel-specific ads and controlled migration.
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_target_stars_check CHECK(target_stars IN (10,15,30,50,75));
ALTER TABLE ad_requests ADD COLUMN IF NOT EXISTS channel TEXT NOT NULL DEFAULT 'world' CHECK(channel IN ('life','world','both'));
ALTER TABLE ad_deliveries ADD COLUMN IF NOT EXISTS destination_type TEXT NOT NULL DEFAULT 'world' CHECK(destination_type IN ('life','world'));
ALTER TABLE ad_deliveries ADD COLUMN IF NOT EXISTS destination_telegram_id BIGINT;
ALTER TABLE ad_deliveries ALTER COLUMN group_id DROP NOT NULL;
ALTER TABLE ad_deliveries DROP CONSTRAINT IF EXISTS ad_deliveries_ad_request_id_group_id_slot_no_key;
CREATE UNIQUE INDEX IF NOT EXISTS uq_ad_delivery_destination ON ad_deliveries(ad_request_id,destination_type,destination_telegram_id,slot_no);
DROP INDEX IF EXISTS idx_ad_delivery_due;
CREATE INDEX IF NOT EXISTS idx_ad_delivery_due ON ad_deliveries(status,scheduled_at,destination_type) WHERE status='scheduled';

ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS migrant_until TIMESTAMPTZ;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS political_hold_until TIMESTAMPTZ;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS last_migrated_at TIMESTAMPTZ;
CREATE TABLE IF NOT EXISTS migration_requests (
 id BIGSERIAL PRIMARY KEY, player_id BIGINT NOT NULL REFERENCES players(id),
 origin_country_id BIGINT NOT NULL REFERENCES countries(id), destination_country_id BIGINT NOT NULL REFERENCES countries(id),
 exit_fee_toman BIGINT NOT NULL CHECK(exit_fee_toman BETWEEN 500000 AND 50000000),
 status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','approved','rejected','expired','cancelled')),
 reviewed_by_player_id BIGINT REFERENCES players(id), review_note TEXT,
 expires_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '72 hours', created_at TIMESTAMPTZ NOT NULL DEFAULT now(), resolved_at TIMESTAMPTZ,
 CHECK(origin_country_id<>destination_country_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_migration_pending ON migration_requests(player_id) WHERE status='pending';
CREATE INDEX IF NOT EXISTS idx_migration_destination_pending ON migration_requests(destination_country_id,expires_at) WHERE status='pending';
```

### `migrations\0012_reliability_live_market_engagement.sql`

```sql
-- Reliability, live market provenance, and group engagement. Additive and rollback-safe.
DO $$
DECLARE constraint_name text;
BEGIN
  SELECT c.conname INTO constraint_name
  FROM pg_constraint c
  WHERE c.conrelid='ad_requests'::regclass AND c.contype='c'
    AND pg_get_constraintdef(c.oid) ILIKE '%price_stars%';
  IF constraint_name IS NOT NULL THEN
    EXECUTE format('ALTER TABLE ad_requests DROP CONSTRAINT %I', constraint_name);
  END IF;
END $$;
ALTER TABLE ad_requests ADD CONSTRAINT ad_requests_price_stars_check
  CHECK (price_stars BETWEEN 1 AND 10000) NOT VALID;
ALTER TABLE ad_requests VALIDATE CONSTRAINT ad_requests_price_stars_check;


-- 0010 used a fixed 10-star round, while application pricing scales to 75 stars.
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_collected_stars_check;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_target_stars_check
  CHECK(target_stars BETWEEN 1 AND 1000) NOT VALID;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_collected_stars_check
  CHECK(collected_stars BETWEEN 0 AND target_stars) NOT VALID;
ALTER TABLE subscription_rounds VALIDATE CONSTRAINT subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds VALIDATE CONSTRAINT subscription_rounds_collected_stars_check;

ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source TEXT NOT NULL DEFAULT 'internal';
ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source_checked_at TIMESTAMPTZ;
ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source_error TEXT;

CREATE TABLE IF NOT EXISTS scheduler_job_runs (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 job_name TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN ('running','succeeded','failed')),
 started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 finished_at TIMESTAMPTZ,
 duration_ms INTEGER,
 result JSONB NOT NULL DEFAULT '{}'::jsonb,
 error_type TEXT,
 error_message TEXT
);
CREATE INDEX IF NOT EXISTS idx_scheduler_job_runs_name_time
 ON scheduler_job_runs(job_name,started_at DESC);

CREATE TABLE IF NOT EXISTS group_engagement_state (
 group_id BIGINT PRIMARY KEY REFERENCES groups(id) ON DELETE CASCADE,
 streak INTEGER NOT NULL DEFAULT 0 CHECK(streak>=0),
 best_streak INTEGER NOT NULL DEFAULT 0 CHECK(best_streak>=0),
 last_active_date DATE,
 last_digest_date DATE,
 last_event_at TIMESTAMPTZ,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS group_live_events (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
 event_code TEXT NOT NULL,
 title TEXT NOT NULL,
 payload JSONB NOT NULL DEFAULT '{}'::jsonb,
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','resolved','expired')),
 starts_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 ends_at TIMESTAMPTZ NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_group_open_event
 ON group_live_events(group_id) WHERE status='open';
```

### `migrations\0013_country_identity_candles_realism.sql`

```sql
-- Country identity, central-bank policy, macro indicators, shocks and national newspaper.
ALTER TABLE countries ADD COLUMN IF NOT EXISTS interest_rate_bp INTEGER NOT NULL DEFAULT 1200 CHECK(interest_rate_bp BETWEEN 0 AND 10000);
ALTER TABLE countries ADD COLUMN IF NOT EXISTS fx_reserve_cents BIGINT NOT NULL DEFAULT 0 CHECK(fx_reserve_cents>=0);
ALTER TABLE countries ADD COLUMN IF NOT EXISTS inflation_target_bp INTEGER NOT NULL DEFAULT 800 CHECK(inflation_target_bp BETWEEN 0 AND 5000);

CREATE TABLE IF NOT EXISTS country_indicator_daily (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 indicator_date DATE NOT NULL,
 inflation_bp INTEGER NOT NULL CHECK(inflation_bp BETWEEN -5000 AND 100000),
 unemployment_bp INTEGER NOT NULL CHECK(unemployment_bp BETWEEN 0 AND 10000),
 satisfaction INTEGER NOT NULL CHECK(satisfaction BETWEEN 0 AND 100),
 growth_bp INTEGER NOT NULL CHECK(growth_bp BETWEEN -10000 AND 10000),
 gdp_toman BIGINT NOT NULL CHECK(gdp_toman>=0),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,indicator_date)
);
CREATE TABLE IF NOT EXISTS country_shocks (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 shock_code TEXT NOT NULL CHECK(shock_code IN ('sanctions','drought','export_boom')),
 title TEXT NOT NULL,
 effects JSONB NOT NULL DEFAULT '{}'::jsonb,
 starts_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 ends_at TIMESTAMPTZ NOT NULL,
 announced_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(country_id,shock_code,starts_at)
);
CREATE INDEX IF NOT EXISTS idx_country_shocks_active ON country_shocks(country_id,ends_at) WHERE announced_at IS NOT NULL;
CREATE TABLE IF NOT EXISTS country_newspapers (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 issue_date DATE NOT NULL,
 headline TEXT NOT NULL,
 body TEXT NOT NULL,
 indicators JSONB NOT NULL DEFAULT '{}'::jsonb,
 shock_id BIGINT REFERENCES country_shocks(id) ON DELETE SET NULL,
 published_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,issue_date)
);
```

### `packages\__init__.py`

```python
"""Package packages."""
```

### `packages\core\__init__.py`

```python
"""Package packages.core."""
```

### `packages\core\bot\__init__.py`

```python
from packages.core.bot.errors import make_error_handler
from packages.core.bot.runtime import PollingService, build_application, run_bot

__all__ = ["PollingService", "build_application", "make_error_handler", "run_bot"]
```

### `packages\core\bot\errors.py`

```python
"""Global error handler - never let a traceback reach the player."""

from __future__ import annotations

import logging
from typing import Any

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


def make_error_handler(user_message: str) -> Any:
    async def handle(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.error("unhandled error", exc_info=context.error)
        if not isinstance(update, Update):
            return
        chat = update.effective_chat
        if chat is None:
            return
        try:
            await context.bot.send_message(chat.id, user_message)
        except Exception:
            logger.warning("failed to deliver error notice to chat %s", chat.id)

    return handle
```

### `packages\core\bot\runtime.py`

```python
"""Shared Telegram application construction and supervised polling lifecycle."""
from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable

from telegram.ext import AIORateLimiter, Application, ApplicationBuilder, Defaults

from packages.core.config import get_config
from packages.core.settings import Service, Settings, get_settings

from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging

logger = logging.getLogger(__name__)
RegisterFn = Callable[[Application], None]


def build_application(settings: Settings, service: Service) -> Application:
    cfg = get_config()
    defaults = Defaults(parse_mode="HTML", block=False)
    return (
        ApplicationBuilder()
        .token(settings.token_for(service))
        .defaults(defaults)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(cfg.int_("core.telegram.concurrent_updates"))
        .connect_timeout(cfg.float_("core.telegram.connect_timeout"))
        .read_timeout(cfg.float_("core.telegram.read_timeout"))
        .build()
    )


class PollingService:
    """Owns one Telegram Application without owning the process event loop."""

    def __init__(self, settings: Settings, service: Service, register: RegisterFn) -> None:
        self.application = build_application(settings, service)
        register(self.application)
        self.service = service

    def healthy(self) -> bool:
        updater = self.application.updater
        return bool(self.application.running and updater and updater.running)

    async def run(self, stop: asyncio.Event) -> None:
        app = self.application
        updater = app.updater
        if updater is None:
            raise RuntimeError(f"{self.service.value} updater is unavailable")
        try:
            await app.initialize()
            # The supervisor owns the lifecycle, so invoke the framework hook explicitly.
            # This clears legacy slash-command menus before polling starts.
            if app.post_init is not None:
                await app.post_init(app)
            await app.start()
            await updater.start_polling(
                drop_pending_updates=True,
                allowed_updates=["message", "callback_query", "my_chat_member"],
            )
            logger.info("%s polling started", self.service.value)
            await stop.wait()
        finally:
            if updater.running:
                await updater.stop()
            if app.running:
                await app.stop()
            await app.shutdown()
            logger.info("%s polling stopped", self.service.value)


def run_bot(service: Service, register: RegisterFn) -> None:
    """Backward-compatible standalone entrypoint; production uses the supervisor."""
    async def standalone() -> None:
        settings = get_settings()
        setup_logging(service.value, settings.log_level)
        await db.create_pool(settings)
        await migrate()
        stop = asyncio.Event()
        polling = PollingService(settings, service, register)
        try:
            await polling.run(stop)
        finally:
            await db.close_pool()
    asyncio.run(standalone())
```

### `packages\core\config\__init__.py`

```python
from packages.core.config.loader import ConfigError, GameConfig, get_config, reload_config

__all__ = ["ConfigError", "GameConfig", "get_config", "reload_config"]
```

### `packages\core\config\data\commerce.yaml`

```yaml
subscription:
  duration_days: 30
  stars_tiers: {20: 10, 100: 15, 500: 30, 1000: 50, overflow: 75}
  contribution_options: [1, 2, 5, 10, 25, 50]
  round_expiry_days: 7
  treasury_percent: 20
  treasury_min_toman: 20000000
  treasury_max_toman: 1000000000
  treasury_per_citizen_toman: 1000000
advertising:
  payment_expiry_hours: 48
  max_ads_per_group_per_day: 2
  active_group_days: 14
  packages:
    economy: {title: "اقتصادی", base_stars: 25, impressions: 1, hours: 1, priority: 0}
    standard: {title: "استاندارد", base_stars: 60, impressions: 3, hours: 24, priority: 1}
    campaign: {title: "کمپین", base_stars: 120, impressions: 6, hours: 72, priority: 2}
    featured: {title: "ویژه", base_stars: 200, impressions: 8, hours: 168, priority: 3}
  channel_multipliers_percent: {life: 100, world: 150, both: 220}
  life_active_days: 30
```

### `packages\core\config\data\core.yaml`

```yaml
# Core engine knobs. Phase 1 scope only.
locale: fa_IR
timezone: Asia/Tehran

menu_cleanup:
  enabled: true
  default_timeout_seconds: 120
  panels:
    profile: 120
    settings: 90
    market: 60
    house: 120

rate_limit:
  private_messages_per_minute: 25
  group_messages_per_minute: 40
  callbacks_per_minute: 45
  cooldown_penalty_seconds: 20

telegram:
  max_retries: 3
  connect_timeout: 10
  read_timeout: 20
  concurrent_updates: 64
```

### `packages\core\config\data\country.yaml`

```yaml
creation:
  protection_days: 7
  founder_joins_country: true
  require_telegram_group_admin: true
  supported_chat_types:
    - group
    - supergroup

validation:
  name_min_length: 3
  name_max_length: 80
  description_min_length: 10
  description_max_length: 500
  announcement_min_length: 3
  announcement_max_length: 1000
  government_type_max_length: 32
  flag_caption_required: true

government_types:
  - republic
  - monarchy
  - dictatorship
  - federal
  - council
  - constitutional_monarchy
  - parliamentary
  - presidential
  - semi_presidential
  - theocracy
  - military_junta
  - oligarchy
  - direct_democracy

citizenship:
  explicit_join_required: true
  one_country_per_player: true

resources:
  asset_codes:
    - oil
    - food
    - minerals
    - energy
    - technology
  country_total: 5000
  minimum_share: 700
  maximum_share: 1300
  allocation_seed_namespace: telelife-country-resources-v1

permissions:
  register_country: telegram_group_admin
  start_election_without_president: citizen
  start_election_with_president: president
  start_project: president
  set_flag: president
  announce: president
  create_poll: citizen

feature_flags:
  defaults:
    economy_frozen: false
    wars: false
    alliances: false
    companies: false
    universities: false
    global_trade: false
    military: false
lifecycle:
  temporary_min_citizens: 1
  official_min_citizens: 5
  require_elected_leader_for_official: true
  remove_citizenship_on_group_leave: true
```

### `packages\core\config\data\country_missions.yaml`

```yaml
daily:
  count_per_country: 1
  instantiate_on_eligible_action: true
  deterministic_selection: true
  selection_seed_namespace: telelife-country-missions-v1
  retention_days: 30

reward:
  effect_code: production_bonus
  effect_duration_hours: 24
  ledger_asset_code: production_bonus

pool:
  country_food_drive:
    metric_key: food_donated
    target_amount: 100
    reward_amount: 10
    reward_magnitude_basis_points: 1000
  country_mineral_drive:
    metric_key: minerals_donated
    target_amount: 80
    reward_amount: 10
    reward_magnitude_basis_points: 1000

progress:
  eligible_actions:
    donate:
      food: food_donated
      minerals: minerals_donated
  clamp_to_target: true
  completion_is_idempotent: true
```

### `packages\core\config\data\daily.yaml`

```yaml
# Daily reward ladder. Streak is the retention engine: the curve must reward
# consistency hard enough to hurt when broken, without printing money.
reward:
  base_toman: 25000
  # Multiplier applied per streak day, capped. day_1 = base, day_7 = base * 2.2
  streak_multiplier_per_day: 0.20
  max_multiplier: 2.2
  xp: 40

# Milestone bonuses paid ON TOP of the ladder, once per streak run.
milestones:
  3:   { toman: 30000,  xp: 60,  label: "سه روز پشت هم" }
  7:   { toman: 120000, xp: 200, label: "یه هفته کامل" }
  14:  { toman: 300000, xp: 450, label: "دو هفته بی‌وقفه" }
  30:  { toman: 900000, xp: 1200, label: "یه ماه تمام" }
  100: { toman: 4000000, xp: 5000, label: "صد روز افسانه‌ای" }

streak:
  # Miss one day and you drop to this, not to zero. Losing 90 days of work to
  # one bad day makes players quit permanently. This is a deliberate mercy rule.
  grace_reset_to: 1
  # A streak only breaks after this many missed days.
  break_after_days: 1

happiness:
  claim_bonus: 3
```

### `packages\core\config\data\daily_events.yaml`

```yaml
scheduler:
  hour_utc: 0
  minute_utc: 10
  catch_up_days: 7
  claim_batch_size: 31
  deterministic_seed_namespace: telelife-daily-events-v1

events:
  harvest_boom:
    weight: 25
    effect_code: food_production
    magnitude_basis_points: 1200
    duration_hours: 24
  mining_surge:
    weight: 20
    effect_code: minerals_production
    magnitude_basis_points: 1200
    duration_hours: 24
  energy_wave:
    weight: 20
    effect_code: energy_production
    magnitude_basis_points: 1150
    duration_hours: 24
  technology_rush:
    weight: 20
    effect_code: technology_production
    magnitude_basis_points: 1150
    duration_hours: 24
  market_day:
    weight: 15
    effect_code: currency_production
    magnitude_basis_points: 1100
    duration_hours: 24
```

### `packages\core\config\data\economy.yaml`

```yaml
# All monetary values are BIGINT minor units. 1 Toman = 1 unit.
currency:
  toman:
    code: IRT
    symbol: "تومان"
    minor_units: 1
  usd:
    code: USD
    symbol: "$"
    minor_units: 100

starting_balance:
  wallet_toman: 500000
  savings_toman: 0
  usd_cents: 0

limits:
  max_wallet_toman: 999999999999
  min_transaction_toman: 1
  max_transaction_toman: 50000000
  min_resource_transaction: 1
  max_resource_transaction: 1000000

country:
  treasury_account: treasury
  daily_base_income_toman: 125000
  daily_base_expense_toman: 50000
  minimum_tax_toman: 5000
  maximum_tax_toman: 50000000
  minimum_donation_toman: 1
  catch_up_days: 7

ledger:
  idempotency_key_max_length: 128
  reason_max_length: 64
  metadata_max_bytes: 8192
  transfer_legs:
    debit_suffix: debit
    credit_suffix: credit

freeze:
  feature_flag_key: economy_frozen
  blocks_player_debits: true
  blocks_player_credits: true
  blocks_country_debits: true
  blocks_country_credits: true
  allows_admin_compensation: true
```

### `packages\core\config\data\elections.yaml`

```yaml
election:
  nomination_duration_hours: 24
  voting_duration_hours: 24
  minimum_candidates: 1
  maximum_candidates: 50
  one_open_per_country: true
  one_vote_per_election: true
  secret_ballot: true
  require_candidate_message_reply: true
  tie_breaker: earliest_nomination
  no_candidate_result: cancelled

poll:
  duration_hours: 24
  minimum_options: 2
  maximum_options: 10
  question_min_length: 3
  question_max_length: 200
  option_min_length: 1
  option_max_length: 100
  one_active_per_creator: true
  one_vote_per_poll: true

scheduler:
  resolution_interval_seconds: 60
  claim_batch_size: 50
  claim_lease_seconds: 120
  skip_locked: true
```

### `packages\core\config\data\jobs.yaml`

```yaml
production:
  time_unit_seconds: 3600
  quantity_scale: 1
  production_multiplier_per_level: 0.35
  minimum_collection_amount: 1
  minimum_collection_fraction_for_xp: 0.05
  collection_xp_at_full_capacity: 200
  checkpoint_before_upgrade: true
  max_accrual_clock_skew_seconds: 60

storage:
  levels:
    1:
      capacity_hours: 6
    2:
      capacity_hours: 12
    3:
      capacity_hours: 24
  upgrade_cost_toman:
    2: 150000
    3: 500000

production_levels:
  minimum: 1
  maximum: 5
  upgrade_cost_toman:
    2: 200000
    3: 650000
    4: 1600000
    5: 4000000

jobs:
  farmer:
    output_asset: food
    base_rate_per_hour: 10
  miner:
    output_asset: minerals
    base_rate_per_hour: 8
  trader:
    output_asset: IRT
    base_rate_per_hour: 30000
  journalist:
    output_asset: IRT
    base_rate_per_hour: 27500
  doctor:
    output_asset: IRT
    base_rate_per_hour: 27500
  programmer:
    output_asset: technology
    base_rate_per_hour: 5
  engineer:
    output_asset: energy
    base_rate_per_hour: 7

idempotency:
  collection_key_ttl_days: 90
  upgrade_key_ttl_days: 365
```

### `packages\core\config\data\market.yaml`

```yaml
usd:
  min_level: 10
  minimum_trade_cents: 100
  maximum_trade_cents: 100000
  daily_buy_limit_cents: 200000
  daily_sell_limit_cents: 200000
  fee_basis_points: 50
  spread_basis_points: 30
  impact_cents_per_step: 50000
  impact_basis_points_per_step: 8
  max_trade_move_basis_points: 80
  daily_band_basis_points: 800
  stabilization_basis_points_per_minute: 2
  presets_cents: [1000, 5000, 10000]
  health:
    healthy_min: 75
    watch_min: 45
```

### `packages\core\config\data\migration.yaml`

```yaml
cooldown_days: 30
approval_hours: 72
migrant_badge_days: 30
political_hold_days: 14
exit_fee_percent: 5
exit_fee_min_toman: 500000
exit_fee_max_toman: 50000000
```

### `packages\core\config\data\missions.yaml`

```yaml
# Daily missions. Pool is sampled per player per day - deterministic by
# (player_id, date) so a restart never reshuffles someone's missions.
daily:
  count_per_day: 3
  reroll_allowed: false

pool:
  - key: claim_daily
    title: "جایزه روزانه‌تو بگیر"
    target: 1
    reward_toman: 15000
    reward_xp: 30
    min_level: 1

  - key: check_profile
    title: "یه سر به پروفایلت بزن"
    target: 1
    reward_toman: 8000
    reward_xp: 15
    min_level: 1

  - key: earn_xp_100
    title: "۱۰۰ تا XP جمع کن"
    target: 100
    reward_toman: 40000
    reward_xp: 50
    min_level: 2

  - key: group_active
    title: "تو یه گروه فعال باش"
    target: 1
    reward_toman: 20000
    reward_xp: 35
    min_level: 2

  - key: streak_keeper
    title: "استریکتو نگه دار"
    target: 1
    reward_toman: 25000
    reward_xp: 40
    min_level: 3
```

### `packages\core\config\data\national_project.yaml`

```yaml
projects:
  national_storage:
    once_per_country: true
    requirements:
      IRT: 2500000
      food: 250
      minerals: 200
    completion:
      country_storage_capacity_bonus_fraction: 0.25
      contributor_reward_xp: 250

contribution:
  minimum_amount: 1
  maximum_amount_per_request: 1000000
  clamp_to_remaining_requirement: true
  citizenship_required: true
  use_ledger_for_every_asset: true
  require_idempotency_key: true

permissions:
  start_without_president: citizen
  start_with_president: president
```

### `packages\core\config\data\news.yaml`

```yaml
outbox:
  publish_interval_seconds: 15
  claim_batch_size: 50
  claim_lease_seconds: 60
  maximum_attempts: 5
  retry_backoff_seconds:
    - 15
    - 60
    - 300
    - 900
    - 3600
  last_error_code_max_length: 64
  payload_max_bytes: 16384
  delivery_semantics: at_least_once

destinations:
  country: source_country_chat
  global: configured_global_news_chat
```

### `packages\core\config\data\phase3.yaml`

```yaml
savings:
  minimum_transfer_toman: 10000
  maximum_transfer_toman: 50000000
  presets_toman: [50000, 200000, 1000000]

living:
  base_daily_cost_toman: 12000
  max_catch_up_days: 7
  missed_day_happiness_penalty: 2

housing:
  rent_period_days: 7
  options:
    room:
      title: "اتاق جمع‌وجور"
      min_level: 3
      purchase_toman: 900000
      weekly_rent_toman: 90000
      daily_living_toman: 7000
      happiness_bonus: 1
    apartment:
      title: "آپارتمان شهری"
      min_level: 8
      purchase_toman: 4500000
      weekly_rent_toman: 320000
      daily_living_toman: 18000
      happiness_bonus: 2
    villa:
      title: "ویلای لوکس"
      min_level: 20
      purchase_toman: 25000000
      weekly_rent_toman: 1200000
      daily_living_toman: 50000
      happiness_bonus: 4
```

### `packages\core\config\data\progression.yaml`

```yaml
# Level curve: xp_required(level) = base * (level ** exponent)
xp_curve:
  base: 100
  exponent: 1.55
  max_level: 200

starting_state:
  level: 1
  xp: 0
  reputation: 0
  happiness: 70

happiness:
  min: 0
  max: 100
```

### `packages\core\config\data\unlocks.yaml`

```yaml
# Level-gated unlocks. The promise: something new every few levels, forever.
# `phase` marks what is already implemented; locked-but-unimplemented items
# still show in the roadmap panel because anticipation is content.
levels:
  2:  { key: daily_missions, title: "ماموریت‌های روزانه", icon: "🎯", phase: 2 }
  3:  { key: savings,        title: "حساب پس‌انداز",      icon: "🏦", phase: 3 }
  5:  { key: jobs_basic,     title: "شغل‌های پایه",        icon: "💼", phase: 3 }
  7:  { key: rankings,       title: "جدول رتبه‌بندی",      icon: "🏆", phase: 5 }
  10: { key: usd_market,     title: "بازار دلار",          icon: "💲", phase: 4 }
  12: { key: housing,        title: "خرید خونه",           icon: "🏠", phase: 3 }
  15: { key: jobs_advanced,  title: "شغل‌های حرفه‌ای",     icon: "🚀", phase: 3 }
  20: { key: investments,    title: "سرمایه‌گذاری",        icon: "📈", phase: 4 }
  25: { key: titles,         title: "لقب‌های ویژه",        icon: "👑", phase: 5 }
  30: { key: society,        title: "ارکان جامعه",         icon: "🏛", phase: 5 }
  40: { key: business,       title: "کسب‌وکار شخصی",       icon: "🏢", phase: 5 }
  50: { key: prestige,       title: "پرستیژ",              icon: "⭐️", phase: 5 }
```

### `packages\core\config\data\xp.yaml`

```yaml
# تنظیمات تجربه و کنترل سوءاستفاده
sources:
  daily_claim: 40
  mission_complete: 50
  profile_view: 2
  group_activity: 5
  onboarding_step: 35
anti_farm:
  daily_cap: 1500
  cooldowns:
    profile_view: 300
    group_activity: 120
level_up:
  happiness_bonus: 5
  reward_toman_per_level: 15000
```

### `packages\core\config\loader.py`

```python
"""YAML game-config loader. Zero hardcoded game numbers anywhere else."""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path
from typing import Any

_MISSING = object()

import yaml

logger = logging.getLogger(__name__)

CONFIG_DIR = Path(__file__).resolve().parent / "data"


class ConfigError(RuntimeError):
    """Raised when game configuration is missing or invalid."""


class GameConfig:
    """Read-only dotted access over merged YAML files."""

    __slots__ = ("_data",)

    def __init__(self, data: dict[str, Any]) -> None:
        self._data = data

    def get(self, path: str, default: Any = _MISSING) -> Any:
        node: Any = self._data
        for part in path.split("."):
            if not isinstance(node, dict):
                if default is _MISSING:
                    raise ConfigError(f"Missing config key: {path}")
                return default
            key: str | int = part
            if key not in node and part.lstrip("-").isdigit():
                key = int(part)
            if key not in node:
                if default is _MISSING:
                    raise ConfigError(f"Missing config key: {path}")
                return default
            node = node[key]
        return node

    def int_(self, path: str, default: int | object = _MISSING) -> int:
        value = self.get(path, default)
        if isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be an integer")
        try:
            return int(value)
        except (TypeError, ValueError) as exc:
            raise ConfigError(f"Config key '{path}' must be an integer") from exc

    def float_(self, path: str, default: float | object = _MISSING) -> float:
        value = self.get(path, default)
        if isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be numeric")
        try:
            return float(value)
        except (TypeError, ValueError) as exc:
            raise ConfigError(f"Config key '{path}' must be numeric") from exc

    def bool_(self, path: str, default: bool | object = _MISSING) -> bool:
        value = self.get(path, default)
        if not isinstance(value, bool):
            raise ConfigError(f"Config key '{path}' must be a boolean")
        return value

    def section(self, path: str) -> dict[str, Any]:
        value = self.get(path)
        if not isinstance(value, dict):
            raise ConfigError(f"Config key '{path}' is not a section")
        return value

    def as_dict(self) -> dict[str, Any]:
        return self._data


@lru_cache(maxsize=1)
def get_config() -> GameConfig:
    merged: dict[str, Any] = {}
    if not CONFIG_DIR.exists():
        raise ConfigError(f"Config directory not found: {CONFIG_DIR}")
    paths = sorted(CONFIG_DIR.glob("*.yaml"))
    if not paths:
        raise ConfigError(f"No YAML config files found in: {CONFIG_DIR}")
    for path in paths:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError) as exc:
            raise ConfigError(f"Unable to load config file '{path.name}': {exc}") from exc
        if not isinstance(data, dict):
            raise ConfigError(f"Config file '{path.name}' must contain a mapping")
        merged[path.stem] = data
    logger.info("loaded game config sections: %s", ", ".join(sorted(merged)))
    return GameConfig(merged)


def reload_config() -> GameConfig:
    get_config.cache_clear()
    return get_config()
```

### `packages\core\db\__init__.py`

```python
"""Public database API resolved lazily to avoid import-time side effects."""

from __future__ import annotations

from typing import Any

__all__ = [
    "acquire",
    "close_pool",
    "create_pool",
    "execute",
    "fetch",
    "fetchrow",
    "fetchval",
    "get_pool",
    "healthcheck",
    "transaction",
]


def __getattr__(name: str) -> Any:
    if name not in __all__:
        raise AttributeError(name)
    from packages.core.db import pool

    return getattr(pool, name)
```

### `packages\core\db\migrator.py`

```python
"""Minimal forward-only SQL migration runner. No Alembic dependency."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from packages.core.db import pool as dbpool

logger = logging.getLogger(__name__)

MIGRATIONS_DIR = Path(__file__).resolve().parents[3] / "migrations"
# Releases before 0008 were distributed without an immutable migration manifest.
# Some installations therefore have the same legacy version with a different
# checksum. Never re-run those migrations: accept the recorded installation and
# keep strict checksum enforcement for every migration released from 0008 onward.
LEGACY_CHECKSUM_VERSIONS = frozenset({
    "0001_core_schema",
    "0002_progression",
    "0003_country_layer",
    "0004_admin_command_center",
    "0005_life_world_hardening",
    "0006_phase3_phase4_complete",
    "0007_unified_ui_onboarding",
})

_BOOTSTRAP = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version     TEXT PRIMARY KEY,
    checksum    TEXT NOT NULL,
    applied_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""


def _checksum(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def discover() -> list[Path]:
    if not MIGRATIONS_DIR.exists():
        return []
    return sorted(MIGRATIONS_DIR.glob("*.sql"), key=lambda p: p.name)


async def migrate() -> list[str]:
    """Apply pending migrations under a PostgreSQL advisory lock."""
    applied: list[str] = []
    async with dbpool.acquire() as conn:
        async with conn.transaction():
            await conn.execute("SELECT pg_advisory_xact_lock($1)", 839204731)
            await conn.execute(_BOOTSTRAP)
            done = {r["version"]: r["checksum"] for r in await conn.fetch(
                "SELECT version, checksum FROM schema_migrations"
            )}
            for path in discover():
                version = path.stem
                sql = path.read_text(encoding="utf-8")
                digest = _checksum(sql)
                if version in done:
                    if done[version] != digest:
                        if version in LEGACY_CHECKSUM_VERSIONS:
                            logger.warning(
                                "legacy migration checksum differs; preserving the "
                                "database record and not re-running SQL: %s",
                                version,
                            )
                            continue
                        raise RuntimeError(
                            f"Migration '{version}' changed after being applied. "
                            "Create a new migration instead of editing history."
                        )
                    continue
                await conn.execute(sql)
                await conn.execute(
                    "INSERT INTO schema_migrations (version, checksum) VALUES ($1, $2)",
                    version, digest,
                )
                applied.append(version)
                logger.info("applied migration %s", version)
    if not applied:
        logger.info("database schema up to date")
    return applied
```

### `packages\core\db\pool.py`

```python
"""Single asyncpg pool per process. Supabase-pooler safe."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import asyncpg
import orjson

from packages.core.settings import Settings

logger = logging.getLogger(__name__)

_pool: asyncpg.Pool | None = None


async def _init_connection(conn: asyncpg.Connection) -> None:
    """Register codecs once per physical connection."""
    await conn.set_type_codec(
        "jsonb",
        encoder=lambda v: orjson.dumps(v).decode(),
        decoder=orjson.loads,
        schema="pg_catalog",
    )


async def create_pool(settings: Settings) -> asyncpg.Pool:
    global _pool
    if _pool is not None:
        return _pool
    _pool = await asyncpg.create_pool(
        dsn=str(settings.database_url),
        min_size=settings.db_pool_min,
        max_size=settings.db_pool_max,
        command_timeout=settings.db_command_timeout,
        # Required for Supabase / pgbouncer transaction mode.
        statement_cache_size=settings.db_statement_cache_size,
        max_inactive_connection_lifetime=settings.db_max_inactive_seconds,
        init=_init_connection,
        server_settings={"application_name": "telelife-supervisor"},
    )
    logger.info("database pool ready")
    return _pool


def get_pool() -> asyncpg.Pool:
    if _pool is None:
        raise RuntimeError("Database pool not initialised. Call create_pool() first.")
    return _pool


async def close_pool() -> None:
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("database pool closed")


@asynccontextmanager
async def acquire() -> AsyncIterator[asyncpg.Connection]:
    async with get_pool().acquire() as conn:
        yield conn


@asynccontextmanager
async def transaction() -> AsyncIterator[asyncpg.Connection]:
    """Every money-touching operation MUST run inside this."""
    async with get_pool().acquire() as conn, conn.transaction():
        yield conn


async def fetch(query: str, *args: Any) -> list[asyncpg.Record]:
    async with acquire() as conn:
        return await conn.fetch(query, *args)


async def fetchrow(query: str, *args: Any) -> asyncpg.Record | None:
    async with acquire() as conn:
        return await conn.fetchrow(query, *args)


async def fetchval(query: str, *args: Any) -> Any:
    async with acquire() as conn:
        return await conn.fetchval(query, *args)


async def execute(query: str, *args: Any) -> str:
    async with acquire() as conn:
        return await conn.execute(query, *args)


async def healthcheck() -> bool:
    try:
        return await fetchval("SELECT 1") == 1
    except Exception:
        logger.exception("database healthcheck failed")
        return False
```

### `packages\core\logging.py`

```python
"""Structured JSON logging - one line per event, cheap to parse in Render logs."""

from __future__ import annotations

import logging
import sys
from datetime import UTC, datetime
from typing import Any

import orjson

_NOISY = ("httpx", "httpcore", "telegram.ext.Application", "asyncio", "apscheduler")


class JsonFormatter(logging.Formatter):
    def __init__(self, service: str) -> None:
        super().__init__()
        self.service = service

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "ts": datetime.now(UTC).isoformat(timespec="milliseconds"),
            "level": record.levelname,
            "service": self.service,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        extra = getattr(record, "extra_fields", None)
        if isinstance(extra, dict):
            payload |= extra
        return orjson.dumps(payload).decode()


def setup_logging(service: str, level: str = "INFO") -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter(service))
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level.upper())
    for name in _NOISY:
        logging.getLogger(name).setLevel(logging.WARNING)


def log_event(logger: logging.Logger, level: int, msg: str, **fields: Any) -> None:
    logger.log(level, msg, extra={"extra_fields": fields})
```

### `packages\core\models\__init__.py`

```python
from packages.core.models.player import Group, Player

__all__ = ["Group", "Player"]
```

### `packages\core\models\player.py`

```python
"""Domain models. Plain dataclasses - no ORM, no magic."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import asyncpg


@dataclass(slots=True, frozen=True)
class Player:
    id: int
    telegram_id: int
    username: str | None
    first_name: str
    language_code: str
    level: int
    xp: int
    reputation: int
    happiness: int
    prestige: int
    wallet_toman: int
    savings_toman: int
    usd_cents: int
    is_banned: bool
    is_frozen: bool
    ban_reason: str | None
    created_at: datetime
    updated_at: datetime
    last_seen_at: datetime

    @classmethod
    def from_record(cls, row: asyncpg.Record) -> Player:
        return cls(**dict(row))

    @property
    def net_worth_toman(self) -> int:
        return self.wallet_toman + self.savings_toman

    @property
    def playable(self) -> bool:
        return not self.is_banned and not self.is_frozen


@dataclass(slots=True, frozen=True)
class Group:
    id: int
    telegram_id: int
    title: str
    is_active: bool
    member_count: int
    settings: dict[str, Any]
    created_at: datetime
    last_active_at: datetime

    @classmethod
    def from_record(cls, row: asyncpg.Record) -> Group:
        return cls(**dict(row))
```

### `packages\core\repositories\__init__.py`

```python
"""Database repository package with lazy submodule imports."""

__all__ = [
    "admin_repo",
    "country_repo",
    "election_repo",
    "group_repo",
    "ledger_repo",
    "mission_repo",
    "outbox_repo",
    "player_repo",
    "production_repo",
    "progression_repo",
    "project_repo",
]
```

### `packages\core\repositories\admin_repo.py`

```python
"""Read models and audited mutation primitives for the admin command center."""
from __future__ import annotations

from typing import Any
import asyncpg
from packages.core import db

async def audit(conn: asyncpg.Connection, actor: str, action: str, request_id: str,
                details: dict[str, Any], player_id: int | None = None,
                country_id: int | None = None) -> bool:
    return await conn.fetchval(
        """INSERT INTO admin_audit_log
        (admin_actor,action,target_player_id,target_country_id,request_id,details)
        VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING id""",
        actor, action, player_id, country_id, request_id, details,
    ) is not None

async def set_ban(conn: asyncpg.Connection, player_id: int, banned: bool,
                  reason: str | None) -> None:
    result = await conn.execute(
        "UPDATE players SET is_banned=$2,ban_reason=$3 WHERE id=$1", player_id, banned, reason
    )
    if result == "UPDATE 0":
        raise ValueError("player_not_found")

async def set_flag(conn: asyncpg.Connection, key: str, enabled: bool, actor: str) -> None:
    await conn.execute(
        """INSERT INTO feature_flags(key,enabled,updated_by) VALUES($1,$2,$3)
        ON CONFLICT(key) DO UPDATE SET enabled=$2,updated_by=$3,updated_at=now()""",
        key, enabled, actor,
    )

async def dashboard_stats() -> asyncpg.Record | None:
    return await db.fetchrow("""
        SELECT
          (SELECT count(*) FROM players) AS players_total,
          (SELECT count(*) FROM players WHERE last_seen_at >= now()-interval '7 days') AS players_active,
          (SELECT count(*) FROM countries) AS countries_total,
          (SELECT count(*) FROM groups WHERE is_active) AS groups_total,
          (SELECT COALESCE(sum(wallet_toman+savings_toman),0) FROM players) AS player_liquidity,
          (SELECT COALESCE(sum(treasury_toman),0) FROM countries) AS country_treasury,
          (SELECT count(*) FROM news_outbox WHERE published_at IS NULL) AS news_pending,
          (SELECT count(*) FROM players WHERE is_banned) AS players_banned
    """)

async def stats() -> asyncpg.Record | None:
    return await db.fetchrow("""SELECT
        (SELECT count(*) FROM players) players,
        (SELECT count(*) FROM countries) countries,
        (SELECT count(*) FROM citizenships WHERE is_active) citizens""")

async def users(limit: int = 100, query: str = "") -> list[asyncpg.Record]:
    needle = f"%{query.strip()}%"
    return await db.fetch("""
        SELECT id,telegram_id,username,first_name,level,xp,wallet_toman,savings_toman,
               usd_cents,is_banned,is_frozen,ban_reason,last_seen_at,created_at
        FROM players
        WHERE $2='' OR first_name ILIKE $3 OR COALESCE(username,'') ILIKE $3
                      OR telegram_id::text=$2 OR id::text=$2
        ORDER BY last_seen_at DESC LIMIT $1
    """, limit, query.strip(), needle)

async def countries(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT c.id,c.name,c.government_type,c.treasury_toman,c.daily_income_toman,
               c.daily_expense_toman,c.president_player_id,p.first_name AS president_name,
               count(DISTINCT z.player_id) AS citizens,
               COALESCE(jsonb_object_agg(r.asset_code,r.quantity)
                 FILTER (WHERE r.asset_code IS NOT NULL),'{}'::jsonb) AS resources,
               c.created_at
        FROM countries c
        LEFT JOIN players p ON p.id=c.president_player_id
        LEFT JOIN citizenships z ON z.country_id=c.id AND z.is_active
        LEFT JOIN country_resources r ON r.country_id=c.id
        GROUP BY c.id,p.first_name ORDER BY c.treasury_toman DESC LIMIT $1
    """, limit)

async def audits(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("SELECT * FROM admin_audit_log ORDER BY created_at DESC LIMIT $1", limit)

async def news_rows(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT id,event_type,destination_chat_id,payload,attempts,available_at,
               processing_until,published_at,last_error_code,created_at
        FROM news_outbox ORDER BY created_at DESC LIMIT $1
    """, limit)

async def market_history(hours: int = 24) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT p.asset_code,p.title_fa,p.current_price_toman,p.updated_at,p.source,p.source_checked_at,p.source_error,
               COALESCE(jsonb_agg(jsonb_build_object(
                 'time',s.captured_at,'price',s.price_toman) ORDER BY s.captured_at)
                 FILTER (WHERE s.captured_at IS NOT NULL),'[]'::jsonb) AS points
        FROM market_prices p
        LEFT JOIN market_price_snapshots s ON s.asset_code=p.asset_code
          AND s.captured_at >= now()-($1::int * interval '1 hour')
        GROUP BY p.asset_code,p.title_fa,p.current_price_toman,p.updated_at,p.source,p.source_checked_at,p.source_error
        ORDER BY CASE p.asset_code WHEN 'USD' THEN 0 ELSE 1 END,p.asset_code
    """, hours)

async def capture_market_snapshot() -> int:
    result = await db.execute("""
        INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
        SELECT asset_code,current_price_toman,date_trunc('minute',now()) FROM market_prices
        ON CONFLICT DO NOTHING
    """)
    return int(result.rsplit(" ", 1)[-1])

async def ads(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("SELECT * FROM ad_campaigns ORDER BY created_at DESC LIMIT $1", limit)

async def ad_owner(ad_id:int):
 return await db.fetchrow("SELECT p.telegram_id,p.first_name FROM ad_requests a JOIN players p ON p.id=a.requester_player_id WHERE a.id=$1",ad_id)


async def operations_status() -> dict[str, object]:
    market=await db.fetchrow("""SELECT asset_code,current_price_toman,source,source_checked_at,
      source_error,updated_at,now()-source_checked_at AS source_age
      FROM market_prices WHERE asset_code='USD'""")
    jobs=await db.fetch("""SELECT DISTINCT ON(job_name) job_name,status,started_at,finished_at,
      duration_ms,result,error_type,error_message FROM scheduler_job_runs
      ORDER BY job_name,started_at DESC""")
    queues=await db.fetchrow("""SELECT
      (SELECT count(*) FROM news_outbox WHERE published_at IS NULL) outbox_pending,
      (SELECT count(*) FROM news_outbox WHERE published_at IS NULL AND last_error_code IS NOT NULL) outbox_failed,
      (SELECT count(*) FROM ad_deliveries WHERE status='scheduled') ads_scheduled,
      (SELECT count(*) FROM ad_deliveries WHERE status='failed') ads_failed,
      (SELECT count(*) FROM group_live_events WHERE status='open') live_events""")
    frozen=bool(await db.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"))
    return {"market":dict(market) if market else None,"jobs":[dict(x) for x in jobs],
            "queues":dict(queues) if queues else {},"market_frozen":frozen}
async def engagement_overview() -> dict[str, object]:
    """Retention and onboarding signals computed from canonical game tables."""
    row = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE created_at >= now()-interval '24 hours') AS new_24h,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '24 hours') AS active_24h,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '7 days') AS active_7d,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '30 days') AS active_30d,
          count(*) FILTER (WHERE level >= 5) AS reached_jobs,
          count(*) FILTER (WHERE level >= 10) AS reached_market,
          count(*) AS total
        FROM players
    """)
    claims = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE last_claim_date=current_date) AS claimed_today,
          count(*) FILTER (WHERE streak>=3) AS streak_3,
          count(*) FILTER (WHERE streak>=7) AS streak_7,
          COALESCE(avg(streak),0)::numeric(10,2) AS avg_streak
        FROM daily_state
    """)
    missions = await db.fetchrow("""
        SELECT
          count(*) AS assigned_today,
          count(*) FILTER (WHERE progress>=target) AS completed_today,
          count(*) FILTER (WHERE claimed_at IS NOT NULL) AS claimed_today
        FROM daily_missions WHERE mission_date=current_date
    """)
    onboarding = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE onboarding_step>=4) AS completed,
          count(*) FILTER (WHERE onboarding_step<4) AS incomplete
        FROM player_ui_state
    """)
    return {
        "activity": dict(row) if row else {},
        "daily": dict(claims) if claims else {},
        "missions": dict(missions) if missions else {},
        "onboarding": dict(onboarding) if onboarding else {},
    }

async def feature_flags() -> list[asyncpg.Record]:
    return await db.fetch("SELECT key,enabled,updated_by,updated_at FROM feature_flags ORDER BY key")

async def ledger_rows(limit: int = 100, player_id: int | None = None) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT l.id,l.player_id,l.country_id,l.reason,l.asset_code,l.account,l.amount,
               l.balance_after,l.metadata,l.created_at,p.first_name,p.username
        FROM ledger l LEFT JOIN players p ON p.id=l.player_id
        WHERE $2::bigint IS NULL OR l.player_id=$2
        ORDER BY l.created_at DESC LIMIT $1
    """, limit, player_id)

async def economy_integrity() -> dict[str, object]:
    row = await db.fetchrow("""
        SELECT
          (SELECT count(*) FROM players WHERE wallet_toman<0 OR savings_toman<0 OR usd_cents<0) negative_players,
          (SELECT count(*) FROM countries WHERE treasury_toman<0) negative_countries,
          (SELECT count(*) FROM ledger WHERE balance_after<0) negative_ledger_rows,
          (SELECT count(*) FROM ledger WHERE created_at>=now()-interval '24 hours') ledger_24h,
          (SELECT COALESCE(sum(amount),0) FROM ledger WHERE asset_code='IRT' AND created_at>=now()-interval '24 hours') net_irt_24h
    """)
    return dict(row) if row else {}
```

### `packages\core\repositories\country_repo.py`

```python
"""Country, citizenship and national-resource queries."""

from __future__ import annotations

from collections.abc import Mapping

import asyncpg

from packages.core import db


async def by_chat(chat_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        """
        SELECT c.*, g.telegram_id, g.title
        FROM countries c
        JOIN groups g ON g.id = c.group_id
        WHERE g.telegram_id = $1
        """,
        chat_id,
    )


async def by_id(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow("SELECT * FROM countries WHERE id = $1", country_id)


async def citizenship(player_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        """
        SELECT cs.*, c.name
        FROM citizenships cs
        JOIN countries c ON c.id = cs.country_id
        WHERE cs.player_id = $1 AND cs.is_active
        """,
        player_id,
    )


async def create(
    conn: asyncpg.Connection,
    group_id: int,
    player_id: int,
    name: str,
    government: str,
    description: str,
    protection_days: int,
    resources: Mapping[str, int],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO countries
            (group_id, name, government_type, description,
             protection_until, created_by_player_id)
        VALUES ($1, $2, $3, $4, now() + ($5::double precision * interval '1 day'), $6)
        RETURNING *
        """,
        group_id,
        name,
        government,
        description,
        protection_days,
        player_id,
    )
    if row is None:
        raise RuntimeError("country_insert_returned_nothing")
    await conn.execute(
        "INSERT INTO citizenships (player_id, country_id) VALUES ($1, $2) "
        "ON CONFLICT DO NOTHING",
        player_id,
        row["id"],
    )
    await conn.executemany(
        """
        INSERT INTO country_resources (country_id, asset_code, quantity)
        VALUES ($1, $2, $3)
        """,
        [(row["id"], asset, qty) for asset, qty in resources.items()],
    )
    return row


async def join(conn: asyncpg.Connection, player_id: int, country_id: int) -> bool:
    joined = await conn.fetchval(
        "INSERT INTO citizenships (player_id, country_id) VALUES ($1, $2) "
        "ON CONFLICT DO NOTHING RETURNING player_id",
        player_id,
        country_id,
    )
    return joined is not None


async def set_flag(
    country_id: int, player_id: int, file_id: str, unique_id: str | None
) -> bool:
    """Only the president can change the flag. False means: not allowed."""
    updated = await db.fetchval(
        """
        UPDATE countries SET flag_file_id = $3, flag_file_unique_id = $4
        WHERE id = $1 AND president_player_id = $2
        RETURNING id
        """,
        country_id,
        player_id,
        file_id,
        unique_id,
    )
    return updated is not None


async def is_president(country_id: int, player_id: int) -> bool:
    return bool(
        await db.fetchval(
            "SELECT president_player_id = $2 FROM countries WHERE id = $1",
            country_id,
            player_id,
        )
    )


async def resources(country_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT asset_code, quantity FROM country_resources "
        "WHERE country_id = $1 ORDER BY asset_code",
        country_id,
    )


async def citizens(country_id: int) -> list[int]:
    rows = await db.fetch(
        "SELECT player_id FROM citizenships WHERE country_id = $1 AND is_active ORDER BY player_id",
        country_id,
    )
    return [int(row["player_id"]) for row in rows]
```

### `packages\core\repositories\election_repo.py`

```python
"""Election and poll queries, including SKIP LOCKED scheduler claims."""

from __future__ import annotations

from datetime import datetime

import asyncpg

from packages.core import db


async def start(
    conn: asyncpg.Connection,
    country_id: int,
    player_id: int,
    nom_end: datetime,
    vote_end: datetime,
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO elections
            (country_id, started_by_player_id, status, nominations_end_at, voting_end_at)
        VALUES ($1, $2, 'nominations', $3, $4)
        RETURNING *
        """,
        country_id,
        player_id,
        nom_end,
        vote_end,
    )
    if row is None:  # `assert` disappears under `python -O`.
        raise RuntimeError("election_insert_returned_nothing")
    return row


async def nominate(
    election_id: int,
    player_id: int,
    chat_id: int | None,
    message_id: int | None,
) -> bool:
    """Register a candidate. Only while the election accepts nominations."""
    accepted = await db.fetchval(
        """
        INSERT INTO election_candidates
            (election_id, player_id, message_chat_id, message_id)
        SELECT $1, $2, $3, $4
        WHERE EXISTS (
            SELECT 1 FROM elections
            WHERE id = $1 AND status = 'nominations' AND nominations_end_at > now()
        )
        ON CONFLICT DO NOTHING
        RETURNING player_id
        """,
        election_id,
        player_id,
        chat_id,
        message_id,
    )
    return accepted is not None


async def vote(election_id: int, voter: int, candidate: int) -> bool:
    """Cast a vote. Rejected unless voting is open and the candidate is real."""
    accepted = await db.fetchval(
        """
        INSERT INTO election_votes
            (election_id, voter_player_id, candidate_player_id)
        SELECT $1, $2, $3
        WHERE EXISTS (
            SELECT 1 FROM elections
            WHERE id = $1 AND status = 'voting' AND voting_end_at > now()
        )
        AND EXISTS (
            SELECT 1 FROM election_candidates
            WHERE election_id = $1 AND player_id = $3
        )
        ON CONFLICT DO NOTHING
        RETURNING voter_player_id
        """,
        election_id,
        voter,
        candidate,
    )
    return accepted is not None


async def open_for_country(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM elections "
        "WHERE country_id = $1 AND status IN ('nominations', 'voting')",
        country_id,
    )


async def claim_due(conn: asyncpg.Connection, limit: int) -> list[asyncpg.Record]:
    return list(
        await conn.fetch(
            """
            SELECT * FROM elections
            WHERE (status = 'nominations' AND nominations_end_at <= now())
               OR (status = 'voting'      AND voting_end_at      <= now())
            ORDER BY id
            FOR UPDATE SKIP LOCKED
            LIMIT $1
            """,
            limit,
        )
    )


async def advance(conn: asyncpg.Connection, election_id: int) -> None:
    """Nominations -> voting. Cancels the election when nobody stood."""
    await conn.execute(
        """
        UPDATE elections SET status = CASE
            WHEN EXISTS (SELECT 1 FROM election_candidates WHERE election_id = $1)
            THEN 'voting' ELSE 'cancelled' END,
            resolved_at = CASE
            WHEN EXISTS (SELECT 1 FROM election_candidates WHERE election_id = $1)
            THEN NULL ELSE now() END
        WHERE id = $1 AND status = 'nominations'
        """,
        election_id,
    )


async def resolve(conn: asyncpg.Connection, election_id: int) -> int | None:
    """Close voting and seat the winner. Ties break on earliest nomination."""
    winner = await conn.fetchval(
        """
        SELECT v.candidate_player_id
        FROM election_votes v
        JOIN election_candidates c
          ON c.election_id = v.election_id AND c.player_id = v.candidate_player_id
        WHERE v.election_id = $1
        GROUP BY v.candidate_player_id, c.created_at
        ORDER BY count(*) DESC, c.created_at, v.candidate_player_id
        LIMIT 1
        """,
        election_id,
    )

    # Only seat the winner if THIS call is the one that closed the election.
    # Without the RETURNING guard a concurrent worker could seat twice.
    closed = await conn.fetchval(
        """
        UPDATE elections
        SET status = 'completed', winner_player_id = $2, resolved_at = now()
        WHERE id = $1 AND status = 'voting'
        RETURNING country_id
        """,
        election_id,
        winner,
    )
    if closed is None:
        return None

    if winner is not None:
        await conn.execute(
            "UPDATE countries SET president_player_id = $2 WHERE id = $1",
            int(closed),
            int(winner),
        )
        return int(winner)
    return None


async def create_poll(
    conn: asyncpg.Connection,
    country_id: int,
    creator: int,
    question: str,
    closes: datetime,
    options: list[str],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO polls (country_id, creator_player_id, question, closes_at)
        VALUES ($1, $2, $3, $4)
        RETURNING *
        """,
        country_id,
        creator,
        question,
        closes,
    )
    if row is None:
        raise RuntimeError("poll_insert_returned_nothing")
    await conn.executemany(
        "INSERT INTO poll_options (poll_id, option_text) VALUES ($1, $2)",
        [(row["id"], text) for text in options],
    )
    return row


async def poll_vote(poll_id: int, voter: int, option_id: int) -> bool:
    """Cast a poll vote. The option must belong to this open poll."""
    accepted = await db.fetchval(
        """
        INSERT INTO poll_votes (poll_id, voter_player_id, option_id)
        SELECT $1, $2, $3
        WHERE EXISTS (
            SELECT 1 FROM polls
            WHERE id = $1 AND status = 'active' AND closes_at > now()
        )
        AND EXISTS (
            SELECT 1 FROM poll_options WHERE id = $3 AND poll_id = $1
        )
        ON CONFLICT DO NOTHING
        RETURNING voter_player_id
        """,
        poll_id,
        voter,
        option_id,
    )
    return accepted is not None


async def polls(country_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT * FROM polls WHERE country_id = $1 ORDER BY created_at DESC LIMIT 20",
        country_id,
    )


async def claim_due_polls(
    conn: asyncpg.Connection, limit: int
) -> list[asyncpg.Record]:
    return list(
        await conn.fetch(
            """
            SELECT * FROM polls
            WHERE status = 'active' AND closes_at <= now()
            ORDER BY id
            FOR UPDATE SKIP LOCKED
            LIMIT $1
            """,
            limit,
        )
    )


async def resolve_poll(conn: asyncpg.Connection, poll_id: int) -> None:
    await conn.execute(
        "UPDATE polls SET status = 'completed', resolved_at = now() "
        "WHERE id = $1 AND status = 'active'",
        poll_id,
    )
```

### `packages\core\repositories\group_repo.py`

```python
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
```

### `packages\core\repositories\ledger_repo.py`

```python
"""Economic persistence primitives. Business rules live in services."""
from __future__ import annotations
from typing import Any
import asyncpg


def player_account(asset: str) -> str:
    """Canonical ledger account for a player-owned asset."""
    return "wallet" if asset == "IRT" else "usd" if asset == "USD" else f"resource:{asset}"


def country_account(asset: str) -> str:
    """Canonical ledger account for a country-owned asset."""
    return "treasury" if asset == "IRT" else f"resource:{asset}"


async def idempotency_exists(conn: asyncpg.Connection, key: str) -> bool:
    return bool(await conn.fetchval("SELECT EXISTS(SELECT 1 FROM ledger WHERE idempotency_key=$1)", key))


async def lock_player(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM players WHERE id=$1 FOR UPDATE", player_id)


async def lock_country(conn: asyncpg.Connection, country_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM countries WHERE id=$1 FOR UPDATE", country_id)


async def player_resource(conn: asyncpg.Connection, player_id: int, asset: str) -> int:
    value = await conn.fetchval(
        "SELECT quantity FROM player_resources WHERE player_id=$1 AND asset_code=$2 FOR UPDATE",
        player_id, asset,
    )
    return int(value or 0)


async def change_player(conn: asyncpg.Connection, player_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value = await conn.fetchval(
            "UPDATE players SET wallet_toman=wallet_toman+$2 WHERE id=$1 AND wallet_toman+$2>=0 RETURNING wallet_toman",
            player_id, delta,
        )
    elif asset == "USD":
        value = await conn.fetchval(
            "UPDATE players SET usd_cents=usd_cents+$2 WHERE id=$1 AND usd_cents+$2>=0 RETURNING usd_cents",
            player_id, delta,
        )
    else:
        value = await conn.fetchval(
            """INSERT INTO player_resources(player_id,asset_code,quantity)
            SELECT $1,$2,$3 WHERE $3>=0
            ON CONFLICT(player_id,asset_code) DO UPDATE SET quantity=player_resources.quantity+$3,updated_at=now()
            WHERE player_resources.quantity+$3>=0 RETURNING quantity""",
            player_id, asset, delta,
        )
    if value is None:
        raise ValueError("insufficient_player_balance")
    return int(value)


async def change_country(conn: asyncpg.Connection, country_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value = await conn.fetchval(
            "UPDATE countries SET treasury_toman=treasury_toman+$2 WHERE id=$1 AND treasury_toman+$2>=0 RETURNING treasury_toman",
            country_id, delta,
        )
    else:
        value = await conn.fetchval(
            """INSERT INTO country_resources(country_id,asset_code,quantity)
            SELECT $1,$2,$3 WHERE $3>=0
            ON CONFLICT(country_id,asset_code) DO UPDATE SET quantity=country_resources.quantity+$3,updated_at=now()
            WHERE country_resources.quantity+$3>=0 RETURNING quantity""",
            country_id, asset, delta,
        )
    if value is None:
        raise ValueError("insufficient_country_balance")
    return int(value)


async def insert(
    conn: asyncpg.Connection, *, player_id: int | None, country_id: int | None,
    key: str, reason: str, asset: str, account: str, amount: int,
    balance: int, metadata: dict[str, Any] | None = None,
) -> bool:
    row = await conn.fetchval(
        """INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,asset_code,account,amount,balance_after,metadata)
        VALUES($1,$2,$3,$4,$5,$5,$6,$7,$8,$9)
        ON CONFLICT(idempotency_key) DO NOTHING RETURNING id""",
        player_id, country_id, key, reason, asset, account, amount, balance, metadata or {},
    )
    return row is not None


async def economy_frozen(conn: asyncpg.Connection) -> bool:
    return bool(await conn.fetchval(
        "SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='economy_frozen'),false)"
    ))
```

### `packages\core\repositories\mission_repo.py`

```python
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
```

### `packages\core\repositories\outbox_repo.py`

```python
"""Transactional outbox and deterministic daily-event queries."""

from __future__ import annotations

from datetime import date
from typing import Any
from uuid import UUID

import asyncpg


async def enqueue(
    conn: asyncpg.Connection,
    key: str,
    event_type: str,
    payload: dict[str, Any],
    destination: int | None,
) -> bool:
    """Queue one message. False means this key was already queued."""
    queued = await conn.fetchval(
        """
        INSERT INTO news_outbox
            (idempotency_key, event_type, payload, destination_chat_id)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (idempotency_key) DO NOTHING
        RETURNING id
        """,
        key,
        event_type,
        payload,
        destination,
    )
    return queued is not None


async def claim(
    conn: asyncpg.Connection,
    token: UUID,
    limit: int,
    lease: int,
    max_attempts: int,
) -> list[asyncpg.Record]:
    """Lease a batch of due messages. Concurrent workers never collide."""
    return list(
        await conn.fetch(
            """
            WITH picked AS (
                SELECT id FROM news_outbox
                WHERE published_at IS NULL
                  AND attempts < $3
                  AND available_at <= now()
                  AND (processing_until IS NULL OR processing_until < now())
                ORDER BY created_at, id
                FOR UPDATE SKIP LOCKED
                LIMIT $2
            )
            UPDATE news_outbox n SET
                processing_token = $1,
                processing_until = now() + ($4::double precision * interval '1 second'),
                attempts = attempts + 1
            FROM picked
            WHERE n.id = picked.id
            RETURNING n.*
            """,
            token,
            limit,
            max_attempts,
            lease,
        )
    )


async def published(conn: asyncpg.Connection, row_id: int, token: UUID) -> None:
    await conn.execute(
        """
        UPDATE news_outbox SET
            published_at = now(), processing_token = NULL, processing_until = NULL
        WHERE id = $1 AND processing_token = $2
        """,
        row_id,
        token,
    )


async def failed(
    conn: asyncpg.Connection,
    row_id: int,
    token: UUID,
    error: str,
    delay: int,
) -> None:
    """Release the lease and schedule a retry."""
    await conn.execute(
        """
        UPDATE news_outbox SET
            processing_token = NULL,
            processing_until = NULL,
            last_error_code  = $3,
            available_at     = now() + ($4::double precision * interval '1 second')
        WHERE id = $1 AND processing_token = $2
        """,
        row_id,
        token,
        error,
        delay,
    )


async def create_event(
    conn: asyncpg.Connection, day: date, code: str, effect: dict[str, Any]
) -> bool:
    """Record the day's event once. False means the day already had one."""
    created = await conn.fetchval(
        """
        INSERT INTO daily_events (event_date, event_code, effect_payload)
        VALUES ($1, $2, $3)
        ON CONFLICT (event_date) DO NOTHING
        RETURNING event_date
        """,
        day,
        code,
        effect,
    )
    return created is not None
```

### `packages\core\repositories\player_repo.py`

```python
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
            "SELECT count(*) FROM players WHERE last_seen_at > now() - ($1::double precision * interval '1 day')",
            str(days),
        )
        or 0
    )
```

### `packages\core\repositories\production_repo.py`

```python
"""Lazy-production row locking and materialisation queries."""

from __future__ import annotations

from datetime import datetime

import asyncpg

from packages.core import db

# Whitelist: the column name is interpolated into SQL, so it can never come
# straight from a caller.
_LEVEL_COLUMNS = {"storage": "storage_level", "production": "production_level"}


async def get(player_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM player_jobs WHERE player_id = $1", player_id
    )


async def choose(player_id: int, job: str, asset: str) -> bool:
    """Pick a job once. False means the player already has one."""
    chosen = await db.fetchval(
        """
        INSERT INTO player_jobs
            (player_id, job_code, output_asset_code, production_updated_at)
        VALUES ($1, $2, $3, now())
        ON CONFLICT DO NOTHING
        RETURNING player_id
        """,
        player_id,
        job,
        asset,
    )
    return chosen is not None


async def lock(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow(
        "SELECT * FROM player_jobs WHERE player_id = $1 FOR UPDATE", player_id
    )


async def checkpoint(
    conn: asyncpg.Connection, player_id: int, stored: int, at: datetime
) -> None:
    await conn.execute(
        "UPDATE player_jobs SET stored_amount = $2, production_updated_at = $3 "
        "WHERE player_id = $1",
        player_id,
        stored,
        at,
    )


async def clear(conn: asyncpg.Connection, player_id: int, at: datetime) -> None:
    await conn.execute(
        "UPDATE player_jobs SET stored_amount = 0, production_updated_at = $2 "
        "WHERE player_id = $1",
        player_id,
        at,
    )


async def level_up(conn: asyncpg.Connection, player_id: int, kind: str) -> None:
    column = _LEVEL_COLUMNS.get(kind)
    if column is None:
        raise ValueError(f"unknown_level_kind: {kind}")
    await conn.execute(
        f"UPDATE player_jobs SET {column} = {column} + 1 WHERE player_id = $1",  # noqa: S608
        player_id,
    )
```

### `packages\core\repositories\progression_repo.py`

```python
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
```

### `packages\core\repositories\project_repo.py`

```python
"""National project persistence."""

from __future__ import annotations

from collections.abc import Mapping

import asyncpg

from packages.core import db


async def start(
    conn: asyncpg.Connection,
    country_id: int,
    player_id: int,
    key: str,
    requirements: Mapping[str, int],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO national_projects (country_id, project_key, started_by_player_id)
        VALUES ($1, $2, $3)
        RETURNING *
        """,
        country_id,
        key,
        player_id,
    )
    if row is None:
        raise RuntimeError("project_insert_returned_nothing")
    await conn.executemany(
        """
        INSERT INTO project_requirements (project_id, asset_code, required_amount)
        VALUES ($1, $2, $3)
        """,
        [(row["id"], asset, amount) for asset, amount in requirements.items()],
    )
    return row


async def active(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM national_projects WHERE country_id = $1 AND status = 'active'",
        country_id,
    )


async def status(project_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT * FROM project_requirements WHERE project_id = $1 ORDER BY asset_code",
        project_id,
    )


async def lock(conn: asyncpg.Connection, project_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow(
        "SELECT * FROM national_projects WHERE id = $1 FOR UPDATE", project_id
    )


async def remaining(
    conn: asyncpg.Connection, project_id: int, asset: str
) -> int | None:
    """Outstanding amount for one asset, with the requirement row locked."""
    value = await conn.fetchval(
        """
        SELECT required_amount - contributed_amount
        FROM project_requirements
        WHERE project_id = $1 AND asset_code = $2
        FOR UPDATE
        """,
        project_id,
        asset,
    )
    return int(value) if value is not None else None


async def contribution(
    conn: asyncpg.Connection,
    project_id: int,
    player_id: int,
    asset: str,
    amount: int,
    key: str,
) -> bool:
    """Record a contribution once. False means the key was already used."""
    added = await conn.fetchval(
        """
        INSERT INTO project_contributions
            (project_id, player_id, asset_code, amount, idempotency_key)
        VALUES ($1, $2, $3, $4, $5)
        ON CONFLICT (idempotency_key) DO NOTHING
        RETURNING id
        """,
        project_id,
        player_id,
        asset,
        amount,
        key,
    )
    if added is None:
        return False
    await conn.execute(
        """
        UPDATE project_requirements
        SET contributed_amount = LEAST(required_amount, contributed_amount + $3)
        WHERE project_id = $1 AND asset_code = $2
        """,
        project_id,
        asset,
        amount,
    )
    return True


async def complete_if_ready(conn: asyncpg.Connection, project_id: int) -> bool:
    """Mark complete only when every requirement is met, exactly once."""
    pending = await conn.fetchval(
        """
        SELECT EXISTS(
            SELECT 1 FROM project_requirements
            WHERE project_id = $1 AND contributed_amount < required_amount
        )
        """,
        project_id,
    )
    if pending:
        return False
    # RETURNING is the reliable "did this row change" signal. Parsing the
    # command tag with endswith('1') also matches "UPDATE 11".
    completed = await conn.fetchval(
        """
        UPDATE national_projects
        SET status = 'completed', completed_at = now()
        WHERE id = $1 AND status = 'active'
        RETURNING id
        """,
        project_id,
    )
    return completed is not None
```

### `packages\core\repositories\ui_state_repo.py`

```python
"""Persistent panel locations and onboarding state."""
from __future__ import annotations
from packages.core import db

async def life(player_id:int):
 return await db.fetchrow("SELECT * FROM player_ui_state WHERE player_id=$1",player_id)
async def ensure_life(player_id:int):
 await db.execute("INSERT INTO player_ui_state(player_id) VALUES($1) ON CONFLICT DO NOTHING",player_id)
 return await life(player_id)
async def set_life_panel(player_id:int,chat_id:int,message_id:int)->None:
 await db.execute("""INSERT INTO player_ui_state(player_id,life_chat_id,life_message_id) VALUES($1,$2,$3)
 ON CONFLICT(player_id) DO UPDATE SET life_chat_id=$2,life_message_id=$3,updated_at=now()""",player_id,chat_id,message_id)
async def set_step(player_id:int,step:int)->None:
 await db.execute("""UPDATE player_ui_state SET onboarding_step=GREATEST(onboarding_step,$2),
 onboarding_completed_at=CASE WHEN $2>=4 THEN COALESCE(onboarding_completed_at,now()) ELSE onboarding_completed_at END,updated_at=now() WHERE player_id=$1""",player_id,step)
async def world(chat_id:int):return await db.fetchrow("SELECT * FROM world_ui_state WHERE chat_id=$1",chat_id)
async def set_world(chat_id:int,message_id:int)->None:
 await db.execute("""INSERT INTO world_ui_state(chat_id,message_id) VALUES($1,$2)
 ON CONFLICT(chat_id) DO UPDATE SET message_id=$2,updated_at=now()""",chat_id,message_id)
```

### `packages\core\repositories\world_access_repo.py`

```python
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
```

### `packages\core\runtime_status.py`

```python
"""Process-local runtime health registry shared with the admin panel."""
from __future__ import annotations

import time
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(slots=True)
class ServiceState:
    name: str
    status: str = "starting"
    restarts: int = 0
    last_error: str | None = None
    last_started_monotonic: float | None = None
    last_healthy_monotonic: float | None = None

    def public(self) -> dict[str, Any]:
        data = asdict(self)
        now = time.monotonic()
        started = data.pop("last_started_monotonic")
        healthy = data.pop("last_healthy_monotonic")
        data["uptime_seconds"] = round(max(0.0, now - started), 1) if started else 0.0
        data["healthy_ago_seconds"] = round(max(0.0, now - healthy), 1) if healthy else None
        return data


_states: dict[str, ServiceState] = {}


def state(name: str) -> ServiceState:
    return _states.setdefault(name, ServiceState(name=name))


def snapshot() -> dict[str, dict[str, Any]]:
    return {name: item.public() for name, item in sorted(_states.items())}
```

### `packages\core\services\__init__.py`

```python
"""Domain service package.

Submodules are intentionally not eagerly imported. Python resolves explicit
``from packages.core.services import xp`` imports lazily, avoiding package-level
cycles while preserving the public import style.
"""

__all__ = [
    "admin",
    "country",
    "country_economy",
    "country_missions",
    "daily",
    "economy",
    "elections",
    "missions",
    "national_project",
    "news",
    "production",
    "progression",
    "unlocks",
    "xp",
]
```

### `packages\core\services\admin.py`

```python
"""Audited privileged operations; mutation and audit commit atomically."""
from __future__ import annotations

from packages.core import db
from packages.core.repositories import admin_repo, outbox_repo
from packages.core.services import xp
from packages.core.services.xp import XPResult

async def ban(actor: str, player_id: int, banned: bool, reason: str | None,
              request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "ban" if banned else "unban",
                                      request_id, {"reason": reason}, player_id):
            return False
        await admin_repo.set_ban(conn, player_id, banned, reason)
        return True

async def feature(actor: str, key: str, enabled: bool, request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "feature_toggle", request_id,
                                      {"key": key, "enabled": enabled}):
            return False
        await admin_repo.set_flag(conn, key, enabled, actor)
        return True

async def grant_xp(actor: str, player_id: int, amount: int,
                   request_id: str) -> XPResult | None:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "grant_xp", request_id,
                                      {"amount": amount}, player_id):
            return None
        return await xp.grant(player_id, "admin_grant",
                              idempotency_key=f"admin-xp:{request_id}", amount=amount, conn=conn)

async def set_market_price(actor: str, asset: str, price: int, request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "market_price", request_id,
                                      {"asset": asset, "price": price}):
            return False
        changed = await conn.fetchval("""
            UPDATE market_prices SET current_price_toman=$2,updated_by=$3,updated_at=now()
            WHERE asset_code=$1 RETURNING asset_code
        """, asset, price, actor)
        if changed is None:
            raise ValueError("asset_not_found")
        await conn.execute("""
            INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
            VALUES($1,$2,date_trunc('minute',now()))
            ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman
        """, asset, price)
        return True

async def adjust_country_asset(actor: str, country_id: int, asset: str, delta: int,
                               request_id: str) -> int:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "country_asset_adjust", request_id,
                                      {"asset": asset, "delta": delta}, country_id=country_id):
            return 0
        exists = await conn.fetchval("SELECT 1 FROM countries WHERE id=$1 FOR UPDATE", country_id)
        if not exists:
            raise ValueError("country_not_found")
        if asset == "IRT":
            value = await conn.fetchval("""
                UPDATE countries SET treasury_toman=treasury_toman+$2
                WHERE id=$1 AND treasury_toman+$2>=0 RETURNING treasury_toman
            """, country_id, delta)
        else:
            value = await conn.fetchval("""
                INSERT INTO country_resources(country_id,asset_code,quantity) VALUES($1,$2,$3)
                ON CONFLICT(country_id,asset_code) DO UPDATE
                SET quantity=country_resources.quantity+$3,updated_at=now()
                WHERE country_resources.quantity+$3>=0 RETURNING quantity
            """, country_id, asset, delta)
        if value is None:
            raise ValueError("insufficient_balance")
        await conn.execute("""
            INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,
                               asset_code,account,amount,balance_after,metadata)
            VALUES(NULL,$1,$2,'admin_adjustment',$3,$3,'treasury',$4,$5,$6)
        """, country_id, f"admin-country:{request_id}", asset, delta, value,
             {"admin_actor": actor})
        return int(value)

async def set_president(actor: str, country_id: int, player_id: int | None,
                        request_id: str) -> bool:
    async with db.transaction() as conn:
        if player_id is not None:
            citizen = await conn.fetchval(
                "SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2",
                country_id, player_id,
            )
            if not citizen:
                raise ValueError("president_must_be_citizen")
        if not await admin_repo.audit(conn, actor, "set_president", request_id,
                                      {"player_id": player_id}, player_id, country_id):
            return False
        result = await conn.execute(
            "UPDATE countries SET president_player_id=$2 WHERE id=$1", country_id, player_id
        )
        if result == "UPDATE 0":
            raise ValueError("country_not_found")
        return True

async def enqueue_news(actor: str, text: str, destination: int,
                       request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "enqueue_news", request_id,
                                      {"destination": destination, "text": text[:200]}):
            return False
        return await outbox_repo.enqueue(conn, f"admin-news:{request_id}",
                                         "admin_announcement", {"text": text}, destination)

async def create_ad(actor: str, title: str, text: str, destination: int,
                    scheduled_at, repeat_minutes: int | None, request_id: str) -> int:
    from packages.core.services.content_filter import require_clean
    require_clean(title, "name"); require_clean(text, "description")
    status = "scheduled" if scheduled_at else "draft"
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "create_ad", request_id,
                                      {"title": title, "destination": destination}): return 0
        return int(await conn.fetchval("""INSERT INTO ad_campaigns
          (title,body,destination_chat_id,status,scheduled_at,repeat_minutes,created_by)
          VALUES($1,$2,$3,$4,$5,$6,$7) RETURNING id""",
          title,text,destination,status,scheduled_at,repeat_minutes,actor))

async def queue_ad(actor: str, ad_id: int, request_id: str) -> bool:
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT * FROM ad_campaigns WHERE id=$1 FOR UPDATE",ad_id)
        if row is None: raise ValueError("ad_not_found")
        if not await admin_repo.audit(conn,actor,"queue_ad",request_id,{"ad_id":ad_id}): return False
        queued=await outbox_repo.enqueue(conn,f"ad:{ad_id}:{request_id}","advertisement",
                                         {"text":row["body"],"ad_id":ad_id},row["destination_chat_id"])
        if queued: await conn.execute("UPDATE ad_campaigns SET status='queued',last_queued_at=now(),updated_at=now() WHERE id=$1",ad_id)
        return queued
```

### `packages\core\services\commerce.py`

```python
"""Atomic subscriptions, Telegram Stars payments, moderation and ad delivery planning."""
from __future__ import annotations
from datetime import UTC,datetime,timedelta
from urllib.parse import urlparse
from uuid import uuid4
from packages.core import db
from packages.core.config import get_config
from packages.core.services.content_filter import require_clean

PACKAGES={"economy":(25,1,1,0),"standard":(60,3,24,1),"campaign":(120,6,72,2),"featured":(200,8,168,3)}
CHANNEL_PERCENT={"life":100,"world":150,"both":220}
def subscription_stars(citizens:int)->int:
 if citizens<=20:return 10
 if citizens<=100:return 15
 if citizens<=500:return 30
 if citizens<=1000:return 50
 return 75
def treasury_price(balance:int,citizens:int=0)->int:return min(1_000_000_000,max(20_000_000,balance*20//100+citizens*1_000_000))
def ad_price(package_code:str,channel:str)->int:
 if package_code not in PACKAGES or channel not in CHANNEL_PERCENT:raise ValueError("invalid_ad_selection")
 return (PACKAGES[package_code][0]*CHANNEL_PERCENT[channel]+99)//100
def valid_url(value:str)->bool:
 try:u=urlparse(value);return u.scheme in {"http","https"} and bool(u.netloc)
 except ValueError:return False

async def subscription_view(chat_id:int):
 return await db.fetchrow("""SELECT g.id,g.telegram_id,g.title,g.ad_free_until,c.treasury_toman,
  (SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens,
  r.id round_id,r.collected_stars,r.target_stars,r.expires_at
  FROM groups g LEFT JOIN countries c ON c.group_id=g.id
  LEFT JOIN subscription_rounds r ON r.group_id=g.id AND r.status='open'
  WHERE g.telegram_id=$1""",chat_id)

async def ensure_round(chat_id:int):
 async with db.transaction() as conn:
  group=await conn.fetchrow("SELECT id FROM groups WHERE telegram_id=$1 FOR UPDATE",chat_id)
  if not group:raise ValueError("group_not_found")
  citizens=int(await conn.fetchval("SELECT count(*) FROM citizenships cs JOIN countries c ON c.id=cs.country_id WHERE c.group_id=$1 AND cs.is_active",group["id"]) or 0);target=subscription_stars(citizens)
  row=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE group_id=$1 AND status='open'",group["id"])
  if row and row["expires_at"]>datetime.now(UTC):
   if int(row["target_stars"])!=target:await conn.execute("UPDATE subscription_rounds SET target_stars=$2 WHERE id=$1",row["id"],max(target,int(row["collected_stars"])))
   return await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1",row["id"])
  if row:await conn.execute("UPDATE subscription_rounds SET status='expired' WHERE id=$1",row["id"])
  return await conn.fetchrow("INSERT INTO subscription_rounds(group_id,target_stars) VALUES($1,$2) RETURNING *",group["id"],target)

async def subscription_invoice(round_id:int,payer_telegram_id:int,stars:int):
 if stars not in {1,2,5,10,25,50}:raise ValueError("invalid_stars")
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1 FOR UPDATE",round_id)
  if not row or row["status"]!='open' or row["expires_at"]<=datetime.now(UTC):raise ValueError("round_closed")
  amount=min(stars,int(row["target_stars"])-int(row["collected_stars"]));payload=f"sub:{round_id}:{payer_telegram_id}:{uuid4().hex}"
  await conn.execute("INSERT INTO star_payments(purpose,reference_id,payer_telegram_id,stars,invoice_payload,expires_at) VALUES('subscription',$1,$2,$3,$4,LEAST($5,now()+interval '30 minutes'))",round_id,payer_telegram_id,amount,payload,row["expires_at"])
  return payload,amount

async def create_ad_request(player_id:int,package_code:str,channel:str,title:str,description:str,url:str,image_bytes:bytes|None,image_mime:str|None,start_at=None)->int:
 if package_code not in PACKAGES or channel not in CHANNEL_PERCENT:raise ValueError("invalid_package")
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 if image_bytes and (len(image_bytes)>5_000_000 or image_mime not in {'image/jpeg','image/png','image/webp'}):raise ValueError("invalid_image")
 base,impressions,hours,priority=PACKAGES[package_code];stars=ad_price(package_code,channel)
 return int(await db.fetchval("""INSERT INTO ad_requests(requester_player_id,package_code,channel,title,description,target_url,image_bytes,image_mime,requested_start_at,price_stars,impressions_planned,campaign_hours,priority)
 VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13) RETURNING id""",player_id,package_code,channel,title,description,url,image_bytes,image_mime,start_at,stars,impressions,hours,priority))

async def ad_invoice(ad_id:int,payer_telegram_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM ad_requests WHERE id=$1 FOR UPDATE",ad_id)
  if not row or row["requester_player_id"]!=await conn.fetchval("SELECT id FROM players WHERE telegram_id=$1",payer_telegram_id):raise PermissionError("not_owner")
  if row["status"]!='approved_unpaid' or not row["payment_expires_at"] or row["payment_expires_at"]<=datetime.now(UTC):raise ValueError("payment_expired")
  payload=f"ad:{ad_id}:{payer_telegram_id}:{uuid4().hex}"
  await conn.execute("INSERT INTO star_payments(purpose,reference_id,payer_telegram_id,stars,invoice_payload,expires_at) VALUES('advertisement',$1,$2,$3,$4,$5)",ad_id,payer_telegram_id,row["price_stars"],payload,row["payment_expires_at"])
  return payload,int(row["price_stars"]),str(row["title"])

async def precheckout(payload:str,payer:int,total:int)->bool:
 row=await db.fetchrow("SELECT * FROM star_payments WHERE invoice_payload=$1",payload)
 return bool(row and row["status"]=='invoiced' and row["payer_telegram_id"]==payer and row["stars"]==total and row["expires_at"]>datetime.now(UTC))

async def settle(payload:str,payer:int,total:int,tg_charge:str,provider_charge:str|None)->str:
 async with db.transaction() as conn:
  payment=await conn.fetchrow("SELECT * FROM star_payments WHERE invoice_payload=$1 FOR UPDATE",payload)
  if not payment or payment["payer_telegram_id"]!=payer or payment["stars"]!=total or payment["status"] not in {'invoiced','paid'}:raise ValueError("invalid_payment")
  if payment["status"]=='paid':return payment["purpose"]
  await conn.execute("UPDATE star_payments SET status='paid',telegram_charge_id=$2,provider_charge_id=$3,paid_at=now() WHERE id=$1",payment["id"],tg_charge,provider_charge)
  if payment["purpose"]=='subscription':
   rnd=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1 FOR UPDATE",payment["reference_id"])
   if rnd and rnd["status"]=='open':
    target=int(rnd["target_stars"]);total_stars=min(target,int(rnd["collected_stars"])+int(payment["stars"]));complete=total_stars>=target
    await conn.execute("UPDATE subscription_rounds SET collected_stars=$2,status=CASE WHEN $3 THEN 'completed' ELSE status END,completed_at=CASE WHEN $3 THEN now() ELSE NULL END WHERE id=$1",rnd["id"],total_stars,complete)
    if complete:
     until=await conn.fetchval("UPDATE groups SET ad_free_until=GREATEST(COALESCE(ad_free_until,now()),now())+interval '30 days' WHERE id=$1 RETURNING ad_free_until",rnd["group_id"])
     await conn.execute("INSERT INTO group_subscription_events(group_id,source,stars,starts_at,ends_at) VALUES($1,'stars',$3,now(),$2)",rnd["group_id"],until,target)
  else:
   await conn.execute("UPDATE ad_requests SET status='paid',paid_at=now(),updated_at=now() WHERE id=$1 AND status='approved_unpaid'",payment["reference_id"])
  return str(payment["purpose"])

async def buy_with_treasury(chat_id:int,player_id:int)->int:
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT g.id,c.id country_id,c.treasury_toman,c.president_player_id,(SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens FROM groups g JOIN countries c ON c.group_id=g.id WHERE g.telegram_id=$1 FOR UPDATE OF c,g",chat_id)
  if not row:raise ValueError("country_not_found")
  if row["president_player_id"]!=player_id:raise PermissionError("president_required")
  price=treasury_price(int(row["treasury_toman"]),int(row["citizens"]));until=await conn.fetchval("UPDATE groups SET ad_free_until=GREATEST(COALESCE(ad_free_until,now()),now())+interval '30 days' WHERE id=$1 RETURNING ad_free_until",row["id"])
  changed=await conn.fetchval("UPDATE countries SET treasury_toman=treasury_toman-$2 WHERE id=$1 AND treasury_toman>=$2 RETURNING treasury_toman",row["country_id"],price)
  if changed is None:raise ValueError("insufficient_balance")
  await conn.execute("INSERT INTO group_subscription_events(group_id,source,treasury_toman,starts_at,ends_at,actor_player_id) VALUES($1,'treasury',$2,now(),$3,$4)",row["id"],price,until,player_id)
  return price

async def approve_ad(ad_id:int,actor:str,note:str|None=None):
 return await db.fetchrow("UPDATE ad_requests SET status='approved_unpaid',approved_by=$2,admin_note=$3,approved_at=now(),payment_expires_at=now()+interval '48 hours',updated_at=now() WHERE id=$1 AND status IN ('pending_review','changes_requested') RETURNING *",ad_id,actor,note)
async def reject_ad(ad_id:int,actor:str,note:str):
 return await db.fetchrow("UPDATE ad_requests SET status='changes_requested',approved_by=$2,admin_note=$3,updated_at=now() WHERE id=$1 AND status IN ('pending_review','approved_unpaid') RETURNING *",ad_id,actor,note)

async def list_ads(limit:int=100):
 return await db.fetch("""SELECT a.id,a.package_code,a.channel,a.title,a.description,a.target_url,a.image_mime,a.status,a.price_stars,a.impressions_planned,a.campaign_hours,a.admin_note,a.requested_start_at,a.payment_expires_at,a.paid_at,a.first_delivery_at,a.created_at,p.telegram_id,p.first_name,
 count(d.id) FILTER(WHERE d.status='sent') delivered,count(d.id) FILTER(WHERE d.status IN ('scheduled','queued')) pending,count(d.id) FILTER(WHERE d.status='failed') failed
 FROM ad_requests a JOIN players p ON p.id=a.requester_player_id LEFT JOIN ad_deliveries d ON d.ad_request_id=a.id GROUP BY a.id,p.telegram_id,p.first_name ORDER BY a.created_at DESC LIMIT $1""",limit)
async def ad_image(ad_id:int):return await db.fetchrow("SELECT image_bytes,image_mime FROM ad_requests WHERE id=$1",ad_id)
async def edit_ad(ad_id:int,title:str,description:str,url:str,start_at):
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 return await db.fetchrow("UPDATE ad_requests SET title=$2,description=$3,target_url=$4,requested_start_at=$5,updated_at=now() WHERE id=$1 AND status IN ('pending_review','changes_requested','approved_unpaid') RETURNING *",ad_id,title,description,url,start_at)
async def pause_ad(ad_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("UPDATE ad_requests SET status='paused',updated_at=now() WHERE id=$1 AND status IN ('paid','active') RETURNING *",ad_id)
  if row:await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE ad_request_id=$1 AND status IN ('scheduled','queued')",ad_id)
  return row
async def refundable(ad_id:int):
 return await db.fetchrow("""SELECT a.*,p.telegram_id,sp.telegram_charge_id FROM ad_requests a JOIN players p ON p.id=a.requester_player_id JOIN star_payments sp ON sp.purpose='advertisement' AND sp.reference_id=a.id AND sp.status='paid' WHERE a.id=$1 AND a.first_delivery_at IS NULL""",ad_id)
async def mark_refunded(ad_id:int):
 async with db.transaction() as conn:
  await conn.execute("UPDATE star_payments SET status='refunded',refunded_at=now() WHERE purpose='advertisement' AND reference_id=$1 AND status='paid'",ad_id)
  await conn.execute("UPDATE ad_requests SET status='refunded',updated_at=now() WHERE id=$1",ad_id)
  await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE ad_request_id=$1 AND status IN ('scheduled','queued')",ad_id)
async def expire_commerce()->dict[str,int]:
 p=await db.execute("UPDATE ad_requests SET status='payment_expired',updated_at=now() WHERE status='approved_unpaid' AND payment_expires_at<=now()")
 s=await db.execute("UPDATE star_payments SET status='expired' WHERE status='invoiced' AND expires_at<=now()")
 return {"ads":int(p.rsplit(' ',1)[-1]),"payments":int(s.rsplit(' ',1)[-1])}
async def plan_paid_ads()->int:
 count=0
 async with db.transaction() as conn:
  ads=await conn.fetch("SELECT * FROM ad_requests WHERE status='paid' FOR UPDATE SKIP LOCKED LIMIT 20")
  for ad in ads:
   start=max(datetime.now(UTC),ad["requested_start_at"] or datetime.now(UTC));n=max(1,int(ad["impressions_planned"]));hours=int(ad["campaign_hours"])
   if ad["channel"] in {'world','both'}:
    groups=await conn.fetch("SELECT id,telegram_id FROM groups WHERE is_active AND last_active_at>=now()-interval '14 days' AND (ad_free_until IS NULL OR ad_free_until<=now())")
    for group in groups:
     for slot in range(n):
      when=start+timedelta(seconds=(hours*3600*slot/max(1,n-1) if n>1 else 0));result=await conn.execute("INSERT INTO ad_deliveries(ad_request_id,group_id,destination_type,destination_telegram_id,slot_no,scheduled_at) VALUES($1,$2,'world',$3,$4,$5) ON CONFLICT DO NOTHING",ad["id"],group["id"],group["telegram_id"],slot+1,when);count+=int(result.rsplit(' ',1)[-1])
   if ad["channel"] in {'life','both'}:
    players=await conn.fetch("SELECT telegram_id FROM players WHERE NOT is_banned AND NOT is_frozen AND last_seen_at>=now()-interval '30 days'")
    for person in players:
     for slot in range(n):
      when=start+timedelta(seconds=(hours*3600*slot/max(1,n-1) if n>1 else 0));result=await conn.execute("INSERT INTO ad_deliveries(ad_request_id,group_id,destination_type,destination_telegram_id,slot_no,scheduled_at) VALUES($1,NULL,'life',$2,$3,$4) ON CONFLICT DO NOTHING",ad["id"],person["telegram_id"],slot+1,when);count+=int(result.rsplit(' ',1)[-1])
   await conn.execute("UPDATE ad_requests SET status='active',updated_at=now() WHERE id=$1",ad["id"])
 return count
async def queue_due_deliveries()->int:
 from packages.core.repositories import outbox_repo
 count=0
 async with db.transaction() as conn:
  rows=await conn.fetch("""SELECT d.*,g.ad_free_until,g.ads_delivered_today,g.ads_delivery_day,a.priority FROM ad_deliveries d JOIN ad_requests a ON a.id=d.ad_request_id LEFT JOIN groups g ON g.id=d.group_id WHERE d.status='scheduled' AND d.scheduled_at<=now() AND a.status='active' ORDER BY a.priority DESC,d.scheduled_at FOR UPDATE OF d SKIP LOCKED LIMIT 200""")
  for row in rows:
   today=datetime.now(UTC).date()
   if row["destination_type"]=='world':
    used=int(row["ads_delivered_today"] if row["ads_delivery_day"]==today else 0)
    if row["ad_free_until"] and row["ad_free_until"]>datetime.now(UTC):await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE id=$1",row["id"]);continue
    if used>=2:await conn.execute("UPDATE ad_deliveries SET scheduled_at=date_trunc('day',now())+interval '1 day 9 hours' WHERE id=$1",row["id"]);continue
   key=f"market-ad:{row['id']}"
   if await outbox_repo.enqueue(conn,key,"marketplace_ad",{"ad_id":row["ad_request_id"],"delivery_id":row["id"],"destination_type":row["destination_type"]},row["destination_telegram_id"]):
    await conn.execute("UPDATE ad_deliveries SET status='queued',outbox_key=$2 WHERE id=$1",row["id"],key)
    if row["destination_type"]=='world':await conn.execute("UPDATE groups SET ads_delivered_today=$2,ads_delivery_day=$3 WHERE id=$1",row["group_id"],used+1,today)
    count+=1
  return count

async def player_ads(player_id:int):
 return await db.fetch("SELECT id,title,status,admin_note,price_stars,payment_expires_at FROM ad_requests WHERE requester_player_id=$1 ORDER BY created_at DESC LIMIT 20",player_id)
async def revision_source(ad_id:int,player_id:int):
 return await db.fetchrow("SELECT * FROM ad_requests WHERE id=$1 AND requester_player_id=$2 AND status='changes_requested'",ad_id,player_id)
async def submit_revision(ad_id:int,player_id:int,title:str,description:str,url:str,image_bytes:bytes|None,image_mime:str|None,start_at)->bool:
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 result=await db.execute("""UPDATE ad_requests SET title=$3,description=$4,target_url=$5,image_bytes=COALESCE($6,image_bytes),image_mime=COALESCE($7,image_mime),requested_start_at=$8,status='pending_review',admin_note=NULL,approved_by=NULL,approved_at=NULL,payment_expires_at=NULL,updated_at=now() WHERE id=$1 AND requester_player_id=$2 AND status='changes_requested'""",ad_id,player_id,title,description,url,image_bytes,image_mime,start_at)
 return result!='UPDATE 0'
```

### `packages\core\services\content_filter.py`

```python
"""Unicode-aware Persian content moderation with bounded obfuscation detection.

The matcher is deliberately boundary-aware: it catches separators and repeated letters
inside a blocked token, but does not reject a longer innocent word merely because it
contains the same substring.
"""
from __future__ import annotations
from dataclasses import dataclass
import re
import unicodedata

@dataclass(frozen=True, slots=True)
class ModerationResult:
    allowed: bool
    category: str | None = None

# Keep the public response generic; never echo an offensive value back to a group.
TERMS: dict[str, tuple[str, ...]] = {
    "sexual": ("کون", "کس", "کیر", "جنده", "پورن", "سکس"),
    "insult": ("حرومزاده", "بی ناموس", "مادر قحبه", "کصخل"),
    "political_extremism": ("داعش", "نازی", "فاشیست"),
}
_CHAR_MAP = str.maketrans({"ي":"ی", "ى":"ی", "ك":"ک", "ة":"ه", "ۀ":"ه", "ؤ":"و", "إ":"ا", "أ":"ا"})
_SEP = r"[\s\-_.ـ‌‍]*"
_WORD = r"\w"

def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).translate(_CHAR_MAP).casefold()
    value = "".join(ch for ch in value if unicodedata.category(ch) not in {"Mn", "Cf"})
    return value

def _pattern(term: str) -> re.Pattern[str]:
    chars = [c for c in normalize(term) if c.isalnum()]
    body = _SEP.join(re.escape(c) + "+" for c in chars)
    # Persian has no case distinction; Unicode word boundaries prevent false positives
    # such as the blocked token being only the prefix of a longer name.
    return re.compile(rf"(?<!{_WORD}){body}(?!{_WORD})", re.UNICODE)

_PATTERNS = [(category, _pattern(term)) for category, terms in TERMS.items() for term in terms]

def inspect(text: str) -> ModerationResult:
    value = normalize(text)
    for category, pattern in _PATTERNS:
        if pattern.search(value):
            return ModerationResult(False, category)
    return ModerationResult(True)

def require_clean(text: str, field: str = "content") -> None:
    result = inspect(text)
    if not result.allowed:
        raise ValueError(f"inappropriate_{field}")
```

### `packages\core\services\country.py`

```python
"""Country lifecycle, membership and deterministic initial-resource allocation."""
from __future__ import annotations
import hashlib, random
import asyncpg
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, group_repo, ledger_repo
from packages.core.services.content_filter import require_clean


def _resources(chat_id: int, name: str) -> dict[str, int]:
    spec = get_config().section("country.resources")
    codes = sorted(str(c) for c in spec["asset_codes"])
    total, low, high = int(spec["country_total"]), int(spec["minimum_share"]), int(spec["maximum_share"])
    if not codes: raise ValueError("no_asset_codes_configured")
    if low > high: raise ValueError("minimum_share_above_maximum_share")
    if not low * len(codes) <= total <= high * len(codes): raise ValueError("country_total_outside_share_bounds")
    digest = hashlib.sha256(f"{spec['allocation_seed_namespace']}:{chat_id}:{name}".encode()).digest()
    rng = random.Random(int.from_bytes(digest[:8], "big")); values = dict.fromkeys(codes, low)
    remaining = total - low * len(codes)
    while remaining:
        choices = [c for c in codes if values[c] < high]
        code = rng.choice(choices); take = min(remaining, high-values[code], rng.randint(1, remaining))
        values[code] += take; remaining -= take
    return values


async def _refresh_status(conn: asyncpg.Connection, country_id: int) -> str:
    cfg = get_config(); row = await conn.fetchrow(
        """SELECT c.status, c.president_player_id,
                  count(cs.player_id) FILTER (WHERE cs.is_active) AS citizens
           FROM countries c LEFT JOIN citizenships cs ON cs.country_id=c.id
           WHERE c.id=$1 GROUP BY c.id""", country_id)
    if row is None: raise ValueError("country_not_found")
    citizens = int(row["citizens"] or 0)
    temporary_min = cfg.int_("country.lifecycle.temporary_min_citizens")
    official_min = cfg.int_("country.lifecycle.official_min_citizens")
    leader_ok = row["president_player_id"] is not None or not cfg.bool_("country.lifecycle.require_elected_leader_for_official", True)
    target = "official" if citizens >= official_min and leader_ok else "temporary" if citizens >= temporary_min else "forming"
    await conn.execute(
        """UPDATE countries SET status=$2,
           temporary_at=CASE WHEN $2 IN ('temporary','official') THEN COALESCE(temporary_at,now()) ELSE temporary_at END,
           official_at=CASE WHEN $2='official' THEN COALESCE(official_at,now()) ELSE NULL END
           WHERE id=$1""", country_id, target)
    return target


async def refresh_status(country_id: int) -> str:
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE", country_id)
        return await _refresh_status(conn, country_id)


async def create_country(*, chat_id: int, chat_title: str, player_id: int,
                         name: str, government: str, description: str) -> asyncpg.Record:
    cfg=get_config(); name=name.strip(); description=description.strip()
    if government not in set(cfg.get("country.government_types")): raise ValueError("invalid_government")
    require_clean(name, "name")
    require_clean(description, "description")
    rules=cfg.section("country.validation")
    if not int(rules["name_min_length"]) <= len(name) <= int(rules["name_max_length"]): raise ValueError("invalid_name")
    if not int(rules["description_min_length"]) <= len(description) <= int(rules["description_max_length"]): raise ValueError("invalid_description")
    group=await group_repo.get_or_create(chat_id,chat_title)
    resources=_resources(chat_id,name)
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM groups WHERE id=$1 FOR UPDATE",group.id)
        if await conn.fetchval("SELECT 1 FROM countries WHERE group_id=$1",group.id): raise ValueError("country_already_exists")
        current=await conn.fetchrow("SELECT country_id,is_active FROM citizenships WHERE player_id=$1 FOR UPDATE",player_id)
        if current and current["is_active"]: raise ValueError("already_citizen_elsewhere")
        row=await country_repo.create(conn,group.id,player_id,name,government,description,
                                      cfg.int_("country.creation.protection_days"),resources)
        for asset,qty in resources.items():
            ok=await ledger_repo.insert(conn,player_id=None,country_id=int(row["id"]),
                key=f"country-genesis:{row['id']}:{asset}",reason="country_genesis",
                asset=asset,account=ledger_repo.country_account(asset),amount=qty,balance=qty,
                metadata={"created_by":player_id})
            if not ok: raise RuntimeError("country_genesis_ledger_conflict")
        await _refresh_status(conn,int(row["id"]))
        return await conn.fetchrow("SELECT * FROM countries WHERE id=$1",row["id"])


async def join_country(*, chat_id: int, player_id: int) -> bool:
    country=await country_repo.by_chat(chat_id)
    if country is None: raise ValueError("country_not_found")
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country["id"])
        current=await conn.fetchrow("SELECT country_id,is_active FROM citizenships WHERE player_id=$1 FOR UPDATE",player_id)
        if current and current["is_active"]:
            if int(current["country_id"]) == int(country["id"]): return False
            raise ValueError("migration_required")
        if current:
            await conn.execute("UPDATE citizenships SET country_id=$2,is_active=TRUE,left_at=NULL,joined_at=now() WHERE player_id=$1",player_id,country["id"])
            joined=True
        else:
            joined=await country_repo.join(conn,player_id,int(country["id"]))
        await _refresh_status(conn,int(country["id"]))
        return joined


async def leave_country(*, chat_id: int, player_id: int) -> bool:
    country=await country_repo.by_chat(chat_id)
    if country is None: return False
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country["id"])
        changed=await conn.fetchval("""UPDATE citizenships SET is_active=FALSE,left_at=now()
          WHERE player_id=$1 AND country_id=$2 AND is_active RETURNING player_id""",player_id,country["id"])
        if changed:
            await conn.execute("UPDATE countries SET president_player_id=NULL WHERE id=$1 AND president_player_id=$2",country["id"],player_id)
            await _refresh_status(conn,int(country["id"]))
        return changed is not None
```

### `packages\core\services\country_economy.py`

```python
"""Idempotent daily country income/expense settlement."""

from __future__ import annotations

from datetime import date, timedelta

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

_IRT = "IRT"


async def settle_day(country_id: int, day: date) -> bool:
    """Settle one country-day. Returns False when already settled."""
    key = f"country-economy:{country_id}:{day}"

    async with db.transaction() as conn:
        # Lock first, then check: checking before locking leaves a window
        # where two schedulers both see "not settled yet".
        row = await ledger_repo.lock_country(conn, country_id)
        if row is None:
            return False
        if await ledger_repo.idempotency_exists(conn, key):
            return False

        cfg = get_config()
        income = int(row["daily_income_toman"]) + cfg.int_(
            "economy.country.daily_base_income_toman"
        )
        expense = int(row["daily_expense_toman"]) + cfg.int_(
            "economy.country.daily_base_expense_toman"
        )
        delta = income - expense
        if delta < 0:
            # Never drive the treasury below zero; the CHECK would abort the
            # whole scheduler batch instead of just skipping this country.
            delta = max(delta, -int(row["treasury_toman"]))

        balance = await ledger_repo.change_country(conn, country_id, _IRT, delta)
        await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=key,
            reason="country_daily_economy",
            asset=_IRT,
            account="treasury",
            amount=delta,
            balance=balance,
            metadata={"date": str(day), "income": income, "expense": expense},
        )
        await conn.execute(
            """
            INSERT INTO country_economy_daily
                (country_id, economy_date, income_toman, expense_toman,
                 closing_treasury, ledger_key)
            VALUES ($1, $2, $3, $4, $5, $6)
            ON CONFLICT DO NOTHING
            """,
            country_id,
            day,
            income,
            expense,
            balance,
            key,
        )
        return True


async def catch_up(today: date | None = None) -> int:
    """Settle any missed days after downtime. Returns settlements performed."""
    end = today or clock.game_today()
    days = get_config().int_("economy.country.catch_up_days")
    rows = await db.fetch("SELECT id FROM countries ORDER BY id")

    settled = 0
    for row in rows:
        for offset in range(days - 1, -1, -1):
            if await settle_day(int(row["id"]), end - timedelta(days=offset)):
                settled += 1
    return settled
```

### `packages\core\services\country_identity.py`

```python
"""Canonical country identity for every group-facing system message."""
from __future__ import annotations
from html import escape
from packages.core import db

SETUP_TEXT="🏗 این گروه هنوز کشور ثبت‌شده ندارد.\n\nیکی از مدیران گروه وارد TeleWorld شود و از «ساخت کشور» نام، حکومت و مشخصات کشور را کامل کند. تا آن زمان خبرها و رویدادهای سیستمی این گروه منتشر نمی‌شوند."

async def destination(chat_id:int):
 """Return None for non-world destinations, or a row with nullable country fields."""
 return await db.fetchrow("""SELECT g.id group_id,g.telegram_id,c.id country_id,c.name country_name,c.status
  FROM groups g LEFT JOIN countries c ON c.group_id=g.id WHERE g.telegram_id=$1""",chat_id)

async def by_chat(chat_id:int):
 row=await destination(chat_id)
 return row if row and row["country_id"] else None

def masthead(country_name:str, text:str)->str:
 return f"🏛 <b>خبرگزاری {escape(country_name)}</b>\n\n{text}"

async def should_send_setup_notice(chat_id:int)->bool:
 key=f"missing-country-notice:{chat_id}"
 return bool(await db.fetchval("""INSERT INTO product_audit_log(event_key,event_type,chat_id,details)
  VALUES($1,'missing_country_notice',$2,'{}'::jsonb) ON CONFLICT DO NOTHING RETURNING id""",key,chat_id))
```

### `packages\core\services\country_missions.py`

```python
"""Country missions: instantiate on action, track progress, pay out once."""

from __future__ import annotations

import hashlib
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import mission_repo, outbox_repo
from packages.core.utils import clock


def _pick_key(country_id: int, day: Any, keys: list[str]) -> str:
    """Deterministic daily pick, stable across restarts and workers."""
    namespace = get_config().get(
        "country_missions.daily.selection_seed_namespace", "country_missions"
    )
    seed = hashlib.sha256(f"{namespace}:{country_id}:{day}".encode()).digest()
    return keys[int.from_bytes(seed[:4], "big") % len(keys)]


async def report(country_id: int, action: str, asset: str, amount: int) -> bool:
    """Report a player action. Returns True only when a mission just paid out."""
    if amount <= 0:
        return False

    cfg = get_config()
    mapping = cfg.get(f"country_missions.progress.eligible_actions.{action}", {})
    if not isinstance(mapping, dict) or asset not in mapping:
        return False

    metric = str(mapping[asset])
    pool = cfg.section("country_missions.pool")
    keys = sorted(k for k, spec in pool.items() if spec["metric_key"] == metric)
    if not keys:
        return False

    day = clock.game_today()
    key = _pick_key(country_id, day, keys)
    spec = pool[key]

    async with db.transaction() as conn:
        await mission_repo.ensure(
            conn,
            country_id,
            day,
            key,
            metric,
            int(spec["target_amount"]),
            cfg.get("country_missions.reward.ledger_asset_code"),
            int(spec["reward_amount"]),
        )
        row = await mission_repo.add(conn, country_id, day, metric, amount)
        if row is None or row["completed_at"] is None:
            return False
        if not await mission_repo.reward_once(conn, country_id, day, key):
            return False

        await mission_repo.effect(
            conn,
            country_id,
            cfg.get("country_missions.reward.effect_code"),
            int(spec["reward_magnitude_basis_points"]),
            f"{day}:{key}",
            cfg.int_("country_missions.reward.effect_duration_hours"),
        )
        destination = await conn.fetchval(
            """
            SELECT g.telegram_id FROM countries c
            JOIN groups g ON g.id = c.group_id
            WHERE c.id = $1
            """,
            country_id,
        )
        await outbox_repo.enqueue(
            conn,
            f"country-mission:{country_id}:{day}:{key}",
            "country_mission_completed",
            {"country_id": country_id, "mission_key": key},
            destination,
        )
        return True
```

### `packages\core\services\country_realism.py`

```python
"""Deterministic daily macro economy, rare shocks, and country newspaper."""
from __future__ import annotations
import hashlib
from datetime import UTC,datetime
from packages.core import db
from packages.core.repositories import outbox_repo

def _roll(country_id:int, day, salt:str, modulo:int)->int:
 return int.from_bytes(hashlib.sha256(f"{country_id}:{day}:{salt}".encode()).digest()[:4],"big")%modulo

async def daily_tick()->dict[str,int]:
 day=datetime.now(UTC).date();indicators=shocks=papers=0
 async with db.transaction() as conn:
  countries=await conn.fetch("""SELECT c.*,g.telegram_id,
   COALESCE((SELECT sum(quantity) FROM country_resources r WHERE r.country_id=c.id),0) resources,
   (SELECT count(*) FROM citizenships z WHERE z.country_id=c.id AND z.is_active) citizens
   FROM countries c JOIN groups g ON g.id=c.group_id WHERE g.is_active""")
  for c in countries:
   citizens=int(c['citizens'] or 0);resources=int(c['resources'] or 0);treasury=int(c['treasury_toman'])
   prev=await conn.fetchrow("SELECT * FROM country_indicator_daily WHERE country_id=$1 ORDER BY indicator_date DESC LIMIT 1",c['id'])
   active=await conn.fetchrow("SELECT * FROM country_shocks WHERE country_id=$1 AND ends_at>now() ORDER BY starts_at DESC LIMIT 1",c['id'])
   adverse=bool(active and active['shock_code'] in {'sanctions','drought'})
   reserve_buffer=min(250,int(c['fx_reserve_cents'])//1_000_000) if adverse else 0
   shock_inflation=max(100,500-reserve_buffer) if adverse else -150 if active else 0
   shock_growth=min(-75,-350+reserve_buffer) if adverse else 450 if active else 0
   base_inflation=int(prev['inflation_bp']) if prev else 1800
   policy_gap=int(c['interest_rate_bp'])-int(c['inflation_target_bp'])
   inflation=max(-500,min(100000,base_inflation-policy_gap//20+shock_inflation+_roll(c['id'],day,'inflation',101)-50))
   unemployment=max(0,min(10000,(int(prev['unemployment_bp']) if prev else 1200)-shock_growth//4+_roll(c['id'],day,'jobs',61)-30))
   interest_drag=max(0,policy_gap)//25
   organic_growth=250+resources//max(1000,citizens*100)-unemployment//20-interest_drag
   growth=max(-10000,min(10000,organic_growth+shock_growth))
   satisfaction=max(0,min(100,70-inflation//150-unemployment//200+min(15,treasury//max(1,50_000_000))))
   gdp=max(0,citizens*5_000_000+resources*1000+treasury//10)
   result=await conn.execute("""INSERT INTO country_indicator_daily(country_id,indicator_date,inflation_bp,unemployment_bp,satisfaction,growth_bp,gdp_toman)
    VALUES($1,$2,$3,$4,$5,$6,$7) ON CONFLICT DO NOTHING""",c['id'],day,inflation,unemployment,satisfaction,growth,gdp)
   indicators+=int(result.rsplit(' ',1)[-1])
   shock=None
   if not active and _roll(c['id'],day,'shock',1000)<8:
    code=('sanctions','drought','export_boom')[_roll(c['id'],day,'kind',3)]
    title={'sanctions':'موج تازه تحریم تجاری','drought':'خشکسالی در مناطق تولیدی','export_boom':'رونق ناگهانی صادرات'}[code]
    effects={'inflation_bp':500,'growth_bp':-350} if code!='export_boom' else {'inflation_bp':-150,'growth_bp':450}
    shock=await conn.fetchrow("""INSERT INTO country_shocks(country_id,shock_code,title,effects,ends_at,announced_at)
      VALUES($1,$2,$3,$4,now()+interval '3 days',now()) RETURNING id,title""",c['id'],code,title,effects);shocks+=1
   headline=(shock['title'] if shock else f"نبض اقتصاد {c['name']}: رشد {growth/100:+.1f}٪")
   body=f"تورم {inflation/100:.1f}٪ · بیکاری {unemployment/100:.1f}٪ · رشد {growth/100:+.1f}٪ · رضایت {satisfaction} از ۱۰۰\nنرخ بهره بانک مرکزی {int(c['interest_rate_bp'])/100:.1f}٪ و ذخیره ارزی {int(c['fx_reserve_cents'])/100:,.0f} دلار است."
   row=await conn.fetchrow("""INSERT INTO country_newspapers(country_id,issue_date,headline,body,indicators,shock_id)
    VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING country_id""",c['id'],day,headline,body,{'inflation_bp':inflation,'unemployment_bp':unemployment,'growth_bp':growth,'satisfaction':satisfaction},shock['id'] if shock else None)
   if row:
    text=f"🗞 <b>{headline}</b>\n\n{body}"
    if await outbox_repo.enqueue(conn,f"country-paper:{c['id']}:{day}","country_newspaper",{'text':text},c['telegram_id']):papers+=1
 return {'indicators':indicators,'shocks':shocks,'newspapers':papers}


async def policy_view(country_id:int):
 return await db.fetchrow("""SELECT c.interest_rate_bp,c.inflation_target_bp,c.fx_reserve_cents,c.treasury_toman,
  i.inflation_bp,i.unemployment_bp,i.satisfaction,i.growth_bp,i.gdp_toman,i.indicator_date
  FROM countries c LEFT JOIN LATERAL(SELECT * FROM country_indicator_daily WHERE country_id=c.id ORDER BY indicator_date DESC LIMIT 1)i ON TRUE
  WHERE c.id=$1""",country_id)

async def set_interest(country_id:int,player_id:int,delta_bp:int):
 if delta_bp not in {-100,100}:raise ValueError('invalid_policy_step')
 return await db.fetchval("""UPDATE countries SET interest_rate_bp=interest_rate_bp+$3,updated_at=now()
  WHERE id=$1 AND president_player_id=$2 AND interest_rate_bp+$3 BETWEEN 0 AND 10000 RETURNING interest_rate_bp""",country_id,player_id,delta_bp)

async def buy_reserve(country_id:int,player_id:int,toman:int=10_000_000):
 if toman<=0:raise ValueError('invalid_amount')
 async with db.transaction() as conn:
  price=int(await conn.fetchval("SELECT current_price_toman FROM market_prices WHERE asset_code='USD'") or 0)
  if price<=0:raise ValueError('market_not_initialized')
  cents=toman*100//price
  row=await conn.fetchrow("""UPDATE countries SET treasury_toman=treasury_toman-$3,fx_reserve_cents=fx_reserve_cents+$4,updated_at=now()
   WHERE id=$1 AND president_player_id=$2 AND treasury_toman>=$3 RETURNING fx_reserve_cents""",country_id,player_id,toman,cents)
  if not row:raise ValueError('president_or_balance_required')
  return cents
```

### `packages\core\services\daily.py`

```python
"""Daily reward + streak engine.

Streak philosophy: missing one day drops you to `grace_reset_to`, not zero.
Wiping a 90-day streak over one bad day is how games lose players permanently.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.utils import clock


@dataclass(slots=True, frozen=True)
class DailyResult:
    claimed: bool
    already_claimed: bool
    streak: int
    best_streak: int
    reward_toman: int
    reward_xp: int
    milestone_label: str | None
    milestone_toman: int
    next_milestone: int | None


def _reward_for(streak: int) -> tuple[int, int]:
    cfg = get_config()
    base = cfg.int_("daily.reward.base_toman")
    step = cfg.float_("daily.reward.streak_multiplier_per_day")
    cap = cfg.float_("daily.reward.max_multiplier")
    multiplier = min(1.0 + step * max(0, streak - 1), cap)
    return int(base * multiplier), cfg.int_("daily.reward.xp")


def _milestone(streak: int) -> dict[str, Any] | None:
    milestones = get_config().section("daily.milestones")
    spec = milestones.get(streak, milestones.get(str(streak)))
    return dict(spec) if spec else None


def _next_milestone(streak: int) -> int | None:
    keys = sorted(int(k) for k in get_config().section("daily.milestones"))
    return next((k for k in keys if k > streak), None)


def _next_streak(last: date | None, today: date) -> tuple[int, bool]:
    """Return (mode, is_continuation).

    mode ==  0 -> already claimed today
    mode == -1 -> continue the streak (increment existing)
    mode >   0 -> restart the streak at this value
    """
    if last is None:
        return 1, False
    gap = (today - last).days
    if gap <= 0:
        return 0, True
    grace = get_config().int_("daily.streak.break_after_days")
    if gap <= max(1, grace):
        return -1, True
    return get_config().int_("daily.streak.grace_reset_to"), False


async def claim(player_id: int, today: date | None = None) -> DailyResult:
    """Claim today's reward. Idempotent per calendar day, enforced in SQL."""
    today = today or clock.game_today()
    cfg = get_config()

    async with db.transaction() as conn:
        # Create the row if missing, then take the row lock in one statement.
        await conn.execute(
            "INSERT INTO daily_state (player_id) VALUES ($1) ON CONFLICT DO NOTHING",
            player_id,
        )
        row = await conn.fetchrow(
            "SELECT streak, best_streak, last_claim_date FROM daily_state "
            "WHERE player_id = $1 FOR UPDATE",
            player_id,
        )
        if row is None:  # pragma: no cover - player row vanished mid-transaction
            raise ValueError(f"player {player_id} not found")

        streak = int(row["streak"])
        best = int(row["best_streak"])
        last: date | None = row["last_claim_date"]

        mode, _ = _next_streak(last, today)
        if mode == 0:
            return DailyResult(
                claimed=False,
                already_claimed=True,
                streak=streak,
                best_streak=best,
                reward_toman=0,
                reward_xp=0,
                milestone_label=None,
                milestone_toman=0,
                next_milestone=_next_milestone(streak),
            )

        new_streak = streak + 1 if mode == -1 else mode
        new_best = max(best, new_streak)

        reward_toman, reward_xp = _reward_for(new_streak)
        milestone = _milestone(new_streak)
        milestone_toman = int(milestone["toman"]) if milestone else 0
        milestone_xp = int(milestone["xp"]) if milestone else 0
        total_toman = reward_toman + milestone_toman

        await conn.execute(
            """
            UPDATE daily_state SET
                streak          = $2,
                best_streak     = $3,
                last_claim_date = $4,
                total_claims    = total_claims + 1
            WHERE player_id = $1
            """,
            player_id,
            new_streak,
            new_best,
            today,
        )

        balance = await conn.fetchval(
            """
            UPDATE players SET
                wallet_toman = wallet_toman + $2,
                happiness    = LEAST(100, happiness + $3)
            WHERE id = $1
            RETURNING wallet_toman
            """,
            player_id,
            total_toman,
            cfg.int_("daily.happiness.claim_bonus"),
        )
        if balance is None:
            raise ValueError(f"player {player_id} not found")

        ledger_id = await conn.fetchval(
            """
            INSERT INTO ledger
                (player_id, idempotency_key, reason, currency, asset_code, account,
                 amount, balance_after, metadata)
            VALUES ($1, $2, 'daily_reward', 'IRT', 'IRT', 'wallet', $3, $4, $5)
            ON CONFLICT (idempotency_key) DO NOTHING RETURNING id
            """,
            player_id,
            f"daily:{player_id}:{today:%Y-%m-%d}",
            total_toman,
            balance,
            {"streak": new_streak, "milestone": bool(milestone)},
        )
        if ledger_id is None:
            # A money mutation without its immutable ledger leg must never commit.
            raise RuntimeError("daily_ledger_conflict")

        return DailyResult(
            claimed=True,
            already_claimed=False,
            streak=new_streak,
            best_streak=new_best,
            reward_toman=total_toman,
            reward_xp=reward_xp + milestone_xp,
            milestone_label=str(milestone["label"]) if milestone else None,
            milestone_toman=milestone_toman,
            next_milestone=_next_milestone(new_streak),
        )


async def state(player_id: int) -> tuple[int, int, date | None]:
    row = await db.fetchrow(
        "SELECT streak, best_streak, last_claim_date FROM daily_state WHERE player_id = $1",
        player_id,
    )
    if row is None:
        return 0, 0, None
    return int(row["streak"]), int(row["best_streak"]), row["last_claim_date"]


def claimable(last: date | None, today: date | None = None) -> bool:
    today = today or clock.game_today()
    return last is None or (today - last).days >= 1


def preview(streak: int) -> int:
    """Reward the player would receive at the given streak day."""
    return _reward_for(streak)[0]


def tomorrow_preview(streak: int) -> int:
    return _reward_for(streak + 1)[0]
```

### `packages\core\services\economy.py`

```python
"""Atomic, idempotent movement of player and country assets."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo

@dataclass(slots=True, frozen=True)
class TransferResult:
    applied: bool
    source_balance: int
    target_balance: int


def _validate_amount(asset: str, amount: int) -> None:
    cfg = get_config()
    if amount <= 0:
        raise ValueError("invalid_amount")
    if asset == "IRT":
        low = cfg.int_("economy.limits.min_transaction_toman")
        high = cfg.int_("economy.limits.max_transaction_toman")
    else:
        low = cfg.int_("economy.limits.min_resource_transaction")
        high = cfg.int_("economy.limits.max_resource_transaction")
    if not low <= amount <= high:
        raise ValueError("amount_out_of_bounds")


async def transfer(player_id: int, country_id: int, asset: str, amount: int, *,
                   reason: str, idempotency_key: str) -> TransferResult:
    _validate_amount(asset, amount)
    cfg = get_config()
    debit_key = f"{idempotency_key}:{cfg.get('economy.ledger.transfer_legs.debit_suffix')}"
    credit_key = f"{idempotency_key}:{cfg.get('economy.ledger.transfer_legs.credit_suffix')}"
    async with db.transaction() as conn:
        if await ledger_repo.economy_frozen(conn):
            raise ValueError("economy_frozen")
        player = await ledger_repo.lock_player(conn, player_id)
        country = await ledger_repo.lock_country(conn, country_id)
        if player is None:
            raise ValueError("player_not_found")
        if country is None:
            raise ValueError("country_not_found")
        # The ownership locks serialize retries. Re-check only after both locks.
        if await ledger_repo.idempotency_exists(conn, debit_key):
            return TransferResult(False, 0, 0)
        source = await ledger_repo.change_player(conn, player_id, asset, -amount)
        target = await ledger_repo.change_country(conn, country_id, asset, amount)
        debit_ok = await ledger_repo.insert(
            conn, player_id=player_id, country_id=None, key=debit_key,
            reason=reason, asset=asset, account=ledger_repo.player_account(asset),
            amount=-amount, balance=source, metadata={"country_id": country_id},
        )
        credit_ok = await ledger_repo.insert(
            conn, player_id=None, country_id=country_id, key=credit_key,
            reason=reason, asset=asset, account=ledger_repo.country_account(asset),
            amount=amount, balance=target, metadata={"player_id": player_id},
        )
        if not (debit_ok and credit_ok):
            raise RuntimeError("ledger_transfer_conflict")
        return TransferResult(True, source, target)


async def country_adjust(country_id: int, asset: str, amount: int, *, reason: str,
                         idempotency_key: str, allow_frozen: bool = False) -> int:
    if amount == 0:
        raise ValueError("invalid_amount")
    _validate_amount(asset, abs(amount))
    async with db.transaction() as conn:
        if not allow_frozen and await ledger_repo.economy_frozen(conn):
            raise ValueError("economy_frozen")
        row = await ledger_repo.lock_country(conn, country_id)
        if row is None:
            raise ValueError("country_not_found")
        if await ledger_repo.idempotency_exists(conn, idempotency_key):
            return 0
        balance = await ledger_repo.change_country(conn, country_id, asset, amount)
        inserted = await ledger_repo.insert(
            conn, player_id=None, country_id=country_id, key=idempotency_key,
            reason=reason, asset=asset, account=ledger_repo.country_account(asset),
            amount=amount, balance=balance,
        )
        if not inserted:
            raise RuntimeError("ledger_adjust_conflict")
        return balance
```

### `packages\core\services\elections.py`

```python
"""Election and poll business rules with citizenship authorization."""
from __future__ import annotations
from datetime import timedelta
import asyncpg
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, election_repo
from packages.core.services import country as country_service
from packages.core.services import migration
from packages.core.services.governance import rules_for
from packages.core.utils import clock

async def _active_citizen(country_id:int, player_id:int)->bool:
    return bool(await db.fetchval("SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2 AND is_active",country_id,player_id))

async def start(country_id:int, player_id:int)->asyncpg.Record:
    country=await country_repo.by_id(country_id)
    if country is None: raise ValueError("country_not_found")
    if not await _active_citizen(country_id,player_id): raise PermissionError("citizen_required")
    president=country["president_player_id"]
    rules=rules_for(str(country["government_type"]))
    if not rules.public_elections: raise PermissionError("elections_forbidden_by_government")
    if rules.election_starter=="leader" and (president is None or int(president)!=player_id): raise PermissionError("president_required")
    if rules.election_starter=="citizen" and president is not None and str(country["government_type"]) not in {"republic","presidential","parliamentary","semi_presidential","federal","direct_democracy","constitutional_monarchy","council"} and int(president)!=player_id: raise PermissionError("president_required")
    cfg=get_config(); now=clock.utcnow()
    nom=now+timedelta(hours=cfg.int_("elections.election.nomination_duration_hours"))
    vote=nom+timedelta(hours=cfg.int_("elections.election.voting_duration_hours"))
    try:
        async with db.transaction() as conn:
            await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country_id)
            if await conn.fetchval("SELECT 1 FROM elections WHERE country_id=$1 AND status IN ('nominations','voting')",country_id):
                raise ValueError("election_already_open")
            return await election_repo.start(conn,country_id,player_id,nom,vote)
    except asyncpg.UniqueViolationError as exc:
        raise ValueError("election_already_open") from exc

async def nominate(election_id:int, player_id:int, chat_id:int|None, message_id:int|None)->bool:
    if await migration.political_hold(player_id): raise PermissionError("migrant_political_hold")
    row=await db.fetchrow("SELECT country_id FROM elections WHERE id=$1",election_id)
    if row is None: raise ValueError("election_not_found")
    if not await _active_citizen(int(row["country_id"]),player_id): raise PermissionError("citizen_required")
    return await election_repo.nominate(election_id,player_id,chat_id,message_id)

async def vote(election_id:int, voter:int, candidate:int)->bool:
    if await migration.political_hold(voter): raise PermissionError("migrant_political_hold")
    row=await db.fetchrow("SELECT country_id FROM elections WHERE id=$1",election_id)
    if row is None: raise ValueError("election_not_found")
    cid=int(row["country_id"])
    if not await _active_citizen(cid,voter) or not await _active_citizen(cid,candidate):
        raise PermissionError("citizen_required")
    return await election_repo.vote(election_id,voter,candidate)

async def create_poll(country_id:int,player_id:int,question:str,options:list[str])->asyncpg.Record:
    if not await _active_citizen(country_id,player_id): raise PermissionError("citizen_required")
    cfg=get_config(); question=question.strip()
    if not cfg.int_("elections.poll.question_min_length")<=len(question)<=cfg.int_("elections.poll.question_max_length"): raise ValueError("invalid_question")
    cleaned=[x.strip() for x in options if x.strip()]
    if len(cleaned)!=len(set(cleaned)): raise ValueError("duplicate_options")
    if not cfg.int_("elections.poll.minimum_options")<=len(cleaned)<=cfg.int_("elections.poll.maximum_options"): raise ValueError("invalid_options")
    if any(not cfg.int_("elections.poll.option_min_length")<=len(x)<=cfg.int_("elections.poll.option_max_length") for x in cleaned): raise ValueError("invalid_option_length")
    closes=clock.utcnow()+timedelta(hours=cfg.int_("elections.poll.duration_hours"))
    async with db.transaction() as conn:return await election_repo.create_poll(conn,country_id,player_id,question,closes,cleaned)

async def resolve_due()->dict[str,int]:
    cfg=get_config(); stats={"elections":0,"polls":0}; touched=set()
    async with db.transaction() as conn:
        for row in await election_repo.claim_due(conn,cfg.int_("elections.scheduler.claim_batch_size")):
            if row["status"]=="nominations": await election_repo.advance(conn,row["id"])
            else:
                await election_repo.resolve(conn,row["id"]); touched.add(int(row["country_id"]))
            stats["elections"]+=1
        for row in await election_repo.claim_due_polls(conn,cfg.int_("elections.scheduler.claim_batch_size")):
            await election_repo.resolve_poll(conn,row["id"]);stats["polls"]+=1
    for cid in touched: await country_service.refresh_status(cid)
    return stats

async def override_result(election_id:int,leader_id:int,winner_id:int)->bool:
    row=await db.fetchrow("SELECT e.country_id,c.government_type,c.president_player_id,e.status FROM elections e JOIN countries c ON c.id=e.country_id WHERE e.id=$1",election_id)
    if row is None:raise ValueError("election_not_found")
    rules=rules_for(str(row["government_type"]))
    if not rules.leader_may_override or row["president_player_id"] is None or int(row["president_player_id"])!=leader_id:raise PermissionError("override_forbidden")
    if not await _active_citizen(int(row["country_id"]),winner_id):raise PermissionError("citizen_required")
    async with db.transaction() as conn:
        await conn.execute("UPDATE elections SET winner_player_id=$2,status='completed',resolved_at=now() WHERE id=$1",election_id,winner_id)
        await conn.execute("UPDATE countries SET president_player_id=$2 WHERE id=$1",row["country_id"],winner_id)
    return True
```

### `packages\core\services\engagement.py`

```python
"""Idempotent group engagement: streaks, timed decisions, market alerts and daily digests."""
from __future__ import annotations
from datetime import UTC, datetime
from packages.core import db
from packages.core.repositories import outbox_repo

async def _update_streaks(conn)->int:
    result=await conn.execute("""INSERT INTO group_engagement_state(group_id,streak,best_streak,last_active_date)
      SELECT id,1,1,current_date FROM groups WHERE is_active AND last_active_at>=now()-interval '1 day'
      ON CONFLICT(group_id) DO UPDATE SET
       streak=CASE WHEN group_engagement_state.last_active_date=current_date THEN group_engagement_state.streak
                   WHEN group_engagement_state.last_active_date=current_date-1 THEN group_engagement_state.streak+1 ELSE 1 END,
       best_streak=GREATEST(group_engagement_state.best_streak,
                   CASE WHEN group_engagement_state.last_active_date=current_date-1 THEN group_engagement_state.streak+1 ELSE 1 END),
       last_active_date=current_date,updated_at=now()
      WHERE group_engagement_state.last_active_date IS DISTINCT FROM current_date""")
    return int(result.rsplit(' ',1)[-1])

async def _queue_digest(conn)->int:
    count=0
    rows=await conn.fetch("""SELECT g.id,g.telegram_id,c.name country_name,e.streak,
      (SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens,
      (SELECT current_price_toman FROM market_prices WHERE asset_code='USD') usd
      FROM groups g JOIN countries c ON c.group_id=g.id JOIN group_engagement_state e ON e.group_id=g.id
      WHERE g.is_active AND EXTRACT(HOUR FROM now() AT TIME ZONE 'UTC')=18
       AND e.last_digest_date IS DISTINCT FROM current_date""")
    for row in rows:
      payload={"text":f"📊 خلاصه امروز {row['country_name']}\n\n🔥 زنجیره فعالیت: {row['streak']} روز\n👥 شهروند فعال: {row['citizens']}\n💱 نرخ تتر: {int(row['usd'] or 0):,} تومان\n\nبرای ادامه زنجیره، امروز یک تصمیم گروهی بگیرید."}
      if await outbox_repo.enqueue(conn,f"group-digest:{row['id']}:{datetime.now(UTC).date()}","group_digest",payload,row['telegram_id']):count+=1
      await conn.execute("UPDATE group_engagement_state SET last_digest_date=current_date WHERE group_id=$1",row['id'])
    return count

async def _queue_events(conn)->int:
    count=0
    # One short collective decision per active group every 48h; resolution can be extended later.
    rows=await conn.fetch("""SELECT g.id,g.telegram_id,c.name country_name FROM groups g
      JOIN countries c ON c.group_id=g.id JOIN group_engagement_state s ON s.group_id=g.id
      WHERE g.is_active AND g.last_active_at>=now()-interval '1 day'
       AND (s.last_event_at IS NULL OR s.last_event_at<=now()-interval '48 hours')
       AND NOT EXISTS(SELECT 1 FROM group_live_events e WHERE e.group_id=g.id AND e.status='open') LIMIT 20""")
    for row in rows:
      event=await conn.fetchrow("""INSERT INTO group_live_events(group_id,event_code,title,payload,ends_at)
       VALUES($1,'market_reserve','تصمیم فوری ذخیره ارزی','{"choices":["تقویت خزانه","سرمایه‌گذاری فناوری"]}',now()+interval '45 minutes') RETURNING id,ends_at""",row['id'])
      text=f"⚡ تصمیم فوری برای {row['country_name']}\n\nذخیره تازه‌ای آزاد شده است. اعضا تا ۴۵ دقیقه فرصت دارند درباره «تقویت خزانه» یا «سرمایه‌گذاری فناوری» گفتگو کنند. رئیس‌جمهور تصمیم نهایی را ثبت می‌کند."
      if await outbox_repo.enqueue(conn,f"live-event:{event['id']}","group_live_event",{"text":text,"event_id":event['id']},row['telegram_id']):count+=1
      await conn.execute("UPDATE group_engagement_state SET last_event_at=now() WHERE group_id=$1",row['id'])
    return count

async def _market_alert(conn)->int:
    row=await conn.fetchrow("""SELECT price_toman,captured_at,previous FROM (
      SELECT s.price_toman,s.captured_at,lag(s.price_toman) OVER(ORDER BY s.captured_at) previous
      FROM market_price_snapshots s WHERE s.asset_code='USD') history
      ORDER BY captured_at DESC LIMIT 1""")
    if not row or not row['previous'] or int(row['previous'])==0:return 0
    change=(int(row['price_toman'])-int(row['previous']))*100/int(row['previous'])
    if abs(change)<0.5:return 0
    count=0
    groups=await conn.fetch("SELECT g.id,g.telegram_id,c.name country_name FROM groups g JOIN countries c ON c.group_id=g.id WHERE g.is_active AND g.last_active_at>=now()-interval '7 days'")
    bucket=row['captured_at'].strftime('%Y%m%d%H%M')
    for group in groups:
      text=f"📈 هشدار بازار: تتر {change:+.2f}٪ تغییر کرد و به {int(row['price_toman']):,} تومان رسید."
      if await outbox_repo.enqueue(conn,f"market-alert:{group['id']}:{bucket}","market_alert",{"text":text},group['telegram_id']):count+=1
    return count

async def minute_tick()->dict[str,int]:
    async with db.transaction() as conn:
      await conn.execute("UPDATE group_live_events SET status='expired' WHERE status='open' AND ends_at<=now()")
      return {"streaks":await _update_streaks(conn),"digests":await _queue_digest(conn),"events":await _queue_events(conn),"alerts":await _market_alert(conn)}
```

### `packages\core\services\governance.py`

```python
"""Executable constitutional rules for each government model."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True,slots=True)
class Rules:
    leadership_selection:str
    public_elections:bool
    election_starter:str
    leader_may_override:bool=False
    candidate_screening:bool=False

RULES={
 "republic":Rules("popular","public"=="public","citizen"),
 "presidential":Rules("popular",True,"citizen"),
 "parliamentary":Rules("parliament",True,"citizen"),
 "semi_presidential":Rules("popular",True,"citizen"),
 "federal":Rules("popular",True,"citizen"),
 "direct_democracy":Rules("popular",True,"citizen"),
 "constitutional_monarchy":Rules("parliament",True,"citizen"),
 "council":Rules("council",True,"citizen"),
 "dictatorship":Rules("leader",True,"leader",leader_may_override=True),
 "theocracy":Rules("clerical",True,"leader",candidate_screening=True),
 "monarchy":Rules("hereditary",False,"none"),
 "military_junta":Rules("military_council",False,"none"),
 "oligarchy":Rules("elite_council",False,"none"),
}
def rules_for(code:str)->Rules:return RULES.get(code,RULES["republic"])
```

### `packages\core\services\live_market.py`

```python
"""Validated server-side synchronization with Zipodo's live USDT/IRT endpoint."""
from __future__ import annotations
import asyncio, json, logging, math
from datetime import UTC, datetime
from urllib.request import Request, urlopen
from packages.core import db

logger=logging.getLogger(__name__)
URL="https://api.zipodo.ir/usdt/"

def extract_price(payload: object) -> int:
    """Accept common JSON envelopes while rejecting booleans, NaN, and implausible rates."""
    keys=("price","last","value","rate","sell","close")
    candidates=[]
    def walk(value, depth=0):
        if depth>4:return
        if isinstance(value,dict):
            for key in keys:
                if key in value:candidates.append(value[key])
            for child in value.values():walk(child,depth+1)
        elif isinstance(value,list):
            for child in value[:20]:walk(child,depth+1)
    walk(payload)
    if not candidates and isinstance(payload,(int,float,str)):candidates=[payload]
    for raw in candidates:
        if isinstance(raw,bool):continue
        try:
            number=float(str(raw).replace(",","").strip())
        except (TypeError,ValueError):continue
        if math.isfinite(number):
            price=round(number)
            # USDT/IRT guardrail: intentionally broad enough for inflation, narrow enough for corrupt JSON.
            if 1_000 <= price <= 100_000_000:return price
    raise ValueError("zipodo_price_missing_or_implausible")

def _fetch(timeout: float=7.0)->int:
    req=Request(URL,headers={"Accept":"application/json","User-Agent":"TeleLife/1.0"})
    with urlopen(req,timeout=timeout) as response:
        if response.status!=200:raise RuntimeError(f"zipodo_http_{response.status}")
        raw=response.read(256_000)
    text=raw.decode("utf-8-sig").strip()
    try: payload=json.loads(text)
    except json.JSONDecodeError: payload=text
    return extract_price(payload)

async def sync()->dict[str,object]:
    checked=datetime.now(UTC)
    try:
        price=await asyncio.to_thread(_fetch)
        async with db.transaction() as conn:
            await conn.execute("""UPDATE usd_market_state SET reference_price_toman=$1,updated_at=now()
                WHERE singleton=TRUE""",price)
            await conn.execute("""UPDATE market_prices SET current_price_toman=$1,source='zipodo',
                source_checked_at=$2,source_error=NULL,updated_by='zipodo-live',updated_at=now()
                WHERE asset_code='USD'""",price,checked)
            await conn.execute("""INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
                VALUES('USD',$1,date_trunc('minute',now()))
                ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman""",price)
        return {"price":price,"source":"zipodo","stale":False}
    except Exception as exc:
        logger.warning("live USDT sync failed; keeping last valid price",exc_info=True)
        await db.execute("""UPDATE market_prices SET source_checked_at=$2,source_error=$1
            WHERE asset_code='USD'""",f"{type(exc).__name__}: {str(exc)[:300]}",checked)
        raise
```

### `packages\core\services\market_chart.py`

```python
"""Real 30-minute OHLC chart rendered as a Telegram-ready PNG."""
from __future__ import annotations
from dataclasses import dataclass
from io import BytesIO
from packages.core import db

@dataclass(frozen=True,slots=True)
class Candle:
 time:object;open:int;high:int;low:int;close:int;trades:int

async def candles(hours:int=24)->list[Candle]:
 rows=await db.fetch("""WITH price AS (
   SELECT date_bin(interval '30 minutes',captured_at,TIMESTAMPTZ '2000-01-01') bucket,
          (array_agg(price_toman ORDER BY captured_at))[1] open,
          max(price_toman) high,min(price_toman) low,
          (array_agg(price_toman ORDER BY captured_at DESC))[1] close
   FROM market_price_snapshots WHERE asset_code='USD' AND captured_at>=now()-($1::int*interval '1 hour') GROUP BY 1),
 trades AS (SELECT date_bin(interval '30 minutes',created_at,TIMESTAMPTZ '2000-01-01') bucket,count(*) trades
   FROM usd_trades WHERE created_at>=now()-($1::int*interval '1 hour') GROUP BY 1)
 SELECT p.bucket,p.open,p.high,p.low,p.close,COALESCE(t.trades,0) trades
 FROM price p LEFT JOIN trades t USING(bucket) ORDER BY p.bucket""",hours)
 return [Candle(r['bucket'],int(r['open']),int(r['high']),int(r['low']),int(r['close']),int(r['trades'])) for r in rows]

def render(rows:list[Candle])->BytesIO:
 from PIL import Image,ImageDraw,ImageFont
 w,h=1200,660;left,right,top,bottom=92,36,68,96
 image=Image.new('RGB',(w,h),'#07131f');d=ImageDraw.Draw(image)
 try:font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17);title=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',27)
 except OSError:font=small=title=ImageFont.load_default()
 d.text((left,20),'USDT / IRT  |  REAL 30M OHLC  |  LAST 24H',fill='#eaf5ff',font=title)
 if not rows:
  d.text((left,280),'No valid market snapshots yet',fill='#8ca6b8',font=font);out=BytesIO();image.save(out,'PNG',optimize=True);out.seek(0);out.name='usdt_30m.png';return out
 lo=min(x.low for x in rows);hi=max(x.high for x in rows);span=max(hi-lo,1);plot_h=h-top-bottom
 def y(v):return top+(hi-v)*plot_h/span
 for i in range(5):
  yy=top+i*plot_h/4;price=round(hi-i*span/4);d.line((left,yy,w-right,yy),fill='#183144',width=1);d.text((8,yy-10),f'{price:,}',fill='#7893a7',font=small)
 slot=(w-left-right)/max(48,len(rows));body=max(5,min(15,int(slot*.55)))
 for i,c in enumerate(rows):
  x=left+(i+.5)*slot;up=c.close>=c.open;color='#35d7c0' if up else '#ff6f91'
  d.line((x,y(c.high),x,y(c.low)),fill=color,width=2)
  y1,y2=y(c.open),y(c.close);d.rectangle((x-body/2,min(y1,y2),x+body/2,max(y1,y2)+1),fill=color)
  if i%8==0:d.text((x-25,h-bottom+18),c.time.strftime('%H:%M'),fill='#7893a7',font=small)
 change=(rows[-1].close-rows[0].open)*100/rows[0].open
 d.text((left,h-38),f'O {rows[0].open:,}   H {hi:,}   L {lo:,}   C {rows[-1].close:,}   {change:+.2f}%',fill='#b9cad6',font=font)
 d.text((w-300,24),f'{rows[-1].close:,} IRT',fill='#35d7c0' if change>=0 else '#ff6f91',font=title)
 out=BytesIO();image.save(out,'PNG',optimize=True);out.seek(0);out.name='usdt_30m.png';return out
```

### `packages\core\services\migration.py`

```python
"""Controlled country migration with escrowed exit fee and destination approval."""
from __future__ import annotations
from datetime import UTC,datetime,timedelta
from packages.core import db

def exit_fee(wealth:int)->int:return min(50_000_000,max(500_000,wealth*5//100))
async def political_hold(player_id:int)->bool:
 return bool(await db.fetchval("SELECT political_hold_until>now() FROM citizenships WHERE player_id=$1 AND is_active",player_id))
async def quote(player_id:int,destination_country_id:int):
 return await db.fetchrow("""SELECT cs.country_id origin_country_id,o.name origin_name,d.id destination_country_id,d.name destination_name,d.president_player_id,p.wallet_toman,p.savings_toman,cs.last_migrated_at
 FROM citizenships cs JOIN countries o ON o.id=cs.country_id JOIN countries d ON d.id=$2 JOIN players p ON p.id=cs.player_id WHERE cs.player_id=$1 AND cs.is_active AND cs.country_id<>d.id""",player_id,destination_country_id)
async def request(player_id:int,destination_country_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("""SELECT cs.country_id origin_country_id,d.president_player_id,p.wallet_toman,p.savings_toman,cs.last_migrated_at FROM citizenships cs JOIN countries d ON d.id=$2 JOIN players p ON p.id=cs.player_id WHERE cs.player_id=$1 AND cs.is_active AND cs.country_id<>d.id FOR UPDATE OF cs,p,d""",player_id,destination_country_id)
  if not row:raise ValueError("migration_not_available")
  if row["last_migrated_at"] and row["last_migrated_at"]>datetime.now(UTC)-timedelta(days=30):raise ValueError("migration_cooldown")
  if await conn.fetchval("SELECT 1 FROM migration_requests WHERE player_id=$1 AND status='pending'",player_id):raise ValueError("migration_pending")
  if await conn.fetchval("SELECT president_player_id=$2 FROM countries WHERE id=$1",row["origin_country_id"],player_id):raise ValueError("leader_must_transfer_power")
  fee=exit_fee(int(row["wallet_toman"])+int(row["savings_toman"]))
  if int(row["wallet_toman"])+int(row["savings_toman"])<fee:raise ValueError("insufficient_balance")
  # Fee is charged only on completion. Approval requests cannot lock funds forever.
  req=await conn.fetchrow("INSERT INTO migration_requests(player_id,origin_country_id,destination_country_id,exit_fee_toman) VALUES($1,$2,$3,$4) RETURNING *",player_id,row["origin_country_id"],destination_country_id,fee)
  if row["president_player_id"] is None:return await _complete(conn,req["id"],None)
  return req
async def _complete(conn,request_id:int,reviewer:int|None):
 req=await conn.fetchrow("SELECT * FROM migration_requests WHERE id=$1 AND status='pending' FOR UPDATE",request_id)
 if not req or req["expires_at"]<=datetime.now(UTC):raise ValueError("migration_expired")
 p=await conn.fetchrow("SELECT wallet_toman,savings_toman FROM players WHERE id=$1 FOR UPDATE",req["player_id"]);fee=int(req["exit_fee_toman"])
 wallet_take=min(int(p["wallet_toman"]),fee);saving_take=fee-wallet_take
 if int(p["wallet_toman"])+int(p["savings_toman"])<fee:raise ValueError("insufficient_balance")
 await conn.execute("UPDATE players SET wallet_toman=wallet_toman-$2,savings_toman=savings_toman-$3 WHERE id=$1",req["player_id"],wallet_take,saving_take)
 await conn.execute("UPDATE countries SET treasury_toman=treasury_toman+$2 WHERE id=$1",req["origin_country_id"],fee)
 await conn.execute("UPDATE citizenships SET country_id=$2,joined_at=now(),left_at=NULL,is_active=TRUE,migrant_until=now()+interval '30 days',political_hold_until=now()+interval '14 days',last_migrated_at=now() WHERE player_id=$1",req["player_id"],req["destination_country_id"])
 await conn.execute("UPDATE migration_requests SET status='approved',reviewed_by_player_id=$2,resolved_at=now() WHERE id=$1",request_id,reviewer)
 return await conn.fetchrow("SELECT * FROM migration_requests WHERE id=$1",request_id)
async def approve(request_id:int,president_id:int):
 async with db.transaction() as conn:
  allowed=await conn.fetchval("SELECT 1 FROM migration_requests r JOIN countries c ON c.id=r.destination_country_id WHERE r.id=$1 AND c.president_player_id=$2 AND r.status='pending'",request_id,president_id)
  if not allowed:raise PermissionError("president_required")
  return await _complete(conn,request_id,president_id)
async def reject(request_id:int,president_id:int,note:str|None=None):
 return bool(await db.fetchval("""UPDATE migration_requests r SET status='rejected',reviewed_by_player_id=$2,review_note=$3,resolved_at=now() FROM countries c WHERE r.id=$1 AND c.id=r.destination_country_id AND c.president_player_id=$2 AND r.status='pending' RETURNING r.id""",request_id,president_id,note))
async def pending_for_country(country_id:int):
 return await db.fetch("""SELECT r.id,r.player_id,r.exit_fee_toman,r.expires_at,p.first_name,o.name origin_name FROM migration_requests r JOIN players p ON p.id=r.player_id JOIN countries o ON o.id=r.origin_country_id WHERE r.destination_country_id=$1 AND r.status='pending' AND r.expires_at>now() ORDER BY r.created_at""",country_id)
async def expire()->int:
 result=await db.execute("UPDATE migration_requests SET status='expired',resolved_at=now() WHERE status='pending' AND expires_at<=now()");return int(result.rsplit(' ',1)[-1])
```

### `packages\core\services\missions.py`

```python
"""Daily missions: deterministic per-player daily selection, no shuffling.

Selection is seeded by (player_id, date) so a restart or a second call always
produces the same missions. No table needed to remember the choice.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import date
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.utils import clock


@dataclass(slots=True, frozen=True)
class Mission:
    key: str
    title: str
    target: int
    reward_toman: int
    reward_xp: int
    progress: int = 0
    claimed: bool = False

    @property
    def done(self) -> bool:
        return self.progress >= self.target


def _all_specs() -> list[dict[str, Any]]:
    pool = get_config().get("missions.pool")
    if not isinstance(pool, list):
        raise TypeError("missions.pool must be a list")
    return pool


def spec_for(mission_key: str) -> dict[str, Any] | None:
    return next((m for m in _all_specs() if str(m["key"]) == mission_key), None)


def _pool(level: int) -> list[dict[str, Any]]:
    return [m for m in _all_specs() if int(m.get("min_level", 1)) <= level]


def _seed(player_id: int, day: date, key: str) -> int:
    raw = f"{player_id}:{day:%Y-%m-%d}:{key}".encode()
    return int.from_bytes(hashlib.blake2b(raw, digest_size=8).digest(), "big")


def select_for(player_id: int, level: int, day: date | None = None) -> list[dict[str, Any]]:
    """Deterministic daily pick. Same inputs always yield the same missions."""
    day = day or clock.game_today()
    candidates = _pool(level)
    count = min(get_config().int_("missions.daily.count_per_day"), len(candidates))
    ranked = sorted(candidates, key=lambda m: _seed(player_id, day, str(m["key"])))
    return ranked[:count]


async def ensure_today(player_id: int, level: int, day: date | None = None) -> list[Mission]:
    """Materialise today's missions, then return them with live progress."""
    day = day or clock.game_today()
    chosen = select_for(player_id, level, day)
    if not chosen:
        return []

    async with db.transaction() as conn:
        await conn.executemany(
            """
            INSERT INTO daily_missions (player_id, mission_date, mission_key, target)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (player_id, mission_date, mission_key) DO NOTHING
            """,
            [(player_id, day, str(m["key"]), int(m["target"])) for m in chosen],
        )
        rows = await conn.fetch(
            """
            SELECT mission_key, progress, target, claimed_at
            FROM daily_missions
            WHERE player_id = $1 AND mission_date = $2
            """,
            player_id,
            day,
        )

    by_key = {r["mission_key"]: r for r in rows}
    out: list[Mission] = []
    for spec in chosen:
        key = str(spec["key"])
        row = by_key.get(key)
        out.append(
            Mission(
                key=key,
                title=str(spec["title"]),
                target=int(spec["target"]),
                reward_toman=int(spec["reward_toman"]),
                reward_xp=int(spec["reward_xp"]),
                progress=int(row["progress"]) if row else 0,
                claimed=bool(row and row["claimed_at"]),
            )
        )
    return out


async def report_progress(
    player_id: int, mission_key: str, amount: int = 1, day: date | None = None
) -> bool:
    """Advance a mission if the player has it today.

    Returns True only on the transition into "completed", so a caller can react
    exactly once.
    """
    if amount <= 0:
        return False
    day = day or clock.game_today()
    row = await db.fetchrow(
        """
        UPDATE daily_missions
        SET progress = LEAST(target, progress + $3)
        WHERE player_id = $1 AND mission_date = $4 AND mission_key = $2
          AND claimed_at IS NULL AND progress < target
        RETURNING progress, target
        """,
        player_id,
        mission_key,
        amount,
        day,
    )
    return bool(row and row["progress"] >= row["target"])


async def claim(player_id: int, mission_key: str, day: date | None = None) -> Mission | None:
    """Claim a completed mission exactly once. Returns the mission, or None."""
    day = day or clock.game_today()
    spec = spec_for(mission_key)
    if spec is None:
        return None

    reward_toman = int(spec["reward_toman"])

    async with db.transaction() as conn:
        row = await conn.fetchrow(
            """
            UPDATE daily_missions SET claimed_at = now()
            WHERE player_id = $1 AND mission_date = $2 AND mission_key = $3
              AND claimed_at IS NULL AND progress >= target
            RETURNING progress, target
            """,
            player_id,
            day,
            mission_key,
        )
        if row is None:
            return None

        balance = await conn.fetchval(
            "UPDATE players SET wallet_toman = wallet_toman + $2 WHERE id = $1 "
            "RETURNING wallet_toman",
            player_id,
            reward_toman,
        )
        await conn.execute(
            """
            INSERT INTO ledger
                (player_id, idempotency_key, reason, currency, asset_code, account,
                 amount, balance_after)
            VALUES ($1, $2, 'mission', 'IRT', 'IRT', 'wallet', $3, $4)
            ON CONFLICT (idempotency_key) DO NOTHING
            """,
            player_id,
            f"mission:{player_id}:{day:%Y-%m-%d}:{mission_key}",
            reward_toman,
            int(balance or 0),
        )

    return Mission(
        key=mission_key,
        title=str(spec["title"]),
        target=int(row["target"]),
        reward_toman=reward_toman,
        reward_xp=int(spec["reward_xp"]),
        progress=int(row["target"]),
        claimed=True,
    )
```

### `packages\core\services\national_project.py`

```python
"""One-time national project with atomic, idempotent contributions.

Money and asset movement happens only through the ledger, inside a single
transaction, keyed by a deterministic idempotency key per leg.
"""

from __future__ import annotations

from typing import Any

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, ledger_repo, project_repo
from packages.core.services import xp, migration

_IRT = "IRT"


def _account_for(asset: str) -> str:
    """Wallet holds currency; everything else lives in inventory."""
    return "wallet" if asset == _IRT else "inventory"


async def start(
    country_id: int,
    player_id: int,
    key: str = "national_storage",
) -> asyncpg.Record:
    """Open a national project. Only the sitting president may start one."""
    if await migration.political_hold(player_id):raise PermissionError("migrant_political_hold")
    country = await country_repo.by_id(country_id)
    if country is None:
        raise ValueError("country_not_found")

    president = country["president_player_id"]
    if president is not None:
        if int(president) != player_id:
            raise PermissionError("president_required")
    elif not await db.fetchval(
        "SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2 AND is_active",
        country_id, player_id,
    ):
        raise PermissionError("citizen_required")

    requirements: dict[str, Any] = get_config().section(
        f"national_project.projects.{key}.requirements"
    )
    parsed = {asset: int(amount) for asset, amount in requirements.items()}

    async with db.transaction() as conn:
        return await project_repo.start(conn, country_id, player_id, key, parsed)


async def contribute(
    project_id: int,
    player_id: int,
    asset: str,
    amount: int,
    key: str,
) -> tuple[int, bool]:
    """Contribute to a project. Returns (amount_accepted, project_completed).

    Exactly-once is guaranteed by the UNIQUE constraint on
    project_contributions.idempotency_key, not by a pre-flight lookup: a
    read-then-write check leaves a race window open under concurrent taps.
    """
    if amount <= 0:
        raise ValueError("amount_must_be_positive")

    completed = False
    accepted = 0
    project_key = "national_storage"

    async with db.transaction() as conn:
        project = await project_repo.lock(conn, project_id)
        if project is None or project["status"] != "active":
            raise ValueError("project_not_active")
        project_key = str(project["project_key"])

        is_citizen = await conn.fetchval(
            "SELECT EXISTS(SELECT 1 FROM citizenships "
            "WHERE player_id = $1 AND country_id = $2 AND is_active)",
            player_id,
            project["country_id"],
        )
        if not is_citizen:
            raise PermissionError("citizen_required")

        remaining = await project_repo.remaining(conn, project_id, asset)
        if remaining is None:
            raise ValueError("asset_not_required")

        accepted = min(amount, remaining)
        if accepted <= 0:
            return 0, False

        # Claim the idempotency slot FIRST. If this returns False the work was
        # already done by an earlier (or concurrent) call: nothing to replay.
        claimed = await project_repo.contribution(
            conn, project_id, player_id, asset, accepted, key
        )
        if not claimed:
            return 0, False

        balance = await ledger_repo.change_player(conn, player_id, asset, -accepted)
        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=f"{key}:debit",
            reason="project_contribution",
            asset=asset,
            account=_account_for(asset),
            amount=-accepted,
            balance=balance,
            metadata={"project_id": project_id},
        )

        completed = await project_repo.complete_if_ready(conn, project_id)

    if completed:
        reward = get_config().int_(
            f"national_project.projects.{project_key}.completion.contributor_reward_xp"
        )
        await xp.grant(
            player_id,
            "national_project",
            idempotency_key=f"project:{project_id}:xp:{player_id}",
            amount=reward,
        )

    return accepted, completed
```

### `packages\core\services\news.py`

```python
"""Outbox publisher with leases, retries and deterministic daily catch-up."""

from __future__ import annotations

import hashlib
import logging
from collections.abc import Awaitable, Callable
from datetime import date, timedelta
from typing import Any
from uuid import uuid4

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import outbox_repo
from packages.core.settings import get_settings
from packages.core.utils import clock

logger = logging.getLogger(__name__)

Sender = Callable[[int | None, str, dict[str, Any]], Awaitable[None]]


def _backoff(delays: list[int], attempts: int) -> int:
    """Delay for the next retry. `attempts` is already incremented by claim()."""
    if not delays:
        return 60
    index = min(max(attempts - 1, 0), len(delays) - 1)
    return int(delays[index])


async def publish_batch(sender: Sender) -> dict[str, int]:
    """Claim a batch, deliver each row, then settle it. One row cannot poison
    the batch: every outcome is committed on its own."""
    cfg = get_config()
    token = uuid4()
    stats = {"published": 0, "failed": 0}

    async with db.transaction() as conn:
        rows = await outbox_repo.claim(
            conn,
            token,
            cfg.int_("news.outbox.claim_batch_size"),
            cfg.int_("news.outbox.claim_lease_seconds"),
            cfg.int_("news.outbox.maximum_attempts"),
        )

    delays = [int(x) for x in cfg.get("news.outbox.retry_backoff_seconds", [60])]

    for row in rows:
        try:
            await sender(row["destination_chat_id"], row["event_type"], row["payload"])
        except Exception as exc:  # noqa: BLE001 - one bad row must not stop the rest
            logger.warning(
                "outbox delivery failed",
                extra={"extra_fields": {"row_id": row["id"], "error": repr(exc)}},
            )
            delay = _backoff(delays, int(row["attempts"]))
            async with db.transaction() as conn:
                await outbox_repo.failed(
                    conn, row["id"], token, type(exc).__name__[:64], delay
                )
            stats["failed"] += 1
        else:
            async with db.transaction() as conn:
                await outbox_repo.published(conn, row["id"], token)
            stats["published"] += 1

    return stats


def _pick_event(weighted: list[tuple[str, int]], day: date, namespace: str) -> str:
    """Deterministic weighted pick for a given day."""
    total = sum(weight for _, weight in weighted)
    digest = hashlib.sha256(f"{namespace}:{day}".encode()).digest()
    roll = int.from_bytes(digest[:4], "big") % total
    for code, weight in weighted:
        if roll < weight:
            return code
        roll -= weight
    return weighted[-1][0]


async def ensure_daily_events(today: date | None = None) -> int:
    """Materialise the daily event for each recent day. Returns how many were
    newly created."""
    cfg = get_config()
    end = today or clock.game_today()
    span = cfg.int_("daily_events.scheduler.catch_up_days")
    start = end - timedelta(days=span - 1)

    events = cfg.section("daily_events.events")
    weighted = sorted((str(k), int(v["weight"])) for k, v in events.items())
    if not weighted or sum(w for _, w in weighted) <= 0:
        raise ValueError("daily_events_pool_empty")

    namespace = cfg.get(
        "daily_events.scheduler.deterministic_seed_namespace", "daily_events"
    )
    destination = get_settings().global_news_chat_id
    created = 0

    for offset in range((end - start).days + 1):
        day = start + timedelta(days=offset)
        code = _pick_event(weighted, day, namespace)
        spec = events[code]
        async with db.transaction() as conn:
            if await outbox_repo.create_event(conn, day, code, spec):
                await outbox_repo.enqueue(
                    conn,
                    f"daily-event:{day}",
                    "daily_event",
                    {"event_date": str(day), "event_code": code, "effect": spec},
                    destination,
                )
                created += 1

    return created
```

### `packages\core\services\personal_economy.py`

```python
"""Phase 3 personal economy: atomic savings, housing, rent and living costs."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import timedelta
from typing import Any
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

@dataclass(frozen=True,slots=True)
class EconomyView:
    wallet:int; savings:int; housing:dict[str,Any]|None; living_due:int; living_days:int

async def view(player_id:int)->EconomyView:
    player=await db.fetchrow("SELECT wallet_toman,savings_toman FROM players WHERE id=$1",player_id)
    if player is None: raise ValueError("player_not_found")
    house=await db.fetchrow("SELECT * FROM player_housing WHERE player_id=$1",player_id)
    today=clock.game_today()
    if house and house["tenure"] == "rent" and (house["rent_paid_until"] is None or house["rent_paid_until"] < today):
        house=None
    state=await db.fetchrow("SELECT last_living_charge_date FROM player_life_economy WHERE player_id=$1",player_id)
    last=state["last_living_charge_date"] if state else None
    days=1 if last is None else max(0,min((today-last).days,get_config().int_("phase3.living.max_catch_up_days")))
    daily=get_config().int_("phase3.living.base_daily_cost_toman")
    if house: daily+=get_config().int_(f"phase3.housing.options.{house['housing_code']}.daily_living_toman")
    return EconomyView(int(player["wallet_toman"]),int(player["savings_toman"]),dict(house) if house else None,daily*days,days)

async def savings_transfer(player_id:int,amount:int,direction:str,key:str)->tuple[int,int]:
    cfg=get_config(); lo=cfg.int_("phase3.savings.minimum_transfer_toman"); hi=cfg.int_("phase3.savings.maximum_transfer_toman")
    if direction not in {"deposit","withdraw"}: raise ValueError("invalid_direction")
    if not lo<=amount<=hi: raise ValueError("amount_out_of_bounds")
    async with db.transaction() as conn:
        row=await ledger_repo.lock_player(conn,player_id)
        if row is None: raise ValueError("player_not_found")
        if await ledger_repo.idempotency_exists(conn,f"{key}:wallet"): return int(row["wallet_toman"]),int(row["savings_toman"])
        wallet_delta=-amount if direction=="deposit" else amount
        savings_delta=amount if direction=="deposit" else -amount
        changed=await conn.fetchrow("""UPDATE players SET wallet_toman=wallet_toman+$2,savings_toman=savings_toman+$3
          WHERE id=$1 AND wallet_toman+$2>=0 AND savings_toman+$3>=0 RETURNING wallet_toman,savings_toman""",player_id,wallet_delta,savings_delta)
        if changed is None: raise ValueError("insufficient_balance")
        a=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:wallet",reason=f"savings_{direction}",asset="IRT",account="wallet",amount=wallet_delta,balance=int(changed["wallet_toman"]))
        b=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:savings",reason=f"savings_{direction}",asset="IRT",account="savings",amount=savings_delta,balance=int(changed["savings_toman"]))
        if not(a and b): raise RuntimeError("savings_ledger_conflict")
        return int(changed["wallet_toman"]),int(changed["savings_toman"])

async def acquire_housing(player_id:int,code:str,tenure:str,key:str)->dict[str,Any]:
    cfg=get_config(); options=cfg.section("phase3.housing.options")
    if code not in options or tenure not in {"rent","owned"}: raise ValueError("invalid_housing")
    spec=options[code]; cost=int(spec["weekly_rent_toman"] if tenure=="rent" else spec["purchase_toman"])
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        if int(player["level"])<int(spec["min_level"]): raise ValueError("housing_locked")
        if await ledger_repo.idempotency_exists(conn,key):
            row=await conn.fetchrow("SELECT * FROM player_housing WHERE player_id=$1",player_id); return dict(row)
        balance=await ledger_repo.change_player(conn,player_id,"IRT",-cost)
        until=clock.game_today()+timedelta(days=cfg.int_("phase3.housing.rent_period_days")) if tenure=="rent" else None
        row=await conn.fetchrow("""INSERT INTO player_housing(player_id,housing_code,tenure,rent_paid_until,purchased_at)
          VALUES($1,$2,$3,$4,CASE WHEN $3='owned' THEN now() END)
          ON CONFLICT(player_id) DO UPDATE SET housing_code=$2,tenure=$3,rent_paid_until=$4,
          purchased_at=CASE WHEN $3='owned' THEN now() END,updated_at=now() RETURNING *""",player_id,code,tenure,until)
        if not await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason=f"housing_{tenure}",asset="IRT",account="wallet",amount=-cost,balance=balance,metadata={"housing":code}): raise RuntimeError("housing_ledger_conflict")
        return dict(row)

async def pay_living(player_id:int,key:str)->tuple[int,int]:
    cfg=get_config(); today=clock.game_today()
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        await conn.execute("INSERT INTO player_life_economy(player_id) VALUES($1) ON CONFLICT DO NOTHING",player_id)
        state=await conn.fetchrow("SELECT * FROM player_life_economy WHERE player_id=$1 FOR UPDATE",player_id)
        last=state["last_living_charge_date"]; days=1 if last is None else max(0,min((today-last).days,cfg.int_("phase3.living.max_catch_up_days")))
        if days==0:return 0,int(player["wallet_toman"])
        house=await conn.fetchrow("SELECT housing_code,tenure,rent_paid_until FROM player_housing WHERE player_id=$1 FOR UPDATE",player_id)
        # Expired rentals stop adding housing costs and are removed atomically.
        if house and house["tenure"] == "rent" and (house["rent_paid_until"] is None or house["rent_paid_until"] < today):
            await conn.execute("DELETE FROM player_housing WHERE player_id=$1", player_id)
            house = None
        daily=cfg.int_("phase3.living.base_daily_cost_toman")+(cfg.int_(f"phase3.housing.options.{house['housing_code']}.daily_living_toman") if house else 0)
        amount=daily*days
        if int(player["wallet_toman"])<amount: raise ValueError("insufficient_balance")
        balance=await ledger_repo.change_player(conn,player_id,"IRT",-amount)
        await conn.execute("UPDATE player_life_economy SET last_living_charge_date=$2,total_living_paid=total_living_paid+$3,missed_living_days=0,updated_at=now() WHERE player_id=$1",player_id,today,amount)
        if not await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason="living_cost",asset="IRT",account="wallet",amount=-amount,balance=balance,metadata={"days":days}): raise RuntimeError("living_ledger_conflict")
        return amount,balance
```

### `packages\core\services\production.py`

```python
"""Capacity-capped lazy production with proportional anti-farm XP."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from math import floor

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo, production_repo
from packages.core.services import xp

UPGRADE_KINDS = frozenset({"storage", "production"})


@dataclass(frozen=True, slots=True)
class Accrual:
    stored: int
    capacity: int
    rate: float


def _max_level(kind: str) -> int:
    cfg = get_config()
    if kind == "storage":
        return max(int(k) for k in cfg.section("jobs.storage.levels"))
    return cfg.int_("jobs.production_levels.maximum")


def _upgrade_cost(kind: str, target: int) -> int:
    section = "jobs.storage.upgrade_cost_toman" if kind == "storage" \
        else "jobs.production_levels.upgrade_cost_toman"
    cfg = get_config()
    path = f"{section}.{target}"
    if not cfg.has(path):
        raise ValueError("max_level_reached")
    return cfg.int_(path)


def accrue(row, at: datetime) -> Accrual:  # type: ignore[no-untyped-def]
    """Compute what the player's job has produced since the last checkpoint."""
    cfg = get_config()
    job = cfg.section(f"jobs.jobs.{row['job_code']}")
    rate = float(job["base_rate_per_hour"]) * (
        1 + (int(row["production_level"]) - 1)
        * cfg.float_("jobs.production.production_multiplier_per_level")
    )

    since = row["production_updated_at"]
    if since.tzinfo is None:
        since = since.replace(tzinfo=UTC)
    if at.tzinfo is None:
        at = at.replace(tzinfo=UTC)

    # Clock skew must never mint resources, and never destroy stored ones.
    skew = cfg.int_("jobs.production.max_accrual_clock_skew_seconds")
    elapsed = (at - since).total_seconds()
    if elapsed < -skew:
        elapsed = 0.0
    hours = max(0.0, elapsed) / cfg.int_("jobs.production.time_unit_seconds")

    capacity_hours = cfg.int_(f"jobs.storage.levels.{row['storage_level']}.capacity_hours")
    cap = floor(rate * capacity_hours)
    stored = min(cap, int(row["stored_amount"]) + floor(rate * hours))
    return Accrual(max(0, stored), max(0, cap), rate)


async def choose(player_id: int, job: str) -> bool:
    player = await db.fetchrow("SELECT level FROM players WHERE id=$1", player_id)
    if player is None:
        raise ValueError("player_not_found")
    if int(player["level"]) < 5:
        raise ValueError("job_locked")
    jobs = get_config().section("jobs.jobs")
    if job not in jobs:
        raise ValueError("invalid_job")
    return await production_repo.choose(player_id, job, str(jobs[job]["output_asset"]))


async def collect(player_id: int, key: str, at: datetime | None = None) -> tuple[int, int]:
    """Bank stored production. Returns (amount, xp_awarded)."""
    now = at or datetime.now(UTC)
    cfg = get_config()

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")
        # The player_jobs lock serializes double taps; re-check idempotency only after it.
        if await ledger_repo.idempotency_exists(conn, key):
            return 0, 0
        accrual = accrue(row, now)
        amount = accrual.stored
        if amount < cfg.int_("jobs.production.minimum_collection_amount"):
            return 0, 0
        asset = row["output_asset_code"]
        balance = await ledger_repo.change_player(conn, player_id, asset, amount)
        if not await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason="production_collect",
            asset=asset,
            account=ledger_repo.player_account(asset),
            amount=amount,
            balance=balance,
            metadata={"job": row["job_code"]},
        ):
            return 0, 0
        await production_repo.clear(conn, player_id, now)

    fraction = amount / accrual.capacity if accrual.capacity else 0.0
    minimum = cfg.float_("jobs.production.minimum_collection_fraction_for_xp")
    award = (
        floor(cfg.int_("jobs.production.collection_xp_at_full_capacity") * fraction)
        if fraction >= minimum
        else 0
    )
    if award:
        result = await xp.grant(
            player_id, "production_collect", idempotency_key=f"{key}:xp", amount=award
        )
        award = result.granted
    return amount, award


async def upgrade(player_id: int, kind: str, key: str, at: datetime | None = None) -> int:
    """Upgrade storage or production. Old rate is checkpointed first."""
    if kind not in UPGRADE_KINDS:
        raise ValueError("invalid_upgrade")
    now = at or datetime.now(UTC)

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")

        current = int(row[f"{kind}_level"])
        target = current + 1
        if target > _max_level(kind):
            raise ValueError("max_level_reached")

        # Duplicate request: stop before touching balances or levels.
        if await ledger_repo.idempotency_exists(conn, key):
            return current

        cost = _upgrade_cost(kind, target)

        # Freeze production at the OLD rate before the level changes, so the
        # upgrade never applies retroactively to hours already elapsed.
        accrual = accrue(row, now)
        await production_repo.checkpoint(conn, player_id, accrual.stored, now)

        balance = await ledger_repo.change_player(conn, player_id, "IRT", -cost)
        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason=f"{kind}_upgrade",
            asset="IRT",
            account="wallet",
            amount=-cost,
            balance=balance,
            metadata={"kind": kind, "level": target},
        )
        await production_repo.level_up(conn, player_id, kind)
        return target
```

### `packages\core\services\progression.py`

```python
"""Level curve maths. Pure functions - trivially testable, zero I/O."""

from __future__ import annotations

from functools import lru_cache

from packages.core.config import get_config


@lru_cache(maxsize=512)
def xp_required(level: int) -> int:
    """Total XP needed to advance FROM `level` to `level + 1`."""
    cfg = get_config()
    base = cfg.int_("progression.xp_curve.base")
    exponent = cfg.float_("progression.xp_curve.exponent")
    return max(1, int(base * (level**exponent)))


def max_level() -> int:
    return get_config().int_("progression.xp_curve.max_level")


def level_progress(level: int, xp: int) -> tuple[int, int]:
    """Return (current_xp_in_level, xp_needed_for_next).

    At max level there is no next threshold; we report the bar as full instead
    of dividing by a meaningless target.
    """
    if level >= max_level():
        return xp, max(xp, 1)
    return xp, xp_required(level)
```

### `packages\core\services\scheduler_ops.py`

```python
"""Isolated, observable execution for scheduler jobs."""
from __future__ import annotations
import logging, time
from typing import Awaitable, Callable, TypeVar
from packages.core import db
logger=logging.getLogger(__name__)
T=TypeVar("T")
async def run(name:str, fn:Callable[[],Awaitable[T]])->T|None:
    started=time.perf_counter()
    row_id=await db.fetchval("INSERT INTO scheduler_job_runs(job_name,status) VALUES($1,'running') RETURNING id",name)
    try:
        result=await fn()
        payload=result if isinstance(result,dict) else {"value":result} if result is not None else {}
        await db.execute("UPDATE scheduler_job_runs SET status='succeeded',finished_at=now(),duration_ms=$2,result=$3 WHERE id=$1",row_id,round((time.perf_counter()-started)*1000),payload)
        return result
    except Exception as exc:
        await db.execute("UPDATE scheduler_job_runs SET status='failed',finished_at=now(),duration_ms=$2,error_type=$3,error_message=$4 WHERE id=$1",row_id,round((time.perf_counter()-started)*1000),type(exc).__name__,str(exc)[:1000])
        logger.exception("scheduler job failed",extra={"job_name":name})
        return None
```

### `packages\core\services\unlocks.py`

```python
"""Level-gated unlock catalogue. Pure config reads - no I/O."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from packages.core.config import get_config


@dataclass(slots=True, frozen=True)
class Unlock:
    level: int
    key: str
    title: str
    icon: str
    phase: int


@lru_cache(maxsize=1)
def catalogue() -> tuple[Unlock, ...]:
    levels = get_config().section("unlocks.levels")
    items = [
        Unlock(int(lvl), str(s["key"]), str(s["title"]), str(s["icon"]), int(s["phase"]))
        for lvl, s in levels.items()
    ]
    return tuple(sorted(items, key=lambda u: u.level))


def unlocked_at(level: int) -> tuple[Unlock, ...]:
    return tuple(u for u in catalogue() if u.level == level)


def available(level: int) -> tuple[Unlock, ...]:
    return tuple(u for u in catalogue() if u.level <= level)


def next_unlock(level: int) -> Unlock | None:
    return next((u for u in catalogue() if u.level > level), None)
```

### `packages\core\services\usd_market.py`

```python
"""Phase 4 USD market: bounded price impact, spread, fees and daily limits."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

@dataclass(frozen=True,slots=True)
class MarketView:
    price:int; buy_price:int; sell_price:int; health:int; volume_cents:int; frozen:bool

@dataclass(frozen=True,slots=True)
class TradeResult:
    applied:bool; side:str; cents:int; toman:int; fee:int; price:int; price_after:int

def _quote(price:int,side:str)->int:
    spread=get_config().int_("market.usd.spread_basis_points")
    return max(1,(price*(10000+(spread if side=="buy" else -spread)))//10000)

async def view()->MarketView:
    row=await db.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE")
    if row is None: raise ValueError("market_not_initialized")
    frozen=bool(await db.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"))
    p=int(row["reference_price_toman"])
    return MarketView(p,_quote(p,"buy"),_quote(p,"sell"),int(row["health"]),int(row["volume_cents"]),frozen)

async def trade(player_id:int,side:str,cents:int,key:str)->TradeResult:
    cfg=get_config()
    if side not in {"buy","sell"}: raise ValueError("invalid_side")
    if not cfg.int_("market.usd.minimum_trade_cents")<=cents<=cfg.int_("market.usd.maximum_trade_cents"): raise ValueError("amount_out_of_bounds")
    today=clock.game_today()
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        if int(player["level"])<cfg.int_("market.usd.min_level"): raise ValueError("market_locked")
        if await ledger_repo.economy_frozen(conn) or await conn.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"): raise ValueError("market_frozen")
        state=await conn.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if await conn.fetchval("SELECT 1 FROM usd_trades WHERE idempotency_key=$1",key):
            return TradeResult(False,side,cents,0,0,int(state["reference_price_toman"]),int(state["reference_price_toman"]))
        await conn.execute("INSERT INTO usd_daily_limits(player_id,trade_date) VALUES($1,$2) ON CONFLICT DO NOTHING",player_id,today)
        limits=await conn.fetchrow("SELECT * FROM usd_daily_limits WHERE player_id=$1 AND trade_date=$2 FOR UPDATE",player_id,today)
        used=int(limits["bought_cents"] if side=="buy" else limits["sold_cents"])
        maximum=cfg.int_(f"market.usd.daily_{side}_limit_cents")
        if used+cents>maximum: raise ValueError("daily_limit")
        reference=int(state["reference_price_toman"]); price=_quote(reference,side)
        gross=(price*cents+99)//100
        fee=(gross*cfg.int_("market.usd.fee_basis_points")+9999)//10000
        wallet_delta=-(gross+fee) if side=="buy" else gross-fee
        usd_delta=cents if side=="buy" else -cents
        changed=await conn.fetchrow("""UPDATE players SET wallet_toman=wallet_toman+$2,usd_cents=usd_cents+$3
          WHERE id=$1 AND wallet_toman+$2>=0 AND usd_cents+$3>=0 RETURNING wallet_toman,usd_cents""",player_id,wallet_delta,usd_delta)
        if changed is None: raise ValueError("insufficient_balance")
        steps=max(1,cents//cfg.int_("market.usd.impact_cents_per_step")); move=min(cfg.int_("market.usd.max_trade_move_basis_points"),steps*cfg.int_("market.usd.impact_basis_points_per_step"))
        candidate=(reference*(10000+(move if side=="buy" else -move)))//10000
        open_price=int(state["open_price_toman"]); band=cfg.int_("market.usd.daily_band_basis_points")
        low=open_price*(10000-band)//10000; high=open_price*(10000+band)//10000; after=max(low,min(high,max(1,candidate)))
        net=int(state["net_flow_cents"])+(cents if side=="buy" else -cents); volume=int(state["volume_cents"])+cents
        health=max(0,100-min(100,abs(net)*100//max(volume,1)))
        await conn.execute("UPDATE usd_market_state SET reference_price_toman=$1,net_flow_cents=$2,volume_cents=$3,health=$4,updated_at=now() WHERE singleton=TRUE",after,net,volume,health)
        col="bought_cents" if side=="buy" else "sold_cents"
        await conn.execute(f"UPDATE usd_daily_limits SET {col}={col}+$3 WHERE player_id=$1 AND trade_date=$2",player_id,today,cents)
        await conn.execute("""INSERT INTO usd_trades(player_id,idempotency_key,side,usd_cents,gross_toman,fee_toman,price_toman,price_after_toman)
          VALUES($1,$2,$3,$4,$5,$6,$7,$8)""",player_id,key,side,cents,gross,fee,price,after)
        ok1=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:irt",reason=f"usd_{side}",asset="IRT",account="wallet",amount=wallet_delta,balance=int(changed["wallet_toman"]),metadata={"fee":fee,"price":price})
        ok2=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:usd",reason=f"usd_{side}",asset="USD",account="usd",amount=usd_delta,balance=int(changed["usd_cents"]),metadata={"price":price})
        if not(ok1 and ok2): raise RuntimeError("market_ledger_conflict")
        await conn.execute("""UPDATE market_prices SET current_price_toman=$1,updated_by='market-engine',updated_at=now() WHERE asset_code='USD'""",after)
        await conn.execute("""INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at) VALUES('USD',$1,date_trunc('minute',now())) ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman""",after)
        return TradeResult(True,side,cents,gross,fee,price,after)

async def stabilize()->int:
    cfg=get_config()
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if row is None:return 0
        current=int(row["reference_price_toman"]); target=int(row["open_price_toman"]); bp=cfg.int_("market.usd.stabilization_basis_points_per_minute")
        step=max(1,current*bp//10000); after=current-step if current>target else current+step if current<target else current
        if (current-target)*(after-target)<0:after=target
        await conn.execute("UPDATE usd_market_state SET reference_price_toman=$1,updated_at=now() WHERE singleton=TRUE",after)
        await conn.execute("UPDATE market_prices SET current_price_toman=$1,updated_by='stabilizer',updated_at=now() WHERE asset_code='USD'",after)
        return after

async def daily_rollover()->None:
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT reference_price_toman,market_date FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if row and row["market_date"]!=clock.game_today():
            await conn.execute("UPDATE usd_market_state SET open_price_toman=reference_price_toman,net_flow_cents=0,volume_cents=0,health=100,market_date=$1,updated_at=now() WHERE singleton=TRUE",clock.game_today())
```

### `packages\core\services\world_access.py`

```python
"""Minimal, cached TeleWorld permission policy.

Only administrator status and message deletion are required. Editing messages sent by
this bot needs no administrator grant; citizenship is explicit and does not consume
Telegram member events. Dangerous grants such as adding administrators are never asked.
"""
from __future__ import annotations
import time
from dataclasses import dataclass
from telegram.constants import ChatMemberStatus
from packages.core.repositories import world_access_repo

_CACHE_TTL = 20.0
_cache: dict[int, tuple[float, "Access"]] = {}

@dataclass(frozen=True, slots=True)
class Access:
    administrator: bool
    can_delete_messages: bool
    missing: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.missing

    @property
    def fingerprint(self) -> str:
        return ",".join(self.missing) or "ready"

    def missing_fa(self) -> str:
        names = {"administrator": "مدیر بودن بات", "delete_messages": "حذف پیام‌ها"}
        return "، ".join(names.get(item, item) for item in self.missing)

async def check(bot, chat_id: int, *, force: bool = False) -> Access:
    now = time.monotonic()
    cached = _cache.get(chat_id)
    if not force and cached and now - cached[0] < _CACHE_TTL:
        return cached[1]
    me = await bot.get_me()
    member = await bot.get_chat_member(chat_id, me.id)
    administrator = member.status in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}
    can_delete = administrator and bool(getattr(member, "can_delete_messages", False))
    missing: list[str] = []
    if not administrator:
        missing.append("administrator")
    elif not can_delete:
        missing.append("delete_messages")
    result = Access(administrator, can_delete, tuple(missing))
    _cache[chat_id] = (now, result)
    await world_access_repo.save_access(chat_id, administrator, can_delete, missing)
    return result

def invalidate(chat_id: int) -> None:
    _cache.pop(chat_id, None)
```

### `packages\core\services\xp.py`

```python
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
```

### `packages\core\settings.py`

```python
"""Validated, environment-driven runtime settings."""

from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

from pydantic import Field, PostgresDsn, ValidationInfo, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunMode(StrEnum):
    POLLING = "polling"
    WEBHOOK = "webhook"


class Service(StrEnum):
    TELELIFE = "telelife"
    TELEWORLD = "teleworld"
    SCHEDULER = "scheduler"
    ADMIN = "admin"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    service: Service = Service.ADMIN
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    database_url: PostgresDsn
    db_pool_min: int = Field(default=1, ge=1, le=50)
    db_pool_max: int = Field(default=5, ge=1, le=50)
    db_command_timeout: float = Field(default=15.0, gt=0, le=300)
    db_statement_cache_size: int = Field(default=0, ge=0)
    db_max_inactive_seconds: float = Field(default=60.0, ge=10, le=3600)
    memory_warning_mb: int = Field(default=450, ge=64, le=4096)

    telelife_bot_token: str = ""
    teleworld_bot_token: str = ""
    global_news_chat_id: int | None = None

    run_mode: RunMode = RunMode.POLLING
    webhook_base_url: str = ""
    webhook_secret: str = ""
    port: int = Field(default=8000, ge=1, le=65535)
    host: str = "0.0.0.0"  # noqa: S104

    admin_username: str = ""
    admin_password: str = ""

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        normalized = value.upper()
        if normalized not in {"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"}:
            raise ValueError("LOG_LEVEL must be a standard Python logging level")
        return normalized

    @field_validator("db_pool_max")
    @classmethod
    def validate_pool_bounds(cls, value: int, info: ValidationInfo) -> int:
        if value < int(info.data.get("db_pool_min", 1)):
            raise ValueError("DB_POOL_MAX must be greater than or equal to DB_POOL_MIN")
        return value

    @model_validator(mode="after")
    def validate_process_requirements(self) -> Settings:
        # A single supervised process always starts both bots and the admin panel.
        telelife_token = self.token_for(Service.TELELIFE)
        teleworld_token = self.token_for(Service.TELEWORLD)
        if telelife_token == teleworld_token:
            raise ValueError(
                "TELELIFE_BOT_TOKEN and TELEWORLD_BOT_TOKEN must belong to two different bots"
            )
        if not self.admin_username or not self.admin_password:
            raise ValueError("ADMIN_USERNAME and ADMIN_PASSWORD are required")
        if len(self.admin_password) < 12:
            raise ValueError("ADMIN_PASSWORD must contain at least 12 characters")
        if self.run_mode is not RunMode.POLLING:
            raise ValueError("The single-service deployment requires RUN_MODE=polling")
        return self

    def token_for(self, service: Service) -> str:
        token = {
            Service.TELELIFE: self.telelife_bot_token,
            Service.TELEWORLD: self.teleworld_bot_token,
        }.get(service, "").strip()
        if not token:
            raise RuntimeError(f"Missing bot token for service '{service.value}'")
        return token

    def webhook_url(self, service: Service) -> str:
        base = self.webhook_base_url.rstrip("/")
        if not base:
            raise RuntimeError("WEBHOOK_BASE_URL is required in webhook mode")
        return f"{base}/telegram/{service.value}"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
```

### `packages\core\supervisor.py`

```python
"""Fault-isolating asyncio supervisor for all long-running application services."""
from __future__ import annotations

import asyncio
import inspect
import logging
import resource
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

from packages.core.runtime_status import state

logger = logging.getLogger(__name__)
Runner = Callable[[asyncio.Event], Awaitable[None]]
HealthCheck = Callable[[], bool | Awaitable[bool]]


@dataclass(frozen=True, slots=True)
class ServiceSpec:
    name: str
    runner: Runner
    healthcheck: HealthCheck


class ServiceSupervisor:
    """Runs isolated service tasks and restarts only the failed/unhealthy service."""

    def __init__(
        self,
        specs: list[ServiceSpec],
        *,
        health_interval: float = 15.0,
        restart_base: float = 1.0,
        restart_cap: float = 60.0,
        memory_warning_mb: int = 450,
    ) -> None:
        self.specs = specs
        self.health_interval = health_interval
        self.restart_base = restart_base
        self.restart_cap = restart_cap
        self.memory_warning_mb = memory_warning_mb
        self.stop = asyncio.Event()
        self._tasks: dict[str, asyncio.Task[None]] = {}
        self._monitor: asyncio.Task[None] | None = None

    async def run(self) -> None:
        for spec in self.specs:
            self._tasks[spec.name] = asyncio.create_task(
                self._supervise(spec), name=f"supervisor:{spec.name}"
            )
        self._monitor = asyncio.create_task(self._monitor_loop(), name="supervisor:monitor")
        await self.stop.wait()
        await self.shutdown()

    async def _supervise(self, spec: ServiceSpec) -> None:
        failures = 0
        item = state(spec.name)
        while not self.stop.is_set():
            local_stop = asyncio.Event()
            item.status = "starting"
            item.last_started_monotonic = time.monotonic()
            service_task = asyncio.create_task(spec.runner(local_stop), name=f"service:{spec.name}")
            try:
                while not self.stop.is_set():
                    stop_waiter = asyncio.create_task(self.stop.wait())
                    done, _ = await asyncio.wait(
                        {service_task, stop_waiter}, timeout=self.health_interval,
                        return_when=asyncio.FIRST_COMPLETED,
                    )
                    if not stop_waiter.done():
                        stop_waiter.cancel()
                    await asyncio.gather(stop_waiter, return_exceptions=True)
                    if stop_waiter in done:
                        local_stop.set()
                        try:
                            await asyncio.wait_for(service_task, timeout=20.0)
                        except TimeoutError:
                            service_task.cancel()
                            await asyncio.gather(service_task, return_exceptions=True)
                        return
                    if service_task.done():
                        exc = service_task.exception()
                        if exc:
                            raise exc
                        raise RuntimeError("service exited unexpectedly")
                    healthy = spec.healthcheck()
                    if inspect.isawaitable(healthy):
                        healthy = await healthy
                    if not healthy:
                        raise RuntimeError("service health check failed")
                    item.status = "healthy"
                    item.last_healthy_monotonic = time.monotonic()
                    if time.monotonic() - (item.last_started_monotonic or 0) >= 300:
                        failures = 0
            except asyncio.CancelledError:
                local_stop.set()
                service_task.cancel()
                await asyncio.gather(service_task, return_exceptions=True)
                raise
            except Exception as exc:  # service boundary intentionally catches everything
                item.status = "restarting"
                item.last_error = f"{type(exc).__name__}: {exc}"
                item.restarts += 1
                failures += 1
                logger.exception("service %s failed; restart scheduled", spec.name)
                local_stop.set()
                service_task.cancel()
                await asyncio.gather(service_task, return_exceptions=True)
                delay = min(self.restart_cap, self.restart_base * (2 ** min(failures - 1, 8)))
                try:
                    await asyncio.wait_for(self.stop.wait(), timeout=delay)
                except TimeoutError:
                    pass
            finally:
                local_stop.set()
        item.status = "stopped"

    async def _monitor_loop(self) -> None:
        while not self.stop.is_set():
            rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            if rss_mb >= self.memory_warning_mb:
                logger.warning("high process memory watermark: %.1f MiB", rss_mb)
            logger.info(
                "supervisor heartbeat rss_mb=%.1f tasks=%d services=%d",
                rss_mb, len(asyncio.all_tasks()), len(self._tasks),
            )
            try:
                await asyncio.wait_for(self.stop.wait(), timeout=60)
            except TimeoutError:
                pass

    async def shutdown(self) -> None:
        self.stop.set()
        for task in self._tasks.values():
            task.cancel()
        if self._monitor:
            self._monitor.cancel()
        await asyncio.gather(*self._tasks.values(), return_exceptions=True)
        if self._monitor:
            await asyncio.gather(self._monitor, return_exceptions=True)
        for spec in self.specs:
            state(spec.name).status = "stopped"
```

### `packages\core\ui\__init__.py`

```python
"""Telegram UI primitives, loaded lazily to keep submodules independent."""

from __future__ import annotations

from typing import Any

__all__ = [
    "Callback",
    "Keyboard",
    "Style",
    "button",
    "cb",
    "schedule_cleanup",
    "timeout_for",
]


def __getattr__(name: str) -> Any:
    if name in {"Callback", "cb"}:
        from packages.core.ui import callbacks

        return getattr(callbacks, name)
    if name in {"Keyboard", "Style", "button"}:
        from packages.core.ui import buttons

        return getattr(buttons, name)
    if name in {"schedule_cleanup", "timeout_for"}:
        from packages.core.ui import panels

        return getattr(panels, name)
    raise AttributeError(name)
```

### `packages\core\ui\buttons.py`

```python
"""Glass keyboard system (Bot API 9.4 button styles).

Telegram exposes exactly three styles: primary / success / danger.
No style = the default translucent "glass" background - our neutral default.

Rules enforced here:
- Colour is emphasis, never meaning. Button text must stand alone.
- At most ONE primary per keyboard. Colour everywhere = colour nowhere.
- Old clients silently ignore `style`, so layouts must read fine uncoloured.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Self

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Style(StrEnum):
    """Bot API 9.4 button styles. GLASS means: send no style field at all."""

    GLASS = "glass"
    PRIMARY = "primary"
    SUCCESS = "success"
    DANGER = "danger"


def button(
    text: str,
    callback_data: str,
    *,
    style: Style = Style.GLASS,
    icon_custom_emoji_id: str | None = None,
) -> InlineKeyboardButton:
    """Build one button. GLASS omits `style` so the client uses its default."""
    kwargs: dict[str, object] = {"text": text, "callback_data": callback_data}
    if style is not Style.GLASS:
        kwargs["style"] = style.value
    if icon_custom_emoji_id:
        kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
    return InlineKeyboardButton(**kwargs)  # type: ignore[arg-type]


def url_button(text: str, url: str, *, style: Style = Style.GLASS) -> InlineKeyboardButton:
    kwargs: dict[str, object] = {"text": text, "url": url}
    if style is not Style.GLASS:
        kwargs["style"] = style.value
    return InlineKeyboardButton(**kwargs)  # type: ignore[arg-type]


class Keyboard:
    """Small fluent builder. Keeps handlers free of nested list noise."""

    __slots__ = ("_rows",)

    def __init__(self) -> None:
        self._rows: list[list[InlineKeyboardButton]] = []

    def row(self, *buttons: InlineKeyboardButton) -> Self:
        if buttons:
            self._rows.append(list(buttons))
        return self

    def add(
        self,
        text: str,
        callback_data: str,
        *,
        style: Style = Style.GLASS,
        icon_custom_emoji_id: str | None = None,
    ) -> Self:
        return self.row(
            button(text, callback_data, style=style, icon_custom_emoji_id=icon_custom_emoji_id)
        )

    def grid(self, buttons: list[InlineKeyboardButton], per_row: int = 2) -> Self:
        for i in range(0, len(buttons), per_row):
            self.row(*buttons[i : i + per_row])
        return self

    def build(self) -> InlineKeyboardMarkup:
        self._assert_single_primary()
        return InlineKeyboardMarkup(self._rows)

    def _assert_single_primary(self) -> None:
        primaries = sum(
            1
            for row in self._rows
            for b in row
            if getattr(b, "style", None) == Style.PRIMARY.value
        )
        if primaries > 1:
            raise ValueError(
                f"Keyboard has {primaries} primary buttons. Exactly one action leads."
            )
```

### `packages\core\ui\callbacks.py`

```python
"""Signed, owned, expiring callback payloads.

Format:  ns:action:owner_id:arg
`owner_id` is embedded so a stranger tapping your panel is rejected without a
database round-trip. Cheapest possible ownership check.
"""

from __future__ import annotations

from dataclasses import dataclass

SEP = ":"


@dataclass(slots=True, frozen=True)
class Callback:
    namespace: str
    action: str
    owner_id: int
    arg: str = ""

    def pack(self) -> str:
        parts = [self.namespace, self.action, str(self.owner_id)]
        if self.arg:
            parts.append(self.arg)
        data = SEP.join(parts)
        if len(data.encode()) > 64:
            raise ValueError(f"callback_data exceeds Telegram 64-byte limit: {data!r}")
        return data

    @classmethod
    def parse(cls, raw: str) -> Callback | None:
        parts = raw.split(SEP)
        if len(parts) < 3:
            return None
        try:
            owner_id = int(parts[2])
        except ValueError:
            return None
        return cls(parts[0], parts[1], owner_id, parts[3] if len(parts) > 3 else "")

    def owned_by(self, telegram_id: int) -> bool:
        return self.owner_id == telegram_id


def cb(namespace: str, action: str, owner_id: int, arg: str = "") -> str:
    return Callback(namespace, action, owner_id, arg).pack()
```

### `packages\core\ui\panels.py`

```python
"""Auto-expiring interactive panels.

Every panel schedules its own cleanup via the PTB job queue. Timeouts come from
`core.menu_cleanup` in config - nothing hardcoded. On expiry the keyboard is
stripped, not the message: the player keeps the information, we free the
callback surface.
"""

from __future__ import annotations

import logging

from telegram import Message
from telegram.error import BadRequest, Forbidden
from telegram.ext import ContextTypes

from packages.core.config import get_config

logger = logging.getLogger(__name__)


def timeout_for(panel: str) -> int:
    cfg = get_config()
    default = cfg.int_("core.menu_cleanup.default_timeout_seconds")
    return int(cfg.section("core.menu_cleanup").get("panels", {}).get(panel, default))


async def _expire(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    if job is None or not isinstance(job.data, dict):
        return
    chat_id = job.data["chat_id"]
    message_id = job.data["message_id"]
    try:
        await context.bot.edit_message_reply_markup(
            chat_id=chat_id, message_id=message_id, reply_markup=None
        )
    except BadRequest as exc:
        logger.debug("panel cleanup no-op for chat %s: %s", chat_id, exc)
    except Forbidden:
        logger.info("panel cleanup skipped: bot removed from chat %s", chat_id)


def schedule_cleanup(
    context: ContextTypes.DEFAULT_TYPE, message: Message, panel: str
) -> None:
    """Arm auto-cleanup for a panel, replacing any previous timer on it."""
    if not get_config().bool_("core.menu_cleanup.enabled"):
        return
    if context.job_queue is None:
        return

    name = f"panel:{message.chat_id}:{message.message_id}"
    for existing in context.job_queue.get_jobs_by_name(name):
        existing.schedule_removal()

    context.job_queue.run_once(
        _expire,
        when=timeout_for(panel),
        name=name,
        data={"chat_id": message.chat_id, "message_id": message.message_id},
    )
```

### `packages\core\utils\__init__.py`

```python
"""Shared formatting and timezone utilities."""

from packages.core.utils import clock, fmt

__all__ = ["clock", "fmt"]
```

### `packages\core\utils\clock.py`

```python
"""Timezone-aware game clock utilities.

All domain dates are derived from the configured IANA timezone. Keeping this in
one module prevents UTC/local-date drift around midnight and makes time policy
explicit for every service.
"""

from __future__ import annotations

from datetime import UTC, date, datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from packages.core.config import ConfigError, get_config


def game_timezone() -> ZoneInfo:
    """Return the configured game timezone, raising a clear config error."""
    name = str(get_config().get("core.timezone"))
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError as exc:
        raise ConfigError(f"Invalid IANA timezone in core.timezone: {name}") from exc


def utcnow() -> datetime:
    """Return an aware UTC timestamp."""
    return datetime.now(UTC)


def game_today(now: datetime | None = None) -> date:
    """Return the calendar date in the configured game timezone."""
    current = now or utcnow()
    if current.tzinfo is None:
        raise ValueError("game_today requires a timezone-aware datetime")
    return current.astimezone(game_timezone()).date()


def day_stamp(now: datetime | None = None) -> str:
    """Return the ISO game date used in idempotency keys."""
    return game_today(now).isoformat()
```

### `packages\core\utils\fmt.py`

```python
"""Persian-first formatting helpers. Numbers must always look native."""

from __future__ import annotations

_FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def group_digits(value: int) -> str:
    return f"{value:,}".replace(",", "٬")


def fa_digits(text: str) -> str:
    return text.translate(_FA_DIGITS)


def toman(amount: int, *, persian: bool = True) -> str:
    out = f"{group_digits(amount)} تومان"
    return fa_digits(out) if persian else out


def usd(cents: int, *, persian: bool = True) -> str:
    whole, frac = divmod(abs(cents), 100)
    sign = "-" if cents < 0 else ""
    out = f"{sign}{group_digits(whole)}.{frac:02d}$"
    return fa_digits(out) if persian else out


def number(value: int, *, persian: bool = True) -> str:
    out = group_digits(value)
    return fa_digits(out) if persian else out


def progress_bar(current: int, total: int, width: int = 10) -> str:
    if total <= 0:
        return "▱" * width
    filled = max(0, min(width, round(current / total * width)))
    return "▰" * filled + "▱" * (width - filled)
```

### `pyproject.toml`

```toml
[project]
name = "telelife"
version = "0.1.0"
description = "TeleLife / TeleWorld - Telegram Virtual Life Simulator"
requires-python = ">=3.13"
dependencies = [
    "python-telegram-bot[rate-limiter,webhooks,job-queue]>=22.8,<23",
    "asyncpg>=0.30,<1",
    "pydantic>=2.9,<3",
    "pydantic-settings>=2.5,<3",
    "PyYAML>=6.0.2,<7",
    "uvicorn[standard]>=0.31,<1",
    "fastapi>=0.115,<1",
    "jinja2>=3.1.4,<4",
    "orjson>=3.10.7,<4",
    "python-multipart>=0.0.12,<1",
]

[project.optional-dependencies]
dev = ["pytest>=8.3.0", "pytest-asyncio>=0.24.0", "ruff>=0.6.0", "mypy>=1.11.0"]

[tool.ruff]
line-length = 100
target-version = "py313"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "ASYNC", "S", "SIM"]
ignore = ["S101"]

[tool.mypy]
python_version = "3.13"
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
asyncio_mode = "auto"
```

### `README.md`

```markdown
# TeleLife / TeleWorld

استقرار تک‌پردازه شامل دو ربات Telegram، زمان‌بند و پنل FastAPI است.

## معماری اجرا

`run.py` یک pool مشترک asyncpg و migrationها را راه‌اندازی می‌کند و `ServiceSupervisor` چهار سرویس زیر را به‌صورت taskهای مستقل اجرا می‌کند:

- TeleLife polling bot
- TeleWorld polling bot
- Scheduler (minute/daily loops)
- FastAPI Admin (تنها listener روی `PORT`)

خرابی هر سرویس در مرز Supervisor مهار و با exponential backoff همان سرویس restart می‌شود. `SIGTERM` و `SIGINT` باعث graceful shutdown همه taskها، Telegram applications، Uvicorn و pool دیتابیس می‌شوند.

## استقرار Render

1. repository را به GitHub push کنید.
2. در Render یک Blueprint از `render.yaml` بسازید؛ فقط یک Web Service Free تعریف می‌شود.
3. secretها را وارد کنید: `DATABASE_URL`، هر دو bot token، و اطلاعات admin.
4. برای Supabase Transaction Pooler از port `6543`، `sslmode=require` و `DB_STATEMENT_CACHE_SIZE=0` استفاده کنید.
5. migrationها هنگام startup و پیش از سرویس‌ها، تحت advisory lock اجرا می‌شوند.

Health: `/healthz` — Readiness: `/readyz` — داشبورد و API مدیریت با HTTP Basic محافظت شده‌اند.

## اجرا و تست
```

### `README_FA.md`

```markdown
# راه‌اندازی نسخه فارسی تله‌لایف

## پیش‌نیازها
- پایتون ۳٫۱۱ یا جدیدتر
- پایگاه‌داده PostgreSQL سازگار
- دو توکن جداگانه: یکی برای بات زندگی و یکی برای بات جهان

## راه‌اندازی
1. فایل `.env.example` را با نام `.env` کپی کنید.
2. نشانی پایگاه‌داده، توکن هر دو بات و اطلاعات پنل مدیریت را وارد کنید.
3. وابستگی‌ها را از `requirements.txt` نصب کنید.
4. برنامه را با `python run.py` اجرا کنید. مهاجرت‌های پایگاه‌داده هنگام راه‌اندازی اعمال می‌شوند.

## تنظیم ضروری بات جهان
برای اینکه بات جهان با **هر پیام معمولی در گروه** صفحه بازی را باز کند، در BotFather برای بات جهان وارد بخش تنظیمات حریم خصوصی گروه شوید و حالت حریم خصوصی را خاموش کنید. سپس بات را در گروه مدیر کنید تا بتواند پیام‌های مرحله ساخت کشور را پاک و صفحه قبلی را ویرایش کند.

بات جهان هیچ فرمان متنی لازم ندارد و منوی فرمان‌های قدیمی را هنگام راه‌اندازی پاک می‌کند. تعامل عمومی کشور با پیام و دکمه‌های درون‌پیامی انجام می‌شود.

## تقسیم مسئولیت دو بات
- **بات زندگی:** شخصیت، هدیه روزانه، کارهای روزانه، انتخاب شغل، کارکردن، دریافت درآمد، ارتقای شغل، بانک، خانه و بازار شخصی.
- **بات جهان:** کشور، شهروندی، خزانه عمومی، منابع کشور، انتخابات و پروژه ملی.

## بررسی سلامت
- `GET /healthz` برای سلامت کل سرویس‌ها
- `GET /readyz` برای آمادگی پایگاه‌داده

## آزمون
پس از نصب وابستگی‌های توسعه، `pytest -q` را اجرا کنید. آزمون قراردادی `test_persian_button_contracts.py` فارسی‌بودن شغل‌ها، نبود فرمان در بات جهان، معتبر بودن تنظیمات و صحت نحوی فایل‌ها را کنترل می‌کند.
```

### `RELEASE_2026_07_27_FA.md`

```markdown
# انتشار ارتقای مدیریت، تبلیغات و سیاست

- پنل مدیریت واکنش‌گرا با صفحه اختصاصی کمپین تبلیغاتی، ارسال فوری، زمان‌بندی و تکرار خودکار.
- صف Outbox برای انتشار مطمئن پیام‌ها و جلوگیری از ارسال تکراری.
- پالایش Unicode-aware نام و معرفی کشور، مقاوم در برابر تکرار حروف، فاصله، نیم‌فاصله، کشیده و خط تیره؛ با مرزبندی برای کاهش خطای مثبت.
- حفظ فرایند ساخت پس از هشدار و دادن فرصت اصلاح به سازنده.
- ۱۳ نوع حکومت همراه با توضیح و تأیید پیش از انتخاب.
- قواعد اجرایی متفاوت برای انتخابات عمومی، انتخاب شورایی/نخبگانی/موروثی، کنترل نامزدها و اختیار دستکاری نتیجه در دیکتاتوری.
- مهاجرت دیتابیس 0009 و تست‌های پالایش و حکمرانی.

> این مدل‌ها شبیه‌سازی بازی‌اند و ادعای بازسازی کامل همه پیچیدگی‌های سیاست واقعی ندارند؛ با این حال تفاوت نهادی آن‌ها اکنون در منطق برنامه اجرا می‌شود، نه فقط در عنوان.
```

### `RELEASE_AUDIT_FA.md`

```markdown
# ممیزی نسخه نهایی فارسی

## خطای گزارش‌شده
خطای «دو دکمه اصلی» از ترکیب حالت آموزش فعال با دکمه اصلی شغل ایجاد می‌شد. صفحه خانه اکنون در هر وضعیت دقیقاً یک اقدام اصلی دارد. همه ۵۰+ ترکیب صفحه‌کلید به‌صورت اجرایی ساخته و محدودیت تعداد دکمه اصلی و اندازه داده بازگشتی بررسی شده‌اند.

## اصلاحات تکمیلی
- حذف کنترل‌گرهای قدیمی و ثبت‌نشده برای جلوگیری از دو منبع حقیقت و بازگشت ناخواسته فرمان‌ها.
- پیام‌محور شدن هر دو بات و پاک‌ماندن منوی فرمان‌ها.
- ساخت صفحه واقعی برای پس‌انداز و خانه؛ این دو دیگر به صفحه عمومی اقتصاد برنمی‌گردند.
- پنهان‌کردن عملیات شغل پیش از سطح ۵ و بازار پیش از سطح ۱۰.
- فارسی‌سازی خروجی شغل و منابع در همه کنترل‌گرهای فعال.
- تفکیک درست مرحله نامزدی و رأی‌گیری؛ دکمه رأی فقط هنگام رأی‌گیری نمایش داده می‌شود.
- بررسی عضویت فعال برای کمک مالی و پروژه ملی.
- جلوگیری از شروع دوباره پروژه ملی یک‌باره پس از تکمیل.
- حذف اجاره منقضی و جلوگیری از محاسبه هزینه خانه پس از پایان اجاره.
- ایمن‌سازی متن‌های کاربرساخته در حالت قالب‌بندی HTML.
- مدیریت دکمه‌های قدیمی، دوبارکلیک و پاسخ منقضی‌شده بدون ایجاد خطای ثانویه.
- افزودن آزمون ماتریسی تمام حالت‌های پویای رابط و آزمون معماری پیام‌محور.

## نتیجه آزمون آفلاین
- نحو همه فایل‌های پایتون: موفق
- اعتبار همه فایل‌های YAML: موفق
- ماتریس اجرایی صفحه‌کلیدها: موفق
- ۷۴ آزمون قابل اجرا در محیط آفلاین: موفق
- اسکن توکن و اطلاعات محرمانه: موفق

آزمون یکپارچه با PostgreSQL و سرور واقعی تلگرام ذاتاً به پایگاه‌داده و توکن‌های محیط استقرار نیاز دارد؛ بنابراین ادعای «صفر باگ مطلق» ممکن نیست، اما مسیرهای قابل آزمون در بسته پوشش داده شده‌اند.
```

### `RELEASE_AUDIT_FA_2026-07-27.md`

```markdown
# ممیزی باگ و منطق

## اصلاح‌شده

1. کنترل‌گر فعال جهان رویداد عضویت بات را ثبت نمی‌کرد؛ اکنون قبل از کنترل‌گرهای رابط ثبت می‌شود.
2. خوش‌آمدگویی قبلی فاقد ثبت پایگاه‌داده بود و تکرار می‌شد؛ اکنون claim اتمیک دارد.
3. عملیات کشور فقط مدیر بودن کاربر را می‌سنجید، نه دسترسی خود بات؛ قفل مرکزی اضافه شد.
4. کلیدهای مالی تصادفی، دوبارکلیک را عملیات تازه می‌دیدند؛ شناسه Callback جایگزین شد.
5. حذف پیام مرحله‌ای بدون بازاعتبارسنجی بود؛ اکنون دسترسی کنترل و شکست حذف به هشدار محدود تبدیل می‌شود.
6. Privacy Mode قابل تشخیص فرض نشده و راهنمای واقعی BotFather نوشته شد.

## تصمیم‌های محصولی

- شهروندی بازی مستقل از عضویت تلگرام نگه داشته شد؛ بنابراین مجوز محدودسازی اعضا لازم نیست.
- ویرایش پیام خود بات مجوز مدیر نمی‌خواهد؛ از فهرست مجوزها حذف شد.
- افزودن مدیر و تغییر اطلاعات گروه مطالبه نمی‌شود.
- در حالت محدود، داده کشور حذف نمی‌شود و فقط mutationها قفل می‌شوند.

## محدودیت محیط تحویل

در محیط ساخت حاضر Python 3.10 نصب است، درحالی‌که پروژه Python 3.13 و وابستگی‌های Telegram/asyncpg/pytest می‌خواهد. اینترنت نیز برای نصب وابستگی‌ها در دسترس نیست. بنابراین آزمون‌های اجرایی و یکپارچه PostgreSQL در این محیط اجرا نشدند و موفق اعلام نمی‌شوند. اعتبارسنجی نحوی Python، YAML، ساختار بسته، اسکن اسرار و آزمون‌های ایستای داخلی انجام می‌شوند.
```

### `RELEASE_COMMERCE_FA.md`

```markdown
# انتشار اشتراک و بازار تبلیغات

## اشتراک گروه
- اشتراک ۳۰روزه بدون تبلیغ با مجموع ۱۰ استار.
- مشارکت گروهی با سهم‌های ۱، ۲، ۵ و ۱۰ استار؛ فعال‌سازی اتمیک با رسیدن مجموع به ۱۰.
- خرید جایگزین از خزانه: ۲۰٪ موجودی، حداقل ۲۰ میلیون و حداکثر ۲۰۰ میلیون تومان؛ فقط رهبر کشور.
- تمدید روی اعتبار موجود و حذف لحظه‌ای گروه مشترک از جامعه هدف.

## بازار تبلیغ در TeleLife
- چهار بسته: اقتصادی ۲۵، استاندارد ۶۰، کمپین ۱۲۰ و ویژه ۲۰۰ استار.
- دریافت عنوان، توضیح، لینک، تصویر تا ۵MB و زمان شروع.
- بررسی مدیر پیش از هر پرداخت؛ تأیید، ویرایش، درخواست اصلاح و ارسال مجدد.
- صدور خودکار صورتحساب XTR پس از تأیید، با مهلت ۴۸ ساعت.
- Pre-checkout امن، شناسه یکتا، تسویه idempotent و ثبت charge ID.
- برنامه‌ریزی خودکار فقط برای گروه‌های فعال، سالم و غیرمشترک؛ سقف دو تبلیغ روزانه برای هر گروه.
- توقف اضطراری، گزارش تحویل و بازپرداخت قبل از نخستین نمایش.

## فنی
- مهاجرت 0010، سرویس commerce، رابط‌های دو بات و صفحه بازبینی پنل مدیریت.
- تصویر در دیتابیس نگهداری می‌شود تا بین TeleLife و TeleWorld قابل ارسال باشد.
- Syntax تمام فایل‌های Python و تست‌های واحد اقتصاد/URL/بسته‌ها بررسی شد.
```

### `RELEASE_NOTES_FA.md`

```markdown
# نسخه پایدار TeleLife + TeleWorld

## تغییرات اصلی
- تکمیل قرارداد Ledger برای حساب بازیکن، خزانه کشور و منابع.
- رفع Race Condition کلیدهای تکراری در انتقال دارایی و اصلاح کشور.
- افزودن چرخه کشور: در حال ساخت، موقت و رسمی.
- افزودن عضویت فعال/خروج و شمارش جمعیت بر اساس شهروندان کشور.
- ثبت منابع اولیه کشور در Ledger.
- الزام شهروندی برای شروع انتخابات، نامزدی و رأی.
- جلوگیری دیتابیسی از دو انتخابات باز برای یک کشور.
- الزام شهروندبودن رئیس کشور در سطح دیتابیس.
- اعمال قفل سطح ۵ برای انتخاب شغل در Service.
- حذف ثبت تکراری مسیر `/start` در TeleWorld.
- تبدیل صفحات اصلی World به ویرایش همان پیام و مدیریت مشخص BadRequest.
- افزودن تست‌های قرارداد و Migration سخت‌سازی.

## راه‌اندازی
1. متغیرهای `.env` را بر اساس `.env.example` تنظیم کنید.
2. Dependencyهای `requirements.txt` را نصب کنید.
3. برنامه در Startup، Migrationهای ترتیبی را اعمال می‌کند.
4. سرویس را با `python run.py` اجرا کنید.

## بررسی انجام‌شده
- استخراج کامل ۱۴۸ فایل متنی دامپ پروژه.
- موفقیت Compile تمام فایل‌های Python.
- موفقیت بررسی AST تمام فایل‌ها.
- موفقیت بررسی استاتیک قرارداد فراخوانی Repositoryها.
- وجود و ترتیب Migration جدید بررسی شد.

## محدودیت بررسی محلی
در محیط بسته‌بندی، Dependencyهای Runtime از جمله `asyncpg` و فرمان `pytest` نصب نبودند؛ بنابراین تست Integration متصل به PostgreSQL/Telegram اجرا نشد. تست‌های پروژه و تست سخت‌سازی داخل بسته قرار دارند و باید در CI یا محیط پروژه، پس از نصب requirements و اتصال دیتابیس آزمایشی اجرا شوند.

## تکمیل فاز ۳ و ۴
- پس‌انداز دوطرفه با دو Leg حسابرسی‌شده و Transaction واحد
- خانه، اجاره هفتگی، خرید خانه و هزینه زندگی
- رابط شغلی شیشه‌ای، دریافت تولید و ارتقای انبار/تولید
- بازار دلار با خرید/فروش، کارمزد، Spread، Price Impact و سقف روزانه
- باند نوسان، شاخص سلامت، Freeze اضطراری، تثبیت دقیقه‌ای و تاریخچه قیمت
- حذف فرمان‌های متنی کاربری؛ فقط `/start` به‌عنوان نقطه ورود الزامی تلگرام باقی مانده است
- ناوبری Life و World بر پایه Inline Keyboard رنگی و ویرایش همان پیام
```

### `RELEASE_SCALING_MIGRATION_FA.md`

```markdown
# انتشار قیمت‌گذاری جمعیتی، تبلیغات چندکاناله و مهاجرت

## اشتراک بدون تبلیغ
- قیمت استارز پلکانی بر اساس شهروندان فعال کشور: تا ۲۰ نفر ۱۰⭐، تا ۱۰۰ نفر ۱۵⭐، تا ۵۰۰ نفر ۳۰⭐، تا ۱۰۰۰ نفر ۵۰⭐ و بیشتر ۷۵⭐.
- مشارکت اعضا با سهم‌های ۱، ۲، ۵، ۱۰، ۲۵ و ۵۰ استار.
- قیمت خزانه: ۲۰٪ خزانه + یک میلیون تومان برای هر شهروند، کف ۲۰ میلیون و سقف یک میلیارد تومان.

## تبلیغات سه‌کاناله
- Life: پیام خصوصی کاربران سالم و فعال ۳۰ روز اخیر، ضریب ×۱.
- World: گروه‌های فعال و غیرمشترک، ضریب ×۱٫۵.
- Life + World: هر دو جامعه، ضریب ×۲٫۲.
- قیمت با گردکردن رو به بالا محاسبه می‌شود؛ برای نمونه اقتصادی ۲۵/۳۸/۵۵ استار است.
- پیام Life با توکن بات Life و پیام World با توکن بات World ارسال می‌شود.

## مهاجرت کشور
- عوارض ۵٪ کل دارایی شخصی، کف ۵۰۰ هزار و سقف ۵۰ میلیون تومان؛ انتقال به خزانه مبدأ هنگام تکمیل.
- محدودیت تغییر کشور هر ۳۰ روز؛ رهبر مبدأ باید ابتدا قدرت را منتقل کند.
- اگر مقصد رهبر داشته باشد، درخواست ۷۲ ساعت اعتبار دارد؛ در غیر این صورت مهاجرت خودکار است.
- نشان «مهاجر» ۳۰ روز و محرومیت رأی، نامزدی و آغاز پروژه ملی ۱۴ روز.
- خروج مستقیم بسته شده تا عوارض و محدودیت زمانی دور زده نشود.
- ثبت دوطرفه عوارض در دفتر کل و انقضای خودکار درخواست‌ها.
```

### `RELEASE_V2_FA.md`

```markdown
# TeleLife V2 — هویت کشور، نمودار واقعی و اقتصاد کلان

## رفتار هویت کشور

- پیام‌های سیستمی Outbox که مقصدشان یک گروه TeleWorld است، پیش از ارسال کشور مقصد را از دیتابیس می‌خوانند.
- سربرگ پیام با «خبرگزاری {نام کشور}» ساخته می‌شود و عنوان تلگرامی گروه در متن استفاده نمی‌شود.
- خلاصه روزانه، رویدادهای کوتاه و هشدارهای بازار فقط برای گروه‌های دارای کشور ساخته می‌شوند.
- اگر گروه ثبت شده اما کشور ندارد، پیام سیستمی ارسال نمی‌شود و راهنمای ساخت کشور فقط یک بار نمایش داده می‌شود.
- پیام‌های شخصی TeleLife و مقصدهای عمومی خارج از TeleWorld بدون سربرگ کشور باقی می‌مانند.

## نمودار بازار TeleLife

- نمودار PNG واقعی USDT/IRT با ۴۸ کندل نیم‌ساعته برای ۲۴ ساعت اخیر.
- OHLC مستقیماً از `market_price_snapshots` ساخته می‌شود.
- snapshotها از نرخ اعتبارسنجی‌شده Zipodo تغذیه می‌شوند.
- فاصله‌های بدون snapshot جعل یا با نوسان تصادفی پر نمی‌شوند.
- نمودار قبلی کاربر هنگام تازه‌سازی حذف می‌شود تا گفت‌وگوی خصوصی شلوغ نشود.
- Pillow به وابستگی‌های Docker افزوده شده است.

## اقتصاد واقعی‌تر کشور

- بانک مرکزی: نرخ بهره، هدف تورم و ذخیره ارزی.
- رئیس کشور می‌تواند نرخ بهره را هر بار یک درصد بالا/پایین ببرد.
- رئیس می‌تواند ۱۰ میلیون تومان خزانه را با نرخ زنده بازار به ذخیره ارزی تبدیل کند.
- شاخص‌های روزانه: تورم، بیکاری، رشد، رضایت و GDP.
- نرخ بهره بالاتر فشار تورمی را کم می‌کند، اما روی رشد هزینه دارد.
- ذخیره ارزی اثر تحریم و خشکسالی را کاهش می‌دهد.
- شوک‌های کمیاب با seed کشور/تاریخ تعیین می‌شوند؛ ری‌استارت نتیجه را عوض نمی‌کند.
- روزنامه اختصاصی هر کشور از داده‌های واقعی همان کشور تولید و با نام کشور منتشر می‌شود.

## استقرار

1. از PostgreSQL پشتیبان بگیرید.
2. نسخه جدید را Deploy کنید تا Migration شماره `0013` اجرا شود.
3. ساخت image جدید ضروری است، چون وابستگی Pillow افزوده شده است.
4. صبر کنید حداقل چند snapshot نرخ ثبت شود؛ نمودار از داده موجود استفاده می‌کند.
5. در TeleLife وارد «بازار ارز» شوید و تصویر کندلی را بررسی کنید.
6. در TeleWorld وارد «اقتصاد و منابع ← بانک مرکزی و شاخص‌ها» شوید.
7. یک گروه بدون کشور را بررسی کنید؛ تنها راهنمای ساخت کشور باید نمایش داده شود.

## اعتبارسنجی

- AST و compile روی ۱۴۱ فایل Python: موفق
- Syntax پنل JavaScript: موفق
- تولید آزمایشی PNG با ۴۸ کندل: موفق، ۱۲۰۰×۶۶۰
- قرارداد Migration 0013: موفق
- نبود استفاده از عنوان گروه در engagement و ارسال سیستمی: تأیید شد
- قفل نامعتبر قدیمی `FOR UPDATE OF d,g`: وجود ندارد
- اجرای کامل pytest در sandbox ممکن نبود، چون pytest و وابستگی‌های پروژه در محیط آفلاین نصب نیستند. پس از build اجرا شود: `python -m pytest -q`.
```

### `render.yaml`

```yaml
services:
  - type: web
    name: telelife
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: free
    healthCheckPath: /healthz
    autoDeployTrigger: commit
    envVars:
      - {key: ENVIRONMENT, value: production}
      - {key: RUN_MODE, value: polling}
      - {key: DATABASE_URL, sync: false}
      - {key: DB_POOL_MIN, value: "1"}
      - {key: DB_POOL_MAX, value: "4"}
      - {key: DB_COMMAND_TIMEOUT, value: "15"}
      - {key: DB_STATEMENT_CACHE_SIZE, value: "0"}
      - {key: DB_MAX_INACTIVE_SECONDS, value: "60"}
      - {key: TELELIFE_BOT_TOKEN, sync: false}
      - {key: TELEWORLD_BOT_TOKEN, sync: false}
      - {key: GLOBAL_NEWS_CHAT_ID, sync: false}
      - {key: ADMIN_USERNAME, sync: false}
      - {key: ADMIN_PASSWORD, sync: false}
      - {key: MEMORY_WARNING_MB, value: "450"}
```

### `requirements.txt`

```text
python-telegram-bot[rate-limiter,webhooks,job-queue]>=22.8,<23
asyncpg>=0.30,<1
pydantic>=2.9,<3
pydantic-settings>=2.5,<3
PyYAML>=6.0.2,<7
uvicorn[standard]>=0.31,<1
fastapi>=0.115,<1
jinja2>=3.1.4,<4
orjson>=3.10.7,<4
python-multipart>=0.0.12,<1
Pillow>=10.4,<12
```

### `run.py`

```python
"""Single-container entrypoint supervising both bots, scheduler and FastAPI."""
from __future__ import annotations

import asyncio
import logging
import signal

import uvicorn

from apps.scheduler.main import SchedulerService
from apps.telelife_bot.main import register as register_telelife
from apps.teleworld_bot.main import register as register_teleworld
from packages.core import db
from packages.core.bot import PollingService
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import Service, get_settings
from packages.core.supervisor import ServiceSpec, ServiceSupervisor

logger = logging.getLogger(__name__)


class AdminService:
    def __init__(self, settings) -> None:  # type: ignore[no-untyped-def]
        config = uvicorn.Config(
            "apps.admin.main:app", host=settings.host, port=settings.port,
            log_level=settings.log_level.lower(), proxy_headers=True,
            forwarded_allow_ips="127.0.0.1", lifespan="on", access_log=True,
        )
        self.server = uvicorn.Server(config)

    def healthy(self) -> bool:
        return bool(self.server.started and not self.server.should_exit)

    async def run(self, stop: asyncio.Event) -> None:
        self.server.should_exit = False
        serve = asyncio.create_task(self.server.serve(), name="admin:uvicorn")
        stop_waiter = asyncio.create_task(stop.wait(), name="admin:stop")
        done, _ = await asyncio.wait({serve, stop_waiter}, return_when=asyncio.FIRST_COMPLETED)
        if stop_waiter in done:
            self.server.should_exit = True
            await serve
        else:
            stop_waiter.cancel()
            await asyncio.gather(stop_waiter, return_exceptions=True)
            await serve


async def amain() -> None:
    settings = get_settings()
    setup_logging("supervisor", settings.log_level)
    await db.create_pool(settings)
    await migrate()

    telelife = PollingService(settings, Service.TELELIFE, register_telelife)
    teleworld = PollingService(settings, Service.TELEWORLD, register_teleworld)
    scheduler = SchedulerService(settings)
    admin = AdminService(settings)
    supervisor = ServiceSupervisor([
        ServiceSpec("telelife", telelife.run, telelife.healthy),
        ServiceSpec("teleworld", teleworld.run, teleworld.healthy),
        ServiceSpec("scheduler", scheduler.run, scheduler.healthy),
        ServiceSpec("admin", admin.run, admin.healthy),
    ], memory_warning_mb=settings.memory_warning_mb)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, supervisor.stop.set)
        except NotImplementedError:
            pass
    try:
        await supervisor.run()
    finally:
        await db.close_pool()
        logger.info("process shutdown complete")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
```

### `TeleLife_Master_Plan.md`

```markdown
# TeleLife | TeleWorld — نقشه راه اصلی پروژه

**نسخه:** 0.1 (Phase 0 — Planning)
**وضعیت:** در انتظار تأیید کارفرما برای شروع Phase 1
**تاریخ:** 2026-07-25

---

## ۱. تعریف نهایی محصول

| مورد | تصمیم |
|---|---|
| **TeleLife** | ربات PV — زندگی شخصی بازیکن: پروفایل، کار، خانه، کیف پول، پس‌انداز، دلار، ماموریت، پرستیژ |
| **TeleWorld** | ربات گروهی — لایه اجتماعی/کشوری: کشورها، ارکان جامعه، رقابت گروهی، رتبه‌بندی، رویدادهای اقتصادی |
| **دیتابیس** | **مشترک و متصل** — یک PostgreSQL، یک هویت بازیکن، یک اقتصاد |
| **Scheduler** | ورکر مستقل — تیک اقتصاد، حقوق، بازار دلار، ریست روزانه، پاکسازی |
| **Admin Panel** | FastAPI + HTMX + Tailwind، دارک، ریسپانسیو |

### قانون طلایی معماری
> بازیکن **یک** موجودیت است. TeleLife و TeleWorld دو **درگاه** به یک دنیا هستند، نه دو بازی.

پول در PV به دست می‌آید و در گروه خرج می‌شود؛ قدرت در گروه به دست می‌آید و در PV بازتاب دارد. این حلقه، موتور اعتیادآور بازی است.

---

## ۲. استک تأییدشده

| لایه | انتخاب | دلیل |
|---|---|---|
| زبان | Python 3.13 (کد سازگار با 3.14) | پایداری wheel روی Render |
| ربات | python-telegram-bot (آخرین نسخه، async) | بلوغ، rate-limiter داخلی |
| دیتابیس | PostgreSQL 15+ / Supabase | نیازمندی پروژه |
| درایور | **asyncpg خام + SQL دستی** | حداکثر سرعت، کنترل کامل کوئری |
| مهاجرت | فایل‌های SQL نسخه‌دار + راه‌انداز سبک داخلی | بدون وابستگی به Alembic |
| کش | in-process TTL cache (فاز ۱) → Redis (فاز ۵ در صورت نیاز) | جلوگیری از overengineering |
| ادمین | FastAPI + Jinja2 + HTMX + Tailwind | بدون build pipeline |
| استقرار | Render (Docker) | کنترل کامل نسخه پایتون |

---

## ۳. فازبندی پروژه

هر فاز یک **خروجی قابل اجرا** دارد. هیچ فازی بدون تأیید تو شروع نمی‌شود.

### Phase 0 — Foundation & Contracts ✅ (همین سند)
- ساختار مخزن، اسناد راهنما، قراردادهای کدنویسی
- تصمیمات معماری ثبت‌شده (ADR)
- بدون کد اجرایی

### Phase 1 — Core Skeleton
- `packages/core`: config loader، connection pool، لایه repository، logger ساختاریافته
- اسکیمای دیتابیس v1 + migration runner
- بوت‌استرپ هر دو ربات با پشتیبانی همزمان Webhook و Polling
- healthcheck و graceful shutdown
- **خروجی:** هر دو ربات بالا می‌آیند، به دیتابیس وصل‌اند، به `/start` جواب می‌دهند

### Phase 2 — Identity & Progression
- ثبت‌نام بازیکن، پروفایل، XP، سطح، شهرت، شادی
- سیستم آنلاک مبتنی بر سطح (config-driven)
- Daily Reward + Streak + Daily Missions
- موتور رندر متن فارسی (قالب‌بندی زیبا، جداکننده هزارگان، بدون متن هاردکد)
- **خروجی:** بازیکن می‌تواند رشد کند

### Phase 3 — Economy Core
- کیف پول، پس‌انداز، دفتر تراکنش (ledger) با idempotency key
- شغل‌ها، حقوق، cooldown، ارتقاء شغلی
- خانه‌ها، اجاره، هزینه زندگی
- **قانون:** هر تغییر پول فقط از طریق یک تابع اتمیک واحد
- **خروجی:** چرخه درآمد/هزینه پایدار

### Phase 4 — USD Market
- موتور عرضه و تقاضا، سقف/کف نوسان، باندهای پایدارسازی
- رویدادهای اقتصادی، Emergency Freeze، سقف خرید/فروش روزانه
- تاریخچه قیمت و شاخص سلامت بازار
- **خروجی:** بازاری که سال‌ها قابل بازی است

### Phase 5 — Group Layer (TeleWorld)
- تشخیص طبیعی متن فارسی با regex پیش‌کامپایل و فیلتر سبک
- کشورها، ارکان جامعه، نقش‌ها، رقابت و رتبه‌بندی گروهی
- **خروجی:** بازی داخل گروه زنده می‌شود

### Phase 6 — Security & Anti-Abuse
- Rate limit چندلایه، ضد فارم XP، ضد اکسپلویت مالی
- محافظت callback (مالکیت + انقضا + امضا)
- **خروجی:** مقاوم در برابر سوءاستفاده

### Phase 7 — Admin Panel
- داشبورد زنده، مدیریت بازیکن، داشبورد دلار با نمودار
- احراز هویت، نقش‌ها، audit log
- **خروجی:** کنترل کامل بازی

### Phase 8 — Hardening & Launch
- بار‌آزمایی، ایندکس‌گذاری نهایی، بکاپ، مانیتورینگ، runbook

---

## ۴. مواردی که نیاز به تصمیم تو دارد (قبل از Phase 1)

طبق قوانین پروژه، این‌ها را پیاده نمی‌کنم تا تأیید کنی:

### ۴.۱ Idempotency روی تراکنش‌های مالی
- **راه‌حل فعلی:** هر دستور، پول را مستقیم تغییر می‌دهد
- **پیشنهاد:** هر تراکنش با یک کلید یکتا (`user_id + action + bucket زمانی`) در جدول ledger ثبت شود و UNIQUE constraint دیتابیس مانع دوباره‌شدن شود
- **مزیت:** کلیک دوباره، تلاش مجدد تلگرام و race condition دیگر پول تولید نمی‌کند
- **عیب:** یک INSERT اضافه در هر تراکنش
- **اثر بر پرفورمنس:** ناچیز (نوشتن index-only)
- **اثر بر مقیاس:** مثبت — امکان sharding و آنالیز اقتصاد
- **اثر بر امنیت:** بسیار مثبت — بستن اصلی‌ترین حفره اقتصادی
- **نیاز به تأیید تو دارد**

### ۴.۲ فیلتر پیام گروهی
- **راه‌حل فعلی:** بررسی هر پیام گروه با هندلرهای متعدد
- **پیشنهاد:** یک هندلر واحد با یک regex پیش‌کامپایل از تمام کلیدواژه‌ها؛ عدم تطابق در چند میکروثانیه رد می‌شود
- **مزیت:** مصرف CPU در هزاران گروه ثابت می‌ماند
- **عیب:** افزودن کلیدواژه نیاز به بازتولید الگو دارد (خودکار می‌شود)
- **نیاز به تأیید تو دارد**

### ۴.۳ Connection Pooler سوپابیس
- Supabase در حالت transaction pooling با prepared statement ناسازگار است. باید `statement_cache_size=0` تنظیم شود.
- این یک الزام فنی است نه سلیقه، ولی چون روی کانفیگ اثر دارد اعلام می‌کنم.

### ۴.۴ استقرار با Docker
- برای قفل‌کردن نسخه پایتون و یکسان‌بودن محیط، پیشنهاد می‌کنم هر چهار سرویس از یک Docker image مشترک با `SERVICE` متفاوت بالا بیایند.
- **مزیت:** یک بیلد، چهار سرویس، صرفه‌جویی در زمان دیپلوی
- **عیب:** image کمی بزرگ‌تر
- **نیاز به تأیید تو دارد**

---

## ۵. قراردادهای کدنویسی (غیرقابل مذاکره)

1. هیچ فایلی بیش از ۴۰۰ خط نشود.
2. هیچ متن فارسی داخل کد منطق نباشد — همه در `texts/`.
3. هیچ عدد بازی (حقوق، قیمت، XP، cooldown) هاردکد نشود — همه در `config/`.
4. هر تابع عمومی type hint کامل داشته باشد.
5. هر تغییر پول فقط از طریق `economy.ledger.apply()`.
6. هر کوئری در لایه repository؛ هندلرها SQL نمی‌نویسند.
7. هر I/O باید async باشد؛ هیچ blocking call در event loop.

---

## ۶. گام بعدی

منتظر تأیید تو برای:
- بندهای ۴.۱ تا ۴.۴
- شروع **Phase 1**

بعد از تأیید، Phase 1 را کامل و قابل اجرا تحویل می‌دهم.

## Phase 5 implementation
See [docs/PHASE_5.md](docs/PHASE_5.md).
## وضعیت اجرایی فعلی — 2026-07-26
- Phase 1: تکمیل
- Phase 2: تکمیل
- Phase 3: تکمیل — اقتصاد شخصی، پس‌انداز، شغل، خانه و هزینه زندگی
- Phase 4: تکمیل — بازار دلار پایدار و حسابرسی‌شده
- Phase 5: یکپارچه و سخت‌سازی‌شده
```

### `TEST_RESULTS_FA_2026-07-27.md`

```markdown
# نتیجه آزمون‌ها

| دسته | موفق | ناموفق | اجرا‌نشده |
|---|---:|---:|---:|
| اعتبارسنجی نحوی Python | 124 فایل | ۰ | ۰ |
| YAML | ۱۷ فایل | ۰ | ۰ |
| قراردادهای ایستای دسترسی/مهاجرت/تکرارناپذیری | ۷ | ۰ | ۰ |
| اسکن اطلاعات محرمانه و پاک‌سازی بسته | ۱ | ۰ | ۰ |
| مجموعه pytest پروژه | ۰ | ۰ | ۳۲ فایل آزمون |
| یکپارچه PostgreSQL واقعی | ۰ | ۰ | ۱ مجموعه |

آزمون‌های اجرایی موفق اعلام نشده‌اند: محیط ساخت Python 3.10 دارد، ولی پروژه Python 3.13 می‌خواهد و بسته‌های `pytest`، `python-telegram-bot` و `asyncpg` نصب نیستند. محیط بدون اینترنت است و نصب وابستگی مجاز/ممکن نبود. برای پذیرش تولید، در CI دارای Python 3.13 و PostgreSQL آزمایشی، `pytest -q` را اجرا کنید.
```

### `tests\__init__.py`

```python
"""Package tests."""
```

### `tests\conftest.py`

```python
"""Shared test configuration.

Tests use the real declared dependencies. Missing runtime packages must fail
collection instead of being hidden by stubs.
"""

from __future__ import annotations
```

### `tests\test_admin_2026_hardening.py`

```python
"""Regression contracts for the 2026 command-centre hardening."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_admin_mutations_have_origin_guard() -> None:
    text = (ROOT / "apps/admin/main.py").read_text(encoding="utf-8")
    assert 'request.method not in {"GET", "HEAD", "OPTIONS"}' in text
    assert "درخواست از مبدأ نامعتبر رد شد" in text


def test_admin_emergency_flags_are_allowlisted() -> None:
    text = (ROOT / "apps/admin/routers/country_admin.py").read_text(encoding="utf-8")
    for key in ("economy_frozen", "usd_market_frozen", "ads_frozen", "registrations_frozen"):
        assert key in text
    assert "if key not in allowed" in text


def test_daily_credit_requires_ledger_leg() -> None:
    text = (ROOT / "packages/core/services/daily.py").read_text(encoding="utf-8")
    assert "daily_ledger_conflict" in text
    assert "DO NOTHING RETURNING id" in text


def test_admin_has_retention_audit_and_ledger_views() -> None:
    html = (ROOT / "apps/admin/templates/dashboard.html").read_text(encoding="utf-8")
    js = (ROOT / "apps/admin/static/admin.js").read_text(encoding="utf-8")
    for view in ("engagement", "ledger", "audit", "controls"):
        assert f'id="view-{view}"' in html
        assert f"async function {view}" in js
    assert "prompt(" not in js


def test_forwarded_headers_are_not_globally_trusted() -> None:
    text = (ROOT / "run.py").read_text(encoding="utf-8")
    assert 'forwarded_allow_ips="*"' not in text
```

### `tests\test_all_keyboard_states.py`

```python
"""Every dynamic keyboard state must build and respect Telegram limits."""
from apps.telelife_bot.keyboards import main as life
from apps.teleworld_bot import keyboards as world

def validate(markup):
    rows=markup.inline_keyboard
    assert rows
    primary=0
    for row in rows:
        assert 1 <= len(row) <= 8
        for button in row:
            data=getattr(button,"callback_data",None)
            if data is not None: assert len(data.encode("utf-8")) <= 64
            if getattr(button,"style",None)=="primary": primary+=1
    assert primary <= 1

def test_every_life_keyboard_state_builds():
    cases=[]
    for daily in (False,True):
        for step in range(5): cases.append(life.home(123456789,daily,step))
    for step in range(6): cases.append(life.journey(123456789,step))
    for ready in (False,True): cases.append(life.daily(123456789,ready))
    for keys in ([],["a"],["a","b","c"]): cases.append(life.missions(123456789,keys))
    for has in (False,True):
        for unlocked in (False,True): cases.append(life.jobs(123456789,has,unlocked))
    for unlocked in (False,True): cases.append(life.market(123456789,unlocked))
    cases += [life.back(123456789),life.economy(123456789),life.savings(123456789),life.housing(123456789)]
    for case in cases: validate(case)

def test_every_world_keyboard_state_builds():
    rows=[{"first_name":"علی","player_id":1},{"first_name":"سارا","player_id":2}]
    cases=[world.private("sample_bot"),world.governments(),world.country(),world.back(),world.cancel(),world.candidates(rows)]
    for country in (False,True):
        for admin in (False,True):
            for citizen in (False,True): cases.append(world.home(country,admin,citizen))
    for status in (None,"nominations","voting"): cases.append(world.politics(status))
    for active in (False,True): cases.append(world.project(active))
    for case in cases: validate(case)
```

### `tests\test_callbacks.py`

```python
from packages.core.ui.callbacks import Callback, cb


def test_roundtrip():
    packed = cb("tl", "claim", 12345, "mission_a")
    parsed = Callback.parse(packed)
    assert parsed == Callback("tl", "claim", 12345, "mission_a")


def test_ownership_check_needs_no_database():
    parsed = Callback.parse(cb("tl", "profile", 777))
    assert parsed is not None
    assert parsed.owned_by(777)
    assert not parsed.owned_by(778)


def test_rejects_garbage():
    assert Callback.parse("nope") is None
    assert Callback.parse("tl:x:notanumber") is None


def test_enforces_telegram_64_byte_limit():
    import pytest

    with pytest.raises(ValueError, match="64-byte"):
        cb("tl", "action", 123456789, "x" * 80)
```

### `tests\test_clock.py`

```python
from datetime import UTC, datetime

import pytest

from packages.core.utils import clock


def test_game_date_uses_configured_timezone():
    instant = datetime(2026, 7, 25, 21, 0, tzinfo=UTC)
    assert clock.game_today(instant).isoformat() == "2026-07-26"


def test_naive_datetimes_are_rejected():
    with pytest.raises(ValueError, match="timezone-aware"):
        clock.game_today(datetime(2026, 7, 26))
```

### `tests\test_commerce.py`

```python
from packages.core.services.commerce import PACKAGES,treasury_price,valid_url,ad_price

def test_package_base_prices_and_delivery_counts():
 assert PACKAGES['economy'][:3]==(25,1,1)
 assert PACKAGES['standard'][:3]==(60,3,24)
 assert PACKAGES['campaign'][:3]==(120,6,72)
 assert PACKAGES['featured'][:3]==(200,8,168)
def test_dynamic_treasury_price_is_population_aware_and_bounded():
 assert treasury_price(1,0)==20_000_000
 assert treasury_price(250_000_000,100)==150_000_000
 assert treasury_price(10_000_000_000,1000)==1_000_000_000
def test_channel_price():
 assert ad_price('economy','life')==25
 assert ad_price('economy','world')==38
 assert ad_price('economy','both')==55
def test_only_http_links():
 assert valid_url('https://example.com/x')
 assert not valid_url('javascript:alert(1)')
```

### `tests\test_commerce_regressions.py`

```python
from packages.core.services.commerce import ad_price

def test_all_channel_adjusted_prices_are_positive_and_schema_safe():
 for package in ("economy","standard","campaign","featured"):
  for channel in ("life","world","both"):
   assert 1 <= ad_price(package,channel) <= 10_000

def test_world_campaign_regression_price():assert ad_price("campaign","world")==180
def test_both_featured_price():assert ad_price("featured","both")==440
```

### `tests\test_config.py`

```python
import pytest

from packages.core.config import ConfigError, get_config


def test_required_sections_present():
    cfg = get_config()
    assert cfg.int_("economy.starting_balance.wallet_toman") > 0
    assert cfg.int_("progression.xp_curve.base") > 0
    assert cfg.bool_("core.menu_cleanup.enabled") is True


def test_missing_key_raises():
    with pytest.raises(ConfigError):
        get_config().get("economy.does.not.exist")


def test_default_is_returned():
    assert get_config().get("nope.nope", "fallback") == "fallback"


def test_explicit_none_default_is_supported():
    assert get_config().get("missing.optional.value", None) is None


def test_numeric_yaml_keys_support_dotted_access():
    assert get_config().int_("jobs.storage.levels.1.capacity_hours") == 6
```

### `tests\test_content_filter.py`

```python
from packages.core.services.content_filter import inspect

def test_obfuscated_blocked_terms():
    for value in ("کون","کوون","کوووون","ک و ن","ک-و-ن","كـوـن"):
        assert not inspect(value).allowed

def test_boundary_avoids_substring_false_positive():
    assert inspect("کونالا").allowed

def test_clean_persian_content():
    assert inspect("جمهوری روشن فردا").allowed
```

### `tests\test_country_realism_contracts.py`

```python
from pathlib import Path

def test_country_identity_is_used_at_outbox_delivery_boundary():
 text=Path("apps/scheduler/jobs/country_jobs.py").read_text()
 assert "country_identity.destination" in text
 assert "country_identity.masthead" in text

def test_group_engagement_uses_country_not_telegram_title():
 text=Path("packages/core/services/engagement.py").read_text()
 assert "c.name country_name" in text
 assert "row['title']" not in text

def test_realism_schema_is_additive():
 text=Path("migrations/0013_country_identity_candles_realism.sql").read_text()
 for table in ("country_indicator_daily","country_shocks","country_newspapers"):
  assert f"CREATE TABLE IF NOT EXISTS {table}" in text
```

### `tests\test_daily.py`

```python
from datetime import date, timedelta

from packages.core.services.daily import (
    _milestone,
    _next_milestone,
    _next_streak,
    _reward_for,
    preview,
)

TODAY = date(2026, 7, 25)


def test_reward_grows_then_caps():
    rewards = [_reward_for(d)[0] for d in range(1, 20)]
    assert rewards == sorted(rewards)
    assert rewards[-1] == rewards[-2], "multiplier must cap"


def test_missing_a_day_does_not_wipe_the_streak():
    """The mercy rule: one bad day costs the streak, not the player."""
    mode, _ = _next_streak(TODAY - timedelta(days=5), TODAY)
    assert mode == 1, "reset must land on 1, never 0"


def test_consecutive_day_continues():
    assert _next_streak(TODAY - timedelta(days=1), TODAY)[0] == -1


def test_same_day_is_blocked():
    assert _next_streak(TODAY, TODAY)[0] == 0


def test_first_ever_claim_starts_at_one():
    assert _next_streak(None, TODAY)[0] == 1


def test_milestones_exist_and_advance():
    assert _milestone(7) is not None
    assert _milestone(8) is None
    assert _next_milestone(7) == 14
    assert _next_milestone(100) is None


def test_preview_matches_ladder():
    assert preview(5) == _reward_for(5)[0]
```

### `tests\test_fmt.py`

```python
from packages.core.utils import fmt


def test_toman_grouping():
    assert fmt.toman(500000, persian=False) == "500\u066c000 \u062a\u0648\u0645\u0627\u0646"


def test_usd_cents():
    assert fmt.usd(2550, persian=False) == "25.50$"
    assert fmt.usd(0, persian=False) == "0.00$"


def test_progress_bar_bounds():
    assert fmt.progress_bar(0, 100) == "\u25b1" * 10
    assert fmt.progress_bar(100, 100) == "\u25b0" * 10
    assert len(fmt.progress_bar(37, 100)) == 10
    assert fmt.progress_bar(5, 0) == "\u25b1" * 10


def test_persian_digits_applied():
    assert "5" not in fmt.number(12345)
```

### `tests\test_glass_buttons.py`

```python
"""Glass keyboard contract tests.

Bot API 9.4 added `style` (primary/success/danger). Omitting it yields the
default translucent look, which is our neutral state.
"""

import pytest

from packages.core.ui.buttons import Keyboard, Style, button


def test_glass_omits_style_field():
    b = button("سلام", "tl:x:1")
    assert getattr(b, "style", None) is None


def test_styles_are_the_three_telegram_values():
    assert {s.value for s in Style} == {"glass", "primary", "success", "danger"}
    for style in (Style.PRIMARY, Style.SUCCESS, Style.DANGER):
        b = button("t", "tl:x:1", style=style)
        assert b.style == style.value


def test_only_one_primary_allowed():
    kb = Keyboard()
    kb.add("یک", "tl:a:1", style=Style.PRIMARY)
    kb.add("دو", "tl:b:1", style=Style.PRIMARY)
    with pytest.raises(ValueError, match="primary"):
        kb.build()


def test_many_success_buttons_are_fine():
    kb = Keyboard()
    for i in range(3):
        kb.add(f"بگیر {i}", f"tl:c:1:{i}", style=Style.SUCCESS)
    assert len(kb.build().inline_keyboard) == 3


def test_grid_wraps_rows():
    kb = Keyboard().grid([button(str(i), f"tl:g:1:{i}") for i in range(5)], per_row=2)
    rows = kb.build().inline_keyboard
    assert [len(r) for r in rows] == [2, 2, 1]
```

### `tests\test_governance.py`

```python
from packages.core.services.governance import rules_for

def test_dictatorship_has_real_override_rule():
    r=rules_for("dictatorship")
    assert r.public_elections and r.election_starter=="leader" and r.leader_may_override

def test_non_electoral_systems_are_distinct():
    assert not rules_for("monarchy").public_elections
    assert not rules_for("military_junta").public_elections
    assert rules_for("republic").public_elections
```

### `tests\test_hardening_contracts.py`

```python
from packages.core.repositories import ledger_repo
from packages.core.services import production

def test_canonical_accounts():
    assert ledger_repo.player_account("IRT") == "wallet"
    assert ledger_repo.player_account("food") == "resource:food"
    assert ledger_repo.country_account("IRT") == "treasury"

def test_production_uses_existing_ledger_contract():
    assert callable(ledger_repo.player_account)
    assert callable(ledger_repo.country_account)

def test_lifecycle_migration_present():
    text=open("migrations/0005_life_world_hardening.sql",encoding="utf-8").read()
    assert "forming" in text and "temporary" in text and "official" in text
    assert "uq_elections_one_open_country" in text
```

### `tests\test_interval_bindings.py`

```python
from pathlib import Path

def test_integer_intervals_use_numeric_bind_casts() -> None:
    targets = [
        Path("packages/core/repositories/country_repo.py"),
        Path("packages/core/repositories/mission_repo.py"),
        Path("packages/core/repositories/player_repo.py"),
        Path("apps/scheduler/jobs/daily_reset.py"),
    ]
    text = "\n".join(path.read_text() for path in targets)
    assert "::text || ' days'" not in text
    assert "::text || ' hours'" not in text
    assert "$1 || ' days'" not in text
    assert "interval '1 day'" in text
```

### `tests\test_live_market.py`

```python
import math
import pytest
from packages.core.services.live_market import extract_price
@pytest.mark.parametrize(("payload","expected"),[
 ({"price":91234},91234),({"data":{"price":"91,234"}},91234),
 ({"result":[{"last":91234.4}]},91234),
])
def test_extract_zipodo_price(payload,expected):assert extract_price(payload)==expected
@pytest.mark.parametrize("payload",[{}, {"price":True},{"price":"nan"},{"price":12},{"price":999999999999}])
def test_rejects_invalid_or_implausible_price(payload):
 with pytest.raises(ValueError):extract_price(payload)
```

### `tests\test_market_chart_contracts.py`

```python
from datetime import UTC,datetime
from packages.core.services.market_chart import Candle,render

def test_market_chart_is_png():
 rows=[Candle(datetime.now(UTC),90000,91000,89500,90500,2)]
 assert render(rows).read(8)==b"\\x89PNG\\r\\n\\x1a\\n"
```

### `tests\test_message_driven_bots.py`

```python
from pathlib import Path

def test_both_active_bots_are_message_and_button_driven():
    life=Path('apps/telelife_bot/handlers/life.py').read_text()
    world=Path('apps/teleworld_bot/handlers/world.py').read_text()
    assert 'CommandHandler' not in life
    assert 'CommandHandler' not in world
    assert 'MessageHandler' in life and 'CallbackQueryHandler' in life
    assert 'MessageHandler' in world and 'CallbackQueryHandler' in world

def test_only_one_active_controller_per_bot():
    assert sorted(p.name for p in Path('apps/telelife_bot/handlers').glob('*.py')) == ['__init__.py','common.py','life.py','panel.py']
    assert sorted(p.name for p in Path('apps/teleworld_bot/handlers').glob('*.py')) == ['__init__.py','world.py']
```

### `tests\test_migrator.py`

```python
from packages.core.db import migrator


def test_migrations_discovered_and_ordered():
    files = migrator.discover()
    assert files, "no migration files found"
    names = [p.name for p in files]
    assert names == sorted(names)
    assert names[0].startswith("0001")


def test_checksum_is_stable():
    a = migrator._checksum("SELECT 1;")
    b = migrator._checksum("SELECT 1;")
    assert a == b and len(a) == 16

def test_only_pre_manifest_migrations_are_legacy_compatible():
    assert migrator.LEGACY_CHECKSUM_VERSIONS == {
        "0001_core_schema", "0002_progression", "0003_country_layer",
        "0004_admin_command_center", "0005_life_world_hardening",
        "0006_phase3_phase4_complete", "0007_unified_ui_onboarding",
    }
    assert "0008_world_access_lifecycle" not in migrator.LEGACY_CHECKSUM_VERSIONS


def test_new_migrations_remain_checksum_strict():
    source = (migrator.Path(migrator.__file__)).read_text(encoding="utf-8")
    assert "if version in LEGACY_CHECKSUM_VERSIONS" in source
    assert "Create a new migration instead of editing history" in source
```

### `tests\test_missions.py`

```python
from datetime import date, timedelta

from packages.core.services.missions import select_for

DAY = date(2026, 7, 25)


def test_selection_is_deterministic():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(12345, 5, DAY)]
    assert a == b, "a restart must never reshuffle a player's missions"


def test_different_players_get_different_missions():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(99999, 5, DAY)]
    assert a != b


def test_missions_rotate_daily():
    a = [m["key"] for m in select_for(12345, 5, DAY)]
    b = [m["key"] for m in select_for(12345, 5, DAY + timedelta(days=1))]
    assert a != b


def test_level_gating_limits_the_pool():
    low = select_for(12345, 1, DAY)
    high = select_for(12345, 10, DAY)
    assert len(low) <= len(high)
    assert all(int(m.get("min_level", 1)) <= 1 for m in low)
```

### `tests\test_outbox_repo.py`

```python
from __future__ import annotations
import asyncio
from typing import Any
from uuid import uuid4
from packages.core.repositories import outbox_repo

class FakeConnection:
    def __init__(self) -> None:
        self.query = ""
        self.args: tuple[Any, ...] = ()
    async def fetch(self, query: str, *args: Any) -> list[Any]:
        self.query, self.args = query, args
        return []
    async def execute(self, query: str, *args: Any) -> str:
        self.query, self.args = query, args
        return "UPDATE 1"

def test_claim_uses_numeric_interval_expression() -> None:
    conn = FakeConnection()
    asyncio.run(outbox_repo.claim(conn, uuid4(), 20, 60, 5))  # type: ignore[arg-type]
    assert "$4::double precision * interval '1 second'" in conn.query
    assert conn.args[3] == 60

def test_failed_uses_numeric_interval_expression() -> None:
    conn = FakeConnection()
    asyncio.run(outbox_repo.failed(conn, 1, uuid4(), "telegram_error", 120))  # type: ignore[arg-type]
    assert "$4::double precision * interval '1 second'" in conn.query
    assert conn.args[3] == 120
```

### `tests\test_panel_edit.py`

```python
from __future__ import annotations
from unittest.mock import AsyncMock, patch
import pytest
from telegram.error import BadRequest
from apps.telelife_bot.handlers.common import send_panel

@pytest.mark.asyncio
async def test_identical_edit_is_a_successful_noop() -> None:
    message = AsyncMock()
    message.edit_text.side_effect = BadRequest("Message is not modified: same content")
    with patch("apps.telelife_bot.handlers.common.schedule_cleanup") as cleanup:
        await send_panel(AsyncMock(), message, "same", None, "profile", edit=True)
    cleanup.assert_called_once()

@pytest.mark.asyncio
async def test_other_bad_request_is_not_hidden() -> None:
    message = AsyncMock()
    message.edit_text.side_effect = BadRequest("Message to edit not found")
    with pytest.raises(BadRequest, match="not found"):
        await send_panel(AsyncMock(), message, "text", None, "profile", edit=True)
```

### `tests\test_persian_button_contracts.py`

```python
from pathlib import Path
import ast,re,yaml
ROOT=Path(__file__).parents[1]
def test_python_syntax():
 for p in ROOT.rglob('*.py'):ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
def test_yaml_valid():
 for p in (ROOT/'packages/core/config/data').glob('*.yaml'):yaml.safe_load(p.read_text(encoding='utf-8'))
def test_world_is_message_and_button_driven():
 src=(ROOT/'apps/teleworld_bot/handlers/world.py').read_text();assert 'CommandHandler' not in src;assert 'MessageHandler(filters.TEXT, text)' in src;assert "pattern=r\"^tw:\"" in src
def test_personal_jobs_stay_in_life():
 life=(ROOT/'apps/telelife_bot/keyboards/main.py').read_text();world=(ROOT/'apps/teleworld_bot/keyboards.py').read_text()
 for label in ['کشاورز','معدن‌کار','برنامه‌نویس','بازرگان','مهندس','پزشک','روزنامه‌نگار']:assert label in life
 assert 'شغل شخصی' not in world
def test_no_visible_slash_in_active_bot_copy():
 for p in [ROOT/'apps/telelife_bot/handlers/life.py',ROOT/'apps/telelife_bot/texts/fa.py',ROOT/'apps/teleworld_bot/handlers/world.py',ROOT/'apps/teleworld_bot/texts/fa.py']:
  assert not re.search(r'["\']/(start|help|job|country|profile|daily)',p.read_text(),re.I)
```

### `tests\test_phase3_phase4_contracts.py`

```python
from pathlib import Path

def test_phase_3_4_migration_contract():
    text=Path("migrations/0006_phase3_phase4_complete.sql").read_text()
    for table in ("player_housing","player_life_economy","usd_market_state","usd_trades","usd_daily_limits"):
        assert table in text

def test_user_bots_register_no_slash_commands():
    for path in (Path("apps/telelife_bot/handlers/life.py"),Path("apps/teleworld_bot/handlers/world.py")):
        text=path.read_text()
        assert "CommandHandler" not in text
        assert "MessageHandler" in text

def test_market_is_bounded_and_idempotent():
    text=Path("packages/core/services/usd_market.py").read_text()
    assert "daily_band_basis_points" in text
    assert "idempotency_key" in text
    assert "FOR UPDATE" in text
    assert "daily_limit" in text

def test_phase3_money_uses_transactions_and_ledger():
    text=Path("packages/core/services/personal_economy.py").read_text()
    assert "db.transaction()" in text
    assert "ledger_repo.insert" in text
    assert "FOR UPDATE" in text
```

### `tests\test_phase5_config.py`

```python
from packages.core.config import get_config
def test_phase5_critical_policy():
 c=get_config();assert len(c.section('jobs.jobs'))==7;assert c.float_('jobs.production.minimum_collection_fraction_for_xp')==0.05;assert c.bool_('jobs.production.checkpoint_before_upgrade');assert c.bool_('country_missions.daily.instantiate_on_eligible_action');assert c.int_('news.outbox.maximum_attempts')==5;assert c.bool_('national_project.projects.national_storage.once_per_country')
```

### `tests\test_production_security.py`

```python
from datetime import UTC,datetime,timedelta
from packages.core.services.production import accrue
class R(dict):
 __getattr__=dict.__getitem__
def row(at,level=1,storage=1,stored=0):return R(job_code='farmer',production_level=level,storage_level=storage,stored_amount=stored,production_updated_at=at)
def test_lazy_accrual_is_capacity_capped():
 now=datetime.now(UTC);a=accrue(row(now-timedelta(days=5)),now);assert a.stored==a.capacity
def test_old_level_accrual_can_be_checkpointed_before_upgrade():
 now=datetime.now(UTC);old=accrue(row(now-timedelta(hours=3),level=1),now);new=accrue(row(now,level=2,stored=old.stored),now);assert old.stored==30;assert new.stored==30
```

### `tests\test_progression.py`

```python
from packages.core.services import progression


def test_curve_is_monotonic():
    values = [progression.xp_required(lvl) for lvl in range(1, 50)]
    assert values == sorted(values)
    assert all(v > 0 for v in values)


def test_level_progress_returns_pair():
    current, needed = progression.level_progress(1, 40)
    assert current == 40
    assert needed == progression.xp_required(1)


def test_max_level_caps_progress():
    top = progression.max_level()
    current, needed = progression.level_progress(top, 999)
    assert current == needed == 999
```

### `tests\test_project_integrity.py`

```python
"""Repository-wide integrity checks for generated-source contamination."""

from __future__ import annotations

import ast
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_all_python_files_parse():
    for path in ROOT.rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_no_shell_heredoc_fragments_in_source():
    banned = ("cat >", "<<'PY'", '<<"PY"', "\nEOF\n")
    for path in [*ROOT.rglob("*.py"), *ROOT.rglob("*.sql")]:
        if path == Path(__file__):
            continue
        text = path.read_text(encoding="utf-8")
        assert not any(token in text for token in banned), path


def test_every_yaml_file_is_a_mapping():
    for path in ROOT.rglob("*.yaml"):
        assert isinstance(yaml.safe_load(path.read_text(encoding="utf-8")), dict), path


def test_required_runtime_directories_exist():
    assert (ROOT / "apps/admin/templates").is_dir()
    assert (ROOT / "apps/admin/static").is_dir()
    assert (ROOT / "migrations").is_dir()
```

### `tests\test_scaling_migration.py`

```python
from packages.core.services.commerce import subscription_stars,treasury_price,ad_price
from packages.core.services.migration import exit_fee

def test_subscription_population_tiers():
 assert subscription_stars(1)==10 and subscription_stars(20)==10
 assert subscription_stars(21)==15 and subscription_stars(100)==15
 assert subscription_stars(101)==30 and subscription_stars(500)==30
 assert subscription_stars(501)==50 and subscription_stars(1000)==50
 assert subscription_stars(1001)==75

def test_treasury_population_formula():
 assert treasury_price(0,1)==20_000_000
 assert treasury_price(250_000_000,100)==150_000_000
 assert treasury_price(10_000_000_000,1000)==1_000_000_000

def test_channel_prices_round_up():
 assert ad_price('economy','life')==25
 assert ad_price('economy','world')==38
 assert ad_price('economy','both')==55
 assert ad_price('standard','world')==90
 assert ad_price('standard','both')==132

def test_migration_fee_bounds():
 assert exit_fee(1)==500_000
 assert exit_fee(100_000_000)==5_000_000
 assert exit_fee(2_000_000_000)==50_000_000
```

### `tests\test_supervisor.py`

```python
from __future__ import annotations
import asyncio
from packages.core.supervisor import ServiceSpec, ServiceSupervisor

async def test_crashed_service_restarts_without_stopping_peer():
    crashes = 0
    peer_ticks = 0
    async def flaky(stop: asyncio.Event) -> None:
        nonlocal crashes
        crashes += 1
        if crashes == 1:
            raise RuntimeError("boom")
        await stop.wait()
    async def peer(stop: asyncio.Event) -> None:
        nonlocal peer_ticks
        while not stop.is_set():
            peer_ticks += 1
            await asyncio.sleep(0.005)
    supervisor = ServiceSupervisor(
        [ServiceSpec("flaky-test", flaky, lambda: True), ServiceSpec("peer-test", peer, lambda: True)],
        health_interval=0.01, restart_base=0.01, restart_cap=0.02,
    )
    task = asyncio.create_task(supervisor.run())
    await asyncio.sleep(0.08)
    supervisor.stop.set()
    await task
    assert crashes >= 2
    assert peer_ticks > 2
```

### `tests\test_teleworld_onboarding.py`

```python
from pathlib import Path

def test_onboarding_has_welcome_wizard_and_navigation() -> None:
    code=Path("apps/teleworld_bot/handlers/onboarding.py").read_text()
    assert "ChatMemberHandler" in code
    assert 'FLOW_KEY="tw_country_flow"' in code
    assert 'action=="create"' in code
    assert 'flow["step"]="government"' in code
    assert 'flow["step"]="description"' in code
    assert 'CommandHandler("menu",start)' in code

def test_world_keyboard_has_glass_navigation() -> None:
    code=Path("apps/teleworld_bot/keyboards.py").read_text()
    assert "InlineKeyboardMarkup" in code
    assert "ساخت کشور" in code
    assert "شغل و تولید" in code
    assert "سیاست" in code
```

### `tests\test_teleworld_start.py`

```python
from __future__ import annotations
from apps.teleworld_bot.handlers import status


def test_teleworld_registers_start_and_menu_callbacks() -> None:
    class App:
        def __init__(self) -> None:
            self.handlers = []
        def add_handler(self, handler) -> None:  # type: ignore[no-untyped-def]
            self.handlers.append(handler)
    app = App()
    status.register(app)
    commands = {
        command
        for handler in app.handlers
        for command in getattr(handler, "commands", set())
    }
    assert {"start", "status", "help"} <= commands
    assert any(getattr(handler, "pattern", None) for handler in app.handlers)
```

### `tests\test_token_isolation.py`

```python
from __future__ import annotations
import pytest
from pydantic import ValidationError
from packages.core.settings import Settings

BASE = {
    "DATABASE_URL": "postgresql://test_user:test_password@127.0.0.1/test_db",
    "ADMIN_USERNAME": "admin",
    "ADMIN_PASSWORD": "a-strong-password",
    "RUN_MODE": "polling",
}

def test_two_pollers_cannot_share_one_token(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in BASE.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("TELELIFE_BOT_TOKEN", "123:shared")
    monkeypatch.setenv("TELEWORLD_BOT_TOKEN", "123:shared")
    with pytest.raises(ValidationError, match="two different bots"):
        Settings()
```

### `tests\test_unlocks.py`

```python
from packages.core.services import unlocks


def test_catalogue_is_sorted_by_level():
    levels = [u.level for u in unlocks.catalogue()]
    assert levels == sorted(levels)


def test_progression_never_stalls_too_long():
    """Promise to the player: something new every few levels."""
    levels = [u.level for u in unlocks.catalogue()]
    gaps = [b - a for a, b in zip(levels, levels[1:], strict=False)]
    assert max(gaps) <= 10, f"a {max(gaps)}-level dead zone kills motivation"


def test_next_unlock_moves_forward():
    nxt = unlocks.next_unlock(1)
    assert nxt is not None and nxt.level == 2


def test_top_level_has_nothing_left():
    assert unlocks.next_unlock(999) is None


def test_available_grows_with_level():
    assert len(unlocks.available(1)) < len(unlocks.available(50))
```

### `tests\test_world_access_contracts.py`

```python
"""Static contracts that require no Telegram or PostgreSQL service."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def test_my_chat_member_is_registered():
    source = text("apps/teleworld_bot/handlers/access.py")
    main = text("apps/teleworld_bot/main.py")
    assert "ChatMemberHandler.MY_CHAT_MEMBER" in source
    assert "access.register(application)" in main

def test_permission_policy_is_minimal():
    source = text("packages/core/services/world_access.py")
    assert "can_delete_messages" in source
    for dangerous in ("can_promote_members", "can_change_info", "can_restrict_members"):
        assert dangerous not in source

def test_all_world_mutations_pass_gate():
    source = text("apps/teleworld_bot/handlers/world.py")
    assert "is_mutating(action)" in source
    assert "if not access.ready" in source

def test_financial_callback_key_is_stable():
    source = text("apps/teleworld_bot/handlers/world.py")
    assert 'world-donate:{p.id}:{query.id}' in source
    assert 'world-project:{p.id}:{query.id}' in source
    assert 'idempotency_key=f"world:{p.id}:{uuid4().hex}"' not in source

def test_migration_is_non_destructive_and_repeatable():
    sql = text("migrations/0008_world_access_lifecycle.sql").upper()
    assert sql.count("CREATE TABLE IF NOT EXISTS") == 2
    assert "DROP TABLE" not in sql and "TRUNCATE" not in sql

def test_callback_payload_literals_fit_limit():
    files = [text("apps/teleworld_bot/keyboards.py"), text("apps/telelife_bot/keyboards/main.py")]
    for source in files:
        for value in re.findall(r'callback_data\s*=\s*f?["\']([^"\']+)', source):
            assert len(value.encode("utf-8")) <= 64

def test_privacy_mode_is_documented_honestly():
    guide = text("docs/DEPLOYMENT_FA.md")
    assert "Privacy Mode" in guide
    assert "قابل تشخیص مستقیم نیست" in guide
    assert "BotFather" in guide
```

### `tests\test_xp.py`

```python
from packages.core.config import get_config
from packages.core.services.xp import _apply_levels, day_key


def test_partial_xp_does_not_level():
    assert _apply_levels(1, 50) == (1, 50)


def test_exact_threshold_levels_once():
    from packages.core.services import progression

    needed = progression.xp_required(1)
    assert _apply_levels(1, needed) == (2, 0)


def test_large_grant_cascades_multiple_levels():
    level, remainder = _apply_levels(1, 5000)
    assert level > 5
    assert remainder >= 0


def test_cascade_never_exceeds_max_level():
    from packages.core.services import progression

    top = progression.max_level()
    level, _ = _apply_levels(top - 1, 10**9)
    assert level == top


def test_daily_cap_exceeds_a_perfect_day():
    """The cap must punish abuse, never a legitimately active player."""
    cfg = get_config()
    perfect_day = (
        cfg.int_("xp.sources.daily_claim")
        + 3 * cfg.int_("xp.sources.mission_complete")
        + cfg.int_("xp.sources.profile_view")
    )
    assert cfg.int_("xp.anti_farm.daily_cap") > perfect_day * 3


def test_day_key_rotates_daily():
    assert day_key("daily", 1).count(":") == 2
    assert day_key("daily", 1) == day_key("daily", 1)
    assert day_key("daily", 1) != day_key("daily", 2)
```

### `UI_REDESIGN_FA.md`

```markdown
# بازطراحی تجربه کاربری Life و World

- هر بات فقط یک کنترلر فعال دارد و فقط `/start` به‌عنوان ورودی اجباری تلگرام ثبت شده است.
- موقعیت آخرین پنل در دیتابیس ذخیره می‌شود؛ شروع دوباره و جابه‌جایی منو ابتدا همان پیام را ویرایش می‌کند.
- پیام جدید فقط وقتی ساخته می‌شود که پنل قبلی وجود نداشته یا دیگر قابل ویرایش نباشد.
- متن و برچسب تمام دکمه‌های کاربر فارسی است.
- Life دارای خانه مرکزی، مسیر شروع چهارمرحله‌ای، هدف بعدی، کارهای روزانه، شغل، بانک، خانه و بازار است.
- World دارای خانه مرکزی، وضعیت کشور، شهروندان، اقتصاد و منابع، انتخابات دکمه‌ای، پروژه ملی و شغل شخصی است.
- Wizard ساخت کشور پیام‌های ورودی کاربر را حذف می‌کند و همان پنل را جلو می‌برد.
```
