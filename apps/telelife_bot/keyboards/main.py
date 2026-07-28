"""صفحه‌کلیدهای بات زندگی.

قواعد طراحی (ثابت در همهٔ صفحه‌ها):
- هر صفحه دقیقاً یک دکمهٔ Primary دارد: بهترین قدم بعدی.
- Success فقط برای چیزی که همین حالا آمادهٔ دریافت است.
- بقیهٔ دکمه‌ها شیشه‌ای‌اند و با یک نقطهٔ رنگی دسته‌بندی می‌شوند:
    🔵 جابه‌جایی و اطلاعات   🟣 اقتصاد و دارایی
    🟡 پول از جیب / فروش     🟢 رشد و پیشرفت
- ردیف آخر همیشه یکسان است: تازه‌سازی یا بازگشت، سپس «خانه».
"""
from telegram import InlineKeyboardMarkup

from packages.core.ui import Keyboard, Style, button, cb, url_button

NS = "tl"

NAV = "🔵"
MONEY = "🟣"
SPEND = "🟡"
GROW = "🟢"
HOME_LABEL = "🏠 خانه"


def B(text, action, owner, arg="", style=Style.GLASS):
    return button(text, cb(NS, action, owner, arg), style=style)


def _footer(k, owner, back_action="home", back_label=None):
    """ردیف پایانی یکنواخت: یک بازگشت روشن، بدون شلوغی."""
    if back_action == "home":
        k.row(B(HOME_LABEL, "home", owner))
    else:
        k.row(B(back_label or f"{NAV} بازگشت", back_action, owner), B(HOME_LABEL, "home", owner))
    return k


def home(owner: int, daily_ready: bool, onboarding: int = 4) -> InlineKeyboardMarkup:
    k = Keyboard()
    k.row(B("▶️ قدم بعدی من", "journey" if onboarding < 4 else "today", owner, style=Style.PRIMARY))
    if daily_ready:
        k.row(B("🎁 هدیهٔ امروز آماده است", "daily", owner, style=Style.SUCCESS))
    k.row(B(f"{GROW} کار و درآمد", "jobs", owner), B(f"{GROW} کارهای امروز", "missions", owner))
    k.row(B(f"{MONEY} پول و دارایی", "economy", owner), B(f"{MONEY} کشور من", "country", owner))
    k.row(B(f"{NAV} وضعیت من", "profile", owner), B(f"{NAV} مسیر پیشرفت", "progress", owner))
    k.row(B(f"{NAV} چرا بازی کنم؟", "why", owner), B(f"{NAV} راهنمای یک‌دقیقه‌ای", "guide", owner))
    k.row(B(f"{GROW} دعوت دوست و جایزه", "referrals", owner))
    k.row(B(f"{SPEND} درخواست تبلیغ", "advertise", owner))
    return k.build()


def referrals(owner, invite_url="", claimable=False):
    k = Keyboard()
    if invite_url:
        k.row(url_button("📨 فرستادن لینک دعوت", f"https://t.me/share/url?url={invite_url}", style=Style.PRIMARY))
    if claimable:
        k.row(B("🎁 دریافت جایزهٔ آماده", "refclaim", owner, style=Style.SUCCESS))
    k.row(B(f"{NAV} تازه‌سازی", "referrals", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def journey(owner, step):
    labels = {
        0: "✨ شروع زندگی من",
        1: "🎁 گرفتن سرمایهٔ شروع",
        2: "🎯 دیدن اولین کار",
        3: "💼 انتخاب شغل و شروع درآمد",
    }
    k = Keyboard()
    if 0 <= step < 4:
        k.row(B(labels[step], "jstep", owner, str(step), Style.PRIMARY))
    return _footer(k, owner).build()


def back(owner, action="home"):
    return Keyboard().row(B(HOME_LABEL, action, owner, style=Style.PRIMARY)).build()


def daily(owner, ready):
    k = Keyboard()
    if ready:
        k.row(B("🎁 دریافت هدیه", "claim", owner, style=Style.SUCCESS))
        k.row(B(f"{GROW} کارهای امروز", "missions", owner))
    else:
        k.row(B("🎯 ادامه با کارهای امروز", "missions", owner, style=Style.PRIMARY))
    return _footer(k, owner).build()


def missions(owner, keys):
    k = Keyboard()
    for i, key in enumerate(keys):
        k.row(B(f"🎁 دریافت پاداش کار {i + 1}", "mclaim", owner, key, Style.SUCCESS))
    if not keys:
        k.row(B("💼 رفتن سر کار", "jobs", owner, style=Style.PRIMARY))
    k.row(B(f"{NAV} تازه‌سازی", "missions", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def economy(owner):
    k = Keyboard()
    k.row(B(f"{MONEY} مدیریت پس‌انداز", "savings", owner, style=Style.PRIMARY))
    k.row(B(f"{SPEND} پرداخت هزینهٔ زندگی", "living", owner), B(f"{MONEY} انتخاب خانه", "housing", owner))
    k.row(B(f"{MONEY} بازار دلار", "market", owner), B(f"{SPEND} منابع و فروش", "resources", owner))
    return _footer(k, owner).build()


def savings(owner):
    k = Keyboard()
    k.row(B(f"{MONEY} واریز ۵۰ هزار", "deposit", owner, "50000", Style.PRIMARY),
          B(f"{SPEND} برداشت ۵۰ هزار", "withdraw", owner, "50000"))
    k.row(B(f"{MONEY} واریز ۲۰۰ هزار", "deposit", owner, "200000"),
          B(f"{SPEND} برداشت ۲۰۰ هزار", "withdraw", owner, "200000"))
    return _footer(k, owner, "economy", f"{NAV} پول و دارایی").build()


def housing(owner):
    k = Keyboard()
    k.row(B(f"{SPEND} اجارهٔ اتاق", "hrent", owner, "room", Style.PRIMARY),
          B(f"{MONEY} خرید اتاق", "hbuy", owner, "room"))
    k.row(B(f"{SPEND} اجارهٔ آپارتمان", "hrent", owner, "apartment"),
          B(f"{MONEY} خرید آپارتمان", "hbuy", owner, "apartment"))
    k.row(B(f"{MONEY} خرید ویلا", "hbuy", owner, "villa"))
    return _footer(k, owner, "economy", f"{NAV} پول و دارایی").build()


def jobs(owner, has_job, unlocked=True):
    k = Keyboard()
    if not unlocked:
        k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY))
        return _footer(k, owner).build()
    if has_job:
        k.row(B("✅ دریافت نتیجهٔ شیفت", "jcollect", owner, style=Style.SUCCESS))
        k.row(B(f"{GROW} شیفت متعادل", "jshift", owner, "balanced"),
              B(f"{GROW} شیفت ملی", "jshift", owner, "national"))
        k.row(B(f"{GROW} شیفت امن", "jshift", owner, "safe"),
              B(f"{GROW} شیفت خصوصی", "jshift", owner, "private"))
        k.row(B(f"{MONEY} ارتقای مهارت", "jupgrade", owner, "production"),
              B(f"{MONEY} افزایش ظرفیت", "jupgrade", owner, "storage"))
        k.row(B(f"{SPEND} منابع و فروش", "resources", owner))
    else:
        k.row(B("🌾 کشاورز", "jchoose", owner, "farmer", Style.PRIMARY),
              B("⛏ معدن‌کار", "jchoose", owner, "miner"))
        k.row(B("💻 برنامه‌نویس", "jchoose", owner, "programmer"),
              B("📈 بازرگان", "jchoose", owner, "trader"))
        k.row(B("⚡ مهندس", "jchoose", owner, "engineer"),
              B("🩺 پزشک", "jchoose", owner, "doctor"))
        k.row(B("📰 روزنامه‌نگار", "jchoose", owner, "journalist"))
    return _footer(k, owner).build()


def resources(owner, rows):
    """اول دسته‌ها، بعد مقدارها؛ صفحه فشرده و قابل خواندن می‌ماند."""
    k = Keyboard()
    owned = [item for item in rows if int(item["quantity"]) > 0]
    for item in owned:
        k.row(B(f"{MONEY} {item['title']} · {item['quantity']} واحد", "rpick", owner, str(item["asset"])))
    if not owned:
        k.row(B("💼 رفتن به کار و تولید", "jobs", owner, style=Style.PRIMARY))
    k.row(B(f"{NAV} تازه‌سازی", "resources", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def resource_amounts(owner, item):
    k = Keyboard()
    quantity = int(item["quantity"])
    asset = str(item["asset"])
    amounts = [x for x in (10, 50, 100, 500) if x <= quantity]
    for i in range(0, len(amounts), 2):
        k.row(*[
            B(f"{SPEND} فروش {x} واحد", "rsell", owner, f"{asset},{x}",
              Style.PRIMARY if x == amounts[-1] else Style.GLASS)
            for x in amounts[i:i + 2]
        ])
    return _footer(k, owner, "resources", f"{NAV} منابع").build()


def market(owner, unlocked=True):
    k = Keyboard()
    if not unlocked:
        k.row(B("🎯 رفتن به کارهای امروز", "missions", owner, style=Style.PRIMARY))
        return _footer(k, owner).build()
    k.row(B(f"{MONEY} خرید ۱۰ دلار", "mbuy", owner, "1000", Style.PRIMARY),
          B(f"{SPEND} فروش ۱۰ دلار", "msell", owner, "1000"))
    k.row(B(f"{MONEY} خرید ۵۰ دلار", "mbuy", owner, "5000"),
          B(f"{SPEND} فروش ۵۰ دلار", "msell", owner, "5000"))
    k.row(B(f"{NAV} تازه‌سازی", "market", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def progress(owner):
    k = Keyboard()
    k.row(B(f"{MONEY} دارایی‌های کاربردی", "assets", owner, style=Style.PRIMARY))
    k.row(B(f"{NAV} همهٔ قابلیت‌ها", "unlocks", owner), B(f"{GROW} کار و رشد مهارت", "jobs", owner))
    return _footer(k, owner).build()


def assets(owner, rows):
    k = Keyboard()
    emphasized = False
    for item in rows:
        if item.available and not item.owned:
            style = Style.PRIMARY if not emphasized else Style.GLASS
            emphasized = True
            k.row(B(f"{MONEY} خرید {item.title}", "abuy", owner, item.code, style))
    return _footer(k, owner, "progress", f"{NAV} مرکز پیشرفت").build()


def today(owner, actions):
    labels = {
        "daily": "🎁 گرفتن هدیهٔ آماده",
        "missions": "🎯 ادامهٔ کارهای امروز",
        "jobs": "💼 کار و دریافت درآمد",
        "economy": "🧾 بررسی هزینهٔ زندگی",
    }
    k = Keyboard()
    primary_used=False
    for action in actions:
        if action in {"daily", "missions"}:
            style = Style.SUCCESS
        elif not primary_used:
            style = Style.PRIMARY
            primary_used = True
        else:
            style = Style.GLASS
        k.row(B(labels.get(action, "ادامه"), action, owner, style=style))
    k.row(B(f"{NAV} تازه‌سازی امروز", "today", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def confirm(owner, token, confirm_action, arg, back_action):
    return (Keyboard()
            .row(B("✅ تأیید و اجرا", confirm_action, owner, arg, Style.SUCCESS))
            .row(B(f"{NAV} انصراف", back_action, owner))
            .build())


def country(owner: int, group_url: str | None, destinations: list[tuple[int, str, int]], *, pending: bool = False):
    k = Keyboard()
    if group_url:
        k.row(url_button("🔗 ورود به گروه کشور من", group_url, style=Style.PRIMARY))
    if not pending:
        for country_id, name, citizens in destinations:
            k.row(B(f"🧳 {name} · {citizens} شهروند", "migrate", owner, str(country_id)))
    k.row(B(f"{NAV} تازه‌سازی", "country", owner), B(HOME_LABEL, "home", owner))
    return k.build()


def learn(owner):
    k = Keyboard()
    k.row(B("▶️ قدم بعدی من", "today", owner, style=Style.PRIMARY))
    k.row(B(f"{GROW} دیدن شغل‌ها", "jobs", owner), B(f"{MONEY} کشور من", "country", owner))
    return _footer(k, owner).build()
