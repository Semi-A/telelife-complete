"""Telegram adapters for jobs and lazy production."""

from __future__ import annotations

from telegram import Message, Update
from telegram.ext import CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import player_repo
from packages.core.services import production


async def resolve(update: Update) -> tuple[Player, Message] | None:
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return None
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    return player, message


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message is not None:
        await message.reply_text(fa.JOBS)


async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    if len(context.args) != 1:
        await message.reply_text(fa.CHOOSE_JOB_USAGE)
        return
    try:
        await production.choose(player.id, context.args[0])
    except ValueError as exc:
        await message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
        return
    await message.reply_text(fa.JOB_CHOSEN)


async def collect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    amount, earned_xp = await production.collect(
        player.id, f"collect:{player.id}:{message.message_id}"
    )
    await message.reply_text(fa.COLLECTED.format(amount=amount, xp=earned_xp))


async def upgrade(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resolved = await resolve(update)
    if resolved is None:
        return
    player, message = resolved
    if len(context.args) != 1:
        await message.reply_text(fa.UPGRADE_USAGE)
        return
    kind = context.args[0]
    try:
        level = await production.upgrade(
            player.id, kind, f"upgrade:{player.id}:{message.message_id}"
        )
    except ValueError as exc:
        await message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
        return
    await message.reply_text(fa.UPGRADED.format(kind=kind, level=level))


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
