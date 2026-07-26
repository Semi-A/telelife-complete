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