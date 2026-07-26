"""Country minute/daily jobs; all operations are retry-safe."""
from __future__ import annotations
from telegram import Bot
from packages.core.services import country_economy,elections,news
async def resolve_due()->dict[str,int]:return await elections.resolve_due()
async def daily_events()->int:
 await country_economy.catch_up()
 return await news.ensure_daily_events()
async def publish_news(bot:Bot)->dict[str,int]:
 async def sender(chat_id,event_type,payload):
  if chat_id is None:return
  text=str(payload.get('text') or payload.get('event_code') or payload.get('mission_key') or event_type)
  await bot.send_message(chat_id=chat_id,text=text)
 return await news.publish_batch(sender)
