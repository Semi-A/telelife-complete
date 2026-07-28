"""Outbox publisher with leases, retries and deterministic daily catch-up."""

from __future__ import annotations

import hashlib
import logging
from collections.abc import Awaitable, Callable
from datetime import date, timedelta
from typing import Any
from uuid import uuid4

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import outbox_repo
from packages.core.settings import get_settings
from packages.core.utils import clock

logger = logging.getLogger(__name__)

Sender = Callable[[int | None, str, dict[str, Any]], Awaitable[None]]

EVENT_TEXTS: dict[str, str] = {
    "harvest_boom": "🌾 رونق برداشت\n\nامروز تولید محصولات کشاورزی ۲۰٪ بیشتر است و این اثر تا ۲۴ ساعت ادامه دارد.",
    "mining_surge": "⛏ رونق استخراج\n\nامروز تولید مواد معدنی ۲۰٪ بیشتر است و این اثر تا ۲۴ ساعت ادامه دارد.",
    "energy_wave": "⚡ موج انرژی\n\nامروز تولید انرژی ۱۵٪ بیشتر است و این اثر تا ۲۴ ساعت ادامه دارد.",
    "technology_rush": "🔬 جهش فناوری\n\nامروز تولید فناوری ۱۵٪ بیشتر است و این اثر تا ۲۴ ساعت ادامه دارد.",
    "market_day": "💱 روز پررونق بازار\n\nامروز تولید ارزی ۱۰٪ بیشتر است و این اثر تا ۲۴ ساعت ادامه دارد.",
}

def daily_event_text(code: object) -> str:
    return EVENT_TEXTS.get(str(code), "📢 رویداد تازه‌ای در جهان آغاز شده است؛ جزئیات آن را در پنل کشور ببینید.")


def _backoff(delays: list[int], attempts: int) -> int:
    """Delay for the next retry. `attempts` is already incremented by claim()."""
    if not delays:
        return 60
    index = min(max(attempts - 1, 0), len(delays) - 1)
    return int(delays[index])


async def publish_batch(sender: Sender) -> dict[str, int]:
    """Claim a batch, deliver each row, then settle it. One row cannot poison
    the batch: every outcome is committed on its own."""
    cfg = get_config()
    token = uuid4()
    stats = {"published": 0, "failed": 0}

    async with db.transaction() as conn:
        rows = await outbox_repo.claim(
            conn,
            token,
            cfg.int_("news.outbox.claim_batch_size"),
            cfg.int_("news.outbox.claim_lease_seconds"),
            cfg.int_("news.outbox.maximum_attempts"),
        )

    delays = [int(x) for x in cfg.get("news.outbox.retry_backoff_seconds", [60])]

    for row in rows:
        try:
            await sender(row["destination_chat_id"], row["event_type"], row["payload"])
        except Exception as exc:  # noqa: BLE001 - one bad row must not stop the rest
            logger.warning(
                "outbox delivery failed",
                extra={"extra_fields": {"row_id": row["id"], "error": repr(exc)}},
            )
            delay = _backoff(delays, int(row["attempts"]))
            async with db.transaction() as conn:
                await outbox_repo.failed(
                    conn, row["id"], token, type(exc).__name__[:64], delay
                )
            stats["failed"] += 1
        else:
            async with db.transaction() as conn:
                await outbox_repo.published(conn, row["id"], token)
            stats["published"] += 1

    return stats


def _pick_event(weighted: list[tuple[str, int]], day: date, namespace: str) -> str:
    """Deterministic weighted pick for a given day."""
    total = sum(weight for _, weight in weighted)
    digest = hashlib.sha256(f"{namespace}:{day}".encode()).digest()
    roll = int.from_bytes(digest[:4], "big") % total
    for code, weight in weighted:
        if roll < weight:
            return code
        roll -= weight
    return weighted[-1][0]


async def ensure_daily_events(today: date | None = None) -> int:
    """Materialise the daily event for each recent day. Returns how many were
    newly created."""
    cfg = get_config()
    end = today or clock.game_today()
    span = cfg.int_("daily_events.scheduler.catch_up_days")
    start = end - timedelta(days=span - 1)

    events = cfg.section("daily_events.events")
    weighted = sorted((str(k), int(v["weight"])) for k, v in events.items())
    if not weighted or sum(w for _, w in weighted) <= 0:
        raise ValueError("daily_events_pool_empty")

    namespace = cfg.get(
        "daily_events.scheduler.deterministic_seed_namespace", "daily_events"
    )
    destination = get_settings().global_news_chat_id
    created = 0

    for offset in range((end - start).days + 1):
        day = start + timedelta(days=offset)
        code = _pick_event(weighted, day, namespace)
        spec = events[code]
        async with db.transaction() as conn:
            if await outbox_repo.create_event(conn, day, code, spec):
                await outbox_repo.enqueue(
                    conn,
                    f"daily-event:{day}",
                    "daily_event",
                    {"event_date": str(day), "event_code": code, "effect": spec, "text": daily_event_text(code)},
                    destination,
                )
                created += 1

    return created
