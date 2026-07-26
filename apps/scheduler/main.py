"""Scheduler for minute-resolution and daily idempotent maintenance."""

from __future__ import annotations

import asyncio
import logging
import signal
from datetime import UTC, datetime, timedelta

from telegram import Bot

from apps.scheduler.jobs import country_jobs, daily_reset
from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import Service, get_settings

logger = logging.getLogger(__name__)


async def minute_loop(stop: asyncio.Event, bot: Bot) -> None:
    while not stop.is_set():
        try:
            await db.execute("DELETE FROM cooldowns WHERE expires_at < now()")
            await country_jobs.resolve_due()
            await country_jobs.publish_news(bot)
        except Exception:
            logger.exception("minute jobs failed")
        try:
            await asyncio.wait_for(stop.wait(), timeout=60)
        except TimeoutError:
            continue


def seconds_until_daily() -> float:
    now = datetime.now(UTC)
    target = (now + timedelta(days=1)).replace(
        hour=0, minute=10, second=0, microsecond=0
    )
    return max(1.0, (target - now).total_seconds())


async def daily_loop(stop: asyncio.Event) -> None:
    while not stop.is_set():
        try:
            await asyncio.wait_for(stop.wait(), timeout=seconds_until_daily())
            return
        except TimeoutError:
            logger.debug("daily maintenance window reached")
        try:
            await daily_reset.run()
            await country_jobs.daily_events()
        except Exception:
            logger.exception("daily jobs failed")


async def run() -> None:
    settings = get_settings()
    setup_logging(Service.SCHEDULER.value, settings.log_level)
    await db.create_pool(settings)
    await migrate()
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, stop.set)
        except NotImplementedError:
            logger.debug("signal handlers are unavailable on this event loop")
    try:
        async with Bot(settings.teleworld_bot_token) as bot:
            await asyncio.gather(minute_loop(stop, bot), daily_loop(stop))
    finally:
        await db.close_pool()


def main() -> None:
    asyncio.run(run())


if __name__ == "__main__":
    main()
