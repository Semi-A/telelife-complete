"""Country minute/daily jobs; all operations are retry-safe."""
from __future__ import annotations
from telegram import Bot
from packages.core.services import country_economy,elections,news,commerce,country_identity
async def resolve_due()->dict[str,int]:return await elections.resolve_due()
async def daily_events()->int:
 await country_economy.catch_up()
 return await news.ensure_daily_events()
async def publish_news(bot:Bot,life_bot:Bot|None=None)->dict[str,int]:
 async def sender(chat_id,event_type,payload):
  if chat_id is None:return
  if event_type=="marketplace_ad":
   from packages.core import db
   ad=await db.fetchrow("SELECT * FROM ad_requests WHERE id=$1",payload["ad_id"])
   if not ad:return
   if payload.get("destination_type")=="world":
    protected=await db.fetchval("SELECT ad_free_until>now() FROM groups WHERE telegram_id=$1",chat_id)
    if protected:
     await db.execute("UPDATE ad_deliveries SET status='cancelled' WHERE id=$1",payload["delivery_id"]);return
   text=f"📣 <b>{ad['title']}</b>\n\n{ad['description']}\n\n🔗 {ad['target_url']}"
   if ad["image_bytes"] and len(text)>1000:text=text[:960]+"…\n\n🔗 "+str(ad['target_url'])[:45]
   sender_bot=life_bot if payload.get("destination_type")=="life" and life_bot is not None else bot
   if ad["image_bytes"]:await sender_bot.send_photo(chat_id=chat_id,photo=bytes(ad["image_bytes"]),caption=text)
   else:await sender_bot.send_message(chat_id=chat_id,text=text)
   await db.execute("UPDATE ad_deliveries SET status='sent',sent_at=now() WHERE id=$1",payload["delivery_id"])
   await db.execute("UPDATE ad_requests SET first_delivery_at=COALESCE(first_delivery_at,now()),updated_at=now() WHERE id=$1",payload["ad_id"])
   await db.execute("UPDATE ad_requests SET status='completed',updated_at=now() WHERE id=$1 AND NOT EXISTS(SELECT 1 FROM ad_deliveries WHERE ad_request_id=$1 AND status IN ('scheduled','queued'))",payload["ad_id"])
   return
  text=str(payload.get('text') or payload.get('event_code') or payload.get('mission_key') or event_type)
  destination=await country_identity.destination(chat_id)
  if destination:
   if not destination['country_id']:
    if await country_identity.should_send_setup_notice(chat_id):await bot.send_message(chat_id=chat_id,text=country_identity.SETUP_TEXT)
    return
   text=country_identity.masthead(str(destination['country_name']),text)
  await bot.send_message(chat_id=chat_id,text=text)
 return await news.publish_batch(sender)

async def queue_due_ads()->int:
 from packages.core import db
 from packages.core.repositories import outbox_repo
 count=0
 async with db.transaction() as conn:
  rows=await conn.fetch("SELECT * FROM ad_campaigns WHERE status='scheduled' AND scheduled_at<=now() FOR UPDATE SKIP LOCKED LIMIT 50")
  for row in rows:
   key=f"ad-scheduled:{row['id']}:{row['scheduled_at'].isoformat()}"
   if await outbox_repo.enqueue(conn,key,"advertisement",{"text":row["body"],"ad_id":row["id"]},row["destination_chat_id"]):count+=1
   if row["repeat_minutes"]:
    await conn.execute("UPDATE ad_campaigns SET scheduled_at=now()+($2::int*interval '1 minute'),last_queued_at=now(),updated_at=now() WHERE id=$1",row["id"],row["repeat_minutes"])
   else: await conn.execute("UPDATE ad_campaigns SET status='queued',last_queued_at=now(),updated_at=now() WHERE id=$1",row["id"])
 return count

async def run_commerce()->dict[str,int]:
 await __import__("packages.core.services.migration",fromlist=["expire"]).expire();expired=await commerce.expire_commerce();planned=await commerce.plan_paid_ads();queued=await commerce.queue_due_deliveries();return {**expired,"planned":planned,"queued":queued}