"""Atomic subscriptions, Telegram Stars payments, moderation and ad delivery planning."""
from __future__ import annotations
from datetime import UTC,datetime,timedelta
from urllib.parse import urlparse
from uuid import uuid4
from packages.core import db
from packages.core.config import get_config
from packages.core.services.content_filter import require_clean

PACKAGES={"economy":(25,1,1,0),"standard":(60,3,24,1),"campaign":(120,6,72,2),"featured":(200,8,168,3)}
CHANNEL_PERCENT={"life":100,"world":150,"both":220}
def subscription_stars(citizens:int)->int:
 if citizens<=20:return 10
 if citizens<=100:return 15
 if citizens<=500:return 30
 if citizens<=1000:return 50
 return 75
def treasury_price(balance:int,citizens:int=0)->int:return min(1_000_000_000,max(20_000_000,balance*20//100+citizens*1_000_000))
def ad_price(package_code:str,channel:str)->int:
 if package_code not in PACKAGES or channel not in CHANNEL_PERCENT:raise ValueError("invalid_ad_selection")
 return (PACKAGES[package_code][0]*CHANNEL_PERCENT[channel]+99)//100
def valid_url(value:str)->bool:
 try:u=urlparse(value);return u.scheme in {"http","https"} and bool(u.netloc)
 except ValueError:return False

async def subscription_view(chat_id:int):
 return await db.fetchrow("""SELECT g.id,g.telegram_id,g.title,g.ad_free_until,c.treasury_toman,
  (SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens,
  r.id round_id,r.collected_stars,r.target_stars,r.expires_at
  FROM groups g LEFT JOIN countries c ON c.group_id=g.id
  LEFT JOIN subscription_rounds r ON r.group_id=g.id AND r.status='open'
  WHERE g.telegram_id=$1""",chat_id)

async def ensure_round(chat_id:int):
 async with db.transaction() as conn:
  group=await conn.fetchrow("SELECT id FROM groups WHERE telegram_id=$1 FOR UPDATE",chat_id)
  if not group:raise ValueError("group_not_found")
  citizens=int(await conn.fetchval("SELECT count(*) FROM citizenships cs JOIN countries c ON c.id=cs.country_id WHERE c.group_id=$1 AND cs.is_active",group["id"]) or 0);target=subscription_stars(citizens)
  row=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE group_id=$1 AND status='open'",group["id"])
  if row and row["expires_at"]>datetime.now(UTC):
   if int(row["target_stars"])!=target:await conn.execute("UPDATE subscription_rounds SET target_stars=$2 WHERE id=$1",row["id"],max(target,int(row["collected_stars"])))
   return await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1",row["id"])
  if row:await conn.execute("UPDATE subscription_rounds SET status='expired' WHERE id=$1",row["id"])
  return await conn.fetchrow("INSERT INTO subscription_rounds(group_id,target_stars) VALUES($1,$2) RETURNING *",group["id"],target)

async def subscription_invoice(round_id:int,payer_telegram_id:int,stars:int):
 if stars not in {1,2,5,10,25,50}:raise ValueError("invalid_stars")
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1 FOR UPDATE",round_id)
  if not row or row["status"]!='open' or row["expires_at"]<=datetime.now(UTC):raise ValueError("round_closed")
  amount=min(stars,int(row["target_stars"])-int(row["collected_stars"]));payload=f"sub:{round_id}:{payer_telegram_id}:{uuid4().hex}"
  await conn.execute("INSERT INTO star_payments(purpose,reference_id,payer_telegram_id,stars,invoice_payload,expires_at) VALUES('subscription',$1,$2,$3,$4,LEAST($5,now()+interval '30 minutes'))",round_id,payer_telegram_id,amount,payload,row["expires_at"])
  return payload,amount

async def create_ad_request(player_id:int,package_code:str,channel:str,title:str,description:str,url:str,image_bytes:bytes|None,image_mime:str|None,start_at=None)->int:
 if package_code not in PACKAGES or channel not in CHANNEL_PERCENT:raise ValueError("invalid_package")
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 if image_bytes and (len(image_bytes)>5_000_000 or image_mime not in {'image/jpeg','image/png','image/webp'}):raise ValueError("invalid_image")
 base,impressions,hours,priority=PACKAGES[package_code];stars=ad_price(package_code,channel)
 return int(await db.fetchval("""INSERT INTO ad_requests(requester_player_id,package_code,channel,title,description,target_url,image_bytes,image_mime,requested_start_at,price_stars,impressions_planned,campaign_hours,priority)
 VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13) RETURNING id""",player_id,package_code,channel,title,description,url,image_bytes,image_mime,start_at,stars,impressions,hours,priority))

async def ad_invoice(ad_id:int,payer_telegram_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT * FROM ad_requests WHERE id=$1 FOR UPDATE",ad_id)
  if not row or row["requester_player_id"]!=await conn.fetchval("SELECT id FROM players WHERE telegram_id=$1",payer_telegram_id):raise PermissionError("not_owner")
  if row["status"]!='approved_unpaid' or not row["payment_expires_at"] or row["payment_expires_at"]<=datetime.now(UTC):raise ValueError("payment_expired")
  payload=f"ad:{ad_id}:{payer_telegram_id}:{uuid4().hex}"
  await conn.execute("INSERT INTO star_payments(purpose,reference_id,payer_telegram_id,stars,invoice_payload,expires_at) VALUES('advertisement',$1,$2,$3,$4,$5)",ad_id,payer_telegram_id,row["price_stars"],payload,row["payment_expires_at"])
  return payload,int(row["price_stars"]),str(row["title"])

async def precheckout(payload:str,payer:int,total:int)->bool:
 row=await db.fetchrow("SELECT * FROM star_payments WHERE invoice_payload=$1",payload)
 return bool(row and row["status"]=='invoiced' and row["payer_telegram_id"]==payer and row["stars"]==total and row["expires_at"]>datetime.now(UTC))

async def settle(payload:str,payer:int,total:int,tg_charge:str,provider_charge:str|None)->str:
 async with db.transaction() as conn:
  payment=await conn.fetchrow("SELECT * FROM star_payments WHERE invoice_payload=$1 FOR UPDATE",payload)
  if not payment or payment["payer_telegram_id"]!=payer or payment["stars"]!=total or payment["status"] not in {'invoiced','paid'}:raise ValueError("invalid_payment")
  if payment["status"]=='paid':return payment["purpose"]
  await conn.execute("UPDATE star_payments SET status='paid',telegram_charge_id=$2,provider_charge_id=$3,paid_at=now() WHERE id=$1",payment["id"],tg_charge,provider_charge)
  if payment["purpose"]=='subscription':
   rnd=await conn.fetchrow("SELECT * FROM subscription_rounds WHERE id=$1 FOR UPDATE",payment["reference_id"])
   if rnd and rnd["status"]=='open':
    target=int(rnd["target_stars"]);total_stars=min(target,int(rnd["collected_stars"])+int(payment["stars"]));complete=total_stars>=target
    await conn.execute("UPDATE subscription_rounds SET collected_stars=$2,status=CASE WHEN $3 THEN 'completed' ELSE status END,completed_at=CASE WHEN $3 THEN now() ELSE NULL END WHERE id=$1",rnd["id"],total_stars,complete)
    if complete:
     until=await conn.fetchval("UPDATE groups SET ad_free_until=GREATEST(COALESCE(ad_free_until,now()),now())+interval '30 days' WHERE id=$1 RETURNING ad_free_until",rnd["group_id"])
     await conn.execute("INSERT INTO group_subscription_events(group_id,source,stars,starts_at,ends_at) VALUES($1,'stars',$3,now(),$2)",rnd["group_id"],until,target)
  else:
   await conn.execute("UPDATE ad_requests SET status='paid',paid_at=now(),updated_at=now() WHERE id=$1 AND status='approved_unpaid'",payment["reference_id"])
  return str(payment["purpose"])

async def buy_with_treasury(chat_id:int,player_id:int)->int:
 async with db.transaction() as conn:
  row=await conn.fetchrow("SELECT g.id,c.id country_id,c.treasury_toman,c.president_player_id,(SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens FROM groups g JOIN countries c ON c.group_id=g.id WHERE g.telegram_id=$1 FOR UPDATE OF c,g",chat_id)
  if not row:raise ValueError("country_not_found")
  if row["president_player_id"]!=player_id:raise PermissionError("president_required")
  price=treasury_price(int(row["treasury_toman"]),int(row["citizens"]));until=await conn.fetchval("UPDATE groups SET ad_free_until=GREATEST(COALESCE(ad_free_until,now()),now())+interval '30 days' WHERE id=$1 RETURNING ad_free_until",row["id"])
  changed=await conn.fetchval("UPDATE countries SET treasury_toman=treasury_toman-$2 WHERE id=$1 AND treasury_toman>=$2 RETURNING treasury_toman",row["country_id"],price)
  if changed is None:raise ValueError("insufficient_balance")
  await conn.execute("INSERT INTO group_subscription_events(group_id,source,treasury_toman,starts_at,ends_at,actor_player_id) VALUES($1,'treasury',$2,now(),$3,$4)",row["id"],price,until,player_id)
  return price

async def approve_ad(ad_id:int,actor:str,note:str|None=None):
 return await db.fetchrow("UPDATE ad_requests SET status='approved_unpaid',approved_by=$2,admin_note=$3,approved_at=now(),payment_expires_at=now()+interval '48 hours',updated_at=now() WHERE id=$1 AND status IN ('pending_review','changes_requested') RETURNING *",ad_id,actor,note)
async def reject_ad(ad_id:int,actor:str,note:str):
 return await db.fetchrow("UPDATE ad_requests SET status='changes_requested',approved_by=$2,admin_note=$3,updated_at=now() WHERE id=$1 AND status IN ('pending_review','approved_unpaid') RETURNING *",ad_id,actor,note)

async def list_ads(limit:int=100):
 return await db.fetch("""SELECT a.id,a.package_code,a.channel,a.title,a.description,a.target_url,a.image_mime,a.status,a.price_stars,a.impressions_planned,a.campaign_hours,a.admin_note,a.requested_start_at,a.payment_expires_at,a.paid_at,a.first_delivery_at,a.created_at,p.telegram_id,p.first_name,
 count(d.id) FILTER(WHERE d.status='sent') delivered,count(d.id) FILTER(WHERE d.status IN ('scheduled','queued')) pending,count(d.id) FILTER(WHERE d.status='failed') failed
 FROM ad_requests a JOIN players p ON p.id=a.requester_player_id LEFT JOIN ad_deliveries d ON d.ad_request_id=a.id GROUP BY a.id,p.telegram_id,p.first_name ORDER BY a.created_at DESC LIMIT $1""",limit)
async def ad_image(ad_id:int):return await db.fetchrow("SELECT image_bytes,image_mime FROM ad_requests WHERE id=$1",ad_id)
async def edit_ad(ad_id:int,title:str,description:str,url:str,start_at):
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 return await db.fetchrow("UPDATE ad_requests SET title=$2,description=$3,target_url=$4,requested_start_at=$5,updated_at=now() WHERE id=$1 AND status IN ('pending_review','changes_requested','approved_unpaid') RETURNING *",ad_id,title,description,url,start_at)
async def pause_ad(ad_id:int):
 async with db.transaction() as conn:
  row=await conn.fetchrow("UPDATE ad_requests SET status='paused',updated_at=now() WHERE id=$1 AND status IN ('paid','active') RETURNING *",ad_id)
  if row:await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE ad_request_id=$1 AND status IN ('scheduled','queued')",ad_id)
  return row
async def refundable(ad_id:int):
 return await db.fetchrow("""SELECT a.*,p.telegram_id,sp.telegram_charge_id FROM ad_requests a JOIN players p ON p.id=a.requester_player_id JOIN star_payments sp ON sp.purpose='advertisement' AND sp.reference_id=a.id AND sp.status='paid' WHERE a.id=$1 AND a.first_delivery_at IS NULL""",ad_id)
async def mark_refunded(ad_id:int):
 async with db.transaction() as conn:
  await conn.execute("UPDATE star_payments SET status='refunded',refunded_at=now() WHERE purpose='advertisement' AND reference_id=$1 AND status='paid'",ad_id)
  await conn.execute("UPDATE ad_requests SET status='refunded',updated_at=now() WHERE id=$1",ad_id)
  await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE ad_request_id=$1 AND status IN ('scheduled','queued')",ad_id)
async def expire_commerce()->dict[str,int]:
 p=await db.execute("UPDATE ad_requests SET status='payment_expired',updated_at=now() WHERE status='approved_unpaid' AND payment_expires_at<=now()")
 s=await db.execute("UPDATE star_payments SET status='expired' WHERE status='invoiced' AND expires_at<=now()")
 return {"ads":int(p.rsplit(' ',1)[-1]),"payments":int(s.rsplit(' ',1)[-1])}
async def plan_paid_ads()->int:
 count=0
 async with db.transaction() as conn:
  ads=await conn.fetch("SELECT * FROM ad_requests WHERE status='paid' FOR UPDATE SKIP LOCKED LIMIT 20")
  for ad in ads:
   start=max(datetime.now(UTC),ad["requested_start_at"] or datetime.now(UTC));n=max(1,int(ad["impressions_planned"]));hours=int(ad["campaign_hours"])
   if ad["channel"] in {'world','both'}:
    groups=await conn.fetch("SELECT id,telegram_id FROM groups WHERE is_active AND last_active_at>=now()-interval '14 days' AND (ad_free_until IS NULL OR ad_free_until<=now())")
    for group in groups:
     for slot in range(n):
      when=start+timedelta(seconds=(hours*3600*slot/max(1,n-1) if n>1 else 0));result=await conn.execute("INSERT INTO ad_deliveries(ad_request_id,group_id,destination_type,destination_telegram_id,slot_no,scheduled_at) VALUES($1,$2,'world',$3,$4,$5) ON CONFLICT DO NOTHING",ad["id"],group["id"],group["telegram_id"],slot+1,when);count+=int(result.rsplit(' ',1)[-1])
   if ad["channel"] in {'life','both'}:
    players=await conn.fetch("SELECT telegram_id FROM players WHERE NOT is_banned AND NOT is_frozen AND last_seen_at>=now()-interval '30 days'")
    for person in players:
     for slot in range(n):
      when=start+timedelta(seconds=(hours*3600*slot/max(1,n-1) if n>1 else 0));result=await conn.execute("INSERT INTO ad_deliveries(ad_request_id,group_id,destination_type,destination_telegram_id,slot_no,scheduled_at) VALUES($1,NULL,'life',$2,$3,$4) ON CONFLICT DO NOTHING",ad["id"],person["telegram_id"],slot+1,when);count+=int(result.rsplit(' ',1)[-1])
   await conn.execute("UPDATE ad_requests SET status='active',updated_at=now() WHERE id=$1",ad["id"])
 return count
async def queue_due_deliveries()->int:
 from packages.core.repositories import outbox_repo
 count=0
 async with db.transaction() as conn:
  rows=await conn.fetch("""SELECT d.*,g.ad_free_until,g.ads_delivered_today,g.ads_delivery_day,a.priority FROM ad_deliveries d JOIN ad_requests a ON a.id=d.ad_request_id LEFT JOIN groups g ON g.id=d.group_id WHERE d.status='scheduled' AND d.scheduled_at<=now() AND a.status='active' ORDER BY a.priority DESC,d.scheduled_at FOR UPDATE OF d,g SKIP LOCKED LIMIT 200""")
  for row in rows:
   today=datetime.now(UTC).date()
   if row["destination_type"]=='world':
    used=int(row["ads_delivered_today"] if row["ads_delivery_day"]==today else 0)
    if row["ad_free_until"] and row["ad_free_until"]>datetime.now(UTC):await conn.execute("UPDATE ad_deliveries SET status='cancelled' WHERE id=$1",row["id"]);continue
    if used>=2:await conn.execute("UPDATE ad_deliveries SET scheduled_at=date_trunc('day',now())+interval '1 day 9 hours' WHERE id=$1",row["id"]);continue
   key=f"market-ad:{row['id']}"
   if await outbox_repo.enqueue(conn,key,"marketplace_ad",{"ad_id":row["ad_request_id"],"delivery_id":row["id"],"destination_type":row["destination_type"]},row["destination_telegram_id"]):
    await conn.execute("UPDATE ad_deliveries SET status='queued',outbox_key=$2 WHERE id=$1",row["id"],key)
    if row["destination_type"]=='world':await conn.execute("UPDATE groups SET ads_delivered_today=$2,ads_delivery_day=$3 WHERE id=$1",row["group_id"],used+1,today)
    count+=1
  return count

async def player_ads(player_id:int):
 return await db.fetch("SELECT id,title,status,admin_note,price_stars,payment_expires_at FROM ad_requests WHERE requester_player_id=$1 ORDER BY created_at DESC LIMIT 20",player_id)
async def revision_source(ad_id:int,player_id:int):
 return await db.fetchrow("SELECT * FROM ad_requests WHERE id=$1 AND requester_player_id=$2 AND status='changes_requested'",ad_id,player_id)
async def submit_revision(ad_id:int,player_id:int,title:str,description:str,url:str,image_bytes:bytes|None,image_mime:str|None,start_at)->bool:
 require_clean(title,"name");require_clean(description,"description")
 if not valid_url(url):raise ValueError("invalid_url")
 result=await db.execute("""UPDATE ad_requests SET title=$3,description=$4,target_url=$5,image_bytes=COALESCE($6,image_bytes),image_mime=COALESCE($7,image_mime),requested_start_at=$8,status='pending_review',admin_note=NULL,approved_by=NULL,approved_at=NULL,payment_expires_at=NULL,updated_at=now() WHERE id=$1 AND requester_player_id=$2 AND status='changes_requested'""",ad_id,player_id,title,description,url,image_bytes,image_mime,start_at)
 return result!='UPDATE 0'
