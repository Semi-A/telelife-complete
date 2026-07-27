"""Shared Telegram application construction and supervised polling lifecycle."""
from __future__ import annotations

import asyncio
import logging
from collections.abc import Callable

from telegram.ext import AIORateLimiter, Application, ApplicationBuilder, Defaults

from packages.core.config import get_config
from packages.core.settings import Service, Settings, get_settings

from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging

logger = logging.getLogger(__name__)
RegisterFn = Callable[[Application], None]


def build_application(settings: Settings, service: Service) -> Application:
    cfg = get_config()
    defaults = Defaults(parse_mode="HTML", block=False)
    return (
        ApplicationBuilder()
        .token(settings.token_for(service))
        .defaults(defaults)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(cfg.int_("core.telegram.concurrent_updates"))
        .connect_timeout(cfg.float_("core.telegram.connect_timeout"))
        .read_timeout(cfg.float_("core.telegram.read_timeout"))
        .build()
    )


class PollingService:
    """Owns one Telegram Application without owning the process event loop."""

    def __init__(self, settings: Settings, service: Service, register: RegisterFn) -> None:
        self.application = build_application(settings, service)
        register(self.application)
        self.service = service

    def healthy(self) -> bool:
        updater = self.application.updater
        return bool(self.application.running and updater and updater.running)

    async def run(self, stop: asyncio.Event) -> None:
        app = self.application
        updater = app.updater
        if updater is None:
            raise RuntimeError(f"{self.service.value} updater is unavailable")
        try:
            await app.initialize()
            # The supervisor owns the lifecycle, so invoke the framework hook explicitly.
            # This clears legacy slash-command menus before polling starts.
            if app.post_init is not None:
                await app.post_init(app)
            await app.start()
            await updater.start_polling(
                drop_pending_updates=True,
                allowed_updates=["message", "callback_query", "my_chat_member"],
            )
            logger.info("%s polling started", self.service.value)
            await stop.wait()
        finally:
            if updater.running:
                await updater.stop()
            if app.running:
                await app.stop()
            await app.shutdown()
            logger.info("%s polling stopped", self.service.value)


def run_bot(service: Service, register: RegisterFn) -> None:
    """Backward-compatible standalone entrypoint; production uses the supervisor."""
    async def standalone() -> None:
        settings = get_settings()
        setup_logging(service.value, settings.log_level)
        await db.create_pool(settings)
        await migrate()
        stop = asyncio.Event()
        polling = PollingService(settings, service, register)
        try:
            await polling.run(stop)
        finally:
            await db.close_pool()
    asyncio.run(standalone())