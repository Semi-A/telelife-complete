"""Database-backed admin identities with audited lifecycle operations."""
from __future__ import annotations

import hashlib
import hmac
import os
import re
from dataclasses import dataclass
from uuid import uuid4

from packages.core import db
from packages.core.settings import get_settings

ROLES = frozenset({"viewer", "support", "content", "economy", "operator", "superadmin"})
USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{3,64}$")
PBKDF2_ITERATIONS = 210_000


@dataclass(frozen=True, slots=True)
class AdminIdentity:
    username: str
    role: str
    enabled: bool
    source: str = "database"


def normalize_username(username: str) -> str:
    value = username.strip().lower()
    if not USERNAME_RE.fullmatch(value):
        raise ValueError("invalid_admin_username")
    return value


def validate_role(role: str) -> str:
    value = role.strip().lower()
    if value not in ROLES:
        raise ValueError("invalid_admin_role")
    return value


def hash_password(password: str) -> str:
    if len(password) < 12 or len(password) > 256:
        raise ValueError("invalid_admin_password")
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PBKDF2_ITERATIONS)
    return f"pbkdf2_sha256${PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, encoded: str | None) -> bool:
    # Run a real derivation even for invalid/missing hashes to reduce username enumeration.
    try:
        algorithm, iterations, salt_hex, expected_hex = (encoded or "").split("$", 3)
        if algorithm != "pbkdf2_sha256":
            raise ValueError
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(expected_hex)
        rounds = int(iterations)
        if not 100_000 <= rounds <= 1_000_000:
            raise ValueError
    except (TypeError, ValueError):
        salt = bytes(16)
        expected = bytes(32)
        rounds = PBKDF2_ITERATIONS
    actual = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, rounds)
    return hmac.compare_digest(actual, expected)


async def authenticate(username: str, password: str) -> AdminIdentity | None:
    settings = get_settings()
    normalized = username.strip().lower()
    env_user = settings.admin_username.strip().lower()
    env_ok = hmac.compare_digest(normalized, env_user) and hmac.compare_digest(
        password, settings.admin_password
    )
    if env_ok:
        return AdminIdentity(env_user, settings.admin_role, True, "environment")

    row = await db.fetchrow(
        "SELECT username,role,enabled,password_hash FROM admin_identities WHERE username=$1",
        normalized,
    )
    encoded = str(row["password_hash"]) if row and row["password_hash"] else None
    password_ok = verify_password(password, encoded)
    if not row or not row["enabled"] or not password_ok:
        return None
    await db.execute(
        """UPDATE admin_identities SET last_login_at=now()
           WHERE username=$1 AND (last_login_at IS NULL OR last_login_at<now()-interval '5 minutes')""",
        normalized,
    )
    return AdminIdentity(normalized, str(row["role"]), True)


async def role_for(username: str) -> str | None:
    settings = get_settings()
    normalized = username.strip().lower()
    if hmac.compare_digest(normalized, settings.admin_username.strip().lower()):
        return settings.admin_role
    return await db.fetchval(
        "SELECT role FROM admin_identities WHERE username=$1 AND enabled", normalized
    )


async def list_identities() -> list[dict[str, object]]:
    settings = get_settings()
    rows = [dict(row) for row in await db.fetch(
        """SELECT username,role,enabled,created_by,created_at,updated_at,last_login_at,
                  'database'::text source
           FROM admin_identities ORDER BY enabled DESC,role DESC,username"""
    )]
    env_user = settings.admin_username.strip().lower()
    if not any(str(row["username"]).lower() == env_user for row in rows):
        rows.insert(0, {
            "username": env_user,
            "role": settings.admin_role,
            "enabled": True,
            "created_by": "environment",
            "created_at": None,
            "updated_at": None,
            "last_login_at": None,
            "source": "environment",
        })
    return rows


async def create_identity(
    actor: str, username: str, password: str, role: str
) -> dict[str, object]:
    normalized = normalize_username(username)
    normalized_role = validate_role(role)
    if normalized == get_settings().admin_username.strip().lower():
        raise ValueError("admin_reserved")
    encoded = hash_password(password)
    request_id = f"admin-create:{uuid4()}"
    async with db.transaction() as conn:
        row = await conn.fetchrow(
            """INSERT INTO admin_identities(username,role,password_hash,enabled,created_by)
               VALUES($1,$2,$3,TRUE,$4)
               ON CONFLICT(username) DO NOTHING
               RETURNING username,role,enabled,created_by,created_at,updated_at,last_login_at,
                         'database'::text source""",
            normalized, normalized_role, encoded, actor,
        )
        if not row:
            raise ValueError("admin_exists")
        await conn.execute(
            """INSERT INTO admin_audit_log(admin_actor,action,request_id,details)
               VALUES($1,'admin_identity_created',$2,$3)""",
            actor, request_id, {"username": normalized, "role": normalized_role},
        )
    return dict(row)


async def update_identity(
    actor: str,
    username: str,
    *,
    role: str | None = None,
    enabled: bool | None = None,
    password: str | None = None,
) -> dict[str, object]:
    normalized = normalize_username(username)
    if normalized == get_settings().admin_username.strip().lower():
        raise ValueError("admin_environment_managed")
    normalized_role = validate_role(role) if role is not None else None
    encoded = hash_password(password) if password is not None else None
    request_id = f"admin-update:{uuid4()}"
    async with db.transaction() as conn:
        current = await conn.fetchrow(
            "SELECT username,role,enabled FROM admin_identities WHERE username=$1 FOR UPDATE",
            normalized,
        )
        if not current:
            raise ValueError("admin_not_found")
        next_role = normalized_role or str(current["role"])
        next_enabled = bool(current["enabled"]) if enabled is None else enabled
        if normalized == actor.lower() and not next_enabled:
            raise ValueError("admin_cannot_disable_self")
        if current["role"] == "superadmin" and current["enabled"] and (
            next_role != "superadmin" or not next_enabled
        ):
            others = await conn.fetchval(
                """SELECT count(*) FROM admin_identities
                   WHERE enabled AND role='superadmin' AND username<>$1""",
                normalized,
            )
            env_is_super = get_settings().admin_role == "superadmin"
            if not env_is_super and int(others or 0) == 0:
                raise ValueError("last_superadmin")
        row = await conn.fetchrow(
            """UPDATE admin_identities SET
                 role=COALESCE($2,role), enabled=COALESCE($3,enabled),
                 password_hash=COALESCE($4,password_hash),
                 disabled_at=CASE WHEN COALESCE($3,enabled) THEN NULL ELSE COALESCE(disabled_at,now()) END,
                 updated_at=now()
               WHERE username=$1
               RETURNING username,role,enabled,created_by,created_at,updated_at,last_login_at,
                         'database'::text source""",
            normalized, normalized_role, enabled, encoded,
        )
        await conn.execute(
            """INSERT INTO admin_audit_log(admin_actor,action,request_id,details)
               VALUES($1,'admin_identity_updated',$2,$3)""",
            actor, request_id,
            {"username": normalized, "role": normalized_role, "enabled": enabled,
             "password_changed": password is not None},
        )
    return dict(row)

async def authentication_blocked(throttle_key: str) -> bool:
    return bool(await db.fetchval(
        "SELECT blocked_until>now() FROM admin_auth_throttle WHERE throttle_key=$1",
        throttle_key,
    ))


async def record_authentication_failure(throttle_key: str) -> None:
    await db.execute(
        """INSERT INTO admin_auth_throttle(throttle_key,failures,first_failed_at,blocked_until,updated_at)
           VALUES($1,1,now(),NULL,now())
           ON CONFLICT(throttle_key) DO UPDATE SET
             failures=CASE WHEN admin_auth_throttle.first_failed_at<now()-interval '15 minutes' THEN 1 ELSE admin_auth_throttle.failures+1 END,
             first_failed_at=CASE WHEN admin_auth_throttle.first_failed_at<now()-interval '15 minutes' THEN now() ELSE admin_auth_throttle.first_failed_at END,
             blocked_until=CASE WHEN (CASE WHEN admin_auth_throttle.first_failed_at<now()-interval '15 minutes' THEN 1 ELSE admin_auth_throttle.failures+1 END)>=8 THEN now()+interval '15 minutes' ELSE admin_auth_throttle.blocked_until END,
             updated_at=now()""",
        throttle_key,
    )


async def clear_authentication_failures(throttle_key: str) -> None:
    await db.execute("DELETE FROM admin_auth_throttle WHERE throttle_key=$1", throttle_key)
