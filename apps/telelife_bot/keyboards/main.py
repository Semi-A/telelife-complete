"""صفحه‌کلیدهای فارسی بات زندگی؛ در هر صفحه فقط یک اقدام اصلی داریم."""
from telegram import InlineKeyboardMarkup
from packages.core.ui import Keyboard, Style, button, cb

NS = "tl"

def B(text, action, owner, arg="", style=Style.GLASS):
    return button(text, cb(NS, action, owner, arg), style=style)

def home(owner: int, daily_ready: bool, onboarding: int = 4) -> InlineKeyboardMarkup:
    k = Keyboard()
    if onboarding < 4:
        k.row(B("🚀 ادامه مسیر شروع", "journey", owner, style=Style.PRIMARY))
    else:
        k.row(B("🎯 کارهای امروز", "missions", owner, style=Style.PRIMARY),
              B("🎁 هدیه روزانه", "daily", owner, style=Style.SUCCESS if daily_ready else Style.GLASS))
    if onboarding < 4:
        k.row(B("🎯 کارهای امروز", "missions", owner),
              B("🎁 هدیه روزانه", "daily", owner, style=Style.SUCCESS if daily_ready else Style.GLASS))
    k.row(B("💼 کار و دریافت درآمد", "jobs", owner), B("💳 دارایی و بانک", "economy", owner))
    k.row(B("💵 بازار ارز", "market", owner), B("🏠 خانه و زندگی", "housing", owner))
    k.row(B("🪪 شخصیت من", "profile", owner), B("🗺 مسیر پیشرفت", "unlocks", owner))
    k.row(B("📣 درخواست تبلیغ", "advertise", owner))
    return k.build()

def journey(owner, step):
    labels = {0:"✨ تعیین هدف نخست", 1:"🎁 دریافت سرمایه آغازین", 2:"🎯 بازکردن نخستین کار روزانه", 3:"🏁 ورود به زندگی اصلی"}
    k = Keyboard()
    if 0 <= step < 4:
        k.row(B(labels[step], "jstep", owner, str(step), Style.PRIMARY))
    k.row(B("🏠 خانه", "home", owner))
    return k.build()

def back(owner, action="home"):
    return Keyboard().row(B("🏠 خانه", action, owner, style=Style.PRIMARY)).build()

def daily(owner, ready):
    k = Keyboard()
    if ready:
        k.row(B("🎁 دریافت هدیه", "claim", owner, style=Style.SUCCESS))
    k.row(B("🎯 ادامه با کارهای امروز", "missions", owner, style=Style.PRIMARY), B("🏠 خانه", "home", owner))
    return k.build()

def missions(owner, keys):
    k = Keyboard()
    for i, key in enumerate(keys):
        k.row(B(f"🎁 دریافت پاداش کار {i + 1}", "mclaim", owner, key, Style.SUCCESS))
    k.row(B("🔄 تازه‌سازی", "missions", owner, style=Style.PRIMARY), B("🏠 خانه", "home", owner))
    return k.build()

def economy(owner):
    return (Keyboard().row(B("🏦 مدیریت پس‌انداز", "savings", owner, style=Style.PRIMARY), B("🧾 پرداخت هزینه زندگی", "living", owner, style=Style.SUCCESS))
            .row(B("🏠 انتخاب خانه", "housing", owner), B("🏠 منوی اصلی", "home", owner)).build())

def savings(owner):
    return (Keyboard().row(B("واریز ۵۰ هزار", "deposit", owner, "50000", Style.PRIMARY), B("برداشت ۵۰ هزار", "withdraw", owner, "50000"))
            .row(B("واریز ۲۰۰ هزار", "deposit", owner, "200000"), B("برداشت ۲۰۰ هزار", "withdraw", owner, "200000"))
            .row(B("↩️ بازگشت", "economy", owner)).build())

def housing(owner):
    return (Keyboard().row(B("اجاره اتاق", "hrent", owner, "room", Style.PRIMARY), B("خرید اتاق", "hbuy", owner, "room"))
            .row(B("اجاره آپارتمان", "hrent", owner, "apartment"), B("خرید آپارتمان", "hbuy", owner, "apartment"))
            .row(B("خرید ویلا", "hbuy", owner, "villa"), B("↩️ بازگشت", "economy", owner)).build())

def jobs(owner, has_job, unlocked=True):
    k = Keyboard()
    if not unlocked:
        return k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY)).row(B("🏠 خانه", "home", owner)).build()
    if has_job:
        k.row(B("🛠 کار کن و درآمد بگیر", "jcollect", owner, style=Style.SUCCESS))
        k.row(B("⚙️ ارتقای مهارت", "jupgrade", owner, "production", Style.PRIMARY), B("🗄 افزایش ظرفیت", "jupgrade", owner, "storage"))
    else:
        k.row(B("🌾 کشاورز", "jchoose", owner, "farmer", Style.PRIMARY), B("⛏ معدن‌کار", "jchoose", owner, "miner"))
        k.row(B("💻 برنامه‌نویس", "jchoose", owner, "programmer"), B("📈 بازرگان", "jchoose", owner, "trader"))
        k.row(B("⚡ مهندس", "jchoose", owner, "engineer"), B("🩺 پزشک", "jchoose", owner, "doctor"))
        k.row(B("📰 روزنامه‌نگار", "jchoose", owner, "journalist"))
    k.row(B("🏠 منوی اصلی", "home", owner))
    return k.build()

def market(owner, unlocked=True):
    k = Keyboard()
    if not unlocked:
        return k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY)).row(B("🏠 خانه", "home", owner)).build()
    return (k.row(B("خرید ۱۰ دلار", "mbuy", owner, "1000", Style.PRIMARY), B("فروش ۱۰ دلار", "msell", owner, "1000"))
            .row(B("خرید ۵۰ دلار", "mbuy", owner, "5000"), B("فروش ۵۰ دلار", "msell", owner, "5000"))
            .row(B("🔄 تازه‌سازی", "market", owner), B("🏠 خانه", "home", owner)).build())