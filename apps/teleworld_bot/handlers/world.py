"""کنترل‌گر یک‌پیامی، فارسی و دکمه‌محور جهان گروهی."""
from __future__ import annotations
from uuid import uuid4
from html import escape
from telegram.constants import ChatMemberStatus, ChatType
from telegram.error import BadRequest, Forbidden
from telegram.ext import CallbackQueryHandler, MessageHandler, filters
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core import db
from packages.core.repositories import country_repo, election_repo, group_repo, player_repo, project_repo, ui_state_repo, world_access_repo
from packages.core.services import country as countries, economy, elections, national_project
from packages.core.services import world_access
from packages.core.utils import fmt

GROUPS = {ChatType.GROUP, ChatType.SUPERGROUP}
FLOW = "world_creation"
STATUS = {"forming":"در حال ساخت", "temporary":"موقت", "official":"رسمی"}
GOV = {"republic":"جمهوری", "monarchy":"پادشاهی", "federal":"فدرال", "council":"شورایی"}
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

MUTATING = {"create", "join", "leave", "estart", "nominate", "pstart"}

def is_mutating(action: str) -> bool:
    return action in MUTATING or action.startswith(("donate:", "vote:", "pcon:", "gov:"))

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
    await show(update, context, fa.ECONOMY.format(treasury=fmt.toman(row["treasury_toman"]), income=fmt.toman(row["daily_income_toman"]), expense=fmt.toman(row["daily_expense_toman"]), resources=lines), kb.back())

async def citizens_page(update, context):
    row, count, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    ids = await country_repo.citizens(row["id"])
    names = [f"• {escape(str(await db.fetchval('SELECT first_name FROM players WHERE id=$1', pid) or 'شهروند'))}" for pid in ids[:25]]
    await show(update, context, fa.CITIZENS.format(count=fmt.number(count), members="\n".join(names) or "هنوز شهروندی ثبت نشده است."), kb.back("country"))

async def politics_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    election = await election_repo.open_for_country(row["id"])
    status = str(election["status"]) if election else None
    state = "انتخابات بازی وجود ندارد." if not election else "مرحله نام‌نویسی نامزدها باز است." if status == "nominations" else "رأی‌گیری باز است."
    await show(update, context, fa.POLITICS.format(state=state), kb.politics(status))

async def project_page(update, context):
    row, _, _ = await facts(update.effective_chat.id)
    if not row: raise ValueError("country_not_found")
    project = await project_repo.active(row["id"])
    latest = project or await db.fetchrow("SELECT * FROM national_projects WHERE country_id=$1 ORDER BY id DESC LIMIT 1", row["id"])
    body = "هنوز پروژه‌ای آغاز نشده است."
    if latest:
        status = await project_repo.status(latest["id"])
        body = "\n".join(f"• {ASSET.get(str(x['asset_code']), 'دارایی')}: {fmt.number(x['contributed_amount'])} از {fmt.number(x['required_amount'])}" for x in status)
        if latest["status"] == "completed": body = "✅ این پروژه ملی تکمیل شده است.\n\n" + body
    markup = kb.project(True) if project else kb.back()
    if latest is None: markup = kb.project(False)
    await show(update, context, "🏗 <b>پروژه ملی</b>\n\n" + body + "\n\nهر شهروند فقط به اندازه نیاز باقی‌مانده کمک می‌کند.", markup)

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
        elif action == "citizens": await answer(query, ); await citizens_page(update, context)
        elif action == "politics": await answer(query, ); await politics_page(update, context)
        elif action == "project": await answer(query, ); await project_page(update, context)
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
            await answer(query, ); flow["government"] = action.split(":", 1)[1]; flow["step"] = "description"; await show(update, context, fa.WIZARD_DESC, kb.cancel())
        elif action == "join":
            p = await player(update); joined = await countries.join_country(chat_id=update.effective_chat.id, player_id=p.id); await answer(query, "شهروند شدی." if joined else "از قبل شهروندی.", show_alert=True); await home(update, context)
        elif action == "leave":
            p = await player(update); left = await countries.leave_country(chat_id=update.effective_chat.id, player_id=p.id); await answer(query, "از کشور خارج شدی." if left else "شهروند این کشور نبودی.", show_alert=True); await home(update, context)
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
        elif action == "pstart":
            p = await player(update); row, _, _ = await facts(update.effective_chat.id)
            if not row: raise ValueError("country_not_found")
            if await db.fetchval("SELECT 1 FROM national_projects WHERE country_id=$1", row["id"]): await answer(query, "پروژه ملی این کشور قبلاً آغاز شده است و تکرارشدنی نیست.", show_alert=True); return
            await national_project.start(row["id"], p.id); await answer(query, "پروژه ملی آغاز شد.", show_alert=True); await project_page(update, context)
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
        if not 3 <= len(value) <= 80:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="نام باید بین ۳ تا ۸۰ نویسه باشد. دوباره نام را بفرست.", reply_markup=kb.cancel()); return
        flow["name"] = value; flow["step"] = "government"
        await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text=fa.WIZARD_GOV, reply_markup=kb.governments()); return
    if flow["step"] == "description":
        if not 10 <= len(value) <= 500:
            await context.bot.edit_message_text(chat_id=chat.id, message_id=flow["panel"], text="معرفی باید بین ۱۰ تا ۵۰۰ نویسه باشد. دوباره معرفی را بفرست.", reply_markup=kb.cancel()); return
        p = await player(update)
        try:
            await countries.create_country(chat_id=chat.id, chat_title=chat.title or "", player_id=p.id, name=flow["name"], government=flow["government"], description=value)
        except (ValueError, PermissionError) as exc:
            context.chat_data.pop(FLOW, None)
            await show(update, context, f"ساخت کشور انجام نشد: {ERRORS.get(str(exc), 'اطلاعات معتبر نبود.')}\n\nاز صفحه اصلی دوباره تلاش کن.", kb.back()); return
        context.chat_data.pop(FLOW, None); await home(update, context)

def register(app):
    app.add_handler(CallbackQueryHandler(callback, pattern=r"^tw:"))
    app.add_handler(MessageHandler(filters.TEXT, text))