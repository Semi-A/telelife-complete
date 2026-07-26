"""Coherent glass keyboard system for TeleWorld onboarding and navigation."""
from __future__ import annotations
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def b(text: str, action: str, *, primary: bool = False, success: bool = False) -> InlineKeyboardButton:
    style = "primary" if primary else "success" if success else None
    return InlineKeyboardButton(text, callback_data=f"tw:{action}", style=style)

def private(bot_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ افزودن به گروه", url=f"https://t.me/{bot_username}?startgroup=true", style="primary")],
        [b("📘 TeleWorld چطور کار می‌کند؟", "guide")],
    ])

def home(has_country: bool, is_admin: bool = False) -> InlineKeyboardMarkup:
    rows=[]
    if has_country:
        rows += [[b("🏛 کشور من", "country", primary=True), b("💼 شغل و تولید", "jobs")],
                 [b("🗳 سیاست", "politics"), b("🎁 کمک به کشور", "donate_help")]]
    elif is_admin:
        rows += [[b("🏗 ساخت کشور", "create", primary=True)], [b("📘 راهنمای شروع", "guide")]]
    else:
        rows += [[b("🤝 عضویت در کشور", "join", primary=True)], [b("📘 راهنمای شروع", "guide")]]
    rows.append([b("🔄 تازه‌سازی", "home")])
    return InlineKeyboardMarkup(rows)

def governments() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [b("🏛 جمهوری", "gov:republic", primary=True), b("👑 پادشاهی", "gov:monarchy")],
        [b("🏢 فدرال", "gov:federal"), b("🤝 شورایی", "gov:council")],
        [b("⚔️ دیکتاتوری", "gov:dictatorship"), b("لغو", "cancel")],
    ])

def cancel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[b("لغو ساخت کشور", "cancel")]])

def back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([[b("بازگشت به منوی اصلی", "home")]])
def country_actions() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
      [b("💰 کمک ۵۰ هزار تومان","donate:50000",primary=True),b("💰 کمک ۲۰۰ هزار","donate:200000")],
      [b("🗳 شروع انتخابات","election"),b("🚪 خروج از کشور","leave")],
      [b("🔄 تازه‌سازی","country"),b("بازگشت","home")],
    ])

def jobs_actions(has_job:bool) -> InlineKeyboardMarkup:
    if has_job:return InlineKeyboardMarkup([[b("📦 دریافت تولید","jcollect",success=True)],[b("⚙️ ارتقای تولید","jup:production",primary=True),b("🗄 ارتقای انبار","jup:storage")],[b("بازگشت","home")]])
    return InlineKeyboardMarkup([[b("🌾 کشاورز","job:farmer",primary=True),b("💻 برنامه‌نویس","job:programmer")],[b("📈 بازرگان","job:trader"),b("⚡ مهندس","job:engineer")],[b("بازگشت","home")]])
