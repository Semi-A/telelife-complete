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
