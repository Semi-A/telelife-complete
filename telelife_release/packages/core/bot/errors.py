"""Global error handler - never let a traceback reach the player."""

from __future__ import annotations

import logging
from typing import Any

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


def make_error_handler(user_message: str) -> Any:
    async def handle(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logger.error("unhandled error", exc_info=context.error)
        if not isinstance(update, Update):
            return
        chat = update.effective_chat
        if chat is None:
            return
        try:
            await context.bot.send_message(chat.id, user_message)
        except Exception:
            logger.warning("failed to deliver error notice to chat %s", chat.id)

    return handle