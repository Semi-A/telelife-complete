"""Unified, Persian, single-message TeleLife experience."""
from __future__ import annotations
from datetime import UTC,datetime
from uuid import uuid4
from html import escape
from telegram import Update
from telegram.ext import CallbackQueryHandler,CommandHandler,ContextTypes,MessageHandler,filters
from apps.telelife_bot.handlers.common import guard_callback,resolve
from apps.telelife_bot.handlers import ux
from apps.telelife_bot.handlers.panel import retire_message, show
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.bot.start_limit import allow_start
from packages.core.repositories import country_repo,player_repo,progression_repo,production_repo,ui_state_repo
from packages.core.services import daily,life_progression,migration,missions,personal_economy,production,progression,resource_economy,unlocks,usd_market,xp,referrals
from packages.core.utils import fmt
from packages.core.utils.fa_labels import government_name

JOB_FA={"farmer":"کشاورز","miner":"معدن‌کار","trader":"بازرگان","journalist":"روزنامه‌نگار","doctor":"پزشک","programmer":"برنامه‌نویس","engineer":"مهندس"}
ASSET_FA={"IRT":"تومان","USD":"دلار","food":"محصول کشاورزی","minerals":"مواد معدنی","technology":"فناوری","energy":"انرژی"}
SHIFT_FA={"safe":"امن","balanced":"متعادل","national":"ملی","private":"خصوصی"}
SKILL_FA={"agriculture":"کشاورزی","extraction":"استخراج","commerce":"تجارت","media":"رسانه","medicine":"پزشکی","software":"نرم‌افزار","engineering":"مهندسی"}
ERR={"amount_out_of_bounds":"مبلغ خارج از محدوده مجاز است.","invalid_housing":"این خانه معتبر نیست.","market_not_initialized":"بازار هنوز راه‌اندازی نشده است.","invalid_upgrade":"نوع ارتقا معتبر نیست.","player_not_found":"بازیکن پیدا نشد.","insufficient_balance":"موجودی کافی نیست.","job_locked":"شغل‌ها از سطح ۱ در دسترس هستند.","market_locked":"بازار دلار از سطح ۱۰ باز می‌شود.","housing_locked":"سطحت برای این خانه کافی نیست.","daily_limit":"سقف معامله امروزت پر شده است.","market_frozen":"بازار فعلاً متوقف است.","economy_frozen":"اقتصاد فعلاً متوقف است.","max_level_reached":"این بخش به آخرین سطح رسیده است.","job_not_found":"ابتدا یک شغل انتخاب کن.","invalid_job":"این شغل معتبر نیست.","insufficient_player_balance":"موجودی کافی نیست.","invalid_asset":"این دارایی معتبر نیست.","asset_owned":"این دارایی را قبلاً خریده‌ای.","asset_locked":"هنوز سطح زندگی یا مهارت لازم برای این دارایی را نداری.","migration_not_available":"این مقصد برای مهاجرت در دسترس نیست.","migration_cooldown":"تا پایان دوره ۳۰روزه امکان مهاجرت دوباره نداری.","migration_pending":"یک درخواست مهاجرت در انتظار داری.","leader_must_transfer_power":"رهبر باید ابتدا قدرت را واگذار کند.","migration_expired":"مهلت این درخواست تمام شده است.","resource_sell_daily_limit":"سقف فروش امروزت پر شده؛ فردا دوباره می‌توانی بفروشی.","invalid_amount":"این مقدار قابل فروش نیست.","insufficient_resource":"از این منبع به‌اندازه کافی نداری."}
def why(e):
 return ERR.get(str(e),"فعلاً نشد انجامش بدیم. یک‌بار صفحه را تازه کن و دوباره امتحان کن.")
def ik(a,p):return f"life:{a}:{p}:{uuid4().hex[:12]}"
async def answer(q,text=None,show_alert=False):
 try:await q.answer(text,show_alert=show_alert)
 except Exception:return
async def panel(ctx,c,text,mark,*,force_new=False):
 return await show(c,ctx.player.id,ctx.message.chat_id,text,mark,message=None if force_new else (ctx.message if getattr(ctx.message,'reply_markup',None) is not None else None),force_new=force_new)
async def fresh(ctx):return await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player
async def home(ctx,c,*,force_new=False):
 p=await fresh(ctx);st=await ui_state_repo.ensure_life(p.id);_,_,last=await daily.state(p.id);cur,need=progression.level_progress(p.level,p.xp);left=max(0,need-cur)
 step=int(st['onboarding_step'])
 if step<4:
  goals=("زندگی مجازی‌ات را فعال کن","سرمایه شروع را بگیر","اولین کار روزانه را ببین","یک شغل انتخاب کن تا درآمدت خودکار جمع شود")
  goal=goals[step];hint=f"🚀 مسیر شروع: {fmt.number(step)} از ۴ قدم کامل"
 else:
  goal="صفحه «امروز من» را باز کن؛ بازی بهترین کار آماده را نشانت می‌دهد"
  hint="☀️ معمولاً ۲ تا ۵ دقیقه برای پیشرفت روزانه کافی است."
 text=fa.HOME.format(name=escape(p.first_name),level=fmt.number(p.level),left=fmt.number(left),wallet=fmt.toman(p.wallet_toman),happy=fmt.number(p.happiness),goal=goal,hint=hint)
 await panel(ctx,c,text,kb.home(ctx.telegram_id,daily.claimable(last),step),force_new=force_new)
async def journey(ctx,c):
 st=await ui_state_repo.ensure_life(ctx.player.id);step=int(st['onboarding_step'])
 titles=("زندگی مجازی‌ات را فعال کن","سرمایه شروع را بگیر","اولین کار روزانه‌ات را باز کن","شغلت را انتخاب کن")
 bodies=("از اینجا شخصیتت رشد می‌کند، پول درمی‌آوری و روی کشور گروهت اثر می‌گذاری.","با سرمایه شروع می‌توانی وارد چرخه کار، پس‌انداز و خرید دارایی شوی.","کارهای کوتاه روزانه به تو پول و تجربه می‌دهند و امکانات تازه باز می‌کنند.","درآمد شغل با گذشت زمان جمع می‌شود؛ نتیجه شیفت را می‌گیری و مهارتت هم بالا می‌رود.")
 benefits=("بازشدن مسیر رشد و نخستین تجربه","پول اولیه برای آغاز تصمیم‌های اقتصادی","پاداش روزانه و رشد سریع‌تر سطح","درآمد مداوم، مهارت و اثر اقتصادی روی کشور")
 if step>=4:
  await today_page(ctx,c);return
 await panel(ctx,c,fa.JOURNEY.format(current=fmt.number(step+1),title=titles[step],body=bodies[step],benefit=benefits[step],bar=fmt.progress_bar(step,4,width=8)),kb.journey(ctx.telegram_id,step))
async def today_page(ctx,c):
 p=await fresh(ctx);view=await ux.today_view(p)
 await panel(ctx,c,view.text,kb.today(ctx.telegram_id,view.actions))
async def why_page(ctx,c):
 await panel(ctx,c,fa.WHY_PLAY,kb.learn(ctx.telegram_id))
async def guide_page(ctx,c):
 await panel(ctx,c,fa.HOW_TO_PLAY,kb.learn(ctx.telegram_id))

async def referrals_page(ctx,c):
 p=await fresh(ctx);view=await referrals.overview(p.id);settings=__import__('packages.core.settings',fromlist=['get_settings']).get_settings();username=str(settings.telelife_bot_username or '').lstrip('@')
 invite_url=f"https://t.me/{username}?start={referrals.start_payload(p.id)}" if username else ""
 next_reward=referrals.MILESTONES.get(view['next'],0)
 text=(f"🎁 دعوت دوست\n\nدوست فعال: {fmt.number(view['qualified'])} نفر\n"
       f"در حال فعال‌شدن: {fmt.number(view['pending'])} نفر\n\n"
       f"هدف بعدی: {fmt.number(view['next'])} دوست فعال\nجایزه: {fmt.toman(next_reward)}\n\n"
       "جایزه فقط وقتی باز می‌شود که دوستت مسیر شروع را کامل کند و در دو روز جدا بازی کند؛ پس عضو فیک حساب نمی‌شود."
       +( "\n\nنام کاربری بات در تنظیمات ثبت نشده؛ TELELIFE_BOT_USERNAME را تنظیم کن." if not invite_url else ""))
 await panel(ctx,c,text,kb.referrals(ctx.telegram_id,invite_url,bool(view['claimable'])))

async def profile(ctx,c):
 p=await fresh(ctx);cur,need=progression.level_progress(p.level,p.xp);rank=await progression_repo.rank_by_level(p.id);streak,_,_=await daily.state(p.id)
 text=fa.PROFILE.format(name=escape(p.first_name),level=fmt.number(p.level),rank=fmt.number(rank),bar=fmt.progress_bar(cur,need),xp=fmt.number(cur),need=fmt.number(need),wallet=fmt.toman(p.wallet_toman),savings=fmt.toman(p.savings_toman),usd=fmt.usd(p.usd_cents),happy=fmt.number(p.happiness),rep=fmt.number(p.reputation),streak=fmt.number(streak))
 from packages.core import db
 mig=await db.fetchrow("SELECT migrant_until,political_hold_until FROM citizenships WHERE player_id=$1 AND is_active",p.id)
 if mig and mig["migrant_until"] and mig["migrant_until"]>datetime.now(UTC):text+="\n\n🧳 وضعیت: مهاجر"
 if mig and mig["political_hold_until"] and mig["political_hold_until"]>datetime.now(UTC):text+="\nمحدودیت فعالیت سیاسی تا: "+mig["political_hold_until"].strftime('%Y-%m-%d')
 await panel(ctx,c,text,kb.back(ctx.telegram_id))
async def daily_page(ctx,c):
 streak,best,last=await daily.state(ctx.player.id);ready=daily.claimable(last)
 text=fa.DAILY_READY.format(streak=fmt.number(streak),amount=fmt.toman(daily.preview(streak+1))) if ready else fa.DAILY_WAIT.format(streak=fmt.number(streak),amount=fmt.toman(daily.tomorrow_preview(streak)))
 await panel(ctx,c,text,kb.daily(ctx.telegram_id,ready))
async def missions_page(ctx,c):
 p=await fresh(ctx);items=await missions.ensure_today(p.id,max(1,p.level));ready=[m.key for m in items if m.done and not m.claimed];rows=[]
 for m in items:rows.append(("✅" if m.claimed else "🎁" if m.done else "▫️")+f" {m.title} — {fmt.number(m.progress)}/{fmt.number(m.target)} · {fmt.toman(m.reward_toman)}")
 await panel(ctx,c,fa.MISSIONS.format(rows="\n".join(rows) or "امروز کاری ثبت نشده است."),kb.missions(ctx.telegram_id,ready))
async def economy(ctx,c):
 v=await personal_economy.view(ctx.player.id);house="نداری" if not v.housing else str(get_config().get(f"phase3.housing.options.{v.housing['housing_code']}.title"));await panel(ctx,c,fa.ECONOMY.format(wallet=fmt.toman(v.wallet),savings=fmt.toman(v.savings),house=house,due=fmt.toman(v.living_due)),kb.economy(ctx.telegram_id))
async def savings_page(ctx,c):
 v=await personal_economy.view(ctx.player.id);await panel(ctx,c,f"🏦 پس‌انداز\n{fa.RULE}\n\n👛 کیف پول: {fmt.toman(v.wallet)}\n🏦 پس‌انداز: {fmt.toman(v.savings)}\n\n{fa.SOFT}\nواریز یعنی پول را کنار می‌گذاری تا خرج روزمره نشود؛ برداشت یعنی برش می‌گردانی به کیف پول. مبلغ را از دکمه‌های زیر انتخاب کن.",kb.savings(ctx.telegram_id))
async def housing_page(ctx,c):
 p=await fresh(ctx);v=await personal_economy.view(p.id);current="نداری" if not v.housing else str(get_config().get(f"phase3.housing.options.{v.housing['housing_code']}.title"));await panel(ctx,c,f"🏠 خانه و زندگی\n{fa.RULE}\n\n🏡 خانهٔ فعلی: {current}\n\n🔓 اتاق از سطح ۳ · آپارتمان از سطح ۸ · ویلا از سطح ۲۰\n📅 اجاره هفت‌روزه است، خرید دائمی.\n\n{fa.SOFT}\nخانهٔ بهتر شادی بیشتری می‌آورد، اما هزینهٔ روزانه‌اش هم بالاتر است. پیش از انتخاب، یک نگاه به موجودی و سطحت بینداز.",kb.housing(ctx.telegram_id))
async def jobs(ctx,c):
 p=await fresh(ctx);row=await production_repo.get(p.id)
 if row:
  a=production.accrue(row,datetime.now(UTC));job=JOB_FA.get(str(row['job_code']),'شغل');asset=ASSET_FA.get(str(row['output_asset_code']),'درآمد');mode=SHIFT_FA.get(str(row.get('shift_mode') or 'balanced'),'متعادل')
  if str(row['output_asset_code'])=='IRT':
   wage=f"حدود {fmt.toman(round(a.rate))} در ساعت"
  else:
   unit=get_config().int_(f"resource_economy.assets.{row['output_asset_code']}.wage_toman_per_unit")
   wage=f"حدود {fmt.toman(round(a.rate*unit*0.8))} در ساعت + منبع"
  body=f"شغل: {job}\nشیفت فعلی: {mode}\n💵 حقوق نقدی: {wage}\n📦 محصول آماده: {fmt.number(a.stored)} از {fmt.number(a.capacity)} {asset}\nسرعت کار: {fmt.number(round(a.rate,1))} {asset} در ساعت\n\nبا دریافت نتیجه شیفت، حقوق نقدی مستقیم به کیف پول می‌رسد و منابع سهم تو هم ذخیره می‌شوند؛ منابع را می‌توانی بفروشی یا در تله‌ورلد اهدا کنی."
 else:body="از همین حالا یک شغل انتخاب کن؛ هر شیفت برای تو درآمد دارد و برای کشورت منبع می‌سازد."
 await panel(ctx,c,fa.JOBS.format(body=body),kb.jobs(ctx.telegram_id,bool(row),True))

async def resources_page(ctx,c):
 rows=await resource_economy.inventory(ctx.player.id)
 lines=[]
 for item in rows:
  value=int(item['quantity'])*int(item['sell_price'])
  lines.append(f"• {item['title']}: {fmt.number(item['quantity'])} واحد · ارزش فروش {fmt.toman(value)}")
 text="📦 منابع من\n\n"+("\n".join(lines) if lines else "هنوز منبعی نداری؛ یک شیفت کاری را کامل کن.")+"\n\nاول نوع منبع را انتخاب کن. ۵٪ کارمزد کم می‌شود و درآمد مستقیم به کیف پولت می‌آید."
 await panel(ctx,c,text,kb.resources(ctx.telegram_id,rows))

async def market(ctx,c):
 v=await usd_market.view();p=await fresh(ctx)
 status="⛔ متوقف" if v.frozen else "✅ آرام" if v.health>=75 else "⚠️ پرنوسان"
 access=("\n🔒 خریدوفروش از سطح ۱۰ باز می‌شود؛ تا آن‌وقت می‌توانی قیمت‌ها را دنبال کنی و بازار را یاد بگیری."
         if p.level<10 else
         "\nقیمت را دیدی؟ همین پایین می‌توانی خرید یا فروش کنی. فاصلهٔ خرید و فروش، سود واقعی‌ات را تعیین می‌کند.")
 text=("💱 بازار دلار\n"
       f"{fa.RULE}\n\n"
       f"🟢 قیمت خرید: {fmt.toman(v.buy_price)}\n"
       f"🔴 قیمت فروش: {fmt.toman(v.sell_price)}\n"
       f"💵 دلار تو: {fmt.usd(p.usd_cents)}\n\n"
       f"وضعیت بازار: {status}\n"
       f"شاخص سلامت: {fmt.number(v.health)} از ۱۰۰\n\n"
       f"{fa.SOFT}"+access)
 await panel(ctx,c,text,kb.market(ctx.telegram_id,p.level>=10))

async def progress_center(ctx,c):
 p=await fresh(ctx);skill=await life_progression.primary_skill(p.id);assets=await life_progression.assets_view(p.id)
 cur,need=progression.level_progress(p.level,p.xp)
 if skill:
  skill_line=f"{SKILL_FA.get(skill.code,skill.code)} · {skill.title} · سطح {fmt.number(skill.level)}\n{fmt.progress_bar(skill.xp,skill.needed,width=8)} {fmt.number(skill.xp)}/{fmt.number(skill.needed)} تجربه مهارت"
 else:skill_line="هنوز مهارتی فعال نیست؛ یک شغل انتخاب کن و نتیجه نخستین شیفت را بگیر."
 next_asset=next((a for a in assets if not a.owned and a.available),None)
 locked=next((a for a in assets if not a.owned),None)
 target=(f"خرید {next_asset.title} با {fmt.toman(next_asset.cost)}" if next_asset else f"بازکردن {locked.title}: {locked.reason}" if locked else "همه دارایی‌های فعلی را ساخته‌ای")
 owned=sum(1 for a in assets if a.owned)
 text=(f"🧭 مرکز پیشرفت واقعی\n\nسطح زندگی {fmt.number(p.level)}\n{fmt.progress_bar(cur,need,width=10)} {fmt.number(cur)}/{fmt.number(need)} XP\n\n🛠 مهارت اصلی\n{skill_line}\n\n🏠 دارایی‌های کاربردی\n{fmt.number(owned)} از {fmt.number(len(assets))} دارایی\n\n🎯 هدف بعدی\n{target}\n\nکار واقعی مهارت می‌سازد؛ سطح زندگی قابلیت باز می‌کند؛ دارایی مناسب بازده، فرصت و هزینه نگهداری واقعی دارد.")
 await panel(ctx,c,text,kb.progress(ctx.telegram_id))

async def assets_page(ctx,c):
 rows=await life_progression.assets_view(ctx.player.id);lines=[]
 for a in rows:
  icon="✅" if a.owned else "🟢" if a.available else "🔒"
  upkeep=f" · نگهداری روزانه {fmt.toman(a.maintenance)}" if a.maintenance else ""
  lines.append(f"{icon} {a.title} — {a.reason}\n{fmt.toman(a.cost)}{upkeep}\n{a.opportunity}")
 await panel(ctx,c,"🚗 دارایی‌های کاربردی\n\n"+"\n\n".join(lines),kb.assets(ctx.telegram_id,rows))

def _group_url(telegram_id:int)->str | None:
 # Public usernames are not stored in the legacy schema. Telegram's private
 # group post link still opens the group for members and is safe to render.
 raw=str(abs(int(telegram_id)))
 if raw.startswith("100") and len(raw)>3:
  return f"https://t.me/c/{raw[3:]}/1"
 return None

async def country_page(ctx,c):
 from packages.core import db
 current=await db.fetchrow("""SELECT cs.country_id,c.name,c.government_type,g.telegram_id,g.title,g.settings->>'public_link' group_link,
   (SELECT count(*) FROM citizenships x WHERE x.country_id=c.id AND x.is_active) citizens
  FROM citizenships cs JOIN countries c ON c.id=cs.country_id JOIN groups g ON g.id=c.group_id
  WHERE cs.player_id=$1 AND cs.is_active""",ctx.player.id)
 if not current:
  text="🌐 کشور من\n\nهنوز شهروند هیچ کشوری نیستی. وارد گروه یک کشور شو و از تله‌ورلد درخواست شهروندی بده؛ بعد کشور و مسیر مهاجرتت همین‌جا نمایش داده می‌شود."
  await panel(ctx,c,text,kb.country(ctx.telegram_id,None,[]));return
 pending=await db.fetchrow("""SELECT r.id,r.status,d.name destination_name,r.expires_at FROM migration_requests r JOIN countries d ON d.id=r.destination_country_id WHERE r.player_id=$1 AND r.status='pending' AND r.expires_at>now() ORDER BY r.created_at DESC LIMIT 1""",ctx.player.id)
 destinations=await db.fetch("""SELECT c.id,c.name,g.telegram_id,(SELECT count(*) FROM citizenships x WHERE x.country_id=c.id AND x.is_active) citizens FROM countries c JOIN groups g ON g.id=c.group_id WHERE c.id<>$1 AND c.status<>'forming' ORDER BY citizens DESC,c.name LIMIT 8""",current['country_id'])
 status=(f"\n\n⏳ درخواست مهاجرت به {escape(str(pending['destination_name']))} در انتظار بررسی است." if pending else "")
 text=(f"🌍 کشور من\n\n🏳 {escape(str(current['name']))}\n"
       f"🏛 نوع حکومت: {government_name(current['government_type'])}\n"
       f"👥 شهروندان: {fmt.number(current['citizens'])}{status}\n\n"
       "برای دیدن گروه، دکمه کشور را بزن. برای مهاجرت، مقصد را انتخاب کن؛ قبل از ثبت نهایی هزینه و محدودیت‌ها را می‌بینی.")
 rows=[(int(x['id']),str(x['name']),int(x['citizens'])) for x in destinations]
 await panel(ctx,c,text,kb.country(ctx.telegram_id,str(current['group_link']) if current['group_link'] else _group_url(int(current['telegram_id'])),rows,pending=bool(pending)))

async def migration_preview(ctx,c,destination_id:int):
 row=await migration.quote(ctx.player.id,destination_id)
 if not row:raise ValueError('migration_not_available')
 fee=migration.exit_fee(int(row['wallet_toman'])+int(row['savings_toman']))
 text=(f"🧳 تأیید مهاجرت\n\nاز {escape(str(row['origin_name']))} به {escape(str(row['destination_name']))}\n"
       f"💳 هزینه خروج: {fmt.toman(fee)}\n⏱ مهلت بررسی: ۷ روز\n"
       "🗳 پس از مهاجرت، فعالیت سیاسی ۱۴ روز محدود می‌شود و تا ۳۰ روز امکان مهاجرت دوباره نداری.\n\n"
       "هزینه فقط هنگام تأیید و تکمیل مهاجرت کم می‌شود.")
 await panel(ctx,c,text,kb.confirm(ctx.telegram_id,'migration','migconfirm',str(destination_id),'country'))

async def unlock_page(ctx,c):
 p=await fresh(ctx);rows=[]
 for level,spec in get_config().section('unlocks.levels').items():rows.append(("✅" if p.level>=int(level) else "🔒")+f" سطح {fmt.number(level)} — {spec['title']}")
 await panel(ctx,c,fa.UNLOCKS.format(rows="\n".join(rows)),kb.back(ctx.telegram_id))
async def start(update,c):
 user,chat=update.effective_user,update.effective_chat
 if not user or not chat:return
 if not await allow_start(c,user.id,chat.id):
  if update.effective_message:await update.effective_message.reply_text("⏳ در هر دقیقه فقط دو بار می‌توانی /start بزنی؛ چند لحظه دیگر دوباره تلاش کن.")
  return
 ctx=await resolve(update)
 if ctx:
  payload=c.args[0] if getattr(c,'args',None) else None
  if payload:await referrals.register(ctx.player.id,payload)
  await referrals.qualify_for_player(ctx.player.id)
  await home(ctx,c,force_new=True)
async def text_start(update,c):
 if c.user_data.get('ad_request_flow'):return
 if update.effective_chat and update.effective_chat.type=='private':
  ctx=await resolve(update)
  if ctx:await home(ctx,c)
async def callback(update,c):
 parsed=await guard_callback(update);q=update.callback_query
 if not parsed or not q:return
 ctx=await resolve(update)
 if not ctx:await answer(q,);return
 state=await ui_state_repo.ensure_life(ctx.player.id)
 active_id=int(state['life_message_id'] or 0) if state else 0
 clicked_id=int(q.message.message_id) if q.message else 0
 if active_id and clicked_id and active_id!=clicked_id:
  await answer(q,'این پنل قدیمی شده؛ از پنل جدیدت ادامه بده.',show_alert=True)
  if q.message:await retire_message(q.message)
  return
 a=parsed.action
 await referrals.qualify_for_player(ctx.player.id)
 if a=='advertise':
  from apps.telelife_bot.handlers.advertising import begin
  await begin(update,c);return
 try:
  if a in {'home','today','profile','daily','missions','economy','jobs','market','unlocks','journey','housing','savings','progress','assets','country','why','guide','resources','referrals'}:
   await answer(q,);fn={'home':home,'today':today_page,'profile':profile,'daily':daily_page,'missions':missions_page,'economy':economy,'jobs':jobs,'market':market,'unlocks':unlock_page,'journey':journey,'housing':housing_page,'savings':savings_page,'progress':progress_center,'assets':assets_page,'country':country_page,'why':why_page,'guide':guide_page,'resources':resources_page,'referrals':referrals_page}[a];await fn(ctx,c);return
  if a=='refclaim':
   await referrals.qualify_for_player(ctx.player.id);result=await referrals.claim(ctx.player.id)
   await answer(q,f"🎁 {fmt.toman(result['paid'])} جایزه گرفتی." if result['paid'] else "هنوز جایزه تازه‌ای آماده نیست.",show_alert=True);await referrals_page(ctx,c);return
  if a=='jstep':
   step=int(parsed.arg);state=await ui_state_repo.ensure_life(ctx.player.id);expected=int(state['onboarding_step'])
   if step!=expected:await answer(q,'این قدم قبلاً انجام شده یا هنوز نوبتش نرسیده است.',show_alert=True);await journey(ctx,c);return
   result=await xp.grant(ctx.player.id,'onboarding_step',idempotency_key=f'onboarding:{ctx.player.id}:{step}',amount=35 if step<3 else 80)
   await ui_state_repo.set_step(ctx.player.id,min(4,step+1))
   await answer(q,f"+{fmt.number(result.granted)} تجربه؛ قدم بعد باز شد.",show_alert=True)
   # Keep the player in the guided four-step flow; the last step opens jobs.
   if step==3:await jobs(ctx,c)
   else:await journey(ctx,c)
   return
  if a=='claim':
   r=await daily.claim(ctx.player.id)
   if r.already_claimed:await answer(q,"امروز گرفته‌ای.");await daily_page(ctx,c);return
   await xp.grant(ctx.player.id,'daily_claim',idempotency_key=xp.day_key('daily',ctx.player.id),amount=r.reward_xp);await missions.report_progress(ctx.player.id,'claim_daily');await answer(q,"پاداش دریافت شد.",show_alert=True);await panel(ctx,c,fa.DAILY_DONE.format(amount=fmt.toman(r.reward_toman),xp=fmt.number(r.reward_xp),streak=fmt.number(r.streak)),kb.daily(ctx.telegram_id,False));return
  if a=='mclaim':
   m=await missions.claim(ctx.player.id,parsed.arg)
   if not m:await answer(q,"هنوز کامل نشده است.",show_alert=True);return
   await xp.grant(ctx.player.id,'mission_complete',idempotency_key=f"mission-xp:{ctx.player.id}:{parsed.arg}:{xp.day_key('d',0)}",amount=m.reward_xp);await answer(q,"پاداش مأموریت دریافت شد.",show_alert=True);await missions_page(ctx,c);return
  if a in {'deposit','withdraw'}:await personal_economy.savings_transfer(ctx.player.id,int(parsed.arg),a,ik(a,ctx.player.id));await answer(q,"انتقال انجام شد.",show_alert=True);await savings_page(ctx,c);return
  if a=='living':paid,_=await personal_economy.pay_living(ctx.player.id,ik(a,ctx.player.id));await answer(q,"تسویه شد." if paid else "بدهی نداری.",show_alert=True);await economy(ctx,c);return
  if a in {'hrent','hbuy'}:
   p=await fresh(ctx);tenure='rent' if a=='hrent' else 'owned';text=ux.housing_preview(p,parsed.arg,tenure)
   await answer(q,);await panel(ctx,c,text,kb.confirm(ctx.telegram_id,'housing','hconfirm',f"{tenure},{parsed.arg}",'housing'));return
  if a=='hconfirm':
   tenure,code=parsed.arg.split(',',1);await personal_economy.acquire_housing(ctx.player.id,code,tenure,ik(a,ctx.player.id));await answer(q,"✅ خانه ثبت شد. حالا هزینه زندگی روزانه‌ات را در بخش دارایی و بانک ببین.",show_alert=True);await economy(ctx,c);return
  if a=='abuy':await life_progression.buy_asset(ctx.player.id,parsed.arg,ik(a,ctx.player.id));await answer(q,"دارایی خریده شد و اثرش فعال است.",show_alert=True);await assets_page(ctx,c);return
  if a=='jchoose':await production.choose(ctx.player.id,parsed.arg);await answer(q,"عالیه؛ شغلت ثبت شد و از همین حالا درآمدش جمع می‌شود.",show_alert=True);await jobs(ctx,c);return
  if a=='jshift':mode=await production.choose_shift(ctx.player.id,parsed.arg);await answer(q,f"شیفت {SHIFT_FA.get(mode,mode)} فعال شد.",show_alert=True);await jobs(ctx,c);return
  if a=='jcollect':
   r=await production.collect_purposeful(ctx.player.id,ik(a,ctx.player.id))
   if not r.amount:msg="هنوز چیزی برای دریافت آماده نیست؛ کمی زمان بده و دوباره سر بزن."
   else:
    personal=(f"💵 حقوق و سهم شما: {fmt.toman(r.amount)}" if r.asset=='IRT' else f"💵 حقوق نقدی: {fmt.toman(r.salary_toman)}\n📦 منبع ذخیره‌شده: {fmt.number(r.amount)} {ASSET_FA.get(r.asset,r.asset)}")
    national=(f"\n🏛 مالیات خزانه: {fmt.toman(r.tax_toman)}" if r.tax_toman else "")+(f"\n🌍 تولید برای {r.country_name}: {fmt.number(r.country_amount)} {ASSET_FA.get(r.country_asset or '',r.country_asset or '')}" if r.country_amount else "\n🌐 برای اثر ملی کامل، شهروند یک کشور شو.")
    msg=f"✅ نتیجه شیفت {SHIFT_FA.get(r.shift_mode,r.shift_mode)}\n\n{personal}{national}\n⭐ تجربه زندگی: +{fmt.number(r.xp)}\n🛠 مهارت {SKILL_FA.get(r.skill_code or '',r.skill_code or 'شغلی')}: سطح {fmt.number(r.skill_level)} · {fmt.number(r.skill_xp)}/{fmt.number(r.skill_needed)}"
   await answer(q,msg,show_alert=True);await jobs(ctx,c);return
  if a=='jupgrade':
   p=await fresh(ctx);row=await production_repo.get(p.id)
   if not row:raise ValueError('job_not_found')
   await answer(q,);await panel(ctx,c,ux.upgrade_preview(row,parsed.arg,p.wallet_toman),kb.confirm(ctx.telegram_id,'upgrade','juconfirm',parsed.arg,'jobs'));return
  if a=='juconfirm':
   lvl=await production.upgrade(ctx.player.id,parsed.arg,ik(a,ctx.player.id));await answer(q,f"✅ ارتقا به سطح {fmt.number(lvl)} انجام شد. نتیجه آن را در نرخ و ظرفیت جدید می‌بینی.",show_alert=True);await jobs(ctx,c);return
  if a in {'mbuy','msell'}:
   p=await fresh(ctx);side='buy' if a=='mbuy' else 'sell';await answer(q,)
   await panel(ctx,c,await ux.market_preview(p,side,int(parsed.arg)),kb.confirm(ctx.telegram_id,'market','mconfirm',f"{side},{parsed.arg}",'market'));return
  if a=='rpick':
   rows=await resource_economy.inventory(ctx.player.id);item=next((x for x in rows if str(x['asset'])==parsed.arg and int(x['quantity'])>0),None)
   if not item:raise ValueError('insufficient_resource')
   await answer(q);await panel(ctx,c,f"📦 {item['title']}\n\nموجودی: {fmt.number(item['quantity'])} واحد\nقیمت هر واحد: {fmt.toman(item['sell_price'])}\n\nچقدر می‌خواهی بفروشی؟",kb.resource_amounts(ctx.telegram_id,item));return
  if a=='rsell':
   asset,amount=parsed.arg.split(',',1);r=await resource_economy.sell(ctx.player.id,asset,int(amount),ik(a,ctx.player.id))
   await answer(q,f"✅ فروش انجام شد؛ {fmt.toman(r.net)} به کیف پولت اضافه شد. (کارمزد: {fmt.toman(r.fee)})",show_alert=True);await resources_page(ctx,c);return
  if a=='migrate':
   await answer(q,);await migration_preview(ctx,c,int(parsed.arg));return
  if a=='migconfirm':
   result=await migration.request(ctx.player.id,int(parsed.arg));await answer(q,'درخواست مهاجرت ثبت شد.' if str(result['status'])=='pending' else 'مهاجرت با موفقیت انجام شد.',show_alert=True);await country_page(ctx,c);return
  if a=='mconfirm':
   side,cents=parsed.arg.split(',',1);r=await usd_market.trade(ctx.player.id,side,int(cents),ik(a,ctx.player.id));await answer(q,f"✅ معامله انجام شد. موجودی دلارت به‌روز شد و {fmt.toman(r.fee)} کارمزد کم شد.",show_alert=True);await market(ctx,c);return
  await answer(q,)
 except (ValueError,PermissionError) as e:
  code=str(e);await answer(q,why(e),show_alert=True)
  if code in {'insufficient_balance','insufficient_player_balance','housing_locked','market_locked','job_not_found','max_level_reached','market_frozen'}:
   await panel(ctx,c,ux.actionable_error(code,player=ctx.player),kb.back(ctx.telegram_id,'home'))
def register(app):
 app.add_handler(CommandHandler('start',start));app.add_handler(CallbackQueryHandler(callback,pattern=r'^tl:'));app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT & ~filters.COMMAND,text_start))
