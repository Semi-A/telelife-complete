"""Country missions: instantiate on action, track progress, pay out once."""

from __future__ import annotations

import hashlib
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import mission_repo, outbox_repo
from packages.core.utils import clock


def _pick_key(country_id: int, day: Any, keys: list[str]) -> str:
    """Deterministic daily pick, stable across restarts and workers."""
    namespace = get_config().get(
        "country_missions.daily.selection_seed_namespace", "country_missions"
    )
    seed = hashlib.sha256(f"{namespace}:{country_id}:{day}".encode()).digest()
    return keys[int.from_bytes(seed[:4], "big") % len(keys)]


async def report(country_id: int, action: str, asset: str, amount: int) -> bool:
    """Report a player action. Returns True only when a mission just paid out."""
    if amount <= 0:
        return False

    cfg = get_config()
    mapping = cfg.get(f"country_missions.progress.eligible_actions.{action}", {})
    if not isinstance(mapping, dict) or asset not in mapping:
        return False

    metric = str(mapping[asset])
    pool = cfg.section("country_missions.pool")
    keys = sorted(k for k, spec in pool.items() if spec["metric_key"] == metric)
    if not keys:
        return False

    day = clock.game_today()
    key = _pick_key(country_id, day, keys)
    spec = pool[key]

    async with db.transaction() as conn:
        await mission_repo.ensure(
            conn,
            country_id,
            day,
            key,
            metric,
            int(spec["target_amount"]),
            cfg.get("country_missions.reward.ledger_asset_code"),
            int(spec["reward_amount"]),
        )
        row = await mission_repo.add(conn, country_id, day, metric, amount)
        if row is None or row["completed_at"] is None:
            return False
        if not await mission_repo.reward_once(conn, country_id, day, key):
            return False

        await mission_repo.effect(
            conn,
            country_id,
            cfg.get("country_missions.reward.effect_code"),
            int(spec["reward_magnitude_basis_points"]),
            f"{day}:{key}",
            cfg.int_("country_missions.reward.effect_duration_hours"),
        )
        destination = await conn.fetchval(
            """
            SELECT g.telegram_id FROM countries c
            JOIN groups g ON g.id = c.group_id
            WHERE c.id = $1
            """,
            country_id,
        )
        await outbox_repo.enqueue(
            conn,
            f"country-mission:{country_id}:{day}:{key}",
            "country_mission_completed",
            {"country_id": country_id, "mission_key": key},
            destination,
        )
        return True
EOF
cat > packages/core/services/country_economy.py <<'EOF'
"""Idempotent daily country income/expense settlement."""

from __future__ import annotations

from datetime import date, timedelta

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

_IRT = "IRT"


async def settle_day(country_id: int, day: date) -> bool:
    """Settle one country-day. Returns False when already settled."""
    key = f"country-economy:{country_id}:{day}"

    async with db.transaction() as conn:
        # Lock first, then check: checking before locking leaves a window
        # where two schedulers both see "not settled yet".
        row = await ledger_repo.lock_country(conn, country_id)
        if row is None:
            return False
        if await ledger_repo.idempotency_exists(conn, key):
            return False

        cfg = get_config()
        income = int(row["daily_income_toman"]) + cfg.int_(
            "economy.country.daily_base_income_toman"
        )
        expense = int(row["daily_expense_toman"]) + cfg.int_(
            "economy.country.daily_base_expense_toman"
        )
        delta = income - expense
        if delta < 0:
            # Never drive the treasury below zero; the CHECK would abort the
            # whole scheduler batch instead of just skipping this country.
            delta = max(delta, -int(row["treasury_toman"]))

        balance = await ledger_repo.change_country(conn, country_id, _IRT, delta)
        await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=key,
            reason="country_daily_economy",
            asset=_IRT,
            account="treasury",
            amount=delta,
            balance=balance,
            metadata={"date": str(day), "income": income, "expense": expense},
        )
        await conn.execute(
            """
            INSERT INTO country_economy_daily
                (country_id, economy_date, income_toman, expense_toman,
                 closing_treasury, ledger_key)
            VALUES ($1, $2, $3, $4, $5, $6)
            ON CONFLICT DO NOTHING
            """,
            country_id,
            day,
            income,
            expense,
            balance,
            key,
        )
        return True


async def catch_up(today: date | None = None) -> int:
    """Settle any missed days after downtime. Returns settlements performed."""
    end = today or clock.game_today()
    days = get_config().int_("economy.country.catch_up_days")
    rows = await db.fetch("SELECT id FROM countries ORDER BY id")

    settled = 0
    for row in rows:
        for offset in range(days - 1, -1, -1):
            if await settle_day(int(row["id"]), end - timedelta(days=offset)):
                settled += 1
    return settled