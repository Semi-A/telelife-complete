# دامپ پروژه: telelife_complete

مسیر مبدا: `D:\PRojects\telelife_complete`

تعداد کل فایل‌ها: 137


## ساختار پوشه‌ها و فایل‌ها

```
telelife_complete/
├── apps/
│   ├── admin/
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── country_admin.py
│   │   ├── static/
│   │   │   └── admin.css
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
│   │   │   ├── common.py
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
│   │   │   ├── country.py
│   │   │   ├── politics.py
│   │   │   ├── production.py
│   │   │   └── status.py
│   │   ├── texts/
│   │   │   ├── __init__.py
│   │   │   └── fa.py
│   │   ├── __init__.py
│   │   └── main.py
│   └── __init__.py
├── docs/
│   ├── CONVENTIONS.md
│   ├── DEPLOYMENT.md
│   ├── FOR_AI_AGENTS.md
│   ├── PHASE_1.md
│   ├── PHASE_2.md
│   └── PHASE_5.md
├── migrations/
│   ├── 0001_core_schema.sql
│   ├── 0002_progression.sql
│   └── 0003_country_layer.sql
├── packages/
│   ├── core/
│   │   ├── bot/
│   │   │   ├── __init__.py
│   │   │   ├── errors.py
│   │   │   └── runtime.py
│   │   ├── config/
│   │   │   ├── data/
│   │   │   │   ├── core.yaml
│   │   │   │   ├── country.yaml
│   │   │   │   ├── country_missions.yaml
│   │   │   │   ├── daily.yaml
│   │   │   │   ├── daily_events.yaml
│   │   │   │   ├── economy.yaml
│   │   │   │   ├── elections.yaml
│   │   │   │   ├── jobs.yaml
│   │   │   │   ├── missions.yaml
│   │   │   │   ├── national_project.yaml
│   │   │   │   ├── news.yaml
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
│   │   │   └── project_repo.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── country.py
│   │   │   ├── country_economy.py
│   │   │   ├── country_missions.py
│   │   │   ├── daily.py
│   │   │   ├── economy.py
│   │   │   ├── elections.py
│   │   │   ├── missions.py
│   │   │   ├── national_project.py
│   │   │   ├── news.py
│   │   │   ├── production.py
│   │   │   ├── progression.py
│   │   │   ├── unlocks.py
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
│   │   └── settings.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_callbacks.py
│   ├── test_clock.py
│   ├── test_config.py
│   ├── test_daily.py
│   ├── test_fmt.py
│   ├── test_glass_buttons.py
│   ├── test_migrator.py
│   ├── test_missions.py
│   ├── test_phase5_config.py
│   ├── test_production_security.py
│   ├── test_progression.py
│   ├── test_project_integrity.py
│   ├── test_unlocks.py
│   └── test_xp.py
├── .dockerignore
├── .env.example
├── .gitignore
├── AUDIT_STATUS.md
├── DELIVERY.md
├── Dockerfile
├── dump.py
├── MANIFEST.sha256
├── pyproject.toml
├── README.md
├── render.yaml
├── requirements.txt
├── run.py
├── telelife_complete_dump.md
└── TeleLife_Master_Plan.md
```

## محتوای فایل‌ها


### `.dockerignore`

_[این فایل باینری/غیرمتنی تشخیص داده شد و محتوایش درج نشد]_


### `.env.example`

```
SERVICE=telelife
ENVIRONMENT=development
LOG_LEVEL=INFO
DEBUG=false

# Paste the Supabase transaction-pooler URL (normally port 6543) and require TLS.
DATABASE_URL=
DB_POOL_MIN=1
DB_POOL_MAX=5
DB_COMMAND_TIMEOUT=15
DB_STATEMENT_CACHE_SIZE=0

TELELIFE_BOT_TOKEN=
TELEWORLD_BOT_TOKEN=
GLOBAL_NEWS_CHAT_ID=

RUN_MODE=polling
WEBHOOK_BASE_URL=
WEBHOOK_SECRET=
PORT=8000
HOST=0.0.0.0

ADMIN_USERNAME=
ADMIN_PASSWORD=
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

security = HTTPBasic()


def require_admin(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:
    """Authenticate an admin with constant-time credential comparisons."""
    settings = get_settings()
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
"""Admin panel - Phase 1 delivers auth + live dashboard skeleton."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from apps.admin.auth import require_admin
from apps.admin.routers.country_admin import router as country_admin_router
from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.repositories import group_repo, player_repo
from packages.core.settings import Service, get_settings
from packages.core.utils import fmt

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
async def _collect_stats() -> dict[str, object]:
    return {
        "players_total": await player_repo.count_total(),
        "players_active": await player_repo.count_active(7),
        "groups_total": await group_repo.count_total(),
        "db_ok": await db.healthcheck(),
    }


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore[no-untyped-def]
    settings = get_settings()
    setup_logging(Service.ADMIN.value, settings.log_level)
    await db.create_pool(settings)
    try:
        await migrate()
        yield
    finally:
        await db.close_pool()


app = FastAPI(title="TeleLife Admin", lifespan=lifespan, docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.include_router(country_admin_router)


@app.get("/healthz")
async def healthz() -> dict[str, object]:
    return {"ok": await db.healthcheck()}


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, _: str = Depends(require_admin)) -> HTMLResponse:
    return templates.TemplateResponse(
        request, "dashboard.html", {"stats": await _collect_stats(), "fmt": fmt}
    )


@app.get("/partials/stats", response_class=HTMLResponse)
async def stats_partial(request: Request, _: str = Depends(require_admin)) -> HTMLResponse:
    return templates.TemplateResponse(
        request, "partials/stats.html", {"stats": await _collect_stats(), "fmt": fmt}
    )
```

### `apps\admin\routers\__init__.py`

```python
"""Package apps.admin.routers."""
```

### `apps\admin\routers\country_admin.py`

```python
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
```

### `apps\admin\static\admin.css`

```css
:root { color-scheme: dark; }
body { font-family: Vazirmatn, system-ui, sans-serif; }
.panel { background: #12151c; border: 1px solid #1f2532; }
```

### `apps\admin\templates\base.html`

```html
<!doctype html>
<html lang="fa" dir="rtl" class="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{% block title %}TeleLife Admin{% endblock %}</title>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/htmx.org@1.9.12"></script>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ url_for('static', path='/admin.css') }}">
</head>
<body class="bg-[#0a0c11] text-slate-200 min-h-screen">
  <header class="border-b border-[#1f2532] bg-[#0d1016]">
    <div class="max-w-6xl mx-auto px-5 py-4 flex items-center justify-between">
      <div class="flex items-baseline gap-3">
        <span class="text-lg font-extrabold tracking-tight text-white">TeleLife</span>
        <span class="text-xs text-slate-500">پنل مدیریت</span>
      </div>
      <span class="text-xs text-slate-500">فاز ۱</span>
    </div>
  </header>
  <main class="max-w-6xl mx-auto px-5 py-8">
    {% block content %}{% endblock %}
  </main>
</body>
</html>
```

### `apps\admin\templates\dashboard.html`

```html
{% extends "base.html" %}
{% block content %}
<h1 class="text-2xl font-extrabold text-white mb-1">داشبورد زنده</h1>
<p class="text-sm text-slate-500 mb-6">هر ۱۰ ثانیه به‌روزرسانی می‌شود</p>

<div id="stats" hx-get="/partials/stats" hx-trigger="every 10s" hx-swap="innerHTML">
  {% include "partials/stats.html" %}
</div>
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
from packages.core.services import country_economy,elections,news
async def resolve_due()->dict[str,int]:return await elections.resolve_due()
async def daily_events()->int:
 await country_economy.catch_up()
 return await news.ensure_daily_events()
async def publish_news(bot:Bot)->dict[str,int]:
 async def sender(chat_id,event_type,payload):
  if chat_id is None:return
  text=str(payload.get('text') or payload.get('event_code') or payload.get('mission_key') or event_type)
  await bot.send_message(chat_id=chat_id,text=text)
 return await news.publish_batch(sender)
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
        "DELETE FROM xp_events WHERE created_at < now() - ($1 || ' days')::interval",
        str(XP_EVENT_RETENTION_DAYS),
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
"""Scheduler for minute-resolution and daily idempotent maintenance."""

from __future__ import annotations

import asyncio
import logging
import signal
from datetime import UTC, datetime, timedelta

from telegram import Bot

from apps.scheduler.jobs import country_jobs, daily_reset
from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import Service, get_settings

logger = logging.getLogger(__name__)


async def minute_loop(stop: asyncio.Event, bot: Bot) -> None:
    while not stop.is_set():
        try:
            await db.execute("DELETE FROM cooldowns WHERE expires_at < now()")
            await country_jobs.resolve_due()
            await country_jobs.publish_news(bot)
        except Exception:
            logger.exception("minute jobs failed")
        try:
            await asyncio.wait_for(stop.wait(), timeout=60)
        except TimeoutError:
            continue


def seconds_until_daily() -> float:
    now = datetime.now(UTC)
    target = (now + timedelta(days=1)).replace(
        hour=0, minute=10, second=0, microsecond=0
    )
    return max(1.0, (target - now).total_seconds())


async def daily_loop(stop: asyncio.Event) -> None:
    while not stop.is_set():
        try:
            await asyncio.wait_for(stop.wait(), timeout=seconds_until_daily())
            return
        except TimeoutError:
            logger.debug("daily maintenance window reached")
        try:
            await daily_reset.run()
            await country_jobs.daily_events()
        except Exception:
            logger.exception("daily jobs failed")


async def run() -> None:
    settings = get_settings()
    setup_logging(Service.SCHEDULER.value, settings.log_level)
    await db.create_pool(settings)
    await migrate()
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, stop.set)
        except NotImplementedError:
            logger.debug("signal handlers are unavailable on this event loop")
    try:
        async with Bot(settings.teleworld_bot_token) as bot:
            await asyncio.gather(minute_loop(stop, bot), daily_loop(stop))
    finally:
        await db.close_pool()


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
```

### `apps\telelife_bot\__init__.py`

```python
"""Package apps.telelife_bot."""
```

### `apps\telelife_bot\handlers\__init__.py`

```python
"""Package apps.telelife_bot.handlers."""
```

### `apps\telelife_bot\handlers\common.py`

```python
"""Shared handler plumbing: player resolution, guards, panel sending."""

from __future__ import annotations

from dataclasses import dataclass

from telegram import Message, Update
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
            fa.BANNED.format(reason=player.ban_reason or fa.NO_REASON)
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
        sent = await message.edit_text(text, reply_markup=markup)
        target = sent if isinstance(sent, Message) else message
    else:
        target = await message.reply_text(text, reply_markup=markup)
    schedule_cleanup(context, target, panel)
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


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("profile", profile))
```

### `apps\telelife_bot\handlers\progression.py`

```python
"""Profile, daily, missions and the unlock map - commands plus glass callbacks."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes

from apps.telelife_bot.handlers.common import Ctx, guard_callback, resolve, send_panel
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from apps.telelife_bot.views import render
from packages.core.repositories import player_repo, progression_repo
from packages.core.services import daily, missions, progression, xp
from packages.core.utils import fmt

MISSIONS_UNLOCK_LEVEL = 2


async def _announce_level_up(ctx: Ctx, result: xp.XPResult) -> None:
    if not result.leveled_up:
        return
    await ctx.message.reply_text(
        render.level_up(result), reply_markup=kb.level_up_panel(ctx.telegram_id)
    )


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
    application.add_handler(CommandHandler("profile", cmd_profile))
    application.add_handler(CommandHandler("daily", cmd_daily))
    application.add_handler(CommandHandler("missions", cmd_missions))
    application.add_handler(CommandHandler("unlocks", cmd_unlocks))
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
    application.add_handler(CommandHandler("help", help_command))
```

### `apps\telelife_bot\keyboards\__init__.py`

```python
from apps.telelife_bot.keyboards import main

__all__ = ["main"]
```

### `apps\telelife_bot\keyboards\main.py`

```python
"""Glass keyboards for TeleLife.

Colour policy, applied consistently everywhere:
  PRIMARY (blue)  - the single action we want tapped. Max one per keyboard.
  SUCCESS (green) - a reward is waiting to be collected. Earned, not decorative.
  DANGER  (red)   - destructive or irreversible. Never used for navigation.
  GLASS           - everything else. Default translucent Telegram look.
"""

from __future__ import annotations

from telegram import InlineKeyboardMarkup

from apps.telelife_bot.texts import fa
from packages.core.ui import Keyboard, Style, button, cb

NS = "tl"


def profile_panel(owner_id: int, *, daily_ready: bool, missions_unlocked: bool) -> InlineKeyboardMarkup:
    kb = Keyboard()
    kb.row(
        button(
            fa.BTN_DAILY_READY if daily_ready else fa.BTN_DAILY,
            cb(NS, "daily", owner_id),
            style=Style.SUCCESS if daily_ready else Style.GLASS,
        )
    )
    second = [button(fa.BTN_UNLOCKS, cb(NS, "unlocks", owner_id))]
    if missions_unlocked:
        second.insert(0, button(fa.BTN_MISSIONS, cb(NS, "missions", owner_id)))
    kb.row(*second)
    kb.row(button(fa.BTN_REFRESH, cb(NS, "profile", owner_id)))
    return kb.build()


def daily_panel(owner_id: int, *, claimable: bool) -> InlineKeyboardMarkup:
    kb = Keyboard()
    if claimable:
        kb.row(button(fa.BTN_CLAIM, cb(NS, "claim", owner_id), style=Style.PRIMARY))
    kb.row(
        button(fa.BTN_MISSIONS, cb(NS, "missions", owner_id)),
        button(fa.BTN_BACK, cb(NS, "profile", owner_id)),
    )
    return kb.build()


def missions_panel(owner_id: int, claimable_keys: list[str]) -> InlineKeyboardMarkup:
    kb = Keyboard()
    kb.grid(
        [
            button(
                f"{fa.BTN_CLAIM} {i + 1}",
                cb(NS, "mclaim", owner_id, key),
                style=Style.SUCCESS,
            )
            for i, key in enumerate(claimable_keys)
        ],
        per_row=2,
    )
    kb.row(
        button(fa.BTN_REFRESH, cb(NS, "missions", owner_id)),
        button(fa.BTN_BACK, cb(NS, "profile", owner_id)),
    )
    return kb.build()


def unlocks_panel(owner_id: int) -> InlineKeyboardMarkup:
    return Keyboard().row(button(fa.BTN_BACK, cb(NS, "profile", owner_id))).build()


def level_up_panel(owner_id: int) -> InlineKeyboardMarkup:
    return (
        Keyboard()
        .row(button(fa.BTN_PROFILE, cb(NS, "profile", owner_id), style=Style.PRIMARY))
        .build()
    )
```

### `apps\telelife_bot\main.py`

```python
"""TeleLife bot entrypoint (private-chat life simulator)."""

from __future__ import annotations

from telegram.ext import Application

from apps.telelife_bot.handlers import progression, start
from apps.telelife_bot.texts import fa
from packages.core.bot import make_error_handler, run_bot
from packages.core.settings import Service


def register(application: Application) -> None:
    start.register(application)
    progression.register(application)
    application.add_error_handler(make_error_handler(fa.ERROR))


def main() -> None:
    run_bot(Service.TELELIFE, register)


if __name__ == "__main__":
    main()
```

### `apps\telelife_bot\texts\__init__.py`

```python
"""Package apps.telelife_bot.texts."""
```

### `apps\telelife_bot\texts\fa.py`

```python
"""All player-facing Persian copy for TeleLife. No text belongs in logic files."""

from __future__ import annotations

# ---------- onboarding ----------
WELCOME_NEW = (
    "🌆 <b>به تله‌لایف خوش اومدی، {name}!</b>\n\n"
    "از همین لحظه یه زندگی دوم داری. حسابت باز شد و {wallet} توش نشسته.\n\n"
    "کارِت اینه که بسازیش: کار کن، پس‌انداز کن، سرمایه‌گذاری کن، بالا برو.\n"
    "هر روزی که بیای، جلوتری از دیروز."
)

WELCOME_BACK = (
    "👋 <b>برگشتی {name}!</b>\n\n"
    "سطح {level} · {wallet}\n"
    "زندگیت همون‌جا که گذاشتیش منتظرته."
)

# ---------- profile ----------
PROFILE = (
    "🪪 <b>{name}</b>\n"
    "<code>─────────────────</code>\n"
    "🎚 سطح <b>{level}</b>{prestige_tag}  ·  رتبه {rank}\n"
    "{xp_bar}\n"
    "<i>{xp} از {xp_needed} XP تا سطح بعد</i>\n\n"
    "💵 کیف پول    <b>{wallet}</b>\n"
    "🏦 پس‌انداز    <b>{savings}</b>\n"
    "💲 دلار        <b>{usd}</b>\n"
    "<code>─────────────────</code>\n"
    "😊 شادی {happiness}٪   ⭐️ شهرت {reputation}\n"
    "🔥 استریک {streak} روز\n\n"
    "<i>ثروت خالص: {net_worth}</i>"
)

PRESTIGE_TAG = " · پرستیژ {prestige}"

# ---------- daily ----------
DAILY_CLAIMED = (
    "🎁 <b>جایزه امروز گرفته شد!</b>\n"
    "<code>─────────────────</code>\n"
    "💰 <b>+{reward}</b>\n"
    "✨ +{xp} XP\n\n"
    "🔥 استریک: <b>{streak} روز</b>\n"
    "{next_line}"
)

DAILY_MILESTONE = (
    "\n\n🏅 <b>{label}</b>\n"
    "پاداش ویژه: <b>+{bonus}</b>\n"
    "<i>ادامه بده، بعدی سنگین‌تره.</i>"
)

DAILY_NEXT = "فردا بیای: <b>{amount}</b>"
DAILY_NEXT_MILESTONE = "🎯 {days} روز دیگه تا نشان بعدی"

DAILY_READY = (
    "🎁 <b>جایزه امروزت آماده‌ست</b>\n"
    "<code>─────────────────</code>\n"
    "🔥 استریک فعلی: <b>{streak} روز</b>\n"
    "🏆 رکوردت: {best} روز\n\n"
    "💰 امروز می‌گیری: <b>{amount}</b>\n"
    "{next_line}"
)

DAILY_READY_NEXT = "<i>فردا می‌شه {amount} — استریکو نشکون.</i>"

DAILY_ALREADY = (
    "⏳ <b>امروز رو گرفتی</b>\n\n"
    "🔥 استریک: <b>{streak} روز</b>\n"
    "فردا برگرد، <b>{tomorrow}</b> منتظرته.\n\n"
    "<i>یه روز غیبت، استریکت برمی‌گرده سر خونه اول.</i>"
)

# ---------- missions ----------
MISSIONS_HEADER = (
    "🎯 <b>ماموریت‌های امروز</b>\n"
    "<code>─────────────────</code>\n"
    "{body}\n"
    "<code>─────────────────</code>\n"
    "<i>نصف‌شب ریست می‌شن. جا نمونی.</i>"
)

MISSION_ROW_DONE = "✅ <s>{title}</s>  <b>+{reward}</b>"
MISSION_ROW_READY = "🎁 <b>{title}</b>  ({progress}/{target})  <b>+{reward}</b>"
MISSION_ROW_OPEN = "▫️ {title}  ({progress}/{target})  +{reward}"

MISSION_CLAIMED = "✅ <b>{title}</b>\nگرفتی: <b>+{reward}</b> و +{xp} XP"
MISSION_NOT_READY = "هنوز تمومش نکردی."
MISSIONS_LOCKED = "🔒 ماموریت‌های روزانه از سطح ۲ باز می‌شن.\nیه کم دیگه بمون."
MISSIONS_EMPTY = "فعلاً ماموریتی برات نیست. فردا سر بزن."

# ---------- level up ----------
LEVEL_UP = (
    "🎉 <b>سطح {level}!</b>\n"
    "<code>─────────────────</code>\n"
    "🎁 پاداش ارتقا: <b>+{reward}</b>\n"
    "{unlock_line}"
)

LEVEL_UP_UNLOCK = "🔓 باز شد: <b>{icon} {title}</b>"
LEVEL_UP_NEXT = "<i>سطح {level}: {icon} {title}</i>"

# ---------- unlocks panel ----------
UNLOCKS_HEADER = (
    "🗺 <b>نقشه پیشرفت</b>\n"
    "<code>─────────────────</code>\n"
    "{body}\n"
    "<code>─────────────────</code>\n"
    "<i>سطح {level} · بعدی تو سطح {next_level}</i>"
)

UNLOCK_ROW_OPEN = "✅ {icon} {title}"
UNLOCK_ROW_LOCKED = "🔒 {icon} {title} <i>— سطح {level}</i>"
UNLOCK_ROW_NEXT = "➡️ <b>{icon} {title}</b> <i>— سطح {level}</i>"
UNLOCKS_ALL_DONE = "همه‌چیز باز شده. افسانه‌ای."

# ---------- buttons ----------
BTN_DAILY = "🎁 جایزه روزانه"
BTN_DAILY_READY = "🎁 جایزه امروز آماده‌ست"
BTN_MISSIONS = "🎯 ماموریت‌ها"
BTN_PROFILE = "🪪 پروفایل"
BTN_UNLOCKS = "🗺 نقشه پیشرفت"
BTN_BACK = "◀️ برگرد"
BTN_REFRESH = "🔄 تازه‌سازی"
BTN_CLAIM = "🎁 بگیر"

# ---------- system ----------
BANNED = "⛔️ حسابت مسدوده.\nدلیل: {reason}"
FROZEN = "🧊 حسابت موقتاً فریز شده."
ERROR = "😵‍💫 یه چیزی این وسط قاطی کرد. چند لحظه دیگه دوباره امتحان کن."
NOT_YOUR_PANEL = "این پنل مال تو نیست 😐"
PANEL_EXPIRED = "این پنل منقضی شده. دوباره بازش کن."
NO_REASON = "نامشخص"
XP_CAPPED = "\n\n<i>سقف XP امروزت پر شد. فردا تازه می‌شه.</i>"

HELP = (
    "🧭 <b>راهنمای تله‌لایف</b>\n"
    "<code>─────────────────</code>\n"
    "/profile — پروفایل و وضعیت زندگیت\n"
    "/daily — جایزه روزانه و استریک\n"
    "/missions — ماموریت‌های امروز\n"
    "/unlocks — نقشه پیشرفت\n"
    "/help — همین صفحه\n\n"
    "<i>تو گروه‌ها هم می‌تونی فارسی حرف بزنی: پول، سطح، روزانه…</i>"
)
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

__all__ = ["country", "politics", "production", "status"]
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
        await ctx.message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
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


def register(application) -> None:  # type: ignore[no-untyped-def]
    for command, handler in (
        ("createcountry", create),
        ("joincountry", join),
        ("country", show),
        ("economy", show),
        ("resources", show),
        ("donate", donate),
        ("paytax", tax),
    ):
        application.add_handler(CommandHandler(command, handler))
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
  e=await election_repo.open_for_country(x[3]['id']);await election_repo.nominate(e['id'],x[2].id,x[0].id,x[1].message_id);await x[1].reply_text(fa.NOMINATED)
async def vote(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and x[1].reply_to_message:
  e=await election_repo.open_for_country(x[3]['id']);candidate=await db.fetchval('SELECT player_id FROM election_candidates WHERE election_id=$1 AND message_id=$2',e['id'],x[1].reply_to_message.message_id)
  ok=await election_repo.vote(e['id'],x[2].id,candidate);await x[1].reply_text(fa.VOTED if ok else fa.DUPLICATE_VOTE)
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
def register(app)->None:
 for c,f in [('startelection',start_election),('nominate',nominate),('vote',vote),('startproject',start_project),('contribute',contribute),('poll',poll),('polls',polls),('pollvote',pollvote),('setflag',setflag),('announce',announce)]:app.add_handler(CommandHandler(c,f))
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


def register(application) -> None:  # type: ignore[no-untyped-def]
    for command, handler in (
        ("jobs", jobs),
        ("choosejob", choose),
        ("collect", collect),
        ("upgrade", upgrade),
    ):
        application.add_handler(CommandHandler(command, handler))
```

### `apps\teleworld_bot\handlers\status.py`

```python
"""Group activation and status for TeleWorld."""

from __future__ import annotations

from telegram import Update
from telegram.constants import ChatType
from telegram.ext import CommandHandler, ContextTypes

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
        fa.STATUS.format(title=title, members=fmt.number(int(members or 0)))
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(fa.HELP)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("help", help_command))
```

### `apps\teleworld_bot\main.py`

```python
"""TeleWorld bot entrypoint."""
from __future__ import annotations
from telegram.ext import Application
from apps.teleworld_bot.handlers import country,politics,production,status
from apps.teleworld_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service
def register(application:Application)->None:
 status.register(application);country.register(application);production.register(application);politics.register(application);application.add_error_handler(make_error_handler(fa.ERROR))
def main()->None:run_bot(Service.TELEWORLD,register)
if __name__=='__main__':main()
```

### `apps\teleworld_bot\texts\__init__.py`

```python
"""Package apps.teleworld_bot.texts."""
```

### `apps\teleworld_bot\texts\fa.py`

```python
"""All player-facing Persian copy for TeleWorld."""
CREATE_USAGE="روش استفاده: /createcountry نام | republic | توضیحات"
ADMIN_REQUIRED="فقط مدیر گروه تلگرام می‌تواند کشور را ثبت کند."
COUNTRY_CREATED="🏛 کشور <b>{name}</b> ساخته شد. حفاظت اولیه فعال است."
COUNTRY_JOINED="🤝 شهروند کشور شدی."
COUNTRY_EXISTS="این گروه قبلاً کشور دارد."
COUNTRY_MISSING="این گروه هنوز کشور ندارد."
COUNTRY_STATUS="🏛 <b>{name}</b>\n{description}\nحکومت: {government}\nخزانه: {treasury}"
DONATE_USAGE="روش استفاده: /donate IRT 10000"
DONATED="🎁 {amount} واحد {asset} به کشور اهدا شد."
TAX_PAID="🧾 مالیات پرداخت شد."
JOBS="شغل‌ها: farmer, miner, trader, journalist, doctor, programmer, engineer"
JOB_CHOSEN="⚙️ شغل انتخاب شد. تولید از همین حالا شروع شد."
COLLECTED="📦 {amount} واحد جمع شد و {xp} XP گرفتی."
UPGRADED="⬆️ {kind} به سطح {level} ارتقا یافت."
ELECTION_STARTED="🗳 انتخابات شروع شد."
NOMINATED="نامزدی ثبت شد."
VOTED="رأی محرمانه ثبت شد."
DUPLICATE_VOTE="قبلاً در این رأی‌گیری شرکت کردی."
PROJECT_STARTED="🏗 پروژه ملی شروع شد."
CONTRIBUTED="🤝 {amount} واحد به پروژه اضافه شد."
POLL_STARTED="📊 نظرسنجی شروع شد."
FLAG_SET="🏳 پرچم کشور ثبت شد."
ANNOUNCED="📣 اطلاعیه در صف انتشار قرار گرفت."
CITIZEN_REQUIRED="اول با /joincountry شهروند شو."
PRESIDENT_REQUIRED="این کار فقط دست رئیس‌جمهور است."
PRIVATE_ONLY="این دستور را داخل گروه اجرا کن."
ERROR="انجام عملیات ممکن نشد. کمی بعد دوباره امتحان کن."
HELP="/createcountry /joincountry /country /donate /paytax /jobs /choosejob /collect /upgrade /startelection /nominate /vote /startproject /contribute /poll /polls /pollvote /setflag /announce"
TAX_USAGE = "روش استفاده: /paytax 10000"
CHOOSE_JOB_USAGE = "روش استفاده: /choosejob farmer"
UPGRADE_USAGE = "روش استفاده: /upgrade production یا /upgrade storage"
INVALID_AMOUNT = "مقدار باید یک عدد صحیح مثبت باشد."
INVALID_INPUT = "ورودی معتبر نیست: {reason}"
```

### `AUDIT_STATUS.md`

```markdown
# TeleLife Audit Status

## Completed validations

- Reconstructed and recursively audited the complete supplied project dump.
- All Python files compile successfully.
- All local imports resolve statically.
- No circular imports remain in the project dependency graph.
- All YAML files parse as mappings.
- Required configuration paths resolve.
- Embedded shell/heredoc contamination was removed.
- Missing clock and admin static resources were added.
- Render multi-service and Docker configuration were repaired.
- Supabase transaction-pooler settings disable asyncpg statement caching.
- 46 dependency-independent logic and integrity tests passed.

## Environment-dependent verification still required

The audit sandbox did not contain Docker, Python 3.13, PostgreSQL, or all declared runtime/test packages. Before production deployment, CI or a deployment environment must install the declared dependencies, run the full pytest suite, build the Docker image, apply migrations to staging Supabase, and smoke-test all four Render services.

## Security action

Rotate the Supabase database password that appeared in the original supplied dump. The corrected environment example contains no credential.
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
from packages.core.bot.runtime import build_application, run_bot

__all__ = ["build_application", "make_error_handler", "run_bot"]
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
"""Shared bot bootstrap: polling and webhook from one code path."""

from __future__ import annotations

import logging
import signal
from collections.abc import Callable

from telegram.ext import AIORateLimiter, Application, ApplicationBuilder, Defaults

from packages.core import db
from packages.core.config import get_config
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import RunMode, Service, Settings, get_settings

logger = logging.getLogger(__name__)

RegisterFn = Callable[[Application], None]


async def _post_init(app: Application, settings: Settings, service: Service) -> None:
    await db.create_pool(settings)
    await migrate()
    logger.info("%s ready in %s mode", service.value, settings.run_mode.value)


async def _post_shutdown(app: Application) -> None:
    await db.close_pool()


def build_application(settings: Settings, service: Service) -> Application:
    cfg = get_config()
    defaults = Defaults(parse_mode="HTML", block=False)
    return (
        ApplicationBuilder()
        .token(settings.token_for(service))
        .post_init(lambda app: _post_init(app, settings, service))
        .post_shutdown(_post_shutdown)
        .defaults(defaults)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(cfg.int_("core.telegram.concurrent_updates"))
        .connect_timeout(cfg.float_("core.telegram.connect_timeout"))
        .read_timeout(cfg.float_("core.telegram.read_timeout"))
        .build()
    )


def run_bot(service: Service, register: RegisterFn) -> None:
    """Entrypoint used by both bots. Blocking; handles its own event loop."""
    settings = get_settings()
    setup_logging(service.value, settings.log_level)

    application = build_application(settings, service)
    register(application)

    if settings.run_mode is RunMode.WEBHOOK:
        application.run_webhook(
            listen=settings.host,
            port=settings.port,
            url_path=f"telegram/{service.value}",
            webhook_url=settings.webhook_url(service),
            secret_token=settings.webhook_secret or None,
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query", "my_chat_member"],
        )
    else:
        application.run_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query", "my_chat_member"],
            stop_signals=(signal.SIGINT, signal.SIGTERM),
        )
```

### `packages\core\config\__init__.py`

```python
from packages.core.config.loader import ConfigError, GameConfig, get_config, reload_config

__all__ = ["ConfigError", "GameConfig", "get_config", "reload_config"]
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
# XP economy. Anti-farming lives here, not in code.
sources:
  daily_claim:      40
  mission_complete: 50
  profile_view:     2
  group_activity:   5

anti_farm:
  # Hard ceiling per player per day across ALL sources.
  daily_cap: 1500
  # Per-source cooldowns in seconds. 0 = no cooldown.
  cooldowns:
    profile_view:   300
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
    """Apply pending migrations. Each file runs in its own transaction."""
    applied: list[str] = []
    async with dbpool.acquire() as conn:
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
                raise RuntimeError(
                    f"Migration '{version}' changed after being applied. "
                    "Create a new migration instead of editing history."
                )
            continue

        async with dbpool.transaction() as conn:
            await conn.execute(sql)
            await conn.execute(
                "INSERT INTO schema_migrations (version, checksum) VALUES ($1, $2)",
                version,
                digest,
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
        max_inactive_connection_lifetime=300.0,
        init=_init_connection,
        server_settings={"application_name": f"telelife-{settings.service}"},
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
"""Admin mutations and append-only audit writes."""
from __future__ import annotations
from typing import Any
import asyncpg
from packages.core import db
async def audit(conn:asyncpg.Connection,actor:str,action:str,request_id:str,details:dict[str,Any],player_id:int|None=None,country_id:int|None=None)->bool:
 return await conn.fetchval("INSERT INTO admin_audit_log(admin_actor,action,target_player_id,target_country_id,request_id,details) VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING id",actor,action,player_id,country_id,request_id,details) is not None
async def set_ban(conn:asyncpg.Connection,player_id:int,banned:bool,reason:str|None)->None:await conn.execute("UPDATE players SET is_banned=$2,ban_reason=$3 WHERE id=$1",player_id,banned,reason)
async def set_flag(conn:asyncpg.Connection,key:str,enabled:bool,actor:str)->None:await conn.execute("INSERT INTO feature_flags(key,enabled,updated_by) VALUES($1,$2,$3) ON CONFLICT(key) DO UPDATE SET enabled=$2,updated_by=$3,updated_at=now()",key,enabled,actor)
async def stats()->asyncpg.Record|None:return await db.fetchrow("SELECT (SELECT count(*) FROM players) players,(SELECT count(*) FROM countries) countries,(SELECT count(*) FROM citizenships) citizens")
async def users(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT id,telegram_id,first_name,level,xp,is_banned FROM players ORDER BY created_at DESC LIMIT $1",limit)
async def countries(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT id,name,government_type,treasury_toman,created_at FROM countries ORDER BY created_at DESC LIMIT $1",limit)
async def audits(limit:int=100)->list[asyncpg.Record]:return await db.fetch("SELECT * FROM admin_audit_log ORDER BY created_at DESC LIMIT $1",limit)
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
        WHERE cs.player_id = $1
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
        VALUES ($1, $2, $3, $4, now() + ($5::text || ' days')::interval, $6)
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
        "SELECT player_id FROM citizenships WHERE country_id = $1 ORDER BY player_id",
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

async def idempotency_exists(conn: asyncpg.Connection, key: str) -> bool:
    return bool(await conn.fetchval("SELECT EXISTS(SELECT 1 FROM ledger WHERE idempotency_key=$1)", key))

async def lock_player(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM players WHERE id=$1 FOR UPDATE", player_id)

async def lock_country(conn: asyncpg.Connection, country_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM countries WHERE id=$1 FOR UPDATE", country_id)

async def player_resource(conn: asyncpg.Connection, player_id: int, asset: str) -> int:
    value=await conn.fetchval("SELECT quantity FROM player_resources WHERE player_id=$1 AND asset_code=$2 FOR UPDATE",player_id,asset)
    return int(value or 0)

async def change_player(conn: asyncpg.Connection, player_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value=await conn.fetchval("UPDATE players SET wallet_toman=wallet_toman+$2 WHERE id=$1 AND wallet_toman+$2>=0 RETURNING wallet_toman",player_id,delta)
    else:
        value=await conn.fetchval("""INSERT INTO player_resources(player_id,asset_code,quantity) VALUES($1,$2,$3)
        ON CONFLICT(player_id,asset_code) DO UPDATE SET quantity=player_resources.quantity+$3,updated_at=now()
        WHERE player_resources.quantity+$3>=0 RETURNING quantity""",player_id,asset,delta)
    if value is None: raise ValueError("insufficient_player_balance")
    return int(value)

async def change_country(conn: asyncpg.Connection, country_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value=await conn.fetchval("UPDATE countries SET treasury_toman=treasury_toman+$2 WHERE id=$1 AND treasury_toman+$2>=0 RETURNING treasury_toman",country_id,delta)
    else:
        value=await conn.fetchval("""INSERT INTO country_resources(country_id,asset_code,quantity) VALUES($1,$2,$3)
        ON CONFLICT(country_id,asset_code) DO UPDATE SET quantity=country_resources.quantity+$3,updated_at=now()
        WHERE country_resources.quantity+$3>=0 RETURNING quantity""",country_id,asset,delta)
    if value is None: raise ValueError("insufficient_country_balance")
    return int(value)

async def insert(conn: asyncpg.Connection, *, player_id: int|None, country_id: int|None,
                 key: str, reason: str, asset: str, account: str, amount: int,
                 balance: int, metadata: dict[str,Any]|None=None) -> bool:
    row=await conn.fetchval("""INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,asset_code,account,amount,balance_after,metadata)
    VALUES($1,$2,$3,$4,$5,$5,$6,$7,$8,$9) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id""",
    player_id,country_id,key,reason,asset,account,amount,balance,metadata or {})
    return row is not None

async def economy_frozen(conn: asyncpg.Connection) -> bool:
    return bool(await conn.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='economy_frozen'),false)"))
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
        VALUES ($1, $2, $3, now(), now() + ($5::text || ' hours')::interval,
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
                processing_until = now() + ($4::text || ' seconds')::interval,
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
            available_at     = now() + ($4::text || ' seconds')::interval
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
            "SELECT count(*) FROM players WHERE last_seen_at > now() - ($1 || ' days')::interval",
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
```

### `packages\core\services\country.py`

```python
"""Country lifecycle and deterministic initial-resource allocation."""

from __future__ import annotations

import hashlib
import random

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, group_repo


def _resources(chat_id: int, name: str) -> dict[str, int]:
    """Split the national endowment deterministically across assets.

    Same (chat_id, name) always yields the same split, so a retry of country
    creation can never hand out a different starting position.
    """
    spec = get_config().section("country.resources")
    codes = sorted(str(code) for code in spec["asset_codes"])
    total = int(spec["country_total"])
    low = int(spec["minimum_share"])
    high = int(spec["maximum_share"])

    if not codes:
        raise ValueError("no_asset_codes_configured")
    if low > high:
        raise ValueError("minimum_share_above_maximum_share")
    if not low * len(codes) <= total <= high * len(codes):
        raise ValueError("country_total_outside_share_bounds")

    digest = hashlib.sha256(
        f"{spec['allocation_seed_namespace']}:{chat_id}:{name}".encode()
    ).digest()
    rng = random.Random(int.from_bytes(digest[:8], "big"))

    values = dict.fromkeys(codes, low)
    remaining = total - low * len(codes)

    while remaining > 0:
        headroom = [code for code in codes if values[code] < high]
        if not headroom:  # Unreachable given the bounds check, but never spin.
            break
        code = rng.choice(headroom)
        take = min(remaining, high - values[code], rng.randint(1, remaining))
        values[code] += take
        remaining -= take

    return values


async def create_country(
    *,
    chat_id: int,
    chat_title: str,
    player_id: int,
    name: str,
    government: str,
    description: str,
) -> asyncpg.Record:
    cfg = get_config()

    if government not in set(cfg.get("country.government_types")):
        raise ValueError("invalid_government")

    name = name.strip()
    description = description.strip()
    rules = cfg.section("country.validation")
    if not (
        int(rules["name_min_length"]) <= len(name) <= int(rules["name_max_length"])
    ):
        raise ValueError("invalid_name")
    if not (
        int(rules["description_min_length"])
        <= len(description)
        <= int(rules["description_max_length"])
    ):
        raise ValueError("invalid_description")

    if await country_repo.by_chat(chat_id) is not None:
        raise ValueError("country_already_exists")

    group = await group_repo.get_or_create(chat_id, chat_title)

    async with db.transaction() as conn:
        return await country_repo.create(
            conn,
            group.id,
            player_id,
            name,
            government,
            description,
            cfg.int_("country.creation.protection_days"),
            _resources(chat_id, name),
        )


async def join_country(*, chat_id: int, player_id: int) -> bool:
    """Become a citizen. False means the player was already a citizen."""
    country = await country_repo.by_chat(chat_id)
    if country is None:
        raise ValueError("country_not_found")
    async with db.transaction() as conn:
        return await country_repo.join(conn, player_id, int(country["id"]))
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

        await conn.execute(
            """
            INSERT INTO ledger
                (player_id, idempotency_key, reason, currency, asset_code, account,
                 amount, balance_after, metadata)
            VALUES ($1, $2, 'daily_reward', 'IRT', 'IRT', 'wallet', $3, $4, $5)
            ON CONFLICT (idempotency_key) DO NOTHING
            """,
            player_id,
            f"daily:{player_id}:{today:%Y-%m-%d}",
            total_toman,
            balance,
            {"streak": new_streak, "milestone": bool(milestone)},
        )

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
"""Single atomic funnel for every money/resource mutation."""

from __future__ import annotations

from dataclasses import dataclass

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo


@dataclass(frozen=True, slots=True)
class TransferResult:
    applied: bool
    duplicate: bool
    source_balance: int
    target_balance: int


def _validate_amount(asset: str, amount: int) -> None:
    if amount <= 0:
        raise ValueError("invalid_amount")
    cfg = get_config()
    if asset == "IRT":
        lo = cfg.int_("economy.limits.min_transaction_toman")
        hi = cfg.int_("economy.limits.max_transaction_toman")
    else:
        lo = cfg.int_("economy.limits.min_resource_transaction")
        hi = cfg.int_("economy.limits.max_resource_transaction")
    if not lo <= amount <= hi:
        raise ValueError("amount_out_of_range")


async def transfer(
    *,
    player_id: int,
    country_id: int,
    asset: str,
    amount: int,
    reason: str,
    idempotency_key: str,
) -> TransferResult:
    """Move `amount` of `asset` from a player to a country treasury, atomically."""
    _validate_amount(asset, amount)

    debit_key = f"{idempotency_key}:debit"
    credit_key = f"{idempotency_key}:credit"

    async with db.transaction() as conn:
        if await ledger_repo.economy_frozen(conn):
            raise RuntimeError("economy_frozen")
        if await ledger_repo.idempotency_exists(conn, debit_key):
            return TransferResult(False, True, 0, 0)

        # Always lock in the same order (player, then country) to avoid deadlocks.
        await ledger_repo.lock_player(conn, player_id)
        await ledger_repo.lock_country(conn, country_id)

        source = await ledger_repo.change_player(conn, player_id, asset, -amount)
        target = await ledger_repo.change_country(conn, country_id, asset, amount)

        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=debit_key,
            reason=reason,
            asset=asset,
            account=ledger_repo.player_account(asset),
            amount=-amount,
            balance=source,
            metadata={"country_id": country_id},
        )
        await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=credit_key,
            reason=reason,
            asset=asset,
            account=ledger_repo.country_account(asset),
            amount=amount,
            balance=target,
            metadata={"player_id": player_id},
        )
        return TransferResult(True, False, source, target)


async def country_adjust(
    *,
    country_id: int,
    asset: str,
    amount: int,
    reason: str,
    key: str,
    allow_frozen: bool = False,
) -> bool:
    """Signed treasury adjustment used by scheduled country economics."""
    async with db.transaction() as conn:
        if not allow_frozen and await ledger_repo.economy_frozen(conn):
            raise RuntimeError("economy_frozen")
        if await ledger_repo.idempotency_exists(conn, key):
            return False
        await ledger_repo.lock_country(conn, country_id)
        balance = await ledger_repo.change_country(conn, country_id, asset, amount)
        return await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=key,
            reason=reason,
            asset=asset,
            account=ledger_repo.country_account(asset),
            amount=amount,
            balance=balance,
        )
```

### `packages\core\services\elections.py`

```python
"""Election and poll business rules with idempotent resolution."""

from __future__ import annotations

from datetime import timedelta

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, election_repo
from packages.core.utils import clock


async def start(country_id: int, player_id: int) -> asyncpg.Record:
    """Open an election. One per country at a time."""
    country = await country_repo.by_id(country_id)
    if country is None:
        raise ValueError("country_not_found")

    president = country["president_player_id"]
    if president is not None and int(president) != player_id:
        raise PermissionError("president_required")

    if get_config().bool_("elections.election.one_open_per_country", True):
        if await election_repo.open_for_country(country_id) is not None:
            raise ValueError("election_already_open")

    cfg = get_config()
    now = clock.utcnow()
    nominations_end = now + timedelta(
        hours=cfg.int_("elections.election.nomination_duration_hours")
    )
    voting_end = nominations_end + timedelta(
        hours=cfg.int_("elections.election.voting_duration_hours")
    )

    async with db.transaction() as conn:
        return await election_repo.start(
            conn, country_id, player_id, nominations_end, voting_end
        )


async def create_poll(
    country_id: int,
    player_id: int,
    question: str,
    options: list[str],
) -> asyncpg.Record:
    """Create a poll after validating the question and the option list."""
    cfg = get_config()

    question = question.strip()
    q_min = cfg.int_("elections.poll.question_min_length")
    q_max = cfg.int_("elections.poll.question_max_length")
    if not q_min <= len(question) <= q_max:
        raise ValueError("invalid_question")

    cleaned = [text.strip() for text in options if text.strip()]
    if len(cleaned) != len(set(cleaned)):
        raise ValueError("duplicate_options")

    lo = cfg.int_("elections.poll.minimum_options")
    hi = cfg.int_("elections.poll.maximum_options")
    if not lo <= len(cleaned) <= hi:
        raise ValueError("invalid_options")

    o_min = cfg.int_("elections.poll.option_min_length")
    o_max = cfg.int_("elections.poll.option_max_length")
    if any(not o_min <= len(text) <= o_max for text in cleaned):
        raise ValueError("invalid_option_length")

    closes = clock.utcnow() + timedelta(
        hours=cfg.int_("elections.poll.duration_hours")
    )
    async with db.transaction() as conn:
        return await election_repo.create_poll(
            conn, country_id, player_id, question, closes, cleaned
        )


async def resolve_due() -> dict[str, int]:
    """Advance or close everything that is due. Safe to run concurrently:
    rows are claimed with FOR UPDATE SKIP LOCKED."""
    cfg = get_config()
    batch = cfg.int_("elections.scheduler.claim_batch_size")
    stats = {"elections": 0, "polls": 0}

    async with db.transaction() as conn:
        for row in await election_repo.claim_due(conn, batch):
            if row["status"] == "nominations":
                await election_repo.advance(conn, row["id"])
            else:
                await election_repo.resolve(conn, row["id"])
            stats["elections"] += 1

        for row in await election_repo.claim_due_polls(conn, batch):
            await election_repo.resolve_poll(conn, row["id"])
            stats["polls"] += 1

    return stats
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
from packages.core.services import xp

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
    country = await country_repo.by_id(country_id)
    if country is None:
        raise ValueError("country_not_found")

    president = country["president_player_id"]
    if president is not None and int(president) != player_id:
        raise PermissionError("president_required")

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
            "WHERE player_id = $1 AND country_id = $2)",
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
        accrual = accrue(row, now)
        amount = accrual.stored
        if amount < cfg.int_("jobs.production.minimum_collection_amount"):
            return 0, 0
        if await ledger_repo.idempotency_exists(conn, key):
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
) -> XPResult:
    """Grant XP exactly once. Safe under retries, races and double taps."""
    cfg = get_config()
    requested = amount if amount is not None else cfg.int_(f"xp.sources.{source}")
    if requested < 0:
        raise ValueError("negative_xp")
    daily_cap = cfg.int_("xp.anti_farm.daily_cap")

    async with db.transaction() as conn:
        row = await conn.fetchrow(
            "SELECT level, xp FROM players WHERE id = $1 FOR UPDATE", player_id
        )
        if row is None:
            raise ValueError(f"player {player_id} not found")

        level_before = int(row["level"])
        current_xp = int(row["xp"])

        # Reserve the idempotency key BEFORE any cap maths, so a duplicate is
        # reported as duplicate even on a day where the cap is already full.
        inserted = await conn.fetchval(
            """
            INSERT INTO xp_events (player_id, idempotency_key, source, amount, level_after)
            VALUES ($1, $2, $3, 0, $4)
            ON CONFLICT (idempotency_key) DO NOTHING
            RETURNING id
            """,
            player_id,
            idempotency_key,
            source,
            level_before,
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

        await conn.execute(
            "UPDATE xp_events SET amount = $2, level_after = $3 WHERE id = $1",
            inserted,
            allowed,
            level_after,
        )

        balance = await conn.fetchval(
            """
            UPDATE players SET
                level         = $2,
                xp            = $3,
                wallet_toman  = wallet_toman + $4,
                happiness     = LEAST(100, happiness + $5)
            WHERE id = $1
            RETURNING wallet_toman
            """,
            player_id,
            level_after,
            remaining,
            reward,
            happiness_bonus,
        )

        if reward:
            await conn.execute(
                """
                INSERT INTO ledger
                    (player_id, idempotency_key, reason, currency, asset_code, account,
                     amount, balance_after)
                VALUES ($1, $2, 'level_up', 'IRT', 'IRT', 'wallet', $3, $4)
                ON CONFLICT (idempotency_key) DO NOTHING
                """,
                player_id,
                f"levelup:{player_id}:{level_after}",
                reward,
                int(balance or 0),
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

    service: Service = Service.TELELIFE
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    database_url: PostgresDsn
    db_pool_min: int = Field(default=1, ge=1, le=50)
    db_pool_max: int = Field(default=5, ge=1, le=50)
    db_command_timeout: float = Field(default=15.0, gt=0, le=300)
    db_statement_cache_size: int = Field(default=0, ge=0)

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
    def validate_service_requirements(self) -> Settings:
        if self.service in {Service.TELELIFE, Service.TELEWORLD}:
            self.token_for(self.service)
            if self.run_mode is RunMode.WEBHOOK:
                if not self.webhook_base_url:
                    raise ValueError("WEBHOOK_BASE_URL is required in webhook mode")
                if len(self.webhook_secret) < 16:
                    raise ValueError("WEBHOOK_SECRET must contain at least 16 characters")
        if self.service is Service.ADMIN:
            if not self.admin_username or not self.admin_password:
                raise ValueError("ADMIN_USERNAME and ADMIN_PASSWORD are required")
            if len(self.admin_password) < 12:
                raise ValueError("ADMIN_PASSWORD must contain at least 12 characters")
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
# TeleLife | تله‌لایف · TeleWorld | تله‌ورلد

A Telegram virtual-life simulator. Two bots, one world.

- **TeleLife** — private chat. Your second life: profile, work, home, wallet, savings, USD.
- **TeleWorld** — groups. The society layer: territories, ranks, competition, economy.

One PostgreSQL database. One player identity. One economy.

## Status

**Phase 2 complete** — progression, daily rewards, missions, unlocks and the
glass button system are live. See `docs/PHASE_1.md` and `docs/PHASE_2.md`.
Roadmap and phase map: `TeleLife_Master_Plan.md`.

## Stack

Python 3.13 · python-telegram-bot · asyncpg (raw SQL) · PostgreSQL 15+ / Supabase ·
FastAPI + HTMX + Tailwind · Docker on Render

## Quick start
```

### `render.yaml`

```yaml
services:
  - type: worker
    name: telelife-bot
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: starter
    envVars:
      - {key: SERVICE, value: telelife}
      - {key: ENVIRONMENT, value: production}
      - {key: RUN_MODE, value: polling}
      - {key: DATABASE_URL, sync: false}
      - {key: DB_POOL_MIN, value: "1"}
      - {key: DB_POOL_MAX, value: "5"}
      - {key: DB_STATEMENT_CACHE_SIZE, value: "0"}
      - {key: TELELIFE_BOT_TOKEN, sync: false}

  - type: worker
    name: teleworld-bot
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: starter
    envVars:
      - {key: SERVICE, value: teleworld}
      - {key: ENVIRONMENT, value: production}
      - {key: RUN_MODE, value: polling}
      - {key: DATABASE_URL, sync: false}
      - {key: DB_POOL_MIN, value: "1"}
      - {key: DB_POOL_MAX, value: "5"}
      - {key: DB_STATEMENT_CACHE_SIZE, value: "0"}
      - {key: TELEWORLD_BOT_TOKEN, sync: false}

  - type: worker
    name: telelife-scheduler
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: starter
    envVars:
      - {key: SERVICE, value: scheduler}
      - {key: ENVIRONMENT, value: production}
      - {key: DATABASE_URL, sync: false}
      - {key: DB_POOL_MIN, value: "1"}
      - {key: DB_POOL_MAX, value: "3"}
      - {key: DB_STATEMENT_CACHE_SIZE, value: "0"}
      - {key: TELEWORLD_BOT_TOKEN, sync: false}

  - type: web
    name: telelife-admin
    runtime: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: starter
    healthCheckPath: /healthz
    envVars:
      - {key: SERVICE, value: admin}
      - {key: ENVIRONMENT, value: production}
      - {key: DATABASE_URL, sync: false}
      - {key: DB_POOL_MIN, value: "1"}
      - {key: DB_POOL_MAX, value: "5"}
      - {key: DB_STATEMENT_CACHE_SIZE, value: "0"}
      - {key: ADMIN_USERNAME, sync: false}
      - {key: ADMIN_PASSWORD, sync: false}
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
```

### `run.py`

```python
"""Container entrypoint dispatching exactly one configured service."""

from __future__ import annotations

import os


def main() -> None:
    service = os.getenv("SERVICE", "telelife").strip().lower()
    if service == "telelife":
        from apps.telelife_bot.main import main as target
    elif service == "teleworld":
        from apps.teleworld_bot.main import main as target
    elif service == "scheduler":
        from apps.scheduler.main import main as target
    elif service == "admin":
        import uvicorn
        from packages.core.settings import get_settings

        settings = get_settings()
        uvicorn.run(
            "apps.admin.main:app",
            host=settings.host,
            port=settings.port,
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
        return
    else:
        raise SystemExit(f"Unknown SERVICE value: {service!r}")
    target()


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
