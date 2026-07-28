"""Shared handler plumbing: player resolution, guards, panel sending."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape

from telegram import Message, Update
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from apps.telelife_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import player_repo
from packages.core.ui import Callback, schedule_cleanup


@dataclass(slots=True, frozen=True)
class Ctx:
    player: Player
    message: Message
    telegram_id: int


async def resolve(update: Update) -> Ctx | None:
    """Fetch-or-create the player and reject unplayable accounts."""
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return None

    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "رفیق",
        language_code=user.language_code or "fa",
    )

    if not player.playable:
        text = (
            fa.BANNED.format(reason=escape(player.ban_reason or fa.NO_REASON))
            if player.is_banned
            else fa.FROZEN
        )
        await message.reply_text(text)
        return None

    return Ctx(player=player, message=message, telegram_id=user.id)


async def guard_callback(update: Update) -> Callback | None:
    """Reject taps on someone else's panel without touching the database."""
    query = update.callback_query
    if query is None or query.data is None:
        return None
    parsed = Callback.parse(query.data)
    if parsed is None:
        await query.answer(fa.PANEL_EXPIRED, show_alert=True)
        return None
    if not parsed.owned_by(query.from_user.id):
        await query.answer(fa.NOT_YOUR_PANEL, show_alert=True)
        return None
    player = await player_repo.get_by_telegram_id(query.from_user.id)
    if player is not None:
        from packages.core import db
        valid = await db.fetchval("""SELECT life_expires_at>now() FROM player_ui_state
          WHERE player_id=$1 AND life_chat_id=$2 AND life_message_id=$3""",
          player.id, query.message.chat_id if query.message else 0,
          query.message.message_id if query.message else 0)
        if valid is False:
            await query.answer("⌛ این پنل منقضی شده است؛ /start را بزن تا پنل تازه باز شود.",show_alert=True)
            return None
    return parsed


async def send_panel(
    context: ContextTypes.DEFAULT_TYPE,
    message: Message,
    text: str,
    markup,  # type: ignore[no-untyped-def]
    panel: str,
    *,
    edit: bool = False,
) -> None:
    """Send or edit a panel and arm its auto-cleanup timer."""
    if edit:
        try:
            sent = await message.edit_text(text, reply_markup=markup)
        except BadRequest as exc:
            # Double taps and refreshes can legitimately produce an identical panel.
            # Telegram rejects that no-op with HTTP 400; it is not an application error.
            if "message is not modified" not in str(exc).lower():
                raise
            target = message
        else:
            target = sent if isinstance(sent, Message) else message
    else:
        target = await message.reply_text(text, reply_markup=markup)
    schedule_cleanup(context, target, panel)
