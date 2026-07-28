"""Authenticated, lightweight administration command center."""
from __future__ import annotations
from pathlib import Path
import logging
from uuid import uuid4
from urllib.parse import urlsplit
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from apps.admin.auth import require_admin
from apps.admin.routers.country_admin import router as country_admin_router
from packages.core import db
from packages.core.repositories import admin_repo
from packages.core.runtime_status import snapshot

logger = logging.getLogger(__name__)
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app = FastAPI(title="TeleLife Admin", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.include_router(country_admin_router)

@app.exception_handler(Exception)
async def admin_unhandled_error(request: Request, exc: Exception) -> JSONResponse:
    incident_id = uuid4().hex[:12]
    logger.exception(
        "admin request failed",
        extra={"extra_fields":{"incident_id":incident_id,"path":request.url.path,"method":request.method}},
    )
    return JSONResponse(
        {"detail":"عملیات سمت سرور کامل نشد.","incident_id":incident_id},
        status_code=500,
        headers={"Cache-Control":"no-store"},
    )

@app.middleware("http")
async def security_headers(request: Request, call_next):  # type: ignore[no-untyped-def]
    # Mutating admin APIs are same-origin JSON only. This is stateless and costs
    # no extra service while blocking cross-site form and simple-request attacks.
    if request.method not in {"GET", "HEAD", "OPTIONS"}:
        host = request.headers.get("host", "").lower()
        origin = request.headers.get("origin")
        referer = request.headers.get("referer")
        supplied = origin or referer
        if supplied:
            try: supplied_host = urlsplit(supplied).netloc.lower()
            except ValueError: supplied_host = ""
            if not host or supplied_host != host:
                return JSONResponse({"detail": "درخواست از مبدأ نامعتبر رد شد."}, status_code=403)
        if request.url.path.startswith("/api/admin"):
            content_type=request.headers.get("content-type","").split(";",1)[0].strip().lower()
            if content_type != "application/json":
                return JSONResponse({"detail": "درخواست مدیریتی باید JSON باشد."}, status_code=415)
    response: Response = await call_next(request)
    response.headers.update({
        "X-Content-Type-Options": "nosniff", "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer", "Cache-Control": "no-store",
        "Permissions-Policy": "camera=(), microphone=(), geolocation=(), payment=()",
        "Cross-Origin-Opener-Policy": "same-origin",
        "Content-Security-Policy": "default-src 'self'; style-src 'self' 'unsafe-inline'; "
          "script-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'",
    })
    return response

@app.get("/healthz")
async def healthz() -> JSONResponse:
    db_ok = await db.healthcheck(); services = snapshot()
    # /healthz describes the HTTP process itself. Bot lifecycle states remain
    # visible in the payload, but a Telegram reconnect must not turn the admin
    # website health endpoint into a false 503.
    admin_ok = services.get("admin", {}).get("status") in {"starting", "healthy", "degraded"}
    code = status.HTTP_200_OK if db_ok and admin_ok else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse({"ok": db_ok and admin_ok, "database": db_ok, "services": services}, code)

@app.get("/readyz")
async def readyz() -> JSONResponse:
    db_ok = await db.healthcheck()
    return JSONResponse({"ready": db_ok}, status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE)

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request, _ = Depends(require_admin)) -> HTMLResponse:
    row = await admin_repo.dashboard_stats()
    return templates.TemplateResponse(request, "dashboard.html", {"stats": dict(row) if row else {}})
