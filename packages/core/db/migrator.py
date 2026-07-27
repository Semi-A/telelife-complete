"""Minimal forward-only SQL migration runner. No Alembic dependency."""

from __future__ import annotations

import hashlib
import logging
from pathlib import Path

from packages.core.db import pool as dbpool

logger = logging.getLogger(__name__)

MIGRATIONS_DIR = Path(__file__).resolve().parents[3] / "migrations"
# Migrations through 0014 were already shipped before this recovered
# distribution normalized text files. Existing databases can therefore contain
# the same applied SQL with checksums calculated from the pre-normalized bytes.
# Never re-run those versions: preserve their records and enforce immutable
# checksums for every migration introduced after the recovered baseline.
LEGACY_CHECKSUM_VERSIONS = frozenset({
    "0001_core_schema",
    "0002_progression",
    "0003_country_layer",
    "0004_admin_command_center",
    "0005_life_world_hardening",
    "0006_phase3_phase4_complete",
    "0007_unified_ui_onboarding",
    "0008_world_access_lifecycle",
    "0009_ads_governance_moderation",
    "0010_stars_subscriptions_ad_marketplace",
    "0011_population_channels_migration",
    "0012_reliability_live_market_engagement",
    "0013_country_identity_candles_realism",
    "0014_free_tier_hardening",
})

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
    """Apply pending migrations under a PostgreSQL advisory lock."""
    applied: list[str] = []
    async with dbpool.acquire() as conn:
        async with conn.transaction():
            await conn.execute("SELECT pg_advisory_xact_lock($1)", 839204731)
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
                        if version in LEGACY_CHECKSUM_VERSIONS:
                            logger.warning(
                                "legacy migration checksum differs; preserving the "
                                "database record and not re-running SQL: %s",
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
                    "INSERT INTO schema_migrations (version, checksum) VALUES ($1, $2)",
                    version, digest,
                )
                applied.append(version)
                logger.info("applied migration %s", version)
    if not applied:
        logger.info("database schema up to date")
    return applied