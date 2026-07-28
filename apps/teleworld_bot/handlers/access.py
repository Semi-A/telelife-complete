"""Telegram my_chat_member lifecycle and the TeleWorld permission gate."""
from __future__ import annotations
from html import escape
from telegram import Update
from telegram.constants import ChatMemberStatus, ChatType
from telegram.error import BadRequest, Forbidden
from telegram.ext import ChatMemberHandler, ContextTypes
from apps.teleworld_bot import keyboards as kb
from packages.core.repositories import group_repo, world_access_repo
from packages.core.services import world_access

GROUPS = {ChatType.GROUP, ChatType.SUPERGROUP}
ACTIVE = {ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}
INACTIVE = {ChatMemberStatus.LEFT, ChatMemberStatus.BANNED}

async def lifecycle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    change = update.my_chat_member
    if not change or change.chat.type not in GROUPS:
        return
    chat = change.chat
    old_status = change.old_chat_member.status
    new_status = change.new_chat_member.status
    active = new_status in ACTIVE
    await world_access_repo.membership(chat.id, chat.title or "سرزمین بی‌نام", new_status, active)
    world_access.invalidate(chat.id)
    if not active:
        await world_access_repo.audit(
            f"bot-membership:{chat.id}:{change.date.isoformat()}:{new_status}", "bot_removed",
            chat_id=chat.id, details={"status": new_status},
        )
        return
    await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    access = await world_access.check(context.bot, chat.id, force=True)
    await world_access_repo.audit(
        f"bot-membership:{chat.id}:{change.date.isoformat()}:{new_status}",
        "bot_added" if old_status in INACTIVE else "bot_access_changed",
        chat_id=chat.id, details={"ready": access.ready, "missing": list(access.missing)},
    )
    if old_status in INACTIVE and await world_access_repo.claim_welcome(chat.id):
        state = "✅ دسترسی لازم کامل است." if access.ready else f"⚠️ دسترسی ناقص: {access.missing_fa()}"
        text = (
            f"🌍 به {escape(chat.title or 'این گروه')} خوش آمدم\n\n"
            "اینجا می‌توانید کشور، شهروندی، اقتصاد عمومی، انتخابات و پروژه ملی بسازید.\n\n"
            f"{state}"
        )
        sent = await context.bot.send_message(chat.id, text, reply_markup=kb.access(access.ready))
        await world_access_repo.set_welcome_message(chat.id, sent.message_id)
    elif not access.ready and await world_access_repo.claim_warning(chat.id, access.fingerprint):
        try:
            await context.bot.send_message(
                chat.id, f"🔒 دسترسی بات تغییر کرده و عملیات کشور قفل شد.\nکمبود: {access.missing_fa()}",
                reply_markup=kb.access(False),
            )
        except (BadRequest, Forbidden):
            return

def register(app) -> None:
    app.add_handler(ChatMemberHandler(lifecycle, ChatMemberHandler.MY_CHAT_MEMBER), group=-10)