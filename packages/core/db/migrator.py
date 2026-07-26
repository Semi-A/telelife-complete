"""Minimal forward-only SQL migration runner. No Alembic dependency."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from packages.core.db import pool as dbpool

logger = logging.getLogger(__name__)

MIGRATIONS_DIR = Path(__file__).resolve().parents[3] / "migrations"

_BOOTSTRAP = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version     TEXT PRIMARY KEY,
    checksum    TEXT NOT NULL,
    applied_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""


def _checksum(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def discover() -> list[Path]:
    if not MIGRATIONS_DIR.exists():
        return []
    return sorted(MIGRATIONS_DIR.glob("*.sql"), key=lambda p: p.name)


async def migrate() -> list[str]:
    """Apply pending migrations. Each file runs in its own transaction."""
    applied: list[str] = []
    async with dbpool.acquire() as conn:
        await conn.execute(_BOOTSTRAP)
        done = {r["version"]: r["checksum"] for r in await conn.fetch(
            "SELECT version, checksum FROM schema_migrations"
        )}

    for path in discover():
        version = path.stem
        sql = path.read_text(encoding="utf-8")
        digest = _checksum(sql)

        if version in done:
            if done[version] != digest:
                raise RuntimeError(
                    f"Migration '{version}' changed after being applied. "
                    "Create a new migration instead of editing history."
                )
            continue

        async with dbpool.transaction() as conn:
            await conn.execute(sql)
            await conn.execute(
                "INSERT INTO schema_migrations (version, checksum) VALUES ($1, $2)",
                version,
                digest,
            )
        applied.append(version)
        logger.info("applied migration %s", version)

    if not applied:
        logger.info("database schema up to date")
    return applied
