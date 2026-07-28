"""Thin election, project, poll and presidential adapters."""
from __future__ import annotations
from telegram import Update
from telegram.ext import CommandHandler,ContextTypes
from apps.teleworld_bot.texts import fa
from packages.core import db
from packages.core.repositories import country_repo,election_repo,player_repo,project_repo,outbox_repo
from packages.core.services import elections,national_project
async def ctx(update:Update):
 chat=update.effective_chat;u=update.effective_user;m=update.effective_message
 if not chat or not u or not m:return None
 p=await player_repo.get_or_create(u.id,username=u.username,first_name=u.first_name or '',language_code=u.language_code or 'fa');c=await country_repo.by_chat(chat.id)
 return chat,m,p,c
async def start_election(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:await elections.start(x[3]['id'],x[2].id);await x[1].reply_text(fa.ELECTION_STARTED)
async def nominate(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:
  e=await election_repo.open_for_country(x[3]['id']);await elections.nominate(e['id'],x[2].id,x[0].id,x[1].message_id);await x[1].reply_text(fa.NOMINATED)
async def vote(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and x[1].reply_to_message:
  e=await election_repo.open_for_country(x[3]['id']);candidate=await db.fetchval('SELECT player_id FROM election_candidates WHERE election_id=$1 AND message_id=$2',e['id'],x[1].reply_to_message.message_id)
  ok=await elections.vote(e['id'],x[2].id,candidate);await x[1].reply_text(fa.VOTED if ok else fa.DUPLICATE_VOTE)
async def start_project(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:await national_project.start(x[3]['id'],x[2].id);await x[1].reply_text(fa.PROJECT_STARTED)
async def contribute(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and len(context.args)==2:
  p=await project_repo.active(x[3]['id']);used,_=await national_project.contribute(p['id'],x[2].id,context.args[0],int(context.args[1]),f'project:{x[1].message_id}:{x[2].id}');await x[1].reply_text(fa.CONTRIBUTED.format(amount=used))
async def poll(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update);parts=[v.strip() for v in ' '.join(context.args).split('|')]
 if x and x[3] and len(parts)>=3:await elections.create_poll(x[3]['id'],x[2].id,parts[0],parts[1:]);await x[1].reply_text(fa.POLL_STARTED)
async def polls(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3]:
  rows=await election_repo.polls(x[3]["id"])
  text="\n".join(f"{v['id']}: {v['question']}" for v in rows) or fa.COUNTRY_MISSING
  await x[1].reply_text(text)
async def pollvote(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and len(context.args)==2:ok=await election_repo.poll_vote(int(context.args[0]),x[2].id,int(context.args[1]));await x[1].reply_text(fa.VOTED if ok else fa.DUPLICATE_VOTE)
async def setflag(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and x[1].photo and x[1].caption:
  photo=x[1].photo[-1];ok=await country_repo.set_flag(x[3]['id'],x[2].id,photo.file_id,photo.file_unique_id);await x[1].reply_text(fa.FLAG_SET if ok else fa.PRESIDENT_REQUIRED)
async def announce(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
 x=await ctx(update)
 if x and x[3] and await country_repo.is_president(x[3]['id'],x[2].id):
  async with db.transaction() as conn:await outbox_repo.enqueue(conn,f'announce:{x[1].message_id}','country_announcement',{'text':' '.join(context.args)},x[0].id)
  await x[1].reply_text(fa.ANNOUNCED)
def register(application) -> None:
    """Legacy slash adapter intentionally disabled; use glass panels."""
    return