"""Supervised scheduler with isolated minute and daily background jobs."""
from __future__ import annotations

import asyncio
import logging
from datetime import UTC, datetime, timedelta

from telegram import Bot

from apps.scheduler.jobs import country_jobs, daily_reset
from packages.core import db
from packages.core.repositories import admin_repo
from packages.core.settings import Settings
from packages.core.services import usd_market, live_market, scheduler_ops, engagement, country_realism, country_economy_b, country_trade, action_outbox, maintenance

logger = logging.getLogger(__name__)


def seconds_until_daily() -> float:
    now = datetime.now(UTC)
    target = (now + timedelta(days=1)).replace(hour=0, minute=10, second=0, microsecond=0)
    return max(1.0, (target - now).total_seconds())


async def _sleep_or_stop(stop: asyncio.Event, seconds: float) -> bool:
    try:
        await asyncio.wait_for(stop.wait(), timeout=seconds)
        return True
    except TimeoutError:
        return False


class SchedulerService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._running = False
        self._heartbeat = 0.0

    def healthy(self) -> bool:
        return self._running

    async def minute_loop(self, stop: asyncio.Event, bot: Bot, life_bot: Bot) -> None:
        while not stop.is_set():
            try:
                jobs = (
                    ("cooldown_cleanup", lambda: db.execute("DELETE FROM cooldowns WHERE expires_at < now()")),
                    ("elections", country_jobs.resolve_due),
                    ("legacy_ads", country_jobs.queue_due_ads),
                    ("commerce", country_jobs.run_commerce),
                    ("country_trade_expiry", country_trade.expire_due),
                    ("country_relation_expiry", country_trade.expire_relations),
                    ("publish_news", lambda: country_jobs.publish_news(bot, life_bot)),
                    ("telegram_actions", lambda: action_outbox.deliver_batch(life_bot, bot)),
                    ("maintenance", maintenance.minute_tick),
                    ("zipodo_rate", live_market.sync),
                    ("engagement", engagement.minute_tick),
                    ("market_snapshot", admin_repo.capture_market_snapshot),
                )
                for name, job in jobs:
                    if stop.is_set(): break
                    await scheduler_ops.run(name, job)
                self._heartbeat = asyncio.get_running_loop().time()
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("minute loop infrastructure failed; next cycle remains scheduled")
            await _sleep_or_stop(stop, 60)

    async def daily_loop(self, stop: asyncio.Event) -> None:
        while not stop.is_set():
            if await _sleep_or_stop(stop, seconds_until_daily()):
                return
            try:
                await daily_reset.run()
                await usd_market.daily_rollover()
                await country_jobs.daily_events()
                await scheduler_ops.run("country_economy_b", country_economy_b.catch_up)
                await scheduler_ops.run("country_realism", country_realism.daily_tick)
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("daily jobs failed; scheduler remains active")

    async def run(self, stop: asyncio.Event) -> None:
        self._running = True
        try:
            async with Bot(self.settings.teleworld_bot_token) as bot, Bot(self.settings.telelife_bot_token) as life_bot:
                minute = asyncio.create_task(self.minute_loop(stop, bot, life_bot), name="scheduler:minute")
                daily = asyncio.create_task(self.daily_loop(stop), name="scheduler:daily")
                stop_waiter = asyncio.create_task(stop.wait(), name="scheduler:stop")
                done, _ = await asyncio.wait(
                    {minute, daily, stop_waiter}, return_when=asyncio.FIRST_COMPLETED
                )
                if stop_waiter not in done:
                    for task in done:
                        if task is not stop_waiter:
                            exc = task.exception()
                            if exc:
                                raise exc
                            raise RuntimeError(f"{task.get_name()} exited unexpectedly")
                for task in (minute, daily, stop_waiter):
                    if not task.done():
                        task.cancel()
                await asyncio.gather(minute, daily, stop_waiter, return_exceptions=True)
        finally:
            self._running = False
