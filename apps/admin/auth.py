"""Authentication dependencies shared by the admin application and routers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated
import hashlib

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from packages.core.services import admin_accounts

security = HTTPBasic(auto_error=False)


@dataclass(frozen=True, slots=True)
class AdminPrincipal:
    username: str
    role: str
    source: str


async def require_admin(
    request: Request,
    credentials: Annotated[HTTPBasicCredentials | None, Depends(security)],
) -> AdminPrincipal:
    """Authenticate the bootstrap account or an enabled database admin."""
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری و گذرواژه لازم است.",
            headers={"WWW-Authenticate": "Basic realm=TeleLife Admin"},
        )
    client_ip = request.client.host if request.client else "unknown"
    throttle_key = hashlib.sha256(f"{client_ip}|{credentials.username.strip().lower()}".encode()).hexdigest()
    if await admin_accounts.authentication_blocked(throttle_key):
        raise HTTPException(status_code=429, detail="تلاش‌های ورود بیش از حد است؛ چند دقیقه بعد دوباره امتحان کنید.")
    identity = await admin_accounts.authenticate(credentials.username, credentials.password)
    if identity is None:
        await admin_accounts.record_authentication_failure(throttle_key)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا گذرواژه نادرست است.",
            headers={"WWW-Authenticate": "Basic realm=TeleLife Admin"},
        )
    await admin_accounts.clear_authentication_failures(throttle_key)
    return AdminPrincipal(identity.username, identity.role, identity.source)