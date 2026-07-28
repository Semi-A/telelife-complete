"""Minimal, cached TeleWorld permission policy.

Only administrator status and message deletion are required. Editing messages sent by
this bot needs no administrator grant; citizenship is explicit and does not consume
Telegram member events. Dangerous grants such as adding administrators are never asked.
"""
from __future__ import annotations
import time
from dataclasses import dataclass
from telegram.constants import ChatMemberStatus
from packages.core.repositories import world_access_repo

_CACHE_TTL = 20.0
_cache: dict[int, tuple[float, "Access"]] = {}

@dataclass(frozen=True, slots=True)
class Access:
    administrator: bool
    can_delete_messages: bool
    missing: tuple[str, ...]

    @property
    def ready(self) -> bool:
        return not self.missing

    @property
    def fingerprint(self) -> str:
        return ",".join(self.missing) or "ready"

    def missing_fa(self) -> str:
        names = {"administrator": "مدیر بودن بات", "delete_messages": "حذف پیام‌ها"}
        return "، ".join(names.get(item, item) for item in self.missing)

async def check(bot, chat_id: int, *, force: bool = False) -> Access:
    now = time.monotonic()
    cached = _cache.get(chat_id)
    if not force and cached and now - cached[0] < _CACHE_TTL:
        return cached[1]
    me = await bot.get_me()
    member = await bot.get_chat_member(chat_id, me.id)
    administrator = member.status in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}
    can_delete = administrator and bool(getattr(member, "can_delete_messages", False))
    missing: list[str] = []
    if not administrator:
        missing.append("administrator")
    elif not can_delete:
        missing.append("delete_messages")
    result = Access(administrator, can_delete, tuple(missing))
    _cache[chat_id] = (now, result)
    await world_access_repo.save_access(chat_id, administrator, can_delete, missing)
    return result

def invalidate(chat_id: int) -> None:
    _cache.pop(chat_id, None)
