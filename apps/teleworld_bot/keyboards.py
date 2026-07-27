"""رابط دکمه‌ای فارسی جهان؛ رنگ فقط برای یک اقدام اصلی در هر صفحه است."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def b(text, action, style=None):
    kwargs = {"text": text, "callback_data": f"tw:{action}"}
    if style:
        kwargs["style"] = style
    return InlineKeyboardButton(**kwargs)

def private(username):
    return InlineKeyboardMarkup([[InlineKeyboardButton("➕ افزودن به گروه", url=f"https://t.me/{username}?startgroup=true", style="primary")], [b("📘 راهنمای استفاده", "guide")]])

def home(country, admin, citizen=False):
    if country:
        rows = [[b("🏛 شناسنامه کشور", "country", "primary"), b("👥 شهروندان", "citizens")],
                [b("💰 اقتصاد و منابع", "economy"), b("🗳 سیاست و انتخابات", "politics")], [b("🏗 پروژه ملی", "project")]]
        rows.append([b("🚪 خروج از شهروندی", "leave", "danger")] if citizen else [b("🤝 شهروند این کشور می‌شوم", "join", "success")])
        rows.append([b("📘 راهنمای همین مرحله", "guide"), b("🔄 تازه‌سازی", "home")])
        return InlineKeyboardMarkup(rows)
    if admin:
        return InlineKeyboardMarkup([[b("🏗 ساخت کشور", "create", "primary")], [b("📘 راهنمای ساخت کشور", "guide")], [b("🔄 تازه‌سازی", "home")]])
    return InlineKeyboardMarkup([[b("📘 برای ساخت کشور چه کنیم؟", "guide", "primary")], [b("🔄 تازه‌سازی", "home")]])

def governments():
    return InlineKeyboardMarkup([[b("🏛 جمهوری", "gov:republic", "primary"), b("👑 پادشاهی", "gov:monarchy")],
                                 [b("🤝 شورایی", "gov:council"), b("🏢 فدرال", "gov:federal")], [b("لغو ساخت کشور", "home")]])

def country():
    return InlineKeyboardMarkup([[b("💰 کمک ۵۰ هزار تومان", "donate:50000", "success"), b("💰 کمک ۲۰۰ هزار تومان", "donate:200000")],
                                 [b("🗳 انتخابات", "politics", "primary"), b("👥 شهروندان", "citizens")], [b("🏠 خانه جهان", "home")]])

def politics(status=None):
    if status == "nominations":
        rows = [[b("🙋 نامزد می‌شوم", "nominate", "primary")], [b("⏳ زمان رأی‌گیری هنوز نرسیده", "politics")]]
    elif status == "voting":
        rows = [[b("🗳 انتخاب نامزد", "votehelp", "primary")]]
    else:
        rows = [[b("🗳 آغاز انتخابات", "estart", "primary")]]
    rows.append([b("📊 نظرسنجی‌ها", "polls"), b("🏠 خانه جهان", "home")])
    return InlineKeyboardMarkup(rows)

def back(action="home"):
    return InlineKeyboardMarkup([[b("🏠 خانه جهان", action, "primary")]])
def cancel(): return back()
def candidates(rows):
    buttons = [[b(f"🗳 رأی به {row['first_name']}", f"vote:{row['player_id']}", "primary" if i == 0 else None)] for i, row in enumerate(rows)]
    buttons.append([b("↩️ بازگشت", "politics")])
    return InlineKeyboardMarkup(buttons)
def project(active):
    if active:
        return InlineKeyboardMarkup([[b("💵 کمک ۵۰ هزار تومان", "pcon:IRT:50000", "success")],
                                     [b("🌾 کمک ۵۰ غذا", "pcon:food:50"), b("⛏ کمک ۵۰ ماده معدنی", "pcon:minerals:50")], [b("🏠 خانه جهان", "home")]])
    return InlineKeyboardMarkup([[b("🏗 آغاز پروژه ملی", "pstart", "primary")], [b("🏠 خانه جهان", "home")]])
