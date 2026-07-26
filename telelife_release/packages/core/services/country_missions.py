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