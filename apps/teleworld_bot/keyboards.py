"""رابط دکمه‌ای فارسی جهان؛ رنگ فقط برای یک اقدام اصلی در هر صفحه است."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def b(text, action, style=None):
    kwargs = {"text": text, "callback_data": f"tw:{action}"}
    if style:
        kwargs["style"] = style
    return InlineKeyboardButton(**kwargs)

def access(ready=False):
    if ready:
        return InlineKeyboardMarkup([[b("✅ ورود به جهان", "access:check", "primary")],
                                     [b("🩺 بررسی وضعیت", "health")]])
    return InlineKeyboardMarkup([[b("🔄 بررسی دوباره دسترسی", "access:check", "primary")],
                                 [b("📘 چرا دسترسی مدیر لازم است؟", "access:why")],
                                 [b("🩺 وضعیت و علت قفل", "health")]])

def private(username):
    return InlineKeyboardMarkup([[InlineKeyboardButton("➕ افزودن به گروه", url=f"https://t.me/{username}?startgroup=true", style="primary")], [b("📘 راهنمای استفاده", "guide")]])

def home(country, admin, citizen=False):
    if country:
        rows = [[b("🏛 شناسنامه کشور", "country", "primary"), b("👥 شهروندان", "citizens")],
                [b("💰 اقتصاد و منابع", "economy"), b("🗳 سیاست و انتخابات", "politics")], [b("🏗 پروژه ملی", "project")]]
        rows.append([b("🚪 خروج از شهروندی", "leave", "danger")] if citizen else [b("🤝 شهروند این کشور می‌شوم", "join", "success")])
        rows.append([b("🛡 اشتراک بدون تبلیغ", "subscription", "primary"),b("✈️ مهاجرت", "migration")])
        if admin:rows.append([b("📥 درخواست‌های مهاجرت", "migration_review")])
        rows.append([b("📘 راهنمای همین مرحله", "guide"), b("🔄 تازه‌سازی", "home")])
        return InlineKeyboardMarkup(rows)
    if admin:
        return InlineKeyboardMarkup([[b("🏗 ساخت کشور", "create", "primary")], [b("📘 راهنمای ساخت کشور", "guide")], [b("🔄 تازه‌سازی", "home")]])
    return InlineKeyboardMarkup([[b("📘 برای ساخت کشور چه کنیم؟", "guide", "primary")], [b("🔄 تازه‌سازی", "home")]])

def governments():
    items=[("🏛 جمهوری","republic"),("🗳 ریاستی","presidential"),("🏢 پارلمانی","parliamentary"),("⚖️ نیمه‌ریاستی","semi_presidential"),("👑 پادشاهی","monarchy"),("📜 مشروطه","constitutional_monarchy"),("🛡 دیکتاتوری","dictatorship"),("🧭 فدرال","federal"),("🤝 شورایی","council"),("👥 مستقیم","direct_democracy"),("⛪ دینی","theocracy"),("🎖 شورای نظامی","military_junta"),("💠 الیگارشی","oligarchy")]
    rows=[[b(label,f"gov:{code}") for label,code in items[i:i+2]] for i in range(0,len(items),2)]
    rows.append([b("لغو ساخت کشور","home")]);return InlineKeyboardMarkup(rows)

def government_confirm(code):
    return InlineKeyboardMarkup([[b("تأیید این حکومت",f"govok:{code}","primary")],[b("انتخاب نوع دیگر","govback")],[b("لغو ساخت کشور","home")]])

def country():
    return InlineKeyboardMarkup([[b("💰 کمک ۵۰ هزار تومان", "donate:50000", "success"), b("💰 کمک ۲۰۰ هزار تومان", "donate:200000")],
                                 [b("🗳 انتخابات", "politics", "primary"), b("👥 شهروندان", "citizens")], [b("🏠 خانه جهان", "home")]])

def politics(status=None, allowed=True):
    if not allowed: return InlineKeyboardMarkup([[b("🏛 شناسنامه کشور","country","primary")],[b("🏠 خانه جهان","home")]])
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

def subscription(round_id:int,remaining:int):
 rows=[]
 for amount in (1,2,5,10,25,50):
  if amount<=remaining: rows.append([b(f"⭐ مشارکت {amount} استار",f"substar:{round_id}:{amount}","primary" if amount==min(remaining,50) else None)])
 rows.append([b("💰 خرید از خزانه کشور","subtreasury")]);rows.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(rows)

def migration_countries(rows,owner_country_id):
 buttons=[[b(f"✈️ مهاجرت به {r['name']}",f"migrate:{r['id']}")] for r in rows if int(r['id'])!=int(owner_country_id)]
 buttons.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(buttons)
def migration_review(rows):
 buttons=[]
 for r in rows:buttons.extend([[b(f"✅ پذیرش {r['first_name']}",f"migaccept:{r['id']}","success"),b("رد",f"migreject:{r['id']}","danger")]])
 buttons.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(buttons)

def central_bank(president=False):
    rows=[]
    if president:
        rows.append([b("➕ افزایش بهره ۱٪","rate:up","primary"),b("➖ کاهش بهره ۱٪","rate:down")])
        rows.append([b("💵 خرید ذخیره ارزی ۱۰M","reserve:buy","success")])
    rows.append([b("↩️ اقتصاد کشور","economy"),b("🏠 خانه جهان","home")])
    return InlineKeyboardMarkup(rows)