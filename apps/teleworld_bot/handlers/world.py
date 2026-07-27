"""کنترل‌گر یک‌پیامی، فارسی و دکمه‌محور جهان گروهی."""
from __future__ import annotations
from uuid import uuid4
from datetime import UTC,datetime
from html import escape
from telegram.constants import ChatMemberStatus, ChatType
from telegram.error import BadRequest, Forbidden
from telegram.ext import CallbackQueryHandler, MessageHandler, PreCheckoutQueryHandler, filters
from telegram import LabeledPrice
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core import db
from packages.core.repositories import country_repo, election_repo, group_repo, player_repo, project_repo, ui_state_repo, world_access_repo
from packages.core.services import country as countries, economy, elections, national_project, commerce, migration, country_realism, country_objectives, country_economy_b, country_trade
from packages.core.services import world_access
from packages.core.utils import fmt

GROUPS = {ChatType.GROUP, ChatType.SUPERGROUP}
FLOW = "world_creation"
STATUS = {"forming":"در حال ساخت", "temporary":"موقت", "official":"رسمی"}
GOV = {code: item[0] for code, item in fa.GOVERNMENT_DETAILS.items()}
ASSET = {"IRT":"تومان", "food":"غذا", "minerals":"مواد معدنی", "oil":"نفت", "energy":"انرژی", "technology":"فناوری"}
ERRORS = {
    "citizen_required":"ابتدا شهروند این کشور شو.", "president_required":"فقط رهبر کشور می‌تواند این کار را انجام دهد.",
    "already_citizen_elsewhere":"اکنون شهروند کشور دیگری هستی؛ ابتدا از آن خارج شو.",
    "election_already_open":"یک انتخابات فعال وجود دارد.", "project_not_active":"پروژه فعالی وجود ندارد.",
    "country_already_exists":"این گروه از قبل کشور دارد.", "insufficient_balance":"موجودی کافی نیست.",
    "insufficient_player_balance":"موجودی کیف پولت کافی نیست.", "country_not_found":"کشوری پیدا نشد.",
    "asset_not_required":"این دارایی برای پروژه لازم نیست.", "project_exists":"از قبل پروژه فعالی وجود دارد.",
}

async def answer(query, text=None, show_alert=False):
    try:
        await query.answer(text, show_alert=show_alert)
    except BadRequest:
        return

async def is_admin(update, context) -> bool:
    member = await context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
    return member.status in {ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER}

async def player(update):
    user = update.effective_user
    return await player_repo.get_or_create(user.id, username=user.username, first_name=user.first_name or "شهروند", language_code=user.language_code or "fa")

async def show(update, context, text, markup):
    chat = update.effective_chat
    query = update.callback_query
    state = await ui_state_repo.world(chat.id)
    message_id = query.message.message_id if query and query.message else int(state["message_id"]) if state else None
    if message_id:
        try:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=message_id, text=text, reply_markup=markup)
            await ui_state_repo.set_world(chat.id, message_id)
            return
        except BadRequest as exc:
            if "message is not modified" in str(exc).lower():
                return
        except Forbidden:
            pass
    sent = await context.bot.send_message(chat.id, text, reply_markup=markup)
    await ui_state_repo.set_world(chat.id, sent.message_id)

async def facts(chat_id):
    row = await country_repo.by_chat(chat_id)
    if not row:
        return None, 0, None
    count = int(await db.fetchval("SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active", row["id"]) or 0)
    leader = await db.fetchval("SELECT first_name FROM players WHERE id=$1", row["president_player_id"]) if row["president_player_id"] else None
    return row, count, leader

MUTATING = {"create", "join", "leave", "estart", "nominate", "subtreasury", "migration", "rate", "reserve", "offices", "tradenew", "aid"}

def is_mutating(action: str) -> bool:
    return action in MUTATING or action.startswith(("donate:", "vote:", "pstart:", "pcon:", "ptreasury:", "gov:", "govok:", "substar:", "migrate:", "migaccept:", "migreject:", "rate:", "reserve:", "budget:", "appoint:", "tradepreset:", "tradeaccept:", "tradecancel:", "relprop:", "relaccept:", "sanction:", "sanctionlift:", "aidsend:"))

async def access_page(update, context, *, force: bool = False):
    access = await world_access.check(context.bot, update.effective_chat.id, force=force)
    if access.ready:
        await show(update, context, "✅ <b>دسترسی کامل است</b>\n\nبات مدیر است و اجازه حذف پیام‌های مرحله‌ای را دارد. جهان آماده استفاده است.", kb.access(True))
    else:
        await show(update, context, "🔒 <b>جهان در حالت محدود است</b>\n\nکمبود: " + access.missing_fa() + "\n\nاز تنظیمات گروه، بات را مدیر کنید و اجازه «حذف پیام‌ها» را فعال کنید. اجازه افزودن مدیر یا تغییر اطلاعات گروه لازم نیست.", kb.access(False))
    return access

async def health_page(update, context):
    access = await world_access.check(context.bot, update.effective_chat.id, force=True)
    country = await country_repo.by_chat(update.effective_chat.id)
    panel = await ui_state_repo.world(update.effective_chat.id)
    election = await election_repo.open_for_country(country["id"]) if country else None
    project = await project_repo.active(country["id"]) if country else None
    lines = [
        f"• دسترسی بات: {'کامل' if access.ready else 'ناقص — ' + access.missing_fa()}",
        f"• اتصال کشور: {'سالم' if country else 'هنوز کشوری ساخته نشده'}",
        f"• صفحه اصلی: {'ثبت شده' if panel else 'با نخستین نمایش ساخته می‌شود'}",
        f"• انتخابات فعال: {'بله' if election else 'خیر'}",
        f"• پروژه فعال: {'بله' if project else 'خیر'}",
        f"• قابلیت‌های اصلی: {'آماده' if access.ready else 'قفل ایمن'}",
    ]
    await show(update, context, "🩺 <b>بررسی وضعیت جهان</b>\n\n" + "\n".join(lines), kb.access(access.ready))

async def home(update, context):
    chat = update.effective_chat
    if chat.type not in GROUPS:
        await show(update, context, fa.PRIVATE, kb.private(context.bot.username or ""))
        return
    await group_repo.get_or_create(chat.id, chat.title or "سرزمین بی‌نام")
    access = await world_access.check(context.bot, chat.id)
    if not access.ready:
        await access_page(update, context)
        return
    row, count, leader = await facts(chat.id)
    p = await player(update)
    citizenship = await country_repo.citizenship(p.id) if row else None
    citizen = bool(citizenship and citizenship["is_active"] and int(citizenship["country_id"]) == int(row["id"]))
    if not row:
        await show(update, context, fa.HOME_EMPTY, kb.home(False, await is_admin(update, context)))
        return
    goal = "شهروند جذب کنید" if row["status"] == "forming" else "انتخابات رهبر را کامل کنید" if not row["president_player_id"] else "پروژه و اقتصاد کشور را رشد دهید"
    text = fa.HOME.format(name=escape(str(row["name"])), status=STATUS.get(row["status"], "نامشخص"), citizens=fmt.number(count), leader=escape(str(leader or "هنوز انتخاب نشده")), treasury=fmt.toman(row["treasury_toman"]), goal=goal)
    await show(update, context, text, kb.home(True, await is_admin(update, context), citizen))

async def country_page(update, context):
    row, count, leader = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    text = fa.COUNTRY.format(name=escape(str(row["name"])), government=GOV.get(row["government_type"], "نامشخص"), status=STATUS.get(row["status"], "نامشخص"), citizens=fmt.number(count), leader=escape(str(leader or "انتخاب نشده")), treasury=fmt.toman(row["treasury_toman"]), description=escape(str(row["description"])))
    await show(update, context, text, kb.country())

async def economy_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    resources = await country_repo.resources(row["id"])
    lines = "\n".join(f"• {ASSET.get(str(x['asset_code']), 'دارایی')}: {fmt.number(x['quantity'])}" for x in resources) or "هنوز منبعی ثبت نشده است."
    from telegram import InlineKeyboardMarkup
    markup=InlineKeyboardMarkup([[kb.b("📊 بودجه، رفاه و بحران","economyb","primary")],[kb.b("🏦 بانک مرکزی و شاخص‌ها","centralbank")],[kb.b("🏠 خانه جهان","home")]])
    await show(update, context, fa.ECONOMY.format(treasury=fmt.toman(row["treasury_toman"]), income=fmt.toman(row["daily_income_toman"]), expense=fmt.toman(row["daily_expense_toman"]), resources=lines), markup)


async def economy_b_page(update,context):
    row,_,_=await facts(update.effective_chat.id)
    if not row:raise ValueError("country_not_found")
    p=await player(update);v=await country_economy_b.view(int(row["id"]))
    if not v:
        await show(update,context,"📊 <b>اقتصاد روزانه کشور</b>\n\nپس از اجرای نخستین چرخه روزانه، گزارش اینجا نمایش داده می‌شود.",kb.country_economy_b(False,False));return
    roles=await db.fetch("SELECT o.role_code,p.first_name FROM country_offices o JOIN players p ON p.id=o.player_id WHERE o.country_id=$1 ORDER BY o.role_code",row["id"])
    role_names={"economy_minister":"وزیر اقتصاد","industry_minister":"وزیر صنعت","foreign_minister":"وزیر خارجه","army_commander":"فرمانده ارتش","intelligence_chief":"رئیس اطلاعات"}
    cabinet="، ".join(f"{role_names.get(str(x['role_code']),'مقام')}: {escape(str(x['first_name']))}" for x in roles) or "هنوز کسی منصوب نشده"
    crisis="بحران فعالی نیست ✅" if int(v["active_crises"] or 0)==0 else f"{fmt.number(v['active_crises'])} بحران فعال ⚠️"
    sat=int(v["satisfaction"] or 70);modifier=int(v["production_modifier_bp"] or 10000)
    text=(f"📊 <b>بودجه و وضعیت {escape(str(row['name']))}</b>\n\n"
          f"🙂 رضایت عمومی: <b>{fmt.number(sat)} از ۱۰۰</b>\n"
          f"🍞 کمبود غذا: <b>{int(v['food_shortage_bp'] or 0)/100:.1f}٪</b>\n"
          f"⚡ کمبود انرژی: <b>{int(v['energy_shortage_bp'] or 0)/100:.1f}٪</b>\n"
          f"🏭 ضریب تولید: <b>{modifier/100:.1f}٪</b>\n"
          f"🫶 رفاه: <b>{fmt.number(v['welfare_level'] or 0)}</b> · 🛡 آمادگی: <b>{fmt.number(v['defense_readiness'] or 0)}</b>\n"
          f"🚨 {crisis}\n\n"
          f"<b>تقسیم بودجه</b>\nرفاه {int(v['welfare_bp'])/100:.0f}٪ · تولید {int(v['production_bp'])/100:.0f}٪ · فناوری {int(v['technology_bp'])/100:.0f}٪\n"
          f"دفاع {int(v['defense_bp'])/100:.0f}٪ · اطلاعات {int(v['intelligence_bp'])/100:.0f}٪ · دیپلماسی {int(v['diplomacy_bp'])/100:.0f}٪ · اضطراری {int(v['emergency_bp'])/100:.0f}٪\n\n"
          f"👔 کابینه: {cabinet}\n\nبودجه از چرخه بعدی روی مصرف، رضایت و تولید واقعی اثر می‌گذارد.")
    can_manage=int(row["president_player_id"] or 0)==p.id or bool(await db.fetchval("SELECT 1 FROM country_offices WHERE country_id=$1 AND player_id=$2 AND role_code='economy_minister'",row["id"],p.id))
    await show(update,context,text,kb.country_economy_b(can_manage,int(row["president_player_id"] or 0)==p.id))

async def offices_page(update,context):
    row,_,_=await facts(update.effective_chat.id);p=await player(update)
    if not row or int(row["president_player_id"] or 0)!=p.id:raise PermissionError("president_required")
    people=await db.fetch("SELECT p.id player_id,p.first_name FROM citizenships c JOIN players p ON p.id=c.player_id WHERE c.country_id=$1 AND c.is_active AND p.id<>$2 ORDER BY c.joined_at LIMIT 5",row["id"],p.id)
    if not people:await answer(update.callback_query,"برای تشکیل کابینه، دست‌کم یک شهروند دیگر لازم است.",show_alert=True);return
    await show(update,context,"👔 <b>کابینه اولیه</b>\n\nروی نام و سمت موردنظر بزن. هر شهروند فقط یک سمت می‌گیرد و تغییرها در گزارش حسابرسی ثبت می‌شوند.",kb.offices(people))

async def central_bank_page(update,context):
    row,_,_=await facts(update.effective_chat.id)
    if not row:raise ValueError("country_not_found")
    v=await country_realism.policy_view(row["id"]);p=await player(update);president=row["president_player_id"]==p.id
    indicators=("هنوز گزارش روزانه محاسبه نشده است." if not v["indicator_date"] else f"تورم: <b>{int(v['inflation_bp'])/100:.1f}٪</b> · بیکاری: <b>{int(v['unemployment_bp'])/100:.1f}٪</b>\nرشد: <b>{int(v['growth_bp'])/100:+.1f}٪</b> · رضایت: <b>{v['satisfaction']}/۱۰۰</b>")
    text=f"🏦 <b>بانک مرکزی {escape(str(row['name']))}</b>\n\nنرخ بهره: <b>{int(v['interest_rate_bp'])/100:.1f}٪</b>\nهدف تورم: <b>{int(v['inflation_target_bp'])/100:.1f}٪</b>\nذخیره ارزی: <b>{fmt.usd(int(v['fx_reserve_cents']))}</b>\n\n{indicators}\n\nافزایش بهره معمولاً تورم را مهار می‌کند اما رشد را کندتر می‌کند. تصمیم امروز در گزارش فردا اثر می‌گذارد."
    await show(update,context,text,kb.central_bank(president))

async def citizens_page(update, context):
    row, count, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    people=await db.fetch("SELECT p.first_name,cs.migrant_until FROM citizenships cs JOIN players p ON p.id=cs.player_id WHERE cs.country_id=$1 AND cs.is_active ORDER BY cs.joined_at LIMIT 25",row["id"])
    names=[f"• {escape(str(x['first_name']))}"+(" · 🧳 مهاجر" if x["migrant_until"] and x["migrant_until"]>datetime.now(UTC) else "") for x in people]
    await show(update, context, fa.CITIZENS.format(count=fmt.number(count), members="\n".join(names) or "هنوز شهروندی ثبت نشده است."), kb.back("country"))

async def politics_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    election = await election_repo.open_for_country(row["id"])
    status = str(election["status"]) if election else None
    from packages.core.services.governance import rules_for
    rules=rules_for(str(row["government_type"]))
    state = "در این نظام، رهبر با انتخابات عمومی تعیین نمی‌شود." if not rules.public_elections else "انتخابات فعالی وجود ندارد." if not election else "مرحله نام‌نویسی نامزدها باز است." if status == "nominations" else "رأی‌گیری باز است."
    await show(update, context, fa.POLITICS.format(state=state), kb.politics(status,allowed=rules.public_elections))

async def project_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    project = await project_repo.active(row["id"])
    objective=await country_objectives.today(row["id"])
    latest = project or await db.fetchrow("SELECT * FROM national_projects WHERE country_id=$1 ORDER BY id DESC LIMIT 1", row["id"])
    body = "هنوز پروژه‌ای آغاز نشده است."
    if latest:
        status = await project_repo.status(latest["id"])
        body = "\n".join(f"• {ASSET.get(str(x['asset_code']), 'دارایی')}: {fmt.number(x['contributed_amount'])} از {fmt.number(x['required_amount'])}" for x in status)
        if latest["status"] == "completed": body = "✅ آخرین پروژه تکمیل شده و اثرش روی تولید فعال است.\n\n" + body
    daily=f"\n\n🎯 هدف کاری امروز کشور: {fmt.number(objective.progress)} از {fmt.number(objective.target)} شیفت · {fmt.number(objective.contributors)} مشارکت‌کننده"+(" ✅" if objective.complete else "")
    available=await national_project.available(row["id"])
    markup=kb.project(True) if project else kb.project(False,available)
    await show(update, context, "🏗 <b>پروژه‌ها و هدف ملی</b>\n\n" + body + daily + "\n\nپروژه تکمیل‌شده بازده شغل مرتبط را واقعاً افزایش می‌دهد.", markup)

async def trade_page(update,context):
 row,_,_=await facts(update.effective_chat.id)
 if not row:raise ValueError("country_not_found")
 p=await player(update);v=await country_trade.overview(int(row["id"]))
 if not v:
  from packages.core import db
  await db.execute("INSERT INTO country_international_reputation(country_id) VALUES($1) ON CONFLICT DO NOTHING",row["id"]);v=await country_trade.overview(int(row["id"]))
 can_manage=int(row["president_player_id"] or 0)==p.id or bool(await db.fetchval("SELECT 1 FROM country_offices WHERE country_id=$1 AND player_id=$2 AND role_code=ANY($3::text[])",row["id"],p.id,["economy_minister","foreign_minister"]))
 text=(f"🌐 <b>تجارت و دیپلماسی {escape(str(row['name']))}</b>\n\n"
       f"⭐ اعتبار بین‌المللی: <b>{fmt.number(v['score'])} از ۱۰۰</b>\n"
       f"📦 قراردادهای باز: <b>{fmt.number(v['open_contracts'])}</b>\n"
       f"✅ قراردادهای موفق: <b>{fmt.number(v['fulfilled_contracts'])}</b>\n"
       f"🤝 روابط رسمی: <b>{fmt.number(v['active_relations'])}</b>\n"
       f"⛔ تحریم‌های مرتبط: <b>{fmt.number(v['sanctions'])}</b>\n\n"
       "منابع پیشنهاددهنده هنگام ساخت قرارداد وارد Escrow می‌شوند. پذیرش، هر دو دارایی را در یک تراکنش جابه‌جا می‌کند؛ انقضا هم دارایی را خودکار پس می‌دهد.")
 await show(update,context,text,kb.trade_home(can_manage))

async def callback(update, context):
    query = update.callback_query
    if not query: return
    action = (query.data or "")[3:]
    try:
        if action == "access:why":
            await answer(query)
            await show(update, context, "📘 <b>چرا مدیر؟</b>\n\nفقط برای حذف پیام‌های مرحله‌ای باید بات مدیر باشد. ویرایش پیام‌های خود بات نیاز به مجوز جداگانه ندارد.\n\nمسیر: اطلاعات گروه ← ویرایش ← مدیران ← افزودن مدیر ← فعال‌کردن «حذف پیام‌ها».\n\nتلگرام پیوند قابل‌اتکایی برای بازکردن مستقیم صفحه ارتقای مدیر ارائه نمی‌کند؛ بنابراین دکمه جعلی نمایش داده نمی‌شود.", kb.access(False))
            return
        if action == "access:check":
            await answer(query)
            access = await access_page(update, context, force=True)
            if access.ready:
                await home(update, context)
            return
        if action == "health":
            await answer(query)
            await health_page(update, context)
            return
        if update.effective_chat.type in GROUPS and is_mutating(action):
            access = await world_access.check(context.bot, update.effective_chat.id)
            if not access.ready:
                await answer(query, "عملیات قفل است: " + access.missing_fa(), show_alert=True)
                await access_page(update, context)
                return
        if action == "home":
            await answer(query, ); context.chat_data.pop(FLOW, None); await home(update, context)
        elif action == "guide":
            await answer(query, ); row, _, _ = await facts(update.effective_chat.id) if update.effective_chat.type in GROUPS else (None, 0, None); await show(update, context, fa.GUIDE if row else fa.GUIDE_EMPTY, kb.back())
        elif action == "country": await answer(query, ); await country_page(update, context)
        elif action == "economy": await answer(query, ); await economy_page(update, context)
        elif action == "economyb": await answer(query); await economy_b_page(update,context)
        elif action == "centralbank": await answer(query); await central_bank_page(update,context)
        elif action.startswith("budget:"):
            row,_,_=await facts(update.effective_chat.id);p=await player(update);preset=action.split(":",1)[1]
            await country_economy_b.set_budget_preset(int(row["id"]),p.id,preset,f"budget:{row['id']}:{p.id}:{preset}:{uuid4().hex[:12]}")
            await answer(query,"بودجه ثبت شد؛ اثرش از چرخه روزانه بعدی دیده می‌شود.",show_alert=True);await economy_b_page(update,context)
        elif action == "offices":
            await answer(query);await offices_page(update,context)
        elif action.startswith("appoint:"):
            _,role,target=action.split(":",2);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            await country_economy_b.appoint(int(row["id"]),p.id,role,int(target),f"appoint:{row['id']}:{role}:{uuid4().hex[:12]}")
            await answer(query,"انتصاب ثبت شد.",show_alert=True);await economy_b_page(update,context)
        elif action.startswith("rate:"):
            row,_,_=await facts(update.effective_chat.id);p=await player(update);delta=100 if action.endswith("up") else -100
            value=await country_realism.set_interest(row["id"],p.id,delta)
            if value is None:await answer(query,"فقط رهبر کشور می‌تواند نرخ را در محدوده مجاز تغییر دهد.",show_alert=True);return
            await answer(query,f"نرخ بهره به {value/100:.1f}٪ تغییر کرد.",show_alert=True);await central_bank_page(update,context)
        elif action == "reserve:buy":
            row,_,_=await facts(update.effective_chat.id);p=await player(update)
            try:cents=await country_realism.buy_reserve(row["id"],p.id)
            except ValueError:await answer(query,"فقط رهبر و با خزانه کافی می‌تواند ذخیره بخرد.",show_alert=True);return
            await answer(query,f"{fmt.usd(cents)} به ذخیره ارزی افزوده شد.",show_alert=True);await central_bank_page(update,context)
        elif action == "citizens": await answer(query, ); await citizens_page(update, context)
        elif action == "politics": await answer(query, ); await politics_page(update, context)
        elif action == "project": await answer(query, ); await project_page(update, context)
        elif action == "trade": await answer(query); await trade_page(update,context)
        elif action == "tradenew":
            row,_,_=await facts(update.effective_chat.id);rows=await country_trade.countries_except(int(row["id"]));await answer(query)
            await show(update,context,"➕ <b>قرارداد تجاری تازه</b>\n\nکشور مقصد را انتخاب کن. در قدم بعد یکی از پیشنهادهای متعادل و محدود را می‌بینی.",kb.trade_countries(rows))
        elif action.startswith("tradeto:"):
            target=int(action.split(":")[1]);presets=get_config().section("country_trade.contracts.presets");await answer(query)
            await show(update,context,"📦 <b>نوع قرارداد</b>\n\nمنبع پیشنهادی همان لحظه از کشور شما کم و تا پذیرش یا انقضا در Escrow نگه داشته می‌شود.",kb.trade_presets(target,presets))
        elif action.startswith("tradepreset:"):
            _,target,preset=action.split(":",2);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            contract=await country_trade.create_contract(int(row["id"]),int(target),p.id,preset,f"trade-create:{row['id']}:{uuid4().hex}")
            await answer(query,f"قرارداد #{int(contract['id'])} ثبت شد و منبع در Escrow قرار گرفت.",show_alert=True);await trade_page(update,context)
        elif action == "tradein":
            row,_,_=await facts(update.effective_chat.id);rows=await country_trade.incoming(int(row["id"]));await answer(query)
            body="پیشنهادی در انتظار نیست." if not rows else "هر پذیرش، منابع دو کشور را اتمیک جابه‌جا می‌کند."
            await show(update,context,"📥 <b>پیشنهادهای دریافتی</b>\n\n"+body,kb.incoming_trade(rows))
        elif action == "tradeout":
            row,_,_=await facts(update.effective_chat.id);rows=await country_trade.outgoing(int(row["id"]));await answer(query)
            body="قرارداد بازی نداری." if not rows else "لغو، دارایی نگه‌داری‌شده را از Escrow پس می‌دهد و کمی از اعتبار کم می‌کند."
            await show(update,context,"📤 <b>پیشنهادهای من</b>\n\n"+body,kb.outgoing_trade(rows))
        elif action.startswith("tradecancel:"):
            cid=int(action.split(":")[1]);p=await player(update);ok=await country_trade.cancel_contract(cid,p.id,f"trade-cancel:{cid}:{uuid4().hex}")
            await answer(query,"قرارداد لغو و دارایی Escrow پس داده شد." if ok else "این قرارداد دیگر قابل لغو نیست.",show_alert=True);await trade_page(update,context)
        elif action == "traderef":
            rows=await country_trade.recent_reference();await answer(query)
            labels={"IRT":"تومان","food":"غذا","energy":"انرژی","oil":"نفت","minerals":"معدن","technology":"فناوری"}
            lines=[f"• {labels.get(str(r['offered_asset']),r['offered_asset'])} ← {labels.get(str(r['requested_asset']),r['requested_asset'])}: نسبت میانگین {r['average_ratio']} · {r['trades']} معامله" for r in rows]
            await show(update,context,"📈 <b>نرخ‌های مرجع بازار کشورها</b>\n\n"+("هنوز معامله تکمیل‌شده‌ای برای نرخ مرجع نداریم." if not lines else "\n".join(lines))+"\n\nاین اعداد فقط تاریخچه واقعی بازی‌اند و قیمت تضمینی نیستند.",kb.back("trade"))
        elif action.startswith("tradeaccept:"):
            cid=int(action.split(":")[1]);p=await player(update);result=await country_trade.accept_contract(cid,p.id,f"trade-accept:{cid}:{uuid4().hex}")
            await answer(query,f"قرارداد انجام شد؛ تعرفه {result['tariff_bp']/100:.1f}٪ بود.",show_alert=True);await trade_page(update,context)
        elif action == "relations":
            row,_,_=await facts(update.effective_chat.id);pending=await country_trade.pending_relations(int(row["id"]));rows=await country_trade.countries_except(int(row["id"]));await answer(query)
            if pending:
                await show(update,context,"🤝 <b>پیشنهادهای دیپلماتیک دریافتی</b>\n\nپیشنهادها ۲۴ ساعت اعتبار دارند. پذیرش، تعرفه تجارت بعدی را تغییر می‌دهد.",kb.pending_relations(pending))
            else:
                await show(update,context,"🤝 <b>روابط خارجی</b>\n\nدوستی، شراکت تجاری و اتحاد به پذیرش کشور مقابل نیاز دارند و تعرفه تجارت را کاهش می‌دهند.",kb.relations_countries(rows))
        elif action.startswith("relmenu:"):
            target=int(action.split(":")[1]);await answer(query);await show(update,context,"🤝 <b>اقدام دیپلماتیک</b>\n\nهمکاری با پذیرش دوطرفه فعال می‌شود. تحریم، تجارت مستقیم را می‌بندد و از اعتبار کشور تحریم‌کننده هم کم می‌کند.",kb.relation_actions(target))
        elif action.startswith("relprop:"):
            _,target,status=action.split(":",2);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            await country_trade.propose_relation(int(row["id"]),int(target),p.id,status,f"relation-propose:{row['id']}:{target}:{uuid4().hex}")
            await answer(query,"پیشنهاد رسمی ثبت شد و ۲۴ ساعت اعتبار دارد.",show_alert=True);await trade_page(update,context)
        elif action.startswith("relaccept:"):
            target=int(action.split(":")[1]);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            await country_trade.accept_relation(int(row["id"]),target,p.id,f"relation-accept:{row['id']}:{target}:{uuid4().hex}")
            await answer(query,"رابطه رسمی شد و تعرفه‌های بعدی بر همین اساس محاسبه می‌شوند.",show_alert=True);await trade_page(update,context)
        elif action.startswith("sanction:"):
            target=int(action.split(":")[1]);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            await country_trade.impose_sanction(int(row["id"]),target,p.id,f"sanction:{row['id']}:{target}:{uuid4().hex}")
            await answer(query,"تحریم فعال شد؛ تجارت مستقیم بسته و از اعتبار کشور شما هم کم شد.",show_alert=True);await trade_page(update,context)
        elif action.startswith("sanctionlift:"):
            target=int(action.split(":")[1]);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            ok=await country_trade.lift_sanction(int(row["id"]),target,p.id,f"sanction-lift:{row['id']}:{target}:{uuid4().hex}")
            await answer(query,"تحریم برداشته شد." if ok else "تحریم فعالی از طرف کشور شما وجود نداشت.",show_alert=True);await trade_page(update,context)
        elif action == "aid":
            row,_,_=await facts(update.effective_chat.id);rows=await db.fetch("""SELECT DISTINCT c.id,c.name FROM countries c JOIN country_crises x ON x.country_id=c.id AND x.status='active' WHERE c.id<>$1 ORDER BY c.name LIMIT 50""",row["id"]);await answer(query)
            await show(update,context,"🆘 <b>کمک اضطراری</b>\n\nفقط کشورهایی که بحران فعال دارند نمایش داده می‌شوند. کمک مستقیماً و اتمیک منتقل می‌شود و اعتبار بین‌المللی می‌سازد.",kb.aid_countries(rows))
        elif action.startswith("aidto:"):
            target=int(action.split(":")[1]);await answer(query);await show(update,context,"🆘 <b>نوع کمک</b>\n\nیکی از بسته‌های محدود را انتخاب کن.",kb.aid_assets(target))
        elif action.startswith("aidsend:"):
            _,target,asset=action.split(":",2);row,_,_=await facts(update.effective_chat.id);p=await player(update)
            amount=await country_trade.send_aid(int(row["id"]),int(target),p.id,asset,f"aid:{row['id']}:{target}:{asset}:{uuid4().hex}")
            await answer(query,f"کمک به مقدار {fmt.number(amount)} ثبت و منتقل شد.",show_alert=True);await trade_page(update,context)
        elif action == "create":
            if update.effective_chat.type not in GROUPS or not await is_admin(update, context):
                await answer(query, "فقط مدیر گروه می‌تواند ساخت را شروع کند.", show_alert=True); return
            if await country_repo.by_chat(update.effective_chat.id):
                await answer(query, "این گروه از قبل کشور دارد.", show_alert=True); return
            await answer(query, ); context.chat_data[FLOW] = {"step":"name", "owner":query.from_user.id, "panel":query.message.message_id}; await show(update, context, fa.WIZARD_NAME, kb.cancel())
        elif action.startswith("gov:"):
            flow = context.chat_data.get(FLOW)
            if not flow or flow.get("owner") != query.from_user.id or flow.get("step") != "government":
                await answer(query, "فرایند ساخت منقضی شده است؛ دوباره آغاز کن.", show_alert=True); return
            code=action.split(":",1)[1]; detail=fa.GOVERNMENT_DETAILS.get(code)
            if not detail: await answer(query,"نوع حکومت معتبر نیست.",show_alert=True);return
            await answer(query); await show(update,context,fa.GOV_CONFIRM.format(title=detail[0],description=detail[1]),kb.government_confirm(code))
        elif action == "govback":
            flow=context.chat_data.get(FLOW)
            if not flow or flow.get("owner") != query.from_user.id: await answer(query,"فرایند ساخت منقضی شده است.",show_alert=True);return
            await answer(query);flow["step"]="government";await show(update,context,fa.WIZARD_GOV,kb.governments())
        elif action.startswith("govok:"):
            flow=context.chat_data.get(FLOW);code=action.split(":",1)[1]
            if not flow or flow.get("owner") != query.from_user.id or flow.get("step") != "government" or code not in fa.GOVERNMENT_DETAILS:
                await answer(query,"فرایند ساخت منقضی شده است؛ دوباره آغاز کن.",show_alert=True);return
            await answer(query);flow["government"]=code;flow["step"]="description";await show(update,context,fa.WIZARD_DESC,kb.cancel())
        elif action == "migration":
            p=await player(update);current=await country_repo.citizenship(p.id)
            if not current:await answer(query,"ابتدا شهروند یک کشور شو.",show_alert=True);return
            rows=await db.fetch("SELECT id,name FROM countries ORDER BY name LIMIT 100");await answer(query)
            await show(update,context,"✈️ <b>تغییر کشور</b>\n\nعوارض هنگام تکمیل مهاجرت: ۵٪ دارایی شخصی، حداقل ۵۰۰ هزار و حداکثر ۵۰ میلیون تومان؛ مبلغ به خزانه کشور مبدأ می‌رود.\n\nمحدودیت تغییر: هر ۳۰ روز. اگر مقصد رهبر داشته باشد، درخواست ۷۲ ساعت برای تأیید اعتبار دارد. پس از مهاجرت، نشان مهاجر ۳۰ روز و محدودیت سیاسی ۱۴ روز فعال است.",kb.migration_countries(rows,current["country_id"]))
        elif action.startswith("migrate:"):
            p=await player(update);dest=int(action.split(":")[1]);qte=await migration.quote(p.id,dest)
            if not qte:await answer(query,"مقصد معتبر نیست.",show_alert=True);return
            fee=migration.exit_fee(int(qte["wallet_toman"])+int(qte["savings_toman"]));row=await migration.request(p.id,dest)
            await answer(query,(f"مهاجرت انجام شد و {fmt.toman(fee)} به خزانه کشور مبدأ رفت." if row["status"]=='approved' else f"درخواست ثبت شد؛ رهبر مقصد تا ۷۲ ساعت فرصت تأیید دارد. عوارض {fmt.toman(fee)} فقط هنگام تأیید کسر می‌شود."),show_alert=True);await home(update,context)
        elif action == "migration_review":
            p=await player(update);row=await country_repo.by_chat(update.effective_chat.id)
            if not row or row["president_player_id"]!=p.id:await answer(query,"فقط رهبر مقصد دسترسی دارد.",show_alert=True);return
            rows=await migration.pending_for_country(row["id"]);await answer(query);await show(update,context,"📥 <b>درخواست‌های مهاجرت</b>\n\n"+("درخواستی وجود ندارد." if not rows else "پذیرش، عوارض را به کشور مبدأ منتقل و مهاجر را وارد کشور می‌کند."),kb.migration_review(rows))
        elif action.startswith("migaccept:"):
            p=await player(update);await migration.approve(int(action.split(":")[1]),p.id);await answer(query,"مهاجر پذیرفته شد.",show_alert=True);await home(update,context)
        elif action.startswith("migreject:"):
            p=await player(update);ok=await migration.reject(int(action.split(":")[1]),p.id);await answer(query,"درخواست رد شد." if ok else "درخواست قابل رد نیست.",show_alert=True);await home(update,context)
        elif action == "subscription":
            await answer(query); view=await commerce.subscription_view(update.effective_chat.id)
            if not view: raise ValueError("group_not_found")
            if view["ad_free_until"] and view["ad_free_until"]>datetime.now(UTC):
                await show(update,context,f"🛡 <b>اشتراک رفاهی کشور فعال است</b>\n\nاعتبار تا: <b>{view['ad_free_until'].strftime('%Y-%m-%d %H:%M UTC')}</b>\n\n✅ تبلیغات عمومی گروه و بات حذف شده است.\n✅ گزارش‌های اقتصادی و سیاسی کامل در دسترس‌اند.\n✅ یادآوری‌های شیفت، پروژه و بحران فعال‌اند.\n\nاین اشتراک هیچ قدرت اقتصادی یا سیاسی اضافه نمی‌کند.",kb.back());return
            rnd=await commerce.ensure_round(update.effective_chat.id);target=int(rnd["target_stars"]);remaining=target-int(rnd["collected_stars"])
            treasury=int(view["treasury_toman"] or 0);citizens=int(view["citizens"] or 0);price=commerce.treasury_price(treasury,citizens)
            await show(update,context,f"🛡 <b>اشتراک رفاهی کشور — ۳۰ روز</b>\n\n<b>امکانات اشتراک</b>\n• حذف تبلیغات عمومی از گروه کشور و پیام‌های مرتبط بات\n• گزارش اقتصادی و سیاسی کامل‌تر با جزئیات بودجه، کمبود، رضایت و بحران\n• یادآوری هوشمند برای شیفت‌ها، پروژه ملی و بحران‌های فعال\n• بدون افزایش درآمد، منابع، قدرت سیاسی یا شانس برد؛ بازی برای همه منصفانه می‌ماند\n\nجمعیت: <b>{citizens}</b> شهروند · قیمت: <b>{target} ⭐</b>\nپیشرفت مشارکت: <b>{rnd['collected_stars']} از {target} ⭐</b>\nهر عضو می‌تواند بخشی از هزینه را بپردازد؛ پس از تکمیل هدف، اشتراک برای کل کشور فعال می‌شود.\n\nخرید از خزانه: <b>{fmt.toman(price)}</b> (۲۰٪ خزانه + یک میلیون برای هر شهروند، کف ۲۰ میلیون و سقف یک میلیارد).",kb.subscription(int(rnd["id"]),remaining))
        elif action.startswith("substar:"):
            _,rid,amount=action.split(":");payload,stars=await commerce.subscription_invoice(int(rid),query.from_user.id,int(amount));await answer(query)
            await context.bot.send_invoice(chat_id=update.effective_chat.id,title="مشارکت اشتراک بدون تبلیغ",description=f"{stars} استار برای اشتراک ۳۰روزه کل کشور: حذف تبلیغات، گزارش کامل و یادآوری هوشمند؛ بدون قدرت اقتصادی",payload=payload,currency="XTR",prices=[LabeledPrice("سهم اشتراک",stars)],provider_token="")
        elif action == "subtreasury":
            p=await player(update);price=await commerce.buy_with_treasury(update.effective_chat.id,p.id);await answer(query,f"اشتراک با {fmt.toman(price)} از خزانه فعال شد.",show_alert=True);await home(update,context)
        elif action == "join":
            p = await player(update); joined = await countries.join_country(chat_id=update.effective_chat.id, player_id=p.id); await answer(query, "شهروند شدی." if joined else "از قبل شهروندی.", show_alert=True); await home(update, context)
        elif action == "leave":
            await answer(query,"برای جلوگیری از دورزدن عوارض و محدودیت زمانی، خروج مستقیم بسته است؛ از بخش «مهاجرت» کشور مقصد را انتخاب کن.",show_alert=True)
        elif action.startswith("donate:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            citizenship = await country_repo.citizenship(p.id)
            if not citizenship or not citizenship["is_active"] or int(citizenship["country_id"]) != int(row["id"]): raise PermissionError("citizen_required")
            await economy.transfer(p.id, row["id"], "IRT", int(action.split(":", 1)[1]), reason="donation", idempotency_key=f"world-donate:{p.id}:{query.id}")
            await answer(query, "کمک مالی ثبت شد.", show_alert=True); await country_page(update, context)
        elif action == "estart":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            await elections.start(row["id"], p.id); await answer(query, "انتخابات آغاز شد.", show_alert=True); await politics_page(update, context)
        elif action == "nominate":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "nominations": await answer(query, "مرحله نام‌نویسی باز نیست.", show_alert=True); return
            accepted = await elections.nominate(election["id"], p.id, update.effective_chat.id, query.message.message_id)
            await answer(query, "نامزدی ثبت شد." if accepted else "قبلاً نامزد شده‌ای.", show_alert=True); await politics_page(update, context)
        elif action == "votehelp":
            row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "voting": await answer(query, "رأی‌گیری هنوز باز نشده است.", show_alert=True); return
            rows = await db.fetch("SELECT ec.player_id,p.first_name FROM election_candidates ec JOIN players p ON p.id=ec.player_id WHERE ec.election_id=$1 ORDER BY ec.created_at", election["id"])
            if not rows: await answer(query, "نامزدی برای رأی‌دادن وجود ندارد.", show_alert=True); return
            await answer(query, ); await show(update, context, "🗳 <b>انتخاب رهبر</b>\n\nنامزد موردنظر را انتخاب کن. رأی فقط یک‌بار ثبت می‌شود.", kb.candidates(rows))
        elif action.startswith("vote:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            election = await election_repo.open_for_country(row["id"])
            if not election or election["status"] != "voting": await answer(query, "رأی‌گیری باز نیست.", show_alert=True); return
            accepted = await elections.vote(election["id"], p.id, int(action.split(":", 1)[1])); await answer(query, "رأی ثبت شد." if accepted else "قبلاً رأی داده‌ای.", show_alert=True); await politics_page(update, context)
        elif action.startswith("pstart:"):
            p=await player(update);row,_,_=await facts(update.effective_chat.id)
            if not row:raise ValueError("country_not_found")
            project_key=action.split(":",1)[1];await national_project.start(row["id"],p.id,project_key);await answer(query,"پروژه ملی آغاز شد.",show_alert=True);await project_page(update,context)
        elif action.startswith("ptreasury:"):
            p=await player(update);row,_,_=await facts(update.effective_chat.id)
            if not row:raise ValueError("country_not_found")
            project=await project_repo.active(row["id"])
            if not project:await answer(query,"پروژه فعالی وجود ندارد.",show_alert=True);return
            _,asset,amount=action.split(":");accepted,done=await national_project.treasury_contribute(project["id"],p.id,asset,int(amount),f"treasury-project:{p.id}:{query.id}")
            await answer(query,f"{fmt.number(accepted)} واحد از دارایی کشور به پروژه رسید."+(" پروژه تکمیل شد!" if done else ""),show_alert=True);await project_page(update,context)
        elif action.startswith("pcon:"):
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            project = await project_repo.active(row["id"])
            if not project: await answer(query, "پروژه فعالی وجود ندارد.", show_alert=True); return
            _, asset, amount = action.split(":")
            accepted, done = await national_project.contribute(project["id"], p.id, asset, int(amount), f"world-project:{p.id}:{query.id}")
            await answer(query, (f"{fmt.number(accepted)} واحد ثبت شد." if accepted else "نیاز این بخش قبلاً تکمیل شده است.") + (" پروژه تکمیل شد!" if done else ""), show_alert=True); await project_page(update, context) if not done else await home(update, context)
        elif action == "polls": await answer(query, "هنوز نظرسنجی فعالی نیست.", show_alert=True)
        else: await answer(query, "این دکمه قدیمی شده است؛ صفحه را تازه‌سازی کن.", show_alert=True)
    except (ValueError, PermissionError, TypeError, KeyError, AttributeError) as exc:
        await answer(query, ERRORS.get(str(exc), "شرایط این کار کامل نیست؛ راهنما را بخوان."), show_alert=True)

async def text(update, context):
    message, chat = update.effective_message, update.effective_chat
    if not message or not chat: return
    if chat.type not in GROUPS: await home(update, context); return
    flow = context.chat_data.get(FLOW)
    if not flow or update.effective_user.id != flow.get("owner"):
        await home(update, context); return
    value = (message.text or "").strip()
    access = await world_access.check(context.bot, chat.id)
    if not access.ready:
        context.chat_data.pop(FLOW, None)
        await access_page(update, context)
        return
    try:
        await message.delete()
    except (BadRequest, Forbidden):
        if await world_access_repo.claim_warning(chat.id, "delete-failed"):
            await message.reply_text("پیام مرحله‌ای حذف نشد؛ فرایند ادامه دارد و دسترسی در بررسی بعدی دوباره کنترل می‌شود.")
    if flow["step"] == "name":
        from packages.core.services.content_filter import inspect
        if not inspect(value).allowed:
            await msg.reply_text(fa.CONTENT_REJECTED); return
        if not 3 <= len(value) <= 80:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="نام باید بین ۳ تا ۸۰ نویسه باشد. دوباره نام را بفرست.", reply_markup=kb.cancel()); return
        flow["name"] = value; flow["step"] = "government"
        await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text=fa.WIZARD_GOV, reply_markup=kb.governments()); return
    if flow["step"] == "description":
        from packages.core.services.content_filter import inspect
        if not inspect(value).allowed:
            await msg.reply_text(fa.CONTENT_REJECTED); return
        if not 10 <= len(value) <= 500:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="معرفی باید بین ۱۰ تا ۵۰۰ نویسه باشد. دوباره معرفی را بفرست.", reply_markup=kb.cancel()); return
        p = await player(update)
        try:
            await countries.create_country(chat_id=chat.id, chat_title=chat.title or "", player_id=p.id, name=flow["name"], government=flow["government"], description=value)
        except (ValueError, PermissionError) as exc:
            context.chat_data.pop(FLOW, None)
            await show(update, context, f"ساخت کشور انجام نشد: {ERRORS.get(str(exc), 'اطلاعات معتبر نبود.')}\n\nاز صفحه اصلی دوباره تلاش کن.", kb.back()); return
        context.chat_data.pop(FLOW, None); await home(update, context)

async def precheckout(update,context):
 q=update.pre_checkout_query;ok=await commerce.precheckout(q.invoice_payload,q.from_user.id,q.total_amount);await q.answer(ok=ok,error_message=None if ok else "صورتحساب نامعتبر یا منقضی شده است.")
async def successful_payment(update,context):
 payment=update.effective_message.successful_payment
 if not payment:return
 purpose=await commerce.settle(payment.invoice_payload,update.effective_user.id,payment.total_amount,payment.telegram_payment_charge_id,payment.provider_payment_charge_id or None)
 await update.effective_message.reply_text("✅ سهم شما ثبت شد. با تکمیل هدف جمعیت‌محور، اشتراک ۳۰روزه گروه فعال می‌شود." if purpose=="subscription" else "✅ پرداخت ثبت شد.")
def register(app):
    app.add_handler(CallbackQueryHandler(callback, pattern=r"^tw:"))
    app.add_handler(PreCheckoutQueryHandler(precheckout))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment))
    app.add_handler(MessageHandler(filters.TEXT, text))