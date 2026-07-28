"""تله‌ورلد onboarding, group activation and status commands."""

from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ChatType
from telegram.ext import CallbackQueryHandler, CommandHandler, ContextTypes

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


def _private_menu(bot_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "➕ افزودن تله‌ورلد به گروه",
            url=f"https://t.me/{bot_username}?startgroup=true",
            style="primary",
        )],
        [InlineKeyboardButton("📚 مشاهده راهنما", callback_data="tw:help")],
    ])


def _group_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🌍 وضعیت گروه", callback_data="tw:status", style="primary"),
            InlineKeyboardButton("💼 فهرست شغل‌ها", callback_data="tw:jobs"),
        ],
        [InlineKeyboardButton("📚 راهنمای دستورات", callback_data="tw:help")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Always acknowledge /start and direct users to the correct game context."""
    message = update.effective_message
    chat = update.effective_chat
    if message is None or chat is None:
        return

    if chat.type in _GROUP_TYPES:
        await _sync(update)
        await message.reply_text(fa.START_GROUP, reply_markup=_group_menu())
        return

    username = context.bot.username or ""
    markup = _private_menu(username) if username else None
    await message.reply_text(fa.START_PRIVATE, reply_markup=markup)


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
        fa.STATUS.format(title=title, members=fmt.number(int(members or 0))),
        reply_markup=_group_menu(),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(
            fa.HELP,
            reply_markup=_group_menu()
            if update.effective_chat and update.effective_chat.type in _GROUP_TYPES
            else None,
        )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query is None:
        return
    await query.answer()
    action = (query.data or "").removeprefix("tw:")
    if action == "status":
        await status(update, context)
    elif action == "jobs":
        await query.message.reply_text(fa.JOBS, reply_markup=_group_menu())
    elif action == "help":
        await query.message.reply_text(fa.HELP)


def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return
