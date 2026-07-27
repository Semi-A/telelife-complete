"""Auto-expiring interactive panels.

Every panel schedules its own cleanup via the PTB job queue. Timeouts come from
`core.menu_cleanup` in config - nothing hardcoded. On expiry the keyboard is
stripped, not the message: the player keeps the information, we free the
callback surface.
"""

from __future__ import annotations

import logging

from telegram import Message
from telegram.error import BadRequest, Forbidden
from telegram.ext import ContextTypes

from packages.core.config import get_config

logger = logging.getLogger(__name__)


def timeout_for(panel: str) -> int:
    cfg = get_config()
    default = cfg.int_("core.menu_cleanup.default_timeout_seconds")
    return int(cfg.section("core.menu_cleanup").get("panels", {}).get(panel, default))


async def _expire(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    if job is None or not isinstance(job.data, dict):
        return
    chat_id = job.data["chat_id"]
    message_id = job.data["message_id"]
    try:
        await context.bot.edit_message_reply_markup(
            chat_id=chat_id, message_id=message_id, reply_markup=None
        )
    except BadRequest as exc:
        logger.debug("panel cleanup no-op for chat %s: %s", chat_id, exc)
    except Forbidden:
        logger.info("panel cleanup skipped: bot removed from chat %s", chat_id)


def schedule_cleanup(
    context: ContextTypes.DEFAULT_TYPE, message: Message, panel: str
) -> None:
    """Arm auto-cleanup for a panel, replacing any previous timer on it."""
    if not get_config().bool_("core.menu_cleanup.enabled"):
        return
    if context.job_queue is None:
        return

    name = f"panel:{message.chat_id}:{message.message_id}"
    for existing in context.job_queue.get_jobs_by_name(name):
        existing.schedule_removal()

    context.job_queue.run_once(
        _expire,
        when=timeout_for(panel),
        name=name,
        data={"chat_id": message.chat_id, "message_id": message.message_id},
    )