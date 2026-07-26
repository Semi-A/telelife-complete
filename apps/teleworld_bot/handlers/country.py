"""Telegram adapters for country and economy commands."""

from __future__ import annotations

from dataclasses import dataclass

from telegram import Chat, Message, Update, User
from telegram.constants import ChatMemberStatus, ChatType
from telegram.ext import CommandHandler, ContextTypes

from apps.teleworld_bot.texts import fa
from packages.core.models import Player
from packages.core.repositories import country_repo, player_repo
from packages.core.services import country as country_service
from packages.core.services import country_missions, economy

_GROUP_TYPES = {ChatType.GROUP, ChatType.SUPERGROUP}


@dataclass(frozen=True, slots=True)
class GroupContext:
    chat: Chat
    user: User
    message: Message
    player: Player


async def resolve_group(update: Update) -> GroupContext | None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    if chat is None or user is None or message is None or chat.type not in _GROUP_TYPES:
        if message is not None:
            await message.reply_text(fa.PRIVATE_ONLY)
        return None
    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "شهروند",
        language_code=user.language_code or "fa",
    )
    return GroupContext(chat, user, message, player)


async def create(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    member = await context.bot.get_chat_member(ctx.chat.id, ctx.user.id)
    if member.status not in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}:
        await ctx.message.reply_text(fa.ADMIN_REQUIRED)
        return
    parts = [part.strip() for part in " ".join(context.args).split("|")]
    if len(parts) != 3:
        await ctx.message.reply_text(fa.CREATE_USAGE)
        return
    try:
        row = await country_service.create_country(
            chat_id=ctx.chat.id,
            chat_title=ctx.chat.title or "",
            player_id=ctx.player.id,
            name=parts[0],
            government=parts[1].lower(),
            description=parts[2],
        )
    except ValueError as exc:
        await ctx.message.reply_text(fa.INVALID_INPUT.format(reason=str(exc)))
        return
    await ctx.message.reply_text(fa.COUNTRY_CREATED.format(name=row["name"]))


async def join(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    await country_service.join_country(chat_id=ctx.chat.id, player_id=ctx.player.id)
    await ctx.message.reply_text(fa.COUNTRY_JOINED)


async def show(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    row = await country_repo.by_chat(ctx.chat.id)
    if row is None:
        await ctx.message.reply_text(fa.COUNTRY_MISSING)
        return
    await ctx.message.reply_text(
        fa.COUNTRY_STATUS.format(
            name=row["name"],
            description=row["description"],
            government=row["government_type"],
            treasury=row["treasury_toman"],
        )
    )


async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve_group(update)
    if ctx is None:
        return
    if len(context.args) != 2:
        await ctx.message.reply_text(fa.DONATE_USAGE)
        return
    try:
        amount = int(context.args[1])
    except ValueError:
        await ctx.message.reply_text(fa.INVALID_AMOUNT)
        return
    asset = context.args[0]
    country = await country_repo.by_chat(ctx.chat.id)
    if country is None:
        await ctx.message.reply_text(fa.COUNTRY_MISSING)
        return
    await economy.transfer(
        player_id=ctx.player.id,
        country_id=country["id"],
        asset=asset,
        amount=amount,
        reason="country_donation",
        idempotency_key=f"donate:{ctx.message.message_id}:{ctx.player.id}",
    )
    await country_missions.report(country["id"], "donate", asset, amount)
    await ctx.message.reply_text(fa.DONATED.format(amount=amount, asset=asset))


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) != 1:
        message = update.effective_message
        if message is not None:
            await message.reply_text(fa.TAX_USAGE)
        return
    context.args = ["IRT", context.args[0]]
    await donate(update, context)


def register(application) -> None:  # type: ignore[no-untyped-def]
    for command, handler in (
        ("createcountry", create),
        ("joincountry", join),
        ("country", show),
        ("economy", show),
        ("resources", show),
        ("donate", donate),
        ("paytax", tax),
    ):
        application.add_handler(CommandHandler(command, handler))
