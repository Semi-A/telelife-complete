"""TeleLife's single live panel.

Normal navigation edits the active message. A deliberate /start creates a fresh
panel and retires the previous keyboard first, so stale controls cannot mutate
state or clutter the conversation.
"""
from __future__ import annotations
from packages.core.utils.message_text import plain_text

import logging
from telegram import Message
from telegram.error import BadRequest, Forbidden
from telegram.ext import ContextTypes

from packages.core.repositories import ui_state_repo
from packages.core.ui import schedule_cleanup

logger = logging.getLogger(__name__)

_EDIT_GONE = ("message to edit not found", "message can't be edited", "message_id_invalid")


async def _retire_remembered(context: ContextTypes.DEFAULT_TYPE, state, fallback_chat_id: int) -> None:
    """Remove controls from the former panel; failure must never block /start."""
    if not state or not state["life_message_id"]:
        return
    try:
        await context.bot.edit_message_text(
            chat_id=int(state["life_chat_id"] or fallback_chat_id),
            message_id=int(state["life_message_id"]),
            text="🔒 بسته شد",
            reply_markup=None,
        )
    except (BadRequest, Forbidden) as exc:
        logger.debug("old TeleLife panel already unavailable: %s", exc)


async def retire_message(message: Message) -> None:
    """Best-effort lock for a stale callback message."""
    try:
        await message.edit_reply_markup(reply_markup=None)
    except (BadRequest, Forbidden):
        return


async def show(
    context: ContextTypes.DEFAULT_TYPE,
    player_id: int,
    chat_id: int,
    text: str,
    markup,
    *,
    message: Message | None = None,
    force_new: bool = False,
):
    text = plain_text(text)
    state = await ui_state_repo.ensure_life(player_id)
    target: Message | None = None

    if force_new:
        await _retire_remembered(context, state, chat_id)
    elif message is not None and getattr(message, "message_id", None):
        try:
            result = await message.edit_text(text, reply_markup=markup)
            target = result if isinstance(result, Message) else message
        except BadRequest as exc:
            detail = str(exc).lower()
            if "message is not modified" in detail:
                target = message
            elif not any(token in detail for token in _EDIT_GONE):
                raise

    if not force_new and target is None and state and state["life_message_id"]:
        try:
            result = await context.bot.edit_message_text(
                chat_id=int(state["life_chat_id"] or chat_id),
                message_id=int(state["life_message_id"]),
                text=text,
                reply_markup=markup,
            )
            target = result if isinstance(result, Message) else None
        except (BadRequest, Forbidden):
            target = None

    if target is None:
        target = await context.bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)

    message_id = target.message_id if target else int(state["life_message_id"])
    await ui_state_repo.set_life_panel(player_id, chat_id, message_id)
    if target is not None:
        schedule_cleanup(context, target, "profile")
    return target
