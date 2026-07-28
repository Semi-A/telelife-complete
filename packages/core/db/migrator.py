"""Forward-only SQL migration runner with a recovered-history baseline."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from packages.core.db import pool as dbpool

logger = logging.getLogger(__name__)
MIGRATIONS_DIR = Path(__file__).resolve().parents[3] / "migrations"

# The source archive was reconstructed after these migrations had shipped. Their
# SQL bytes may differ from records produced by older releases (line endings and
# recovered source revisions), so an applied row is authoritative and is never
# re-executed. All schema corrections belong in 0027 and later.
RECOVERED_BASELINE_END = "0027_production_integrity_hardening"
STRICT_CHECKSUM_FROM = "0028_"
LEGACY_CHECKSUM_VERSIONS = frozenset()

_BOOTSTRAP = """
CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    checksum TEXT NOT NULL,
    applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""


def _normalise(text: str) -> str:
    """Line endings are a packaging detail, never a schema change.

    The archive has travelled through Windows and Linux checkouts, so the same
    migration can arrive with CRLF or LF. Hashing the normalised text keeps a
    deployment from failing on a difference that has no effect on SQL.
    """
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def _checksum(text: str) -> str:
    return hashlib.sha256(_normalise(text).encode("utf-8")).hexdigest()[:16]


def discover() -> list[Path]:
    if not MIGRATIONS_DIR.exists():
        return []
    return sorted(MIGRATIONS_DIR.glob("*.sql"), key=lambda path: path.name)


def _is_recovered_history(version: str) -> bool:
    return version <= RECOVERED_BASELINE_END


async def migrate() -> list[str]:
    """Apply pending migrations atomically under a transaction advisory lock."""
    applied: list[str] = []
    async with dbpool.acquire() as conn:
        async with conn.transaction():
            await conn.execute("SELECT pg_advisory_xact_lock($1)", 839204731)
            await conn.execute(_BOOTSTRAP)
            rows = await conn.fetch("SELECT version, checksum FROM schema_migrations")
            done = {row["version"]: row["checksum"] for row in rows}

            for path in discover():
                version = path.stem
                sql = path.read_text(encoding="utf-8")
                digest = _checksum(sql)
                recorded = done.get(version)
                if recorded is not None:
                    if recorded != digest:
                        if _is_recovered_history(version):
                            logger.warning(
                                "recovered migration checksum differs; preserving applied "
                                "database history without re-running SQL: %s",
                                version,
                            )
                            continue
                        raise RuntimeError(
                            f"Migration '{version}' changed after being applied. "
                            "Create a new migration instead of editing history."
                        )
                    continue

                await conn.execute(sql)
                await conn.execute(
                    "INSERT INTO schema_migrations(version, checksum) VALUES($1, $2)",
                    version,
                    digest,
                )
                applied.append(version)
                logger.info("applied migration %s", version)

    if not applied:
        logger.info("database schema up to date")
    return applied
