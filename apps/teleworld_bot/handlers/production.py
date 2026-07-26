"""Thin job and lazy-production Telegram adapters."""
from __future__ import annotations
from telegram import Update
from telegram.ext import CommandHandler,ContextTypes
from apps.teleworld_bot.texts import fa
from packages.core.repositories import player_repo
from packages.core.services import production
async def player(update:Update):
 u=update.effective_user
 return await player_repo.get_or_create(u.id,username=u.username,first_name=u.first_name or '',language_code=u.language_code or 'fa') if u else None
async def jobs(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 if update.effective_message:await update.effective_message.reply_text(fa.JOBS)
async def choose(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 p=await player(update)
 if p and context.args:
  await production.choose(p.id,context.args[0]);await update.effective_message.reply_text(fa.JOB_CHOSEN)
async def collect(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 p=await player(update)
 if p:
  a,x=await production.collect(p.id,f'collect:{p.id}:{update.effective_message.message_id}');await update.effective_message.reply_text(fa.COLLECTED.format(amount=a,xp=x))
async def upgrade(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 p=await player(update)
 if p and context.args:
  kind=context.args[0];level=await production.upgrade(p.id,kind,f'upgrade:{p.id}:{update.effective_message.message_id}');await update.effective_message.reply_text(fa.UPGRADED.format(kind=kind,level=level))
def register(app)->None:
 for c,f in [('jobs',jobs),('choosejob',choose),('collect',collect),('upgrade',upgrade)]:app.add_handler(CommandHandler(c,f))
