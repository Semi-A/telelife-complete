"""Shared bot bootstrap: polling and webhook from one code path."""

from __future__ import annotations

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


async def _post_init(app: Application, settings: Settings, service: Service) -> None:
    await db.create_pool(settings)
    await migrate()
    logger.info("%s ready in %s mode", service.value, settings.run_mode.value)


async def _post_shutdown(app: Application) -> None:
    await db.close_pool()


def build_application(settings: Settings, service: Service) -> Application:
    cfg = get_config()
    defaults = Defaults(parse_mode="HTML", block=False)
    return (
        ApplicationBuilder()
        .token(settings.token_for(service))
        .post_init(lambda app: _post_init(app, settings, service))
        .post_shutdown(_post_shutdown)
        .defaults(defaults)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(cfg.int_("core.telegram.concurrent_updates"))
        .connect_timeout(cfg.float_("core.telegram.connect_timeout"))
        .read_timeout(cfg.float_("core.telegram.read_timeout"))
        .build()
    )


def run_bot(service: Service, register: RegisterFn) -> None:
    """Entrypoint used by both bots. Blocking; handles its own event loop."""
    settings = get_settings()
    setup_logging(service.value, settings.log_level)

    application = build_application(settings, service)
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
