"""Daily missions: deterministic per-player daily selection, no shuffling.

Selection is seeded by (player_id, date) so a restart or a second call always
produces the same missions. No table needed to remember the choice.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from datetime import date
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.utils import clock


@dataclass(slots=True, frozen=True)
class Mission:
    key: str
    title: str
    target: int
    reward_toman: int
    reward_xp: int
    progress: int = 0
    claimed: bool = False

    @property
    def done(self) -> bool:
        return self.progress >= self.target


def _all_specs() -> list[dict[str, Any]]:
    pool = get_config().get("missions.pool")
    if not isinstance(pool, list):
        raise TypeError("missions.pool must be a list")
    return pool


def spec_for(mission_key: str) -> dict[str, Any] | None:
    return next((m for m in _all_specs() if str(m["key"]) == mission_key), None)


def _pool(level: int) -> list[dict[str, Any]]:
    return [m for m in _all_specs() if int(m.get("min_level", 1)) <= level]


def _seed(player_id: int, day: date, key: str) -> int:
    raw = f"{player_id}:{day:%Y-%m-%d}:{key}".encode()
    return int.from_bytes(hashlib.blake2b(raw, digest_size=8).digest(), "big")


def select_for(player_id: int, level: int, day: date | None = None) -> list[dict[str, Any]]:
    """Deterministic daily pick. Same inputs always yield the same missions."""
    day = day or clock.game_today()
    candidates = _pool(level)
    count = min(get_config().int_("missions.daily.count_per_day"), len(candidates))
    ranked = sorted(candidates, key=lambda m: _seed(player_id, day, str(m["key"])))
    return ranked[:count]


async def ensure_today(player_id: int, level: int, day: date | None = None) -> list[Mission]:
    """Materialise today's missions, then return them with live progress."""
    day = day or clock.game_today()
    chosen = select_for(player_id, level, day)
    if not chosen:
        return []

    async with db.transaction() as conn:
        await conn.executemany(
            """
            INSERT INTO daily_missions (player_id, mission_date, mission_key, target)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (player_id, mission_date, mission_key) DO NOTHING
            """,
            [(player_id, day, str(m["key"]), int(m["target"])) for m in chosen],
        )
        rows = await conn.fetch(
            """
            SELECT mission_key, progress, target, claimed_at
            FROM daily_missions
            WHERE player_id = $1 AND mission_date = $2
            """,
            player_id,
            day,
        )

    by_key = {r["mission_key"]: r for r in rows}
    out: list[Mission] = []
    for spec in chosen:
        key = str(spec["key"])
        row = by_key.get(key)
        out.append(
            Mission(
                key=key,
                title=str(spec["title"]),
                target=int(spec["target"]),
                reward_toman=int(spec["reward_toman"]),
                reward_xp=int(spec["reward_xp"]),
                progress=int(row["progress"]) if row else 0,
                claimed=bool(row and row["claimed_at"]),
            )
        )
    return out


async def report_progress(
    player_id: int, mission_key: str, amount: int = 1, day: date | None = None
) -> bool:
    """Advance a mission if the player has it today.

    Returns True only on the transition into "completed", so a caller can react
    exactly once.
    """
    if amount <= 0:
        return False
    day = day or clock.game_today()
    row = await db.fetchrow(
        """
        UPDATE daily_missions
        SET progress = LEAST(target, progress + $3)
        WHERE player_id = $1 AND mission_date = $4 AND mission_key = $2
          AND claimed_at IS NULL AND progress < target
        RETURNING progress, target
        """,
        player_id,
        mission_key,
        amount,
        day,
    )
    return bool(row and row["progress"] >= row["target"])


async def claim(player_id: int, mission_key: str, day: date | None = None) -> Mission | None:
    """Claim a completed mission exactly once. Returns the mission, or None."""
    day = day or clock.game_today()
    spec = spec_for(mission_key)
    if spec is None:
        return None

    reward_toman = int(spec["reward_toman"])

    async with db.transaction() as conn:
        row = await conn.fetchrow(
            """
            UPDATE daily_missions SET claimed_at = now()
            WHERE player_id = $1 AND mission_date = $2 AND mission_key = $3
              AND claimed_at IS NULL AND progress >= target
            RETURNING progress, target
            """,
            player_id,
            day,
            mission_key,
        )
        if row is None:
            return None

        balance = await conn.fetchval(
            "UPDATE players SET wallet_toman = wallet_toman + $2 WHERE id = $1 "
            "RETURNING wallet_toman",
            player_id,
            reward_toman,
        )
        await conn.execute(
            """
            INSERT INTO ledger
                (player_id, idempotency_key, reason, currency, asset_code, account,
                 amount, balance_after)
            VALUES ($1, $2, 'mission', 'IRT', 'IRT', 'wallet', $3, $4)
            ON CONFLICT (idempotency_key) DO NOTHING
            """,
            player_id,
            f"mission:{player_id}:{day:%Y-%m-%d}:{mission_key}",
            reward_toman,
            int(balance or 0),
        )

    return Mission(
        key=mission_key,
        title=str(spec["title"]),
        target=int(row["target"]),
        reward_toman=reward_toman,
        reward_xp=int(spec["reward_xp"]),
        progress=int(row["target"]),
        claimed=True,
    )
