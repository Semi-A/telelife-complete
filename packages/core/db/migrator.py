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
# This recovered distribution may differ byte-for-byte from migrations already
# applied by earlier releases. Never re-run shipped history. Starting with 0023,
# checksums are strict and changing an applied migration remains a hard failure.
LEGACY_CHECKSUM_VERSIONS = frozenset({
    "0001_core_schema", "0002_progression", "0003_country_layer",
    "0004_admin_command_center", "0005_life_world_hardening",
    "0006_phase3_phase4_complete", "0007_unified_ui_onboarding",
    "0008_world_access_lifecycle", "0009_ads_governance_moderation",
    "0010_stars_subscriptions_ad_marketplace", "0011_population_channels_migration",
    "0012_reliability_live_market_engagement", "0013_country_identity_candles_realism",
    "0014_free_tier_hardening", "0015_purposeful_work_loop",
    "0016_national_projects_and_missions", "0017_country_economy_release_b",
    "0018_country_trade_diplomacy_release_c", "0019_life_progression_system",
    "0020_admin_operations_10", "0021_multi_admin_hardening",
    "0022_ui_panel_expiry",
})
# 0021 and 0022 belong to the recovered project history and may already exist
# with checksums produced from older line endings/source dumps. 0023 is the
# first migration created by this release and is therefore the strict boundary.
STRICT_CHECKSUM_FROM = "0023_country_social_life"

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
                        # Every migration shipped before the strict baseline belongs to
                        # recovered history, including installations with variant names.
                        if version in LEGACY_CHECKSUM_VERSIONS or version < STRICT_CHECKSUM_FROM:
                            logger.info(
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