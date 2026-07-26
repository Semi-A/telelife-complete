"""Capacity-capped lazy production with proportional anti-farm XP."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from math import floor

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo, production_repo
from packages.core.services import xp

UPGRADE_KINDS = frozenset({"storage", "production"})


@dataclass(frozen=True, slots=True)
class Accrual:
    stored: int
    capacity: int
    rate: float


def _max_level(kind: str) -> int:
    cfg = get_config()
    if kind == "storage":
        return max(int(k) for k in cfg.section("jobs.storage.levels"))
    return cfg.int_("jobs.production_levels.maximum")


def _upgrade_cost(kind: str, target: int) -> int:
    section = "jobs.storage.upgrade_cost_toman" if kind == "storage" \
        else "jobs.production_levels.upgrade_cost_toman"
    cfg = get_config()
    path = f"{section}.{target}"
    if not cfg.has(path):
        raise ValueError("max_level_reached")
    return cfg.int_(path)


def accrue(row, at: datetime) -> Accrual:  # type: ignore[no-untyped-def]
    """Compute what the player's job has produced since the last checkpoint."""
    cfg = get_config()
    job = cfg.section(f"jobs.jobs.{row['job_code']}")
    rate = float(job["base_rate_per_hour"]) * (
        1 + (int(row["production_level"]) - 1)
        * cfg.float_("jobs.production.production_multiplier_per_level")
    )

    since = row["production_updated_at"]
    if since.tzinfo is None:
        since = since.replace(tzinfo=UTC)
    if at.tzinfo is None:
        at = at.replace(tzinfo=UTC)

    # Clock skew must never mint resources, and never destroy stored ones.
    skew = cfg.int_("jobs.production.max_accrual_clock_skew_seconds")
    elapsed = (at - since).total_seconds()
    if elapsed < -skew:
        elapsed = 0.0
    hours = max(0.0, elapsed) / cfg.int_("jobs.production.time_unit_seconds")

    capacity_hours = cfg.int_(f"jobs.storage.levels.{row['storage_level']}.capacity_hours")
    cap = floor(rate * capacity_hours)
    stored = min(cap, int(row["stored_amount"]) + floor(rate * hours))
    return Accrual(max(0, stored), max(0, cap), rate)


async def choose(player_id: int, job: str) -> bool:
    player = await db.fetchrow("SELECT level FROM players WHERE id=$1", player_id)
    if player is None:
        raise ValueError("player_not_found")
    if int(player["level"]) < 5:
        raise ValueError("job_locked")
    jobs = get_config().section("jobs.jobs")
    if job not in jobs:
        raise ValueError("invalid_job")
    return await production_repo.choose(player_id, job, str(jobs[job]["output_asset"]))


async def collect(player_id: int, key: str, at: datetime | None = None) -> tuple[int, int]:
    """Bank stored production. Returns (amount, xp_awarded)."""
    now = at or datetime.now(UTC)
    cfg = get_config()

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")
        accrual = accrue(row, now)
        amount = accrual.stored
        if amount < cfg.int_("jobs.production.minimum_collection_amount"):
            return 0, 0
        if await ledger_repo.idempotency_exists(conn, key):
            return 0, 0
        asset = row["output_asset_code"]
        balance = await ledger_repo.change_player(conn, player_id, asset, amount)
        if not await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason="production_collect",
            asset=asset,
            account=ledger_repo.player_account(asset),
            amount=amount,
            balance=balance,
            metadata={"job": row["job_code"]},
        ):
            return 0, 0
        await production_repo.clear(conn, player_id, now)

    fraction = amount / accrual.capacity if accrual.capacity else 0.0
    minimum = cfg.float_("jobs.production.minimum_collection_fraction_for_xp")
    award = (
        floor(cfg.int_("jobs.production.collection_xp_at_full_capacity") * fraction)
        if fraction >= minimum
        else 0
    )
    if award:
        result = await xp.grant(
            player_id, "production_collect", idempotency_key=f"{key}:xp", amount=award
        )
        award = result.granted
    return amount, award


async def upgrade(player_id: int, kind: str, key: str, at: datetime | None = None) -> int:
    """Upgrade storage or production. Old rate is checkpointed first."""
    if kind not in UPGRADE_KINDS:
        raise ValueError("invalid_upgrade")
    now = at or datetime.now(UTC)

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")

        current = int(row[f"{kind}_level"])
        target = current + 1
        if target > _max_level(kind):
            raise ValueError("max_level_reached")

        # Duplicate request: stop before touching balances or levels.
        if await ledger_repo.idempotency_exists(conn, key):
            return current

        cost = _upgrade_cost(kind, target)

        # Freeze production at the OLD rate before the level changes, so the
        # upgrade never applies retroactively to hours already elapsed.
        accrual = accrue(row, now)
        await production_repo.checkpoint(conn, player_id, accrual.stored, now)

        balance = await ledger_repo.change_player(conn, player_id, "IRT", -cost)
        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason=f"{kind}_upgrade",
            asset="IRT",
            account="wallet",
            amount=-cost,
            balance=balance,
            metadata={"kind": kind, "level": target},
        )
        await production_repo.level_up(conn, player_id, kind)
        return target