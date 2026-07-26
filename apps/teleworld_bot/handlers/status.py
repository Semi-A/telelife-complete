"""Group activation and status for TeleWorld."""

from __future__ import annotations

from telegram import Update
from telegram.constants import ChatType
from telegram.ext import CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.repositories import group_repo, player_repo
from packages.core.utils import fmt

_GROUP_TYPES = {ChatType.GROUP, ChatType.SUPERGROUP}


async def _sync(update: Update) -> tuple[int, str] | None:
    chat = update.effective_chat
    user = update.effective_user
    if chat is None or user is None or chat.type not in _GROUP_TYPES:
        return None
    group = await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    await group_repo.link_member(group.id, player.id)
    return group.id, group.title


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is None:
        return
    synced = await _sync(update)
    if synced is None:
        await message.reply_text(fa.PRIVATE_ONLY)
        return
    group_id, title = synced
    from packages.core import db

    members = await db.fetchval(
        "SELECT count(*) FROM group_members WHERE group_id = $1", group_id
    )
    await message.reply_text(
        fa.STATUS.format(title=title, members=fmt.number(int(members or 0)))
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(fa.HELP)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("help", help_command))