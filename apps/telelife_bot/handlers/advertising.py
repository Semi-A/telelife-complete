"""Guided private ad request flow and Telegram Stars settlement."""
from __future__ import annotations
from datetime import UTC,datetime
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,LabeledPrice,Update
from telegram.ext import CallbackQueryHandler,ContextTypes,MessageHandler,PreCheckoutQueryHandler,filters
from packages.core.repositories import player_repo
from packages.core.services import commerce
from packages.core.services.content_filter import inspect
FLOW="ad_request_flow"
PACK={"economy":"اقتصادی · پایه ۲۵ ⭐ · یک پخش","standard":"استاندارد · پایه ۶۰ ⭐ · ۳ پخش / ۲۴ ساعت","campaign":"کمپین · پایه ۱۲۰ ⭐ · ۶ پخش / ۳ روز","featured":"ویژه · پایه ۲۰۰ ⭐ · ۸ پخش / ۷ روز"}
CHANNEL={"life":"فقط Life · کاربران فعال ۳۰ روز · ×۱","world":"فقط World · گروه‌های فعال غیرمشترک · ×۱٫۵","both":"Life + World · ×۲٫۲"}
def keyboard(rows):return InlineKeyboardMarkup(rows)
def menu():return keyboard([[InlineKeyboardButton(v,callback_data=f"ad:pkg:{k}")] for k,v in PACK.items()]+[[InlineKeyboardButton("📂 درخواست‌های من",callback_data="ad:mine")],[InlineKeyboardButton("لغو",callback_data="ad:cancel")]])
def channels(package):
 return keyboard([[InlineKeyboardButton(label+f" · {commerce.ad_price(package,code)} ⭐",callback_data=f"ad:channel:{package}:{code}")] for code,label in CHANNEL.items()]+[[InlineKeyboardButton("بازگشت",callback_data="ad:new")]])
async def begin(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.callback_query
 if q:await q.answer();await q.edit_message_text("📣 <b>درخواست تبلیغ</b>\n\nبسته را انتخاب کن. تبلیغ پیش از پرداخت کامل در پنل مدیریت بررسی می‌شود.",reply_markup=menu())
async def callback(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.callback_query;action=(q.data or "").split(":")
 if action[1]=="cancel":context.user_data.pop(FLOW,None);await q.answer();await q.edit_message_text("درخواست لغو شد.");return
 if action[1]=="mine":
  p=await player_repo.get_by_telegram_id(q.from_user.id);rows=await commerce.player_ads(p.id) if p else []
  buttons=[];lines=["📂 <b>درخواست‌های من</b>"]
  for row in rows:
   lines.append(f"#{row['id']} · {row['title']} · {row['status']}"+(f"\nیادداشت: {row['admin_note']}" if row['admin_note'] else ""))
   if row['status']=='changes_requested':buttons.append([InlineKeyboardButton(f"✏️ اصلاح #{row['id']}",callback_data=f"ad:revise:{row['id']}")])
  buttons.append([InlineKeyboardButton("درخواست تازه",callback_data="ad:new")]);await q.answer();await q.edit_message_text("\n\n".join(lines) if rows else "درخواستی نداری.",reply_markup=keyboard(buttons));return
 if action[1]=="new":await q.answer();await q.edit_message_text("بسته را انتخاب کن.",reply_markup=menu());return
 if action[1]=="revise":
  p=await player_repo.get_by_telegram_id(q.from_user.id);row=await commerce.revision_source(int(action[2]),p.id) if p else None
  if not row:await q.answer("این درخواست قابل اصلاح نیست.",show_alert=True);return
  context.user_data[FLOW]={"step":"title","package":row['package_code'],"channel":row['channel'],"revision_id":row['id']};await q.answer();await q.edit_message_text(f"عنوان اصلاح‌شده را بفرست.\nعنوان فعلی: {row['title']}");return
 if action[1]=="pkg":await q.answer();await q.edit_message_text("محل نمایش تبلیغ را انتخاب کن. قیمت نهایی بر اساس کانال محاسبه می‌شود.",reply_markup=channels(action[2]));return
 if action[1]=="channel":context.user_data[FLOW]={"step":"title","package":action[2],"channel":action[3]};await q.answer();await q.edit_message_text(f"قیمت نهایی: {commerce.ad_price(action[2],action[3])} ⭐\n\nعنوان کوتاه تبلیغ را بفرست (۳ تا ۱۲۰ نویسه).")
async def text(update:Update,context:ContextTypes.DEFAULT_TYPE):
 flow=context.user_data.get(FLOW);msg=update.effective_message
 if not flow or not msg:return
 value=(msg.text or "").strip();step=flow["step"]
 if step in {"title","description"} and not inspect(value).allowed:await msg.reply_text("⚠️ متن شامل عبارت غیرمجاز است؛ آن را اصلاح کن و دوباره بفرست.");return
 if step=="title":
  if not 3<=len(value)<=120:await msg.reply_text("عنوان باید بین ۳ تا ۱۲۰ نویسه باشد.");return
  flow.update(title=value,step="description");await msg.reply_text("توضیح کامل تبلیغ را بفرست (۱۰ تا ۲۰۰۰ نویسه).");return
 if step=="description":
  if not 10<=len(value)<=2000:await msg.reply_text("توضیح باید بین ۱۰ تا ۲۰۰۰ نویسه باشد.");return
  flow.update(description=value,step="url");await msg.reply_text("لینک مقصد را با https:// بفرست.");return
 if step=="url":
  if not commerce.valid_url(value):await msg.reply_text("لینک معتبر نیست؛ یک لینک کامل http یا https بفرست.");return
  flow.update(url=value,step="image");await msg.reply_text("حالا تصویر تبلیغ را بفرست (JPG/PNG/WebP، حداکثر ۵ مگابایت). اگر تصویر نمی‌خواهی «بدون عکس» بنویس.");return
 if step=="image" and value=="بدون عکس":flow.update(image=None,mime=None,step="start");await msg.reply_text("زمان شروع دلخواه را به شکل 2026-07-30 18:30 UTC بفرست یا «اولین زمان ممکن» بنویس.");return
 if step=="start":
  start=None
  if value!="اولین زمان ممکن":
   try:start=datetime.strptime(value,"%Y-%m-%d %H:%M").replace(tzinfo=UTC)
   except ValueError:await msg.reply_text("قالب زمان درست نیست؛ نمونه: 2026-07-30 18:30 یا «اولین زمان ممکن».");return
  user=update.effective_user;p=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "کاربر",language_code=user.language_code or "fa")
  if flow.get("revision_id"):
   ad_id=int(flow["revision_id"]);ok=await commerce.submit_revision(ad_id,p.id,flow["title"],flow["description"],flow["url"],flow.get("image"),flow.get("mime"),start)
   if not ok:raise ValueError("revision_closed")
  else:ad_id=await commerce.create_ad_request(p.id,flow["package"],flow["channel"],flow["title"],flow["description"],flow["url"],flow.get("image"),flow.get("mime"),start)
  context.user_data.pop(FLOW,None);await msg.reply_text(f"✅ درخواست #{ad_id} برای بررسی مدیر ثبت شد.\n\nدر صورت تأیید، صورتحساب استارز با اعتبار ۴۸ ساعت همین‌جا ارسال می‌شود. تا پیش از تأیید هیچ پرداختی انجام نمی‌دهی.")
async def photo(update:Update,context:ContextTypes.DEFAULT_TYPE):
 flow=context.user_data.get(FLOW);msg=update.effective_message
 if not flow or flow.get("step")!="image" or not msg.photo:return
 photo=msg.photo[-1]
 if photo.file_size and photo.file_size>5_000_000:await msg.reply_text("حجم تصویر بیشتر از ۵ مگابایت است.");return
 f=await photo.get_file();data=bytes(await f.download_as_bytearray());flow.update(image=data,mime="image/jpeg",step="start");await msg.reply_text("زمان شروع دلخواه را به شکل 2026-07-30 18:30 UTC بفرست یا «اولین زمان ممکن» بنویس.")
async def precheckout(update:Update,context:ContextTypes.DEFAULT_TYPE):
 q=update.pre_checkout_query;ok=await commerce.precheckout(q.invoice_payload,q.from_user.id,q.total_amount);await q.answer(ok=ok,error_message=None if ok else "صورتحساب نامعتبر یا منقضی شده است.")
async def paid(update:Update,context:ContextTypes.DEFAULT_TYPE):
 p=update.effective_message.successful_payment
 if not p:return
 purpose=await commerce.settle(p.invoice_payload,update.effective_user.id,p.total_amount,p.telegram_payment_charge_id,p.provider_payment_charge_id or None)
 await update.effective_message.reply_text("✅ پرداخت ثبت شد. کمپین به‌صورت خودکار در گروه‌های واجد شرایط برنامه‌ریزی می‌شود." if purpose=="advertisement" else "✅ سهم استارز ثبت شد؛ با تکمیل ۱۰ استار اشتراک گروه فعال می‌شود.")
def register(app):
 app.add_handler(CallbackQueryHandler(callback,pattern=r"^ad:"),group=0)
 app.add_handler(PreCheckoutQueryHandler(precheckout),group=0)
 app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT,paid),group=0)
 app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.PHOTO,photo),group=1)
 app.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT & ~filters.COMMAND,text),group=2)