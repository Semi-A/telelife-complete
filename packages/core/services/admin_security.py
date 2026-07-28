"""Backend-enforced RBAC and one-use previews for privileged admin mutations."""
from __future__ import annotations

import hashlib
import json
import secrets
from datetime import UTC, datetime, timedelta

from fastapi import HTTPException, Request

from packages.core import db

ROLE_PERMISSIONS = {
    "viewer": {"read"},
    "support": {"read", "players"},
    "content": {"read", "content"},
    "economy": {"read", "economy", "countries"},
    "operator": {"read", "operations", "content"},
    "superadmin": {
        "read", "players", "content", "economy", "countries", "operations", "undo", "admins"
    },
}
SENSITIVE = (
    ("/admins", "admins"),
    ("/users/", "players"),
    ("/market/", "economy"),
    ("/countries/", "countries"),
    ("/feature-flags/", "operations"),
    ("/operations/", "operations"),
    ("/ad-requests/", "content"),
    ("/undo/", "undo"),
)


def permission_for(path: str, method: str) -> str:
    if method in {"GET", "HEAD", "OPTIONS"}:
        return "read"
    for fragment, permission in SENSITIVE:
        if fragment in path:
            return permission
    return "content"


def require_permission(actor: str, role: str, path: str, method: str) -> str:
    permission = permission_for(path, method)
    if permission not in ROLE_PERMISSIONS.get(role, set()):
        raise HTTPException(403, f"نقش {role} اجازه این عملیات را ندارد.")
    return role


def payload_hash(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


async def issue_preview(
    actor: str, role: str, method: str, path: str, payload: object
) -> dict[str, object]:
    require_permission(actor, role, path, method)
    if not path.startswith("/api/admin/") or path == "/api/admin/action-preview":
        raise HTTPException(400, "مسیر پیش‌نمایش معتبر نیست.")
    token = secrets.token_urlsafe(32)
    digest = hashlib.sha256(token.encode()).hexdigest()
    expires = datetime.now(UTC) + timedelta(minutes=2)
    await db.execute(
        """INSERT INTO admin_action_previews
           (token_hash,admin_actor,method,path,payload_hash,expires_at)
           VALUES($1,$2,$3,$4,$5,$6)""",
        digest, actor, method.upper(), path, payload_hash(payload), expires,
    )
    return {
        "token": token,
        "expires_at": expires,
        "permission": permission_for(path, method),
        "summary": f"{method.upper()} {path}",
    }


async def verify_request(request: Request, actor: str, role: str) -> None:
    assigned_role = require_permission(actor, role, request.url.path, request.method)
    if request.method in {"GET", "HEAD", "OPTIONS"}:
        request.state.admin_role = assigned_role
        return
    if request.url.path == "/api/admin/action-preview":
        request.state.admin_role = assigned_role
        return
    token = request.headers.get("x-admin-preview", "")
    if not token:
        raise HTTPException(428, "برای این عملیات پیش‌نمایش معتبر لازم است.")
    try:
        payload = await request.json()
    except (ValueError, json.JSONDecodeError):
        payload = {}
    digest = hashlib.sha256(token.encode()).hexdigest()
    used = await db.fetchval(
        """UPDATE admin_action_previews SET used_at=now()
           WHERE token_hash=$1 AND admin_actor=$2 AND method=$3 AND path=$4
             AND payload_hash=$5 AND used_at IS NULL AND expires_at>now()
           RETURNING token_hash""",
        digest, actor, request.method.upper(), request.url.path, payload_hash(payload),
    )
    if not used:
        raise HTTPException(409, "پیش‌نمایش منقضی، مصرف‌شده یا ناسازگار است.")
    request.state.admin_role = assigned_role
