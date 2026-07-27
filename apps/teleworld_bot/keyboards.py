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

def home(country, admin, citizen=False, official_role=None):
    """Reveal only actions relevant to this member's current country role."""
    if country:
        if not citizen:
            rows = [[b("🤝 شهروند این کشور می‌شوم", "join", "success")],
                    [b("🏛 وضعیت کشور", "country", "primary"), b("👥 شهروندان", "citizens")],
                    [b("📘 قوانین شهروندی", "migration_rules"), b("🔄 تازه‌سازی", "home")]]
            return InlineKeyboardMarkup(rows)
        rows = [[b("☀️ وضعیت امروز کشور", "country_today", "primary")],
                [b("🏘 جامعه کشور", "society"), b("👥 شهروندان", "citizens")],
                [b("💰 اقتصاد و منابع", "economy"), b("🗳 سیاست و انتخابات", "politics")],
                [b("🏗 پروژه ملی", "project"), b("🌐 تجارت و دیپلماسی", "trade")],
                [b("✈️ مهاجرت", "migration"), b("🏛 شناسنامه", "country")]]
        if official_role in {"president", "economy_minister", "industry_minister"}:
            rows.insert(2,[b("⚙️ مدیریت حوزه من", "economyb", "success")])
        if official_role in {"president", "foreign_minister"}:
            rows.insert(3,[b("🤝 عملیات دیپلماسی", "trade", "success")])
        if official_role == "president" or admin:
            rows.append([b("📥 درخواست‌های مهاجرت", "migration_review")])
        rows.append([b("🛡 اشتراک بدون تبلیغ", "subscription"), b("🔄 تازه‌سازی", "home")])
        return InlineKeyboardMarkup(rows)
    if admin:
        return InlineKeyboardMarkup([[b("🏗 ساخت کشور", "create", "primary")], [b("📘 راهنمای ساخت کشور", "guide")], [b("🔄 تازه‌سازی", "home")]])
    return InlineKeyboardMarkup([[b("📘 برای ساخت کشور چه کنیم؟", "guide", "primary")], [b("🔄 تازه‌سازی", "home")]])



def confirm_world(confirm_action, back_action="home"):
 return InlineKeyboardMarkup([[b("✅ تأیید و اجرا",confirm_action,"success")],[b("↩️ انصراف",back_action,"primary")]])

def citizenship_elsewhere():
    return InlineKeyboardMarkup([
        [b("✈️ قوانین مهاجرت", "migration_rules", "primary")],
        [b("🚪 لغو شهروندی فعلی", "citizenship_cancel_ask", "danger")],
        [b("🏠 خانه جهان", "home")],
    ])

def citizenship_cancel_confirm():
    return InlineKeyboardMarkup([
        [b("تأیید لغو شهروندی", "citizenship_cancel_confirm", "danger")],
        [b("انصراف", "home", "primary")],
    ])

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
def project(active, available=None):
    if active:
        return InlineKeyboardMarkup([[b("💵 کمک شخصی ۵۰ هزار", "pcon:IRT:50000", "success"),b("🏛 از خزانه ۲۰۰ هزار","ptreasury:IRT:200000")],
                                     [b("🌾 کمک ۵۰ غذا", "pcon:food:50"), b("⛏ کمک ۵۰ معدن", "pcon:minerals:50")],
                                     [b("🛢 کمک ۵۰ نفت", "pcon:oil:50"),b("⚡ کمک ۵۰ انرژی", "pcon:energy:50")],
                                     [b("🔬 کمک ۵۰ فناوری", "pcon:technology:50")], [b("🏠 خانه جهان", "home")]])
    rows=[]
    for key,title in (available or []):rows.append([b(f"🏗 آغاز {title}",f"pstart:{key}","primary" if not rows else None)])
    rows.append([b("🏠 خانه جهان", "home")]);return InlineKeyboardMarkup(rows)

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

def country_economy_b(can_manage=False, president=False):
    rows=[]
    if can_manage:
        rows += [[b("⚖️ بودجه متعادل","budget:balanced","primary"),b("🫶 تمرکز رفاه","budget:welfare")],
                 [b("🏭 تمرکز رشد","budget:growth"),b("🛡 تمرکز امنیت","budget:security")]]
    if president:
        rows.append([b("👔 کابینه اولیه","offices")])
    rows.append([b("↩️ اقتصاد کشور","economy"),b("🏠 خانه جهان","home")])
    return InlineKeyboardMarkup(rows)

def offices(rows):
    buttons=[]
    labels={"economy_minister":"وزیر اقتصاد","industry_minister":"وزیر صنعت","foreign_minister":"وزیر خارجه","army_commander":"فرمانده ارتش","intelligence_chief":"رئیس اطلاعات"}
    for row in rows:
        for role,label in labels.items():buttons.append([b(f"{label}: {row['first_name']}",f"appoint:{role}:{row['player_id']}")])
    buttons.append([b("↩️ اقتصاد و بودجه","economyb")]);return InlineKeyboardMarkup(buttons)

def central_bank(president=False):
    rows=[]
    if president:
        rows.append([b("➕ افزایش بهره ۱٪","rate:up","primary"),b("➖ کاهش بهره ۱٪","rate:down")])
        rows.append([b("💵 خرید ذخیره ارزی ۱۰M","reserve:buy","success")])
    rows.append([b("↩️ اقتصاد کشور","economy"),b("🏠 خانه جهان","home")])
    return InlineKeyboardMarkup(rows)

def trade_home(can_manage=False):
 rows=[[b("📥 پیشنهادهای دریافتی","tradein","primary"),b("📤 پیشنهادهای من","tradeout")],
       [b("🤝 روابط خارجی","relations"),b("🆘 کمک اضطراری","aid")],
       [b("📈 نرخ‌های مرجع","traderef"),b("🏠 خانه جهان","home")]]
 if can_manage:rows.insert(1,[b("➕ قرارداد تازه","tradenew","success")])
 return InlineKeyboardMarkup(rows)

def trade_countries(rows,action="tradeto"):
 buttons=[[b(f"🌍 {r['name']}",f"{action}:{r['id']}")] for r in rows]
 buttons.append([b("↩️ تجارت و دیپلماسی","trade")]);return InlineKeyboardMarkup(buttons)

def trade_presets(target_id,presets):
 buttons=[[b(str(spec['title']),f"tradepreset:{target_id}:{key}","primary" if i==0 else None)] for i,(key,spec) in enumerate(presets.items())]
 buttons.append([b("↩️ انتخاب کشور","tradenew")]);return InlineKeyboardMarkup(buttons)

def incoming_trade(rows):
 buttons=[[b(f"✅ پذیرش #{r['id']} از {r['proposer_name']}",f"tradeaccept:{r['id']}","success")] for r in rows]
 buttons.append([b("↩️ تجارت و دیپلماسی","trade")]);return InlineKeyboardMarkup(buttons)

def relations_countries(rows):
 buttons=[]
 for r in rows:
  buttons.append([b(f"🤝 پیشنهاد همکاری با {r['name']}",f"relmenu:{r['id']}")])
 buttons.append([b("↩️ تجارت و دیپلماسی","trade")]);return InlineKeyboardMarkup(buttons)

def relation_actions(target_id):
 return InlineKeyboardMarkup([[b("🙂 دوستی",f"relprop:{target_id}:friend"),b("📦 شریک تجاری",f"relprop:{target_id}:trade_partner","primary")],
  [b("🛡 متحد دفاعی",f"relprop:{target_id}:defensive_ally"),b("✅ پذیرش پیشنهاد",f"relaccept:{target_id}","success")],
  [b("⛔ تحریم مستقیم",f"sanction:{target_id}","danger"),b("♻️ رفع تحریم",f"sanctionlift:{target_id}")],[b("↩️ روابط خارجی","relations")]])

def aid_countries(rows):
 buttons=[[b(f"🆘 {r['name']}",f"aidto:{r['id']}")] for r in rows]
 buttons.append([b("↩️ تجارت و دیپلماسی","trade")]);return InlineKeyboardMarkup(buttons)

def aid_assets(target_id):
 return InlineKeyboardMarkup([[b("🌾 ارسال ۵۰ غذا",f"aidsend:{target_id}:food","success"),b("⚡ ارسال ۵۰ انرژی",f"aidsend:{target_id}:energy")],
  [b("💰 ارسال ۵۰۰ هزار تومان",f"aidsend:{target_id}:IRT")],[b("↩️ انتخاب کشور","aid")]])


def outgoing_trade(rows):
 buttons=[[b(f"لغو #{r['id']} برای {r['recipient_name']}",f"tradecancel:{r['id']}","danger")] for r in rows]
 buttons.append([b("↩️ تجارت و دیپلماسی","trade")]);return InlineKeyboardMarkup(buttons)

def pending_relations(rows):
 buttons=[[b(f"✅ پذیرش {r['counterparty_name']}",f"relaccept:{r['counterparty_id']}","success")] for r in rows]
 buttons.append([b("↩️ روابط خارجی","relations")]);return InlineKeyboardMarkup(buttons)
# ---------- جامعه کشور ----------
def society_home(pending=(), competitions=(), married=False):
 rows=[[b("🤝 کمک به شهروند","socpeople:help","success"),b("🫂 دوستی‌ها","socpeople:friend")],
       [b("💍 ازدواج و خانواده","socmarriage","primary"),b("🏆 رقابت دوستانه","socpeople:compete")],
       [b("⚖️ دادگاه شهروندی","soccases"),b("🛡 گزارش امن","socpeople:report")]]
 for r in pending:
  label="💍" if r["kind"]=="marriage" else "🫂"
  rows.append([b(f"{label} قبول پیشنهاد {r['proposer_name']}",f"socaccept:{r['id']}","success"),b("رد",f"socreject:{r['id']}","danger")])
 for c in competitions:
  if c["status"]=="pending":rows.append([b(f"🏆 قبول رقابت {c['opponent_name']}",f"compaccept:{c['id']}","success"),b("رد",f"compreject:{c['id']}")])
  elif c["status"]=="active":rows.append([b(f"🎯 ادامه رقابت با {c['opponent_name']}",f"compview:{c['id']}")])
 if married:rows.append([b("💔 درخواست جدایی","divorceask","danger")])
 rows.append([b("🏠 خانه جهان","home")]);return InlineKeyboardMarkup(rows)

def social_people(rows,mode):
 labels={"help":"🤝 کمک به","friend":"🫂 دوستی با","marry":"💍 پیشنهاد به","compete":"🏆 رقابت با","report":"🛡 گزارش","case":"⚖️ شکایت از"}
 buttons=[[b(f"{labels.get(mode,'انتخاب')} {r['first_name']}",f"socperson:{mode}:{r['id']}")] for r in rows]
 buttons.append([b("↩️ جامعه کشور","society")]);return InlineKeyboardMarkup(buttons)

def help_amount(target):
 return InlineKeyboardMarkup([[b("۱۰ هزار",f"shelp:{target}:10000"),b("۵۰ هزار",f"shelp:{target}:50000","success")],
 [b("۱۰۰ هزار",f"shelp:{target}:100000"),b("۲۰۰ هزار",f"shelp:{target}:200000")],[b("↩️ جامعه کشور","society")]])

def social_categories(target,prefix):
 labels=[("آزار","harassment"),("کلاهبرداری","fraud"),("تهدید","threat"),("اسپم","spam"),("سایر","other")]
 return InlineKeyboardMarkup([[b(label,f"{prefix}:{target}:{code}") for label,code in labels[i:i+2]] for i in range(0,len(labels),2)]+[[b("↩️ جامعه کشور","society")]])

def competition(cid,can_play=True):
 rows=[]
 if can_play:rows.append([b("🎯 حرکت مطمئن +۲",f"compplay:{cid}:focus","primary"),b("🎲 حرکت پرریسک ۰/۳",f"compplay:{cid}:risk")])
 rows.append([b("🔄 تازه‌سازی رقابت",f"compview:{cid}"),b("↩️ جامعه کشور","society")]);return InlineKeyboardMarkup(rows)

def court_cases(rows):
 buttons=[]
 for r in rows:
  buttons.append([b(f"⚖️ پرونده #{r['id']}: {r['plaintiff_name']} / {r['defendant_name']}",f"caseview:{r['id']}")])
 buttons.append([b("➕ ثبت شکایت رسمی","socpeople:case","primary"),b("↩️ جامعه کشور","society")]);return InlineKeyboardMarkup(buttons)

def court_vote(case_id):
 return InlineKeyboardMarkup([[b("رأی: تخلف رخ داده",f"casevote:{case_id}:guilty","danger")],
 [b("رأی: اثبات نشده",f"casevote:{case_id}:not_guilty","success")],[b("↩️ پرونده‌ها","soccases")]])

def divorce_confirm():
 return InlineKeyboardMarkup([[b("تأیید جدایی و شروع انتظار ۷روزه","divorceok","danger")],[b("انصراف","society","primary")]])
