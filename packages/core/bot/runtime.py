"""Shared bot bootstrap: polling and webhook from one code path."""

from __future__ import annotations

import asyncio
import logging
import signal
from collections.abc import Callable

from telegram.ext import AIORateLimiter, Application, ApplicationBuilder, Defaults

from packages.core import db
from packages.core.config import get_config
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import RunMode, Service, Settings, get_settings

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


async def _startup(settings: Settings) -> None:
    await db.create_pool(settings)
    await migrate()


async def _shutdown() -> None:
    await db.close_pool()


def run_bot(service: Service, register: RegisterFn) -> None:
    """Entrypoint used by both bots. Blocking; handles its own event loop."""
    settings = get_settings()
    setup_logging(service.value, settings.log_level)

    async def post_init(app: Application) -> None:
        await _startup(settings)
        logger.info("%s ready in %s mode", service.value, settings.run_mode.value)

    async def post_shutdown(app: Application) -> None:
        await _shutdown()

    application = build_application(settings, service)
    application.post_init = post_init
    application.post_shutdown = post_shutdown
    register(application)

    if settings.run_mode is RunMode.WEBHOOK:
        application.run_webhook(
            listen=settings.host,
            port=settings.port,
            url_path=f"telegram/{service.value}",
            webhook_url=settings.webhook_url(service),
            secret_token=settings.webhook_secret or None,
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query", "my_chat_member"],
        )
    else:
        application.run_polling(
            drop_pending_updates=True,
            allowed_updates=["message", "callback_query", "my_chat_member"],
            stop_signals=(signal.SIGINT, signal.SIGTERM),
        )