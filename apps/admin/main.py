"""Authenticated admin panel and process/service health endpoints."""
from __future__ import annotations

from pathlib import Path

from fastapi import Depends, FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from apps.admin.auth import require_admin
from apps.admin.routers.country_admin import router as country_admin_router
from packages.core import db
from packages.core.repositories import group_repo, player_repo
from packages.core.runtime_status import snapshot
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

app = FastAPI(title="TeleLife Admin", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.include_router(country_admin_router)

@app.middleware("http")
async def security_headers(request: Request, call_next):  # type: ignore[no-untyped-def]
    response: Response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Cache-Control"] = "no-store"
    return response

@app.get("/healthz")
async def healthz() -> JSONResponse:
    db_ok = await db.healthcheck()
    services = snapshot()
    admin_ok = services.get("admin", {}).get("status") in {"starting", "healthy"}
    code = status.HTTP_200_OK if db_ok and admin_ok else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse({"ok": db_ok and admin_ok, "database": db_ok, "services": services}, code)

@app.get("/readyz")
async def readyz() -> JSONResponse:
    db_ok = await db.healthcheck()
    return JSONResponse({"ready": db_ok}, status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, _: str = Depends(require_admin)) -> HTMLResponse:
    return templates.TemplateResponse(request, "dashboard.html", {"stats": await _collect_stats(), "fmt": fmt})

@app.get("/partials/stats", response_class=HTMLResponse)
async def stats_partial(request: Request, _: str = Depends(require_admin)) -> HTMLResponse:
    return templates.TemplateResponse(request, "partials/stats.html", {"stats": await _collect_stats(), "fmt": fmt})
