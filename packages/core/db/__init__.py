"""Public database API resolved lazily to avoid import-time side effects."""

from __future__ import annotations

from typing import Any

__all__ = [
    "acquire",
    "close_pool",
    "create_pool",
    "execute",
    "fetch",
    "fetchrow",
    "fetchval",
    "get_pool",
    "healthcheck",
    "transaction",
]


def __getattr__(name: str) -> Any:
    if name not in __all__:
        raise AttributeError(name)
    from packages.core.db import pool

    return getattr(pool, name)