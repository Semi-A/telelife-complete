"""Unified, Persian, single-message TeleLife experience."""
from __future__ import annotations
from datetime import UTC,datetime
from uuid import uuid4
from html import escape
from telegram import Update
from telegram.ext import CallbackQueryHandler,CommandHandler,ContextTypes,MessageHandler,filters
from apps.telelife_bot.handlers.common import guard_callback,resolve
from apps.telelife_bot.handlers.panel import show
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.bot.start_limit import allow_start
from packages.core.repositories import player_repo,progression_repo,production_repo,ui_state_repo
from packages.core.services import daily,life_progression,missions,personal_economy,production,progression,unlocks,usd_market,xp
from packages.core.utils import fmt

JOB_FA={"farmer":"کشاورز","miner":"معدن‌کار","trader":"بازرگان","journalist":"روزنامه‌نگار","doctor":"پزشک","programmer":"برنامه‌نویس","engineer":"مهندس"}
ASSET_FA={"IRT":"تومان","USD":"دلار","food":"محصول کشاورزی","minerals":"مواد معدنی","technology":"فناوری","energy":"انرژی"}
SHIFT_FA={"safe":"امن","balanced":"متعادل","national":"ملی","private":"خصوصی"}
SKILL_FA={"agriculture":"کشاورزی","extraction":"استخراج","commerce":"تجارت","media":"رسانه","medicine":"پزشکی","software":"نرم‌افزار","engineering":"مهندسی"}
ERR={"amount_out_of_bounds":"مبلغ خارج از محدوده مجاز است.","invalid_housing":"این خانه معتبر نیست.","market_not_initialized":"بازار هنوز راه‌اندازی نشده است.","invalid_upgrade":"نوع ارتقا معتبر نیست.","player_not_found":"بازیکن پیدا نشد.","insufficient_balance":"موجودی کافی نیست.","job_locked":"شغل‌ها از سطح ۱ در دسترس هستند.","market_locked":"بازار دلار از سطح ۱۰ باز می‌شود.","housing_locked":"سطحت برای این خانه کافی نیست.","daily_limit":"سقف معامله امروزت پر شده است.","market_frozen":"بازار فعلاً متوقف است.","economy_frozen":"اقتصاد فعلاً متوقف است.","max_level_reached":"این بخش به آخرین سطح رسیده است.","job_not_found":"ابتدا یک شغل انتخاب کن.","invalid_job":"این شغل معتبر نیست.","insufficient_player_balance":"موجودی کافی نیست.","invalid_asset":"این دارایی معتبر نیست.","asset_owned":"این دارایی را قبلاً خریده‌ای.","asset_locked":"هنوز سطح زندگی یا مهارت لازم برای این دارایی را نداری."}
def why(e):
 return ERR.get(str(e),"فعلاً نشد انجامش بدیم. یک‌بار صفحه را تازه کن و دوباره امتحان کن.")
def ik(a,p):return f"life:{a}:{p}:{uuid4().hex[:12]}"
async def answer(q,text=None,show_alert=False):
 try:await q.answer(text,show_alert=show_alert)
 except Exception:return
async def panel(ctx,c,text,mark):return await show(c,ctx.player.id,ctx.message.chat_id,text,mark,message=ctx.message if getattr(ctx.message,'reply_markup',None) is not None else None)
async def fresh(ctx):return await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player
async def home(ctx,c):
 p=await fresh(ctx);st=await ui_state_repo.ensure_life(p.id);_,_,last=await daily.state(p.id);cur,need=progression.level_progress(p.level,p.xp);left=max(0,need-cur)
 step=int(st['onboarding_step']);goal=("چهار قدم شروع را کامل کن" if step<4 else "شغل بگیر، شیفت انجام بده و به رشد کشورت کمک کن")
 hint="🚀 مسیر شروع آماده ادامه است." if step<4 else "🎯 کارهای امروز بهترین راه رشد هستند."
 text=fa.HOME.format(name=escape(p.first_name),level=fmt.number(p.level),bar=fmt.progress_bar(cur,need,width=10),left=fmt.number(left),wallet=fmt.toman(p.wallet_toman),happy=fmt.number(p.happiness),goal=goal,hint=hint)
 await panel(ctx,c,text,kb.home(ctx.telegram_id,daily.claimable(last),step))
async def journey(ctx,c):
 st=await ui_state_repo.ensure_life(ctx.player.id);step=int(st['onboarding_step']);bodies=["هدف نخست را ثبت کن تا نوار پیشرفت و مسیر رشدت فعال شود.","سرمایه آغازین را بگیر؛ بلافاصله بعد از آن کارهای روزانه منتظرت هستند.","نخستین کار روزانه را باز کن؛ پاداش آغاز فقط شروع بازی است، نه پایان آن.","وارد زندگی اصلی شو؛ از همین سطح شغل انتخاب کن و اثر کارت را روی کشور ببین.","مسیر شروع کامل شده است؛ هدیه روزانه، کارها، شغل، بانک و خانه چرخه ادامه بازی را می‌سازند."]
 await panel(ctx,c,fa.JOURNEY.format(body=bodies[min(step,4)],done=fmt.number(step),bar=fmt.progress_bar(step,4,width=8)),kb.journey(ctx.telegram_id,step))
async def profile(ctx,c):
 p=await fresh(ctx);cur,need=progression.level_progress(p.level,p.xp);rank=await progression_repo.rank_by_level(p.id);streak,_,_=await daily.state(p.id)
 text=fa.PROFILE.format(name=escape(p.first_name),level=fmt.number(p.level),rank=fmt.number(rank),bar=fmt.progress_bar(cur,need),xp=fmt.number(cur),need=fmt.number(need),wallet=fmt.toman(p.wallet_toman),savings=fmt.toman(p.savings_toman),usd=fmt.usd(p.usd_cents),happy=fmt.number(p.happiness),rep=fmt.number(p.reputation),streak=fmt.number(streak))
 from packages.core import db
 mig=await db.fetchrow("SELECT migrant_until,political_hold_until FROM citizenships WHERE player_id=$1 AND is_active",p.id)
 if mig and mig["migrant_until"] and mig["migrant_until"]>datetime.now(UTC):text+="\n\n🧳 <b>وضعیت: مهاجر</b>"
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
 v=await personal_economy.view(ctx.player.id);await panel(ctx,c,f"🏦 <b>مدیریت پس‌انداز</b>\n\nکیف پول: <b>{fmt.toman(v.wallet)}</b>\nپس‌انداز: <b>{fmt.toman(v.savings)}</b>\n\nواریز، پول را از کیف پول به پس‌انداز منتقل می‌کند؛ برداشت برعکس آن است. مبلغ را انتخاب کن.",kb.savings(ctx.telegram_id))
async def housing_page(ctx,c):
 p=await fresh(ctx);v=await personal_economy.view(p.id);current="نداری" if not v.housing else str(get_config().get(f"phase3.housing.options.{v.housing['housing_code']}.title"));await panel(ctx,c,f"🏠 <b>خانه و زندگی</b>\n\nخانه فعلی: <b>{current}</b>\n\nاتاق از سطح ۳، آپارتمان از سطح ۸ و ویلا از سطح ۲۰ باز می‌شود. اجاره هفت‌روزه است و خرید دائمی. خانه بهتر هزینه روزانه بیشتری دارد؛ پیش از انتخاب، موجودی و سطح خودت را بررسی کن.",kb.housing(ctx.telegram_id))
async def jobs(ctx,c):
 p=await fresh(ctx);row=await production_repo.get(p.id)
 if row:
  a=production.accrue(row,datetime.now(UTC));job=JOB_FA.get(str(row['job_code']),'شغل');asset=ASSET_FA.get(str(row['output_asset_code']),'درآمد');mode=SHIFT_FA.get(str(row.get('shift_mode') or 'balanced'),'متعادل')
  body=f"شغل: <b>{job}</b>\nشیفت فعلی: <b>{mode}</b>\nدرآمد آماده: <b>{fmt.number(a.stored)} از {fmt.number(a.capacity)} {asset}</b>\nسرعت کار: <b>{fmt.number(round(a.rate,1))} {asset} در ساعت</b>\n\nهر دریافت، سهم شخصی، مالیات و اثر ملی را شفاف ثبت می‌کند."
 else:body="از همین حالا یک شغل انتخاب کن؛ هر شیفت برای تو درآمد دارد و برای کشورت منبع می‌سازد."
 await panel(ctx,c,fa.JOBS.format(body=body),kb.jobs(ctx.telegram_id,bool(row),True))

async def market(ctx,c):
 v=await usd_market.view();p=await fresh(ctx)
 status="⛔ متوقف" if v.frozen else "✅ عادی" if v.health>=75 else "⚠️ پرنوسان"
 access="\n\n🔒 خریدوفروش از سطح ۱۰ باز می‌شود؛ تا آن موقع می‌توانی قیمت‌ها را دنبال کنی." if p.level<10 else "\n\nقیمت را دیدی؟ پایین همین صفحه می‌توانی خرید یا فروش انجام بدهی."
 text=("💱 <b>بازار دلار</b>\n\n"
       f"🟢 قیمت خرید: <b>{fmt.toman(v.buy_price)}</b>\n"
       f"🔴 قیمت فروش: <b>{fmt.toman(v.sell_price)}</b>\n"
       f"💵 موجودی شما: <b>{fmt.usd(p.usd_cents)}</b>\n\n"
       f"وضعیت بازار: <b>{status}</b>\n"
       f"شاخص سلامت: <b>{fmt.number(v.health)} از ۱۰۰</b>"
       +access)
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
 text=(f"🧭 <b>مرکز پیشرفت واقعی</b>\n\n<b>سطح زندگی {fmt.number(p.level)}</b>\n{fmt.progress_bar(cur,need,width=10)} {fmt.number(cur)}/{fmt.number(need)} XP\n\n🛠 <b>مهارت اصلی</b>\n{skill_line}\n\n🏠 <b>دارایی‌های کاربردی</b>\n{fmt.number(owned)} از {fmt.number(len(assets))} دارایی\n\n🎯 <b>هدف بعدی</b>\n{target}\n\nکار واقعی مهارت می‌سازد؛ سطح زندگی قابلیت باز می‌کند؛ دارایی مناسب بازده، فرصت و هزینه نگهداری واقعی دارد.")
 await panel(ctx,c,text,kb.progress(ctx.telegram_id))

async def assets_page(ctx,c):
 rows=await life_progression.assets_view(ctx.player.id);lines=[]
 for a in rows:
  icon="✅" if a.owned else "🟢" if a.available else "🔒"
  upkeep=f" · نگهداری روزانه {fmt.toman(a.maintenance)}" if a.maintenance else ""
  lines.append(f"{icon} <b>{a.title}</b> — {a.reason}\n{fmt.toman(a.cost)}{upkeep}\n{a.opportunity}")
 await panel(ctx,c,"🚗 <b>دارایی‌های کاربردی</b>\n\n"+"\n\n".join(lines),kb.assets(ctx.telegram_id,rows))

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
 if ctx:await home(ctx,c)
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
 a=parsed.action
 if a=='advertise':
  from apps.telelife_bot.handlers.advertising import begin
  await begin(update,c);return
 try:
  if a in {'home','profile','daily','missions','economy','jobs','market','unlocks','journey','housing','savings','progress','assets'}:
   await answer(q,);fn={'home':home,'profile':profile,'daily':daily_page,'missions':missions_page,'economy':economy,'jobs':jobs,'market':market,'unlocks':unlock_page,'journey':journey,'housing':housing_page,'savings':savings_page,'progress':progress_center,'assets':assets_page}[a];await fn(ctx,c);return
  if a=='jstep':
   step=int(parsed.arg);state=await ui_state_repo.ensure_life(ctx.player.id);expected=int(state['onboarding_step'])
   if step!=expected:await answer(q,'این قدم قبلاً انجام شده یا هنوز نوبتش نرسیده است.',show_alert=True);await journey(ctx,c);return
   result=await xp.grant(ctx.player.id,'onboarding_step',idempotency_key=f'onboarding:{ctx.player.id}:{step}',amount=35 if step<3 else 80);await ui_state_repo.set_step(ctx.player.id,min(4,step+1));await answer(q,f"+{fmt.number(result.granted)} تجربه؛ قدم بعد باز شد.",show_alert=True)
   if step==1:await missions_page(ctx,c)
   elif step==3:await home(ctx,c)
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
  if a in {'hrent','hbuy'}:await personal_economy.acquire_housing(ctx.player.id,parsed.arg,'rent' if a=='hrent' else 'owned',ik(a,ctx.player.id));await answer(q,"خانه ثبت شد.",show_alert=True);await housing_page(ctx,c);return
  if a=='abuy':await life_progression.buy_asset(ctx.player.id,parsed.arg,ik(a,ctx.player.id));await answer(q,"دارایی خریده شد و اثرش فعال است.",show_alert=True);await assets_page(ctx,c);return
  if a=='jchoose':await production.choose(ctx.player.id,parsed.arg);await answer(q,"عالیه؛ شغلت ثبت شد و از همین حالا درآمدش جمع می‌شود.",show_alert=True);await jobs(ctx,c);return
  if a=='jshift':mode=await production.choose_shift(ctx.player.id,parsed.arg);await answer(q,f"شیفت {SHIFT_FA.get(mode,mode)} فعال شد.",show_alert=True);await jobs(ctx,c);return
  if a=='jcollect':
   r=await production.collect_purposeful(ctx.player.id,ik(a,ctx.player.id))
   if not r.amount:msg="هنوز چیزی برای دریافت آماده نیست؛ کمی زمان بده و دوباره سر بزن."
   else:
    personal=f"💵 سهم شما: {fmt.toman(r.amount)}" if r.asset=='IRT' else f"📦 سهم شما: {fmt.number(r.amount)} {ASSET_FA.get(r.asset,r.asset)}"
    national=(f"\n🏛 مالیات خزانه: {fmt.toman(r.tax_toman)}" if r.tax_toman else "")+(f"\n🌍 تولید برای {r.country_name}: {fmt.number(r.country_amount)} {ASSET_FA.get(r.country_asset or '',r.country_asset or '')}" if r.country_amount else "\n🌐 برای اثر ملی کامل، شهروند یک کشور شو.")
    msg=f"✅ نتیجه شیفت {SHIFT_FA.get(r.shift_mode,r.shift_mode)}\n\n{personal}{national}\n⭐ تجربه زندگی: +{fmt.number(r.xp)}\n🛠 مهارت {SKILL_FA.get(r.skill_code or '',r.skill_code or 'شغلی')}: سطح {fmt.number(r.skill_level)} · {fmt.number(r.skill_xp)}/{fmt.number(r.skill_needed)}"
   await answer(q,msg,show_alert=True);await jobs(ctx,c);return
  if a=='jupgrade':lvl=await production.upgrade(ctx.player.id,parsed.arg,ik(a,ctx.player.id));await answer(q,f"ارتقا به سطح {fmt.number(lvl)}",show_alert=True);await jobs(ctx,c);return
  if a in {'mbuy','msell'}:r=await usd_market.trade(ctx.player.id,'buy' if a=='mbuy' else 'sell',int(parsed.arg),ik(a,ctx.player.id));await answer(q,f"معامله انجام شد؛ کارمزد {fmt.toman(r.fee)}",show_alert=True);await market(ctx,c);return
  await answer(q,)
 except (ValueError,PermissionError) as e:await answer(q,why(e),show_alert=True)
def register(app):
 app.add_handler(CommandHandler('start',start));app.add_handler(CallbackQueryHandler(callback,pattern=r'^tl:'));app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT & ~filters.COMMAND,text_start))