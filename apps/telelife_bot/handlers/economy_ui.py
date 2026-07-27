"""Button-only Phase 3/4 UI. All navigation edits one owned glass panel."""
from __future__ import annotations
from uuid import uuid4
from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes
from apps.telelife_bot.handlers.common import guard_callback,resolve,send_panel
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.repositories import player_repo,production_repo
from packages.core.services import personal_economy,production,usd_market
from packages.core.utils import fmt

ERRORS={
 "insufficient_balance":"موجودی کافی نیست.","amount_out_of_bounds":"مبلغ خارج از محدوده مجاز است.",
 "job_locked":"مشاغل از سطح ۱ در دسترس هستند.","job_not_found":"هنوز شغلی انتخاب نکرده‌ای.",
 "housing_locked":"سطحت برای این خانه کافی نیست.","market_locked":"بازار دلار از سطح ۱۰ باز می‌شود.",
 "market_frozen":"بازار فعلاً برای حفاظت از اقتصاد متوقف است.","economy_frozen":"اقتصاد فعلاً متوقف است.",
 "daily_limit":"سقف معامله امروزت پر شده است.","invalid_housing":"انتخاب خانه معتبر نیست.",
 "invalid_job":"این شغل معتبر نیست.","max_level_reached":"به آخرین سطح ارتقا رسیده‌ای.",
}
def err(exc:Exception)->str:return ERRORS.get(str(exc),"عملیات انجام نشد؛ کمی بعد دوباره تلاش کن.")
def key(prefix:str,pid:int)->str:return f"ui:{prefix}:{pid}:{uuid4().hex[:16]}"

async def economy_panel(ctx,context):
 v=await personal_economy.view(ctx.player.id); title="بدون خانه"
 if v.housing:
  spec=get_config().section(f"phase3.housing.options.{v.housing['housing_code']}");title=str(spec['title'])
 text=fa.ECONOMY_PANEL.format(wallet=fmt.toman(v.wallet),savings=fmt.toman(v.savings),housing=title,living=fmt.toman(v.living_due))
 await send_panel(context,ctx.message,text,kb.economy_panel(ctx.telegram_id),"profile",edit=True)
async def savings(ctx,context):
 v=await personal_economy.view(ctx.player.id)
 await send_panel(context,ctx.message,f"🏦 <b>پس‌انداز امن</b>\n\nکیف پول: <b>{fmt.toman(v.wallet)}</b>\nپس‌انداز: <b>{fmt.toman(v.savings)}</b>\n\nمبلغ را انتخاب کن.",kb.savings_panel(ctx.telegram_id),"profile",edit=True)
async def housing(ctx,context):
 await send_panel(context,ctx.message,"🏠 <b>خانه و زندگی</b>\n\nخانه بهتر هزینه زندگی بیشتری دارد، اما مسیر رشد شخصیتت را کامل می‌کند. اجاره هفت‌روزه است؛ خرید دائمی.",kb.housing_panel(ctx.telegram_id),"profile",edit=True)
async def jobs(ctx,context):
 row=await production_repo.get(ctx.player.id)
 if row:
  a=production.accrue(row,__import__('datetime').datetime.now(__import__('datetime').UTC)); body=f"شغل: <b>{row['job_code']}</b>\nتولید ذخیره‌شده: <b>{fmt.number(a.stored)} / {fmt.number(a.capacity)}</b>\nنرخ: <b>{a.rate:.1f}</b> در ساعت\nسطح تولید: <b>{fmt.number(row['production_level'])}</b> · انبار: <b>{fmt.number(row['storage_level'])}</b>"
 else: body="هنوز شغلی نداری. از بین گزینه‌ها خودت شغلی را انتخاب کن که به سبک بازیت می‌خورد."
 await send_panel(context,ctx.message,fa.JOBS_PANEL.format(body=body),kb.jobs_panel(ctx.telegram_id,bool(row)),"profile",edit=True)
async def market(ctx,context):
 v=await usd_market.view();p=await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player
 status="متوقف" if v.frozen else "سالم" if v.health>=75 else "نیازمند توجه" if v.health>=45 else "پرنوسان"
 text=fa.MARKET_PANEL.format(buy=fmt.toman(v.buy_price),sell=fmt.toman(v.sell_price),health=fmt.number(v.health),volume=fmt.usd(v.volume_cents),status=status,usd=fmt.usd(p.usd_cents))
 await send_panel(context,ctx.message,text,kb.market_panel(ctx.telegram_id),"profile",edit=True)

async def callback(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 parsed=await guard_callback(update);q=update.callback_query
 if parsed is None or q is None:return
 if parsed.action not in {"economy","savings","housing","living","deposit","withdraw","jobs","jchoose","jcollect","jshift","jupgrade","market","mbuy","msell","hrent","hbuy"}:return
 ctx=await resolve(update)
 if ctx is None:await q.answer();return
 try:
  a=parsed.action
  if a=="economy":await q.answer();await economy_panel(ctx,context)
  elif a=="savings":await q.answer();await savings(ctx,context)
  elif a=="housing":await q.answer();await housing(ctx,context)
  elif a=="jobs":await q.answer();await jobs(ctx,context)
  elif a=="market":await q.answer();await market(ctx,context)
  elif a in {"deposit","withdraw"}:
   await personal_economy.savings_transfer(ctx.player.id,int(parsed.arg),a,key(a,ctx.player.id));await q.answer(fa.ACTION_DONE);await savings(ctx,context)
  elif a=="living":
   paid,_=await personal_economy.pay_living(ctx.player.id,key(a,ctx.player.id));await q.answer("هزینه‌ای باقی نمانده." if not paid else f"{fmt.toman(paid)} پرداخت شد.",show_alert=True);await economy_panel(ctx,context)
  elif a in {"hrent","hbuy"}:
   await personal_economy.acquire_housing(ctx.player.id,parsed.arg,"rent" if a=="hrent" else "owned",key(a,ctx.player.id));await q.answer(fa.ACTION_DONE,show_alert=True);await economy_panel(ctx,context)
  elif a=="jchoose":
   if not await production.choose(ctx.player.id,parsed.arg):raise ValueError("job_already_selected")
   await q.answer("عالیه؛ شغلت ثبت شد و درآمدش از همین حالا جمع می‌شود.",show_alert=True);await jobs(ctx,context)
  elif a=="jshift":
   await production.choose_shift(ctx.player.id,parsed.arg);await q.answer("نوع شیفت تغییر کرد.",show_alert=True);await jobs(ctx,context)
  elif a=="jcollect":
   r=await production.collect_purposeful(ctx.player.id,key(a,ctx.player.id));await q.answer(f"سهم شما {fmt.number(r.amount)}؛ مالیات {fmt.toman(r.tax_toman)}؛ سهم کشور {fmt.number(r.country_amount)}",show_alert=True);await jobs(ctx,context)
  elif a=="jupgrade":
   lvl=await production.upgrade(ctx.player.id,parsed.arg,key(a,ctx.player.id));await q.answer(f"به سطح {fmt.number(lvl)} ارتقا یافت.",show_alert=True);await jobs(ctx,context)
  elif a in {"mbuy","msell"}:
   r=await usd_market.trade(ctx.player.id,"buy" if a=="mbuy" else "sell",int(parsed.arg),key(a,ctx.player.id));await q.answer(f"معامله انجام شد؛ کارمزد {fmt.toman(r.fee)}",show_alert=True);await market(ctx,context)
 except (ValueError,PermissionError) as exc:await q.answer(err(exc),show_alert=True)

def register(app)->None:app.add_handler(CallbackQueryHandler(callback,pattern=r"^tl:(economy|savings|housing|living|deposit|withdraw|jobs|jchoose|jcollect|jshift|jupgrade|market|mbuy|msell|hrent|hbuy):"),group=-1)
