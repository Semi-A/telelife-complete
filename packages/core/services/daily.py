"""Daily reward + streak engine.

Streak philosophy: missing one day drops you to `grace_reset_to`, not zero.
Wiping a 90-day streak over one bad day is how games lose players permanently.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

from packages.core import db
from packages.core.config import get_config
from packages.core.utils import clock


@dataclass(slots=True, frozen=True)
class DailyResult:
    claimed: bool
    already_claimed: bool
    streak: int
    best_streak: int
    reward_toman: int
    reward_xp: int
    milestone_label: str | None
    milestone_toman: int
    next_milestone: int | None


def _reward_for(streak: int) -> tuple[int, int]:
    cfg = get_config()
    base = cfg.int_("daily.reward.base_toman")
    step = cfg.float_("daily.reward.streak_multiplier_per_day")
    cap = cfg.float_("daily.reward.max_multiplier")
    multiplier = min(1.0 + step * max(0, streak - 1), cap)
    return int(base * multiplier), cfg.int_("daily.reward.xp")


def _milestone(streak: int) -> dict[str, Any] | None:
    milestones = get_config().section("daily.milestones")
    spec = milestones.get(streak, milestones.get(str(streak)))
    return dict(spec) if spec else None


def _next_milestone(streak: int) -> int | None:
    keys = sorted(int(k) for k in get_config().section("daily.milestones"))
    return next((k for k in keys if k > streak), None)


def _next_streak(last: date | None, today: date) -> tuple[int, bool]:
    """Return (mode, is_continuation).

    mode ==  0 -> already claimed today
    mode == -1 -> continue the streak (increment existing)
    mode >   0 -> restart the streak at this value
    """
    if last is None:
        return 1, False
    gap = (today - last).days
    if gap <= 0:
        return 0, True
    grace = get_config().int_("daily.streak.break_after_days")
    if gap <= max(1, grace):
        return -1, True
    return get_config().int_("daily.streak.grace_reset_to"), False


async def claim(player_id: int, today: date | None = None) -> DailyResult:
    """Claim today's reward. Idempotent per calendar day, enforced in SQL."""
    today = today or clock.game_today()
    cfg = get_config()

    async with db.transaction() as conn:
        # Create the row if missing, then take the row lock in one statement.
        await conn.execute(
            "INSERT INTO daily_state (player_id) VALUES ($1) ON CONFLICT DO NOTHING",
            player_id,
        )
        row = await conn.fetchrow(
            "SELECT streak, best_streak, last_claim_date FROM daily_state "
            "WHERE player_id = $1 FOR UPDATE",
            player_id,
        )
        if row is None:  # pragma: no cover - player row vanished mid-transaction
            raise ValueError(f"player {player_id} not found")

        streak = int(row["streak"])
        best = int(row["best_streak"])
        last: date | None = row["last_claim_date"]

        mode, _ = _next_streak(last, today)
        if mode == 0:
            return DailyResult(
                claimed=False,
                already_claimed=True,
                streak=streak,
                best_streak=best,
                reward_toman=0,
                reward_xp=0,
                milestone_label=None,
                milestone_toman=0,
                next_milestone=_next_milestone(streak),
            )

        new_streak = streak + 1 if mode == -1 else mode
        new_best = max(best, new_streak)

        reward_toman, reward_xp = _reward_for(new_streak)
        milestone = _milestone(new_streak)
        milestone_toman = int(milestone["toman"]) if milestone else 0
        milestone_xp = int(milestone["xp"]) if milestone else 0
        total_toman = reward_toman + milestone_toman

        await conn.execute(
            """
            UPDATE daily_state SET
                streak          = $2,
                best_streak     = $3,
                last_claim_date = $4,
                total_claims    = total_claims + 1
            WHERE player_id = $1
            """,
            player_id,
            new_streak,
            new_best,
            today,
        )

        balance = await conn.fetchval(
            """
            UPDATE players SET
                wallet_toman = wallet_toman + $2,
                happiness    = LEAST(100, happiness + $3)
            WHERE id = $1
            RETURNING wallet_toman
            """,
            player_id,
            total_toman,
            cfg.int_("daily.happiness.claim_bonus"),
        )
        if balance is None:
            raise ValueError(f"player {player_id} not found")

        await conn.execute(
            """
            INSERT INTO ledger
                (player_id, idempotency_key, reason, currency, asset_code, account,
                 amount, balance_after, metadata)
            VALUES ($1, $2, 'daily_reward', 'IRT', 'IRT', 'wallet', $3, $4, $5)
            ON CONFLICT (idempotency_key) DO NOTHING
            """,
            player_id,
            f"daily:{player_id}:{today:%Y-%m-%d}",
            total_toman,
            balance,
            {"streak": new_streak, "milestone": bool(milestone)},
        )

        return DailyResult(
            claimed=True,
            already_claimed=False,
            streak=new_streak,
            best_streak=new_best,
            reward_toman=total_toman,
            reward_xp=reward_xp + milestone_xp,
            milestone_label=str(milestone["label"]) if milestone else None,
            milestone_toman=milestone_toman,
            next_milestone=_next_milestone(new_streak),
        )


async def state(player_id: int) -> tuple[int, int, date | None]:
    row = await db.fetchrow(
        "SELECT streak, best_streak, last_claim_date FROM daily_state WHERE player_id = $1",
        player_id,
    )
    if row is None:
        return 0, 0, None
    return int(row["streak"]), int(row["best_streak"]), row["last_claim_date"]


def claimable(last: date | None, today: date | None = None) -> bool:
    today = today or clock.game_today()
    return last is None or (today - last).days >= 1


def preview(streak: int) -> int:
    """Reward the player would receive at the given streak day."""
    return _reward_for(streak)[0]


def tomorrow_preview(streak: int) -> int:
    return _reward_for(streak + 1)[0]
