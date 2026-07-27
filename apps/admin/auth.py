"""Authentication dependencies shared by the admin application and routers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from packages.core.services import admin_accounts

security = HTTPBasic(auto_error=False)


@dataclass(frozen=True, slots=True)
class AdminPrincipal:
    username: str
    role: str
    source: str


async def require_admin(
    credentials: Annotated[HTTPBasicCredentials | None, Depends(security)],
) -> AdminPrincipal:
    """Authenticate the bootstrap account or an enabled database admin."""
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری و گذرواژه لازم است.",
            headers={"WWW-Authenticate": "Basic realm=TeleLife Admin"},
        )
    identity = await admin_accounts.authenticate(credentials.username, credentials.password)
    if identity is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا گذرواژه نادرست است.",
            headers={"WWW-Authenticate": "Basic realm=TeleLife Admin"},
        )
    return AdminPrincipal(identity.username, identity.role, identity.source)