"""One persistent TeleLife panel: edit first, send only when no editable panel exists."""
from __future__ import annotations
from telegram import Message
from telegram.error import BadRequest,Forbidden
from telegram.ext import ContextTypes
from packages.core.repositories import ui_state_repo
from packages.core.ui import schedule_cleanup

async def show(context:ContextTypes.DEFAULT_TYPE,player_id:int,chat_id:int,text:str,markup,*,message:Message|None=None):
 state=await ui_state_repo.ensure_life(player_id); target=None
 # A callback's own message is always the freshest valid panel.
 if message is not None and getattr(message,"message_id",None):
  try:
   result=await message.edit_text(text,reply_markup=markup);target=result if isinstance(result,Message) else message
  except BadRequest as exc:
   if "message is not modified" in str(exc).lower():target=message
   elif "message to edit not found" not in str(exc).lower() and "message can't be edited" not in str(exc).lower():raise
 # On /start, edit the remembered panel instead of producing another one.
 if target is None and state and state["life_message_id"]:
  try:
   result=await context.bot.edit_message_text(chat_id=int(state["life_chat_id"] or chat_id),message_id=int(state["life_message_id"]),text=text,reply_markup=markup)
   target=result if isinstance(result,Message) else None
  except (BadRequest,Forbidden):target=None
 if target is None:
  target=await context.bot.send_message(chat_id=chat_id,text=text,reply_markup=markup)
 await ui_state_repo.set_life_panel(player_id,chat_id,target.message_id if target else int(state["life_message_id"]))
 if target is not None:
  schedule_cleanup(context,target,"profile")
 return target
