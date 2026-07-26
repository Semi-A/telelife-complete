"""Thin Telegram adapters for country/economy commands."""
from __future__ import annotations
from uuid import uuid4
from telegram import Update
from telegram.constants import ChatMemberStatus,ChatType
from telegram.ext import CommandHandler,ContextTypes
from apps.teleworld_bot.texts import fa
from packages.core.repositories import country_repo,player_repo
from packages.core.services import country as country_service,economy,country_missions
GROUPS={ChatType.GROUP,ChatType.SUPERGROUP}
async def _ctx(update:Update):
 chat=update.effective_chat;user=update.effective_user;message=update.effective_message
 if not chat or not user or not message or chat.type not in GROUPS:
  if message:await message.reply_text(fa.PRIVATE_ONLY)
  return None
 player=await player_repo.get_or_create(user.id,username=user.username,first_name=user.first_name or '',language_code=user.language_code or 'fa')
 return chat,user,message,player
async def create(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await _ctx(update)
 if not x:return
 chat,user,message,player=x;member=await context.bot.get_chat_member(chat.id,user.id)
 if member.status not in {ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER}:await message.reply_text(fa.ADMIN_REQUIRED);return
 parts=[p.strip() for p in ' '.join(context.args).split('|')]
 if len(parts)!=3:await message.reply_text(fa.CREATE_USAGE);return
 row=await country_service.create_country(chat_id=chat.id,chat_title=chat.title or '',player_id=player.id,name=parts[0],government=parts[1].lower(),description=parts[2]);await message.reply_text(fa.COUNTRY_CREATED.format(name=row['name']))
async def join(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await _ctx(update)
 if x:
  chat,_,message,player=x;await country_service.join_country(chat_id=chat.id,player_id=player.id);await message.reply_text(fa.COUNTRY_JOINED)
async def show(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await _ctx(update)
 if x:
  chat,_,message,_=x;row=await country_repo.by_chat(chat.id)
  if not row:await message.reply_text(fa.COUNTRY_MISSING);return
  await message.reply_text(fa.COUNTRY_STATUS.format(name=row['name'],description=row['description'],government=row['government_type'],treasury=row['treasury_toman']))
async def donate(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await _ctx(update)
 if not x:return
 chat,_,message,player=x
 if len(context.args)!=2:await message.reply_text(fa.DONATE_USAGE);return
 asset=context.args[0];amount=int(context.args[1]);c=await country_repo.by_chat(chat.id)
 if not c:await message.reply_text(fa.COUNTRY_MISSING);return
 await economy.transfer(player_id=player.id,country_id=c['id'],asset=asset,amount=amount,reason='country_donation',idempotency_key=f'donate:{message.message_id}:{player.id}')
 await country_missions.report(c['id'],'donate',asset,amount);await message.reply_text(fa.DONATED.format(amount=amount,asset=asset))
async def tax(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 if len(context.args)!=1:return await donate(update,context)
 context.args=['IRT',context.args[0]];await donate(update,context)
def register(application)->None:
 for cmd,fn in [('createcountry',create),('joincountry',join),('country',show),('economy',show),('resources',show),('donate',donate),('paytax',tax)]:application.add_handler(CommandHandler(cmd,fn))
