"""Authenticated, lightweight administration command center."""
from __future__ import annotations
from pathlib import Path
from fastapi import Depends, FastAPI, Request, Response, status
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
