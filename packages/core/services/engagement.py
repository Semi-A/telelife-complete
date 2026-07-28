"""Idempotent group engagement: streaks, timed decisions, market alerts and daily digests."""
from __future__ import annotations
from datetime import UTC, datetime
from packages.core import db
from packages.core.repositories import outbox_repo

async def _update_streaks(conn)->int:
    result=await conn.execute("""INSERT INTO group_engagement_state(group_id,streak,best_streak,last_active_date)
      SELECT id,1,1,current_date FROM groups WHERE is_active AND last_active_at>=now()-interval '1 day'
      ON CONFLICT(group_id) DO UPDATE SET
       streak=CASE WHEN group_engagement_state.last_active_date=current_date THEN group_engagement_state.streak
                   WHEN group_engagement_state.last_active_date=current_date-1 THEN group_engagement_state.streak+1 ELSE 1 END,
       best_streak=GREATEST(group_engagement_state.best_streak,
                   CASE WHEN group_engagement_state.last_active_date=current_date-1 THEN group_engagement_state.streak+1 ELSE 1 END),
       last_active_date=current_date,updated_at=now()
      WHERE group_engagement_state.last_active_date IS DISTINCT FROM current_date""")
    return int(result.rsplit(' ',1)[-1])

async def _queue_digest(conn)->int:
    count=0
    rows=await conn.fetch("""SELECT g.id,g.telegram_id,c.name country_name,e.streak,
      (SELECT count(*) FROM citizenships cs WHERE cs.country_id=c.id AND cs.is_active) citizens,
      (SELECT current_price_toman FROM market_prices WHERE asset_code='USD') usd
      FROM groups g JOIN countries c ON c.group_id=g.id JOIN group_engagement_state e ON e.group_id=g.id
      WHERE g.is_active AND EXTRACT(HOUR FROM now() AT TIME ZONE 'UTC')=18
       AND e.last_digest_date IS DISTINCT FROM current_date""")
    for row in rows:
      payload={"text":f"📊 خلاصه امروز {row['country_name']}\n\n🔥 زنجیره فعالیت: {row['streak']} روز\n👥 شهروند فعال: {row['citizens']}\n💱 نرخ تتر: {int(row['usd'] or 0):,} تومان\n\nبرای ادامه زنجیره، امروز یک تصمیم گروهی بگیرید."}
      if await outbox_repo.enqueue(conn,f"group-digest:{row['id']}:{datetime.now(UTC).date()}","group_digest",payload,row['telegram_id']):count+=1
      await conn.execute("UPDATE group_engagement_state SET last_digest_date=current_date WHERE group_id=$1",row['id'])
    return count

async def _queue_events(conn)->int:
    count=0
    # One short collective decision per active group every 48h; resolution can be extended later.
    rows=await conn.fetch("""SELECT g.id,g.telegram_id,c.name country_name FROM groups g
      JOIN countries c ON c.group_id=g.id JOIN group_engagement_state s ON s.group_id=g.id
      WHERE g.is_active AND g.last_active_at>=now()-interval '1 day'
       AND (s.last_event_at IS NULL OR s.last_event_at<=now()-interval '48 hours')
       AND NOT EXISTS(SELECT 1 FROM group_live_events e WHERE e.group_id=g.id AND e.status='open') LIMIT 20""")
    for row in rows:
      event=await conn.fetchrow("""INSERT INTO group_live_events(group_id,event_code,title,payload,ends_at)
       VALUES($1,'market_reserve','تصمیم فوری ذخیره ارزی','{"choices":["تقویت خزانه","سرمایه‌گذاری فناوری"]}',now()+interval '45 minutes') RETURNING id,ends_at""",row['id'])
      text=f"⚡ تصمیم فوری برای {row['country_name']}\n\nذخیره تازه‌ای آزاد شده است. اعضا تا ۴۵ دقیقه فرصت دارند درباره «تقویت خزانه» یا «سرمایه‌گذاری فناوری» گفتگو کنند. رئیس‌جمهور تصمیم نهایی را ثبت می‌کند."
      if await outbox_repo.enqueue(conn,f"live-event:{event['id']}","group_live_event",{"text":text,"event_id":event['id']},row['telegram_id']):count+=1
      await conn.execute("UPDATE group_engagement_state SET last_event_at=now() WHERE group_id=$1",row['id'])
    return count

async def _market_alert(conn)->int:
    row=await conn.fetchrow("""SELECT price_toman,captured_at,previous FROM (
      SELECT s.price_toman,s.captured_at,lag(s.price_toman) OVER(ORDER BY s.captured_at) previous
      FROM market_price_snapshots s WHERE s.asset_code='USD') history
      ORDER BY captured_at DESC LIMIT 1""")
    if not row or not row['previous'] or int(row['previous'])==0:return 0
    change=(int(row['price_toman'])-int(row['previous']))*100/int(row['previous'])
    if abs(change)<0.5:return 0
    count=0
    groups=await conn.fetch("SELECT g.id,g.telegram_id,c.name country_name FROM groups g JOIN countries c ON c.group_id=g.id WHERE g.is_active AND g.last_active_at>=now()-interval '7 days'")
    bucket=row['captured_at'].strftime('%Y%m%d%H%M')
    for group in groups:
      text=f"📈 هشدار بازار: تتر {change:+.2f}٪ تغییر کرد و به {int(row['price_toman']):,} تومان رسید."
      if await outbox_repo.enqueue(conn,f"market-alert:{group['id']}:{bucket}","market_alert",{"text":text},group['telegram_id']):count+=1
    return count

async def minute_tick()->dict[str,int]:
    async with db.transaction() as conn:
      await conn.execute("UPDATE group_live_events SET status='expired' WHERE status='open' AND ends_at<=now()")
      return {"streaks":await _update_streaks(conn),"digests":await _queue_digest(conn),"events":await _queue_events(conn),"alerts":await _market_alert(conn)}
