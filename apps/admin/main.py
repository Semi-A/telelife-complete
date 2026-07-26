"""Admin panel - Phase 1 delivers auth + live dashboard skeleton."""

from __future__ import annotations

import secrets
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.repositories import group_repo, player_repo
from packages.core.settings import Service, get_settings
from packages.core.utils import fmt

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
security = HTTPBasic()


def require_admin(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    settings = get_settings()
    ok_user = secrets.compare_digest(credentials.username, settings.admin_username)
    ok_pass = secrets.compare_digest(credentials.password, settings.admin_password)
    if not (ok_user and ok_pass):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


async def _collect_stats() -> dict[str, object]:
    return {
        "players_total": await player_repo.count_total(),
        "players_active": await player_repo.count_active(7),
        "groups_total": await group_repo.count_total(),
        "db_ok": await db.healthcheck(),
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    setup_logging(Service.ADMIN.value, settings.log_level)
    await db.create_pool(settings)
    await migrate()
    yield
    await db.close_pool()


app = FastAPI(title="TeleLife Admin", lifespan=lifespan, docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


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
from apps.admin.routers.country_admin import router as country_admin_router  # noqa: E402
app.include_router(country_admin_router)
