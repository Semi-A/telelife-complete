"""صفحه‌کلیدهای فارسی بات زندگی؛ در هر صفحه فقط یک اقدام اصلی داریم."""
from telegram import InlineKeyboardMarkup
from packages.core.ui import Keyboard, Style, button, cb, url_button

NS = "tl"

def B(text, action, owner, arg="", style=Style.GLASS):
    return button(text, cb(NS, action, owner, arg), style=style)

def home(owner: int, daily_ready: bool, onboarding: int = 4) -> InlineKeyboardMarkup:
    k = Keyboard()
    if onboarding < 4:
        k.row(B("▶️ قدم بعدی من", "journey", owner, style=Style.PRIMARY))
    else:
        k.row(B("▶️ قدم بعدی من", "today", owner, style=Style.PRIMARY))
    k.row(B("💼 کار و درآمد", "jobs", owner, style=Style.SUCCESS),
          B("🎯 کارهای امروز", "missions", owner, style=Style.SUCCESS))
    k.row(B("💳 پول و دارایی", "economy", owner), B("🌍 کشور من", "country", owner))
    k.row(B("🪪 وضعیت من", "profile", owner), B("🧭 مسیر پیشرفت", "progress", owner))
    k.row(B("❓ چرا بازی کنم؟", "why", owner), B("📘 راهنمای یک‌دقیقه‌ای", "guide", owner))
    k.row(B("🎁 دعوت دوست و جایزه", "referrals", owner, style=Style.SUCCESS))
    k.row(B("📣 درخواست تبلیغ", "advertise", owner))
    return k.build()

def referrals(owner, invite_url="", claimable=False):
    k=Keyboard()
    if invite_url:k.row(url_button("📨 فرستادن لینک دعوت",f"https://t.me/share/url?url={invite_url}",style=Style.PRIMARY))
    if claimable:k.row(B("🎁 دریافت جایزه آماده","refclaim",owner,style=Style.SUCCESS))
    k.row(B("🔵 تازه‌سازی","referrals",owner),B("🏠 خانه","home",owner))
    return k.build()

def journey(owner, step):
    labels = {0:"✨ شروع زندگی من", 1:"🎁 گرفتن سرمایه شروع", 2:"🎯 دیدن اولین کار", 3:"💼 انتخاب شغل و شروع درآمد"}
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
    return (Keyboard()
            .row(B("🔵 مدیریت پس‌انداز", "savings", owner, style=Style.PRIMARY), B("🟡 پرداخت هزینه زندگی", "living", owner, style=Style.SUCCESS))
            .row(B("🏠 انتخاب خانه", "housing", owner), B("🟣 بازار دلار", "market", owner))
            .row(B("📦 منابع و فروش", "resources", owner), B("🏠 خانه", "home", owner)).build())

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
        k.row(B("✅ دریافت نتیجه شیفت", "jcollect", owner, style=Style.SUCCESS))
        k.row(B("⚖️ متعادل", "jshift", owner, "balanced", Style.PRIMARY), B("🏛 ملی", "jshift", owner, "national"))
        k.row(B("🛡 امن", "jshift", owner, "safe"), B("💵 خصوصی", "jshift", owner, "private"))
        k.row(B("⚙️ ارتقای مهارت", "jupgrade", owner, "production"), B("🗄 افزایش ظرفیت", "jupgrade", owner, "storage"))
    else:
        k.row(B("🌾 کشاورز", "jchoose", owner, "farmer", Style.PRIMARY), B("⛏ معدن‌کار", "jchoose", owner, "miner"))
        k.row(B("💻 برنامه‌نویس", "jchoose", owner, "programmer"), B("📈 بازرگان", "jchoose", owner, "trader"))
        k.row(B("⚡ مهندس", "jchoose", owner, "engineer"), B("🩺 پزشک", "jchoose", owner, "doctor"))
        k.row(B("📰 روزنامه‌نگار", "jchoose", owner, "journalist"))
    k.row(B("📦 منابع و فروش", "resources", owner, style=Style.SUCCESS), B("🏠 منوی اصلی", "home", owner))
    return k.build()

def resources(owner, rows):
    """Show resource categories first, then amounts, to keep the panel compact."""
    k=Keyboard();owned=[item for item in rows if int(item["quantity"])>0]
    for item in owned:
        k.row(B(f"🟣 {item['title']} · {item['quantity']} واحد","rpick",owner,str(item["asset"])))
    if not owned:k.row(B("💼 رفتن به کار و تولید","jobs",owner,style=Style.SUCCESS))
    k.row(B("🔵 تازه‌سازی","resources",owner,style=Style.PRIMARY),B("🏠 خانه","home",owner))
    return k.build()

def resource_amounts(owner,item):
    k=Keyboard();quantity=int(item["quantity"]);asset=str(item["asset"])
    amounts=[x for x in (10,50,100,500) if x<=quantity]
    for i in range(0,len(amounts),2):
        k.row(*[B(f"🟡 فروش {x} واحد","rsell",owner,f"{asset},{x}",Style.PRIMARY if x==amounts[-1] else Style.GLASS) for x in amounts[i:i+2]])
    k.row(B("↩️ منابع","resources",owner))
    return k.build()

def market(owner, unlocked=True):
    k=Keyboard()
    if not unlocked:return k.row(B("🎯 رفتن به کارهای امروز","missions",owner,style=Style.PRIMARY)).row(B("🏠 خانه","home",owner)).build()
    return (k.row(B("🟣 خرید ۱۰ دلار","mbuy",owner,"1000",Style.PRIMARY),B("🟡 فروش ۱۰ دلار","msell",owner,"1000"))
            .row(B("🟣 خرید ۵۰ دلار","mbuy",owner,"5000"),B("🟡 فروش ۵۰ دلار","msell",owner,"5000",Style.SUCCESS))
            .row(B("🔵 تازه‌سازی","market",owner),B("🏠 خانه","home",owner)).build())


def progress(owner):
    return (Keyboard().row(B("🚗 دارایی‌های کاربردی", "assets", owner, style=Style.PRIMARY), B("🗺 همه قابلیت‌ها", "unlocks", owner))
            .row(B("💼 کار و رشد مهارت", "jobs", owner), B("🏠 خانه", "home", owner)).build())

def assets(owner, rows):
    k=Keyboard()
    emphasized=False
    for item in rows:
        if item.available and not item.owned:
            style=Style.PRIMARY if not emphasized else Style.SUCCESS
            emphasized=True
            k.row(B(f"خرید {item.title}", "abuy", owner, item.code, style))
    k.row(B("🧭 مرکز پیشرفت", "progress", owner), B("🏠 خانه", "home", owner))
    return k.build()

def today(owner, actions):
    labels={"daily":"🎁 گرفتن هدیه آماده","missions":"🎯 ادامه کارهای امروز","jobs":"💼 کار و دریافت درآمد","economy":"🧾 بررسی هزینه زندگی"}
    k=Keyboard()
    primary_used=False
    for action in actions:
        if action in {"daily", "missions"}:
            style=Style.SUCCESS
        elif not primary_used:
            style=Style.PRIMARY
            primary_used=True
        else:
            style=Style.SUCCESS
        k.row(B(labels.get(action,"ادامه"),action,owner,style=style))
    k.row(B("🔄 تازه‌سازی امروز", "today", owner),B("🏠 خانه", "home", owner))
    return k.build()

def confirm(owner, token, confirm_action, arg, back_action):
    return (Keyboard().row(B("✅ تأیید و اجرا",confirm_action,owner,arg,Style.SUCCESS))
            .row(B("↩️ انصراف",back_action,owner)).build())

def country(owner:int,group_url:str|None,destinations:list[tuple[int,str,int]],*,pending:bool=False):
    k=Keyboard()
    if group_url:
        k.row(url_button("🔗 ورود به گروه کشور من",group_url,style=Style.PRIMARY))
    if not pending:
        for country_id,name,citizens in destinations:
            k.row(B(f"🧳 {name} · {citizens} شهروند","migrate",owner,str(country_id)))
    k.row(B("🔄 تازه‌سازی", "country", owner),B("🏠 خانه", "home", owner))
    return k.build()

def learn(owner):
    return (Keyboard().row(B("▶️ قدم بعدی من", "today", owner, style=Style.PRIMARY))
            .row(B("💼 دیدن شغل‌ها", "jobs", owner, style=Style.SUCCESS),
                 B("🌍 کشور من", "country", owner))
            .row(B("🏠 خانه", "home", owner)).build())