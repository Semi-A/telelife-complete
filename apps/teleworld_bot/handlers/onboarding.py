"""Welcoming lifecycle, guided menu and country-creation conversation."""
from __future__ import annotations
from telegram import Update
from telegram.error import BadRequest
from telegram.constants import ChatMemberStatus, ChatType
from telegram.ext import CallbackQueryHandler, ChatMemberHandler, CommandHandler, ContextTypes, MessageHandler, filters
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core.repositories import country_repo, group_repo, player_repo
from packages.core.services import country as country_service
from packages.core.services import economy, elections, production
from packages.core.repositories import production_repo
from packages.core.utils import fmt
from uuid import uuid4

_GROUPS={ChatType.GROUP,ChatType.SUPERGROUP}
FLOW_KEY="tw_country_flow"

async def _is_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
 chat=update.effective_chat; user=update.effective_user
 if not chat or not user:return False
 member=await context.bot.get_chat_member(chat.id,user.id)
 return member.status in {ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER}

async def _home(update: Update, context: ContextTypes.DEFAULT_TYPE, *, edit: bool=False) -> None:
 chat=update.effective_chat; msg=update.effective_message
 if not chat or not msg:return
 if chat.type not in _GROUPS:
  username=context.bot.username or ""
  await msg.reply_text(fa.WORLD_PRIVATE,reply_markup=kb.private(username) if username else None)
  return
 await group_repo.get_or_create(chat.id,chat.title or "سرزمین بی‌نام")
 country=await country_repo.by_chat(chat.id); admin=await _is_admin(update,context)
 text=fa.WORLD_HOME_COUNTRY.format(name=country["name"]) if country else fa.WORLD_HOME_EMPTY_ADMIN if admin else fa.WORLD_HOME_EMPTY_MEMBER
 markup=kb.home(bool(country),admin)
 if edit and update.callback_query:
  try: await update.callback_query.edit_message_text(text,reply_markup=markup)
  except BadRequest as exc:
   if "message is not modified" not in str(exc).lower(): raise
 else: await msg.reply_text(text,reply_markup=markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None: await _home(update,context)

async def welcomed(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 change=update.my_chat_member
 if not change or change.chat.type not in _GROUPS:return
 old,new=change.old_chat_member.status,change.new_chat_member.status
 if old in {ChatMemberStatus.LEFT,ChatMemberStatus.BANNED} and new in {ChatMemberStatus.MEMBER,ChatMemberStatus.ADMINISTRATOR}:
  await group_repo.get_or_create(change.chat.id,change.chat.title or "سرزمین بی‌نام")
  await context.bot.send_message(change.chat.id,fa.WORLD_ADDED,reply_markup=kb.home(False,False))

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 q=update.callback_query
 if not q:return
 action=(q.data or "").removeprefix("tw:")
 if action in {"home","cancel"}:
  await q.answer();context.chat_data.pop(FLOW_KEY,None);await _home(update,context,edit=True);return
 if action=="guide":await q.answer();await q.edit_message_text(fa.WORLD_GUIDE,reply_markup=kb.back());return
 if action=="create":
  if not await _is_admin(update,context):await q.answer(fa.ADMIN_REQUIRED,show_alert=True);return
  if await country_repo.by_chat(q.message.chat.id):await q.answer(fa.COUNTRY_EXISTS,show_alert=True);return
  await q.answer();context.chat_data[FLOW_KEY]={"step":"name","owner_id":q.from_user.id}
  await q.edit_message_text(fa.WIZARD_NAME,reply_markup=kb.cancel());return
 if action.startswith("gov:"):
  flow=context.chat_data.get(FLOW_KEY)
  if not flow or flow.get("owner_id")!=q.from_user.id or flow.get("step")!="government":return
  await q.answer();flow["government"]=action.split(":",1)[1];flow["step"]="description"
  await q.edit_message_text(fa.WIZARD_DESCRIPTION.format(name=flow["name"]),reply_markup=kb.cancel());return
 if action=="join":
  user=q.from_user; player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try: joined=await country_service.join_country(chat_id=q.message.chat.id,player_id=player.id)
  except ValueError:await q.answer(fa.COUNTRY_MISSING,show_alert=True);return
  await q.answer();await q.edit_message_text(fa.COUNTRY_JOINED if joined else fa.ALREADY_CITIZEN,reply_markup=kb.back());return
 if action=="country":
  row=await country_repo.by_chat(q.message.chat.id)
  await q.answer()
  if row:await q.edit_message_text(fa.COUNTRY_STATUS.format(name=row['name'],description=row['description'],government=fa.GOVERNMENT_NAMES.get(row['government_type'],row['government_type']),treasury=row['treasury_toman']),reply_markup=kb.country_actions())
  return
 if action=="jobs":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  row=await production_repo.get(player.id);await q.answer();await q.edit_message_text(fa.JOBS_GUIDE,reply_markup=kb.jobs_actions(bool(row)));return
 if action.startswith("donate:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");country=await country_repo.by_chat(q.message.chat.id)
  try: await economy.transfer(player.id,int(country["id"]),"IRT",int(action.split(":")[1]),reason="donation",idempotency_key=f"ui-donate:{player.id}:{uuid4().hex}");await q.answer("کمک مالی ثبت شد.",show_alert=True)
  except ValueError as exc: await q.answer("موجودی کافی نیست یا اقتصاد متوقف است.",show_alert=True)
  return
 if action=="leave":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");ok=await country_service.leave_country(chat_id=q.message.chat.id,player_id=player.id);await q.answer("از کشور خارج شدی." if ok else "عضویت فعالی نداشتی.",show_alert=True);return
 if action=="election":
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa");country=await country_repo.by_chat(q.message.chat.id)
  try: await elections.start(int(country["id"]),player.id);await q.answer("انتخابات آغاز شد.",show_alert=True)
  except (ValueError,PermissionError):await q.answer("شروع انتخابات برایت مجاز نیست یا انتخابات دیگری باز است.",show_alert=True)
  return
 if action.startswith("job:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:ok=await production.choose(player.id,action.split(":")[1]);await q.answer("شغل ثبت شد." if ok else "قبلاً شغل انتخاب کرده‌ای.",show_alert=True)
  except ValueError:await q.answer("شغل از سطح ۵ باز می‌شود.",show_alert=True)
  return
 if action=="jcollect" or action.startswith("jup:"):
  user=q.from_user;player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:
   if action=="jcollect":amount,xp=await production.collect(player.id,f"ui-collect:{player.id}:{uuid4().hex}");text=f"{fmt.number(amount)} واحد و {fmt.number(xp)} XP دریافت شد."
   else:lvl=await production.upgrade(player.id,action.split(":")[1],f"ui-up:{player.id}:{uuid4().hex}");text=f"ارتقا به سطح {fmt.number(lvl)} انجام شد."
   await q.answer(text,show_alert=True)
  except ValueError:await q.answer("عملیات شغلی انجام نشد؛ موجودی یا شرایط را بررسی کن.",show_alert=True)
  return
 if action=="politics":await q.answer();await q.edit_message_text(fa.POLITICS_GUIDE,reply_markup=kb.back());return
 if action=="donate_help":await q.answer();await q.edit_message_text(fa.DONATE_GUIDE,reply_markup=kb.back());return

async def wizard_text(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
 flow=context.chat_data.get(FLOW_KEY);msg=update.effective_message;user=update.effective_user;chat=update.effective_chat
 if not flow or not msg or not user or not chat or user.id!=flow.get("owner_id"):return
 text=(msg.text or "").strip()
 if flow["step"]=="name":
  if not 3<=len(text)<=80:await msg.reply_text(fa.WIZARD_NAME_ERROR);return
  flow["name"]=text;flow["step"]="government";await msg.reply_text(fa.WIZARD_GOVERNMENT,reply_markup=kb.governments());return
 if flow["step"]=="description":
  if not 10<=len(text)<=500:await msg.reply_text(fa.WIZARD_DESCRIPTION_ERROR);return
  player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or "شهروند",language_code=user.language_code or "fa")
  try:row=await country_service.create_country(chat_id=chat.id,chat_title=chat.title or "",player_id=player.id,name=flow["name"],government=flow["government"],description=text)
  except ValueError as exc:context.chat_data.pop(FLOW_KEY,None);await msg.reply_text(fa.INVALID_INPUT.format(reason=fa.ERROR_NAMES.get(str(exc),str(exc))),reply_markup=kb.home(False,True));return
  context.chat_data.pop(FLOW_KEY,None);await msg.reply_text(fa.COUNTRY_CREATED_GUIDED.format(name=row["name"]),reply_markup=kb.home(True,True))

def register(app)->None:
 app.add_handler(CommandHandler("start",start),group=0)
 app.add_handler(ChatMemberHandler(welcomed,ChatMemberHandler.MY_CHAT_MEMBER),group=0)
 app.add_handler(CallbackQueryHandler(callback,pattern=r"^tw:"),group=0)
 app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,wizard_text),group=1)
