"""Read models and audited mutation primitives for the admin command center."""
from __future__ import annotations

from typing import Any
import asyncpg
from packages.core import db

async def audit(conn: asyncpg.Connection, actor: str, action: str, request_id: str,
                details: dict[str, Any], player_id: int | None = None,
                country_id: int | None = None) -> bool:
    return await conn.fetchval(
        """INSERT INTO admin_audit_log
        (admin_actor,action,target_player_id,target_country_id,request_id,details)
        VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING id""",
        actor, action, player_id, country_id, request_id, details,
    ) is not None

async def set_ban(conn: asyncpg.Connection, player_id: int, banned: bool,
                  reason: str | None) -> None:
    result = await conn.execute(
        "UPDATE players SET is_banned=$2,ban_reason=$3 WHERE id=$1", player_id, banned, reason
    )
    if result == "UPDATE 0":
        raise ValueError("player_not_found")

async def set_flag(conn: asyncpg.Connection, key: str, enabled: bool, actor: str) -> None:
    await conn.execute(
        """INSERT INTO feature_flags(key,enabled,updated_by) VALUES($1,$2,$3)
        ON CONFLICT(key) DO UPDATE SET enabled=$2,updated_by=$3,updated_at=now()""",
        key, enabled, actor,
    )

async def dashboard_stats() -> asyncpg.Record | None:
    return await db.fetchrow("""
        SELECT
          (SELECT count(*) FROM players) AS players_total,
          (SELECT count(*) FROM players WHERE last_seen_at >= now()-interval '7 days') AS players_active,
          (SELECT count(*) FROM countries) AS countries_total,
          (SELECT count(*) FROM groups WHERE is_active) AS groups_total,
          (SELECT COALESCE(sum(wallet_toman+savings_toman),0) FROM players) AS player_liquidity,
          (SELECT COALESCE(sum(treasury_toman),0) FROM countries) AS country_treasury,
          (SELECT count(*) FROM news_outbox WHERE published_at IS NULL) AS news_pending,
          (SELECT count(*) FROM players WHERE is_banned) AS players_banned
    """)

async def stats() -> asyncpg.Record | None:
    return await db.fetchrow("""SELECT
        (SELECT count(*) FROM players) players,
        (SELECT count(*) FROM countries) countries,
        (SELECT count(*) FROM citizenships WHERE is_active) citizens""")

async def users(limit: int = 100, query: str = "") -> list[asyncpg.Record]:
    needle = f"%{query.strip()}%"
    return await db.fetch("""
        SELECT id,telegram_id,username,first_name,level,xp,wallet_toman,savings_toman,
               usd_cents,is_banned,is_frozen,ban_reason,last_seen_at,created_at
        FROM players
        WHERE $2='' OR first_name ILIKE $3 OR COALESCE(username,'') ILIKE $3
                      OR telegram_id::text=$2 OR id::text=$2
        ORDER BY last_seen_at DESC LIMIT $1
    """, limit, query.strip(), needle)

async def countries(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT c.id,c.name,c.government_type,c.treasury_toman,c.daily_income_toman,
               c.daily_expense_toman,c.president_player_id,p.first_name AS president_name,
               count(DISTINCT z.player_id) AS citizens,
               COALESCE(jsonb_object_agg(r.asset_code,r.quantity)
                 FILTER (WHERE r.asset_code IS NOT NULL),'{}'::jsonb) AS resources,
               c.created_at
        FROM countries c
        LEFT JOIN players p ON p.id=c.president_player_id
        LEFT JOIN citizenships z ON z.country_id=c.id AND z.is_active
        LEFT JOIN country_resources r ON r.country_id=c.id
        GROUP BY c.id,p.first_name ORDER BY c.treasury_toman DESC LIMIT $1
    """, limit)

async def audits(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("SELECT * FROM admin_audit_log ORDER BY created_at DESC LIMIT $1", limit)

async def news_rows(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT id,event_type,destination_chat_id,payload,attempts,available_at,
               processing_until,published_at,last_error_code,created_at
        FROM news_outbox ORDER BY created_at DESC LIMIT $1
    """, limit)

async def market_history(hours: int = 24) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT p.asset_code,p.title_fa,p.current_price_toman,p.updated_at,p.source,p.source_checked_at,p.source_error,
               COALESCE(jsonb_agg(jsonb_build_object(
                 'time',s.captured_at,'price',s.price_toman) ORDER BY s.captured_at)
                 FILTER (WHERE s.captured_at IS NOT NULL),'[]'::jsonb) AS points
        FROM market_prices p
        LEFT JOIN market_price_snapshots s ON s.asset_code=p.asset_code
          AND s.captured_at >= now()-($1::int * interval '1 hour')
        GROUP BY p.asset_code,p.title_fa,p.current_price_toman,p.updated_at,p.source,p.source_checked_at,p.source_error
        ORDER BY CASE p.asset_code WHEN 'USD' THEN 0 ELSE 1 END,p.asset_code
    """, hours)

async def capture_market_snapshot() -> int:
    result = await db.execute("""
        INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
        SELECT asset_code,current_price_toman,date_trunc('minute',now()) FROM market_prices
        ON CONFLICT DO NOTHING
    """)
    return int(result.rsplit(" ", 1)[-1])

async def ads(limit: int = 100) -> list[asyncpg.Record]:
    return await db.fetch("SELECT * FROM ad_campaigns ORDER BY created_at DESC LIMIT $1", limit)

async def ad_owner(ad_id:int):
 return await db.fetchrow("SELECT p.telegram_id,p.first_name FROM ad_requests a JOIN players p ON p.id=a.requester_player_id WHERE a.id=$1",ad_id)


async def operations_status() -> dict[str, object]:
    market=await db.fetchrow("""SELECT asset_code,current_price_toman,source,source_checked_at,
      source_error,updated_at,now()-source_checked_at AS source_age
      FROM market_prices WHERE asset_code='USD'""")
    jobs=await db.fetch("""SELECT DISTINCT ON(job_name) job_name,status,started_at,finished_at,
      duration_ms,result,error_type,error_message FROM scheduler_job_runs
      ORDER BY job_name,started_at DESC""")
    queues=await db.fetchrow("""SELECT
      (SELECT count(*) FROM news_outbox WHERE published_at IS NULL) outbox_pending,
      (SELECT count(*) FROM news_outbox WHERE published_at IS NULL AND last_error_code IS NOT NULL) outbox_failed,
      (SELECT count(*) FROM ad_deliveries WHERE status='scheduled') ads_scheduled,
      (SELECT count(*) FROM ad_deliveries WHERE status='failed') ads_failed,
      (SELECT count(*) FROM group_live_events WHERE status='open') live_events""")
    frozen=bool(await db.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"))
    return {"market":dict(market) if market else None,"jobs":[dict(x) for x in jobs],
            "queues":dict(queues) if queues else {},"market_frozen":frozen}
async def engagement_overview() -> dict[str, object]:
    """Retention and onboarding signals computed from canonical game tables."""
    row = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE created_at >= now()-interval '24 hours') AS new_24h,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '24 hours') AS active_24h,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '7 days') AS active_7d,
          count(*) FILTER (WHERE last_seen_at >= now()-interval '30 days') AS active_30d,
          count(*) FILTER (WHERE level >= 5) AS reached_jobs,
          count(*) FILTER (WHERE level >= 10) AS reached_market,
          count(*) AS total
        FROM players
    """)
    claims = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE last_claim_date=current_date) AS claimed_today,
          count(*) FILTER (WHERE streak>=3) AS streak_3,
          count(*) FILTER (WHERE streak>=7) AS streak_7,
          COALESCE(avg(streak),0)::numeric(10,2) AS avg_streak
        FROM daily_state
    """)
    missions = await db.fetchrow("""
        SELECT
          count(*) AS assigned_today,
          count(*) FILTER (WHERE progress>=target) AS completed_today,
          count(*) FILTER (WHERE claimed_at IS NOT NULL) AS claimed_today
        FROM daily_missions WHERE mission_date=current_date
    """)
    onboarding = await db.fetchrow("""
        SELECT
          count(*) FILTER (WHERE onboarding_step>=4) AS completed,
          count(*) FILTER (WHERE onboarding_step<4) AS incomplete
        FROM player_ui_state
    """)
    return {
        "activity": dict(row) if row else {},
        "daily": dict(claims) if claims else {},
        "missions": dict(missions) if missions else {},
        "onboarding": dict(onboarding) if onboarding else {},
    }

async def feature_flags() -> list[asyncpg.Record]:
    return await db.fetch("SELECT key,enabled,updated_by,updated_at FROM feature_flags ORDER BY key")

async def ledger_rows(limit: int = 100, player_id: int | None = None) -> list[asyncpg.Record]:
    return await db.fetch("""
        SELECT l.id,l.player_id,l.country_id,l.reason,l.asset_code,l.account,l.amount,
               l.balance_after,l.metadata,l.created_at,p.first_name,p.username
        FROM ledger l LEFT JOIN players p ON p.id=l.player_id
        WHERE $2::bigint IS NULL OR l.player_id=$2
        ORDER BY l.created_at DESC LIMIT $1
    """, limit, player_id)

async def economy_integrity() -> dict[str, object]:
    row = await db.fetchrow("""
        SELECT
          (SELECT count(*) FROM players WHERE wallet_toman<0 OR savings_toman<0 OR usd_cents<0) negative_players,
          (SELECT count(*) FROM countries WHERE treasury_toman<0) negative_countries,
          (SELECT count(*) FROM ledger WHERE balance_after<0) negative_ledger_rows,
          (SELECT count(*) FROM ledger WHERE created_at>=now()-interval '24 hours') ledger_24h,
          (SELECT COALESCE(sum(amount),0) FROM ledger WHERE asset_code='IRT' AND created_at>=now()-interval '24 hours') net_irt_24h
    """)
    return dict(row) if row else {}


async def command_center() -> dict[str, object]:
    """Actionable operational picture assembled from canonical tables."""
    overview = await dashboard_stats()
    ops = await operations_status()
    integrity = await economy_integrity()
    countries_rows = await db.fetch("""
      SELECT c.id,c.name,c.status,c.treasury_toman,
        count(DISTINCT cs.player_id) FILTER (WHERE cs.is_active) citizens,
        COALESCE(i.inflation_bp,0) inflation_bp,
        COALESCE(i.unemployment_bp,0) unemployment_bp,
        COALESCE(e.production_modifier_bp,10000) production_modifier_bp,
        EXISTS(SELECT 1 FROM country_crises x WHERE x.country_id=c.id AND x.status='active') crisis
      FROM countries c
      LEFT JOIN citizenships cs ON cs.country_id=c.id
      LEFT JOIN country_economy_state e ON e.country_id=c.id
      LEFT JOIN LATERAL (SELECT inflation_bp,unemployment_bp FROM country_indicator_daily d WHERE d.country_id=c.id ORDER BY indicator_date DESC LIMIT 1) i ON TRUE
      GROUP BY c.id,i.inflation_bp,i.unemployment_bp,e.production_modifier_bp
      ORDER BY crisis DESC,c.treasury_toman DESC LIMIT 24
    """)
    alerts: list[dict[str, object]] = []
    queues = dict(ops.get("queues") or {})
    market = dict(ops.get("market") or {}) if ops.get("market") else {}
    if int(queues.get("outbox_failed") or 0):
        alerts.append({"severity":"critical","domain":"service","title":"خطا در صف انتشار","detail":f"{queues['outbox_failed']} پیام ناموفق نیازمند بررسی است.","action":"operations"})
    if int(queues.get("ads_failed") or 0):
        alerts.append({"severity":"warning","domain":"content","title":"تحویل تبلیغ ناموفق","detail":f"{queues['ads_failed']} تحویل تبلیغ شکست خورده است.","action":"requests"})
    failed_jobs=[j for j in ops.get("jobs",[]) if j.get("status") not in {"success","completed","healthy"}]
    for job in failed_jobs[:4]:
        alerts.append({"severity":"critical","domain":"service","title":f"Job ناموفق: {job['job_name']}","detail":job.get("error_message") or "اجرای اخیر موفق نبوده است.","action":"operations"})
    if market.get("source_error"):
        alerts.append({"severity":"warning","domain":"economy","title":"منبع نرخ بازار ناپایدار","detail":str(market["source_error"]),"action":"operations"})
    if bool(ops.get("market_frozen")):
        alerts.append({"severity":"info","domain":"economy","title":"بازار دلار متوقف است","detail":"فریز مدیریتی بازار فعال است.","action":"controls"})
    negatives=sum(int(integrity.get(k) or 0) for k in ("negative_players","negative_countries","negative_ledger_rows"))
    if negatives:
        alerts.append({"severity":"critical","domain":"economy","title":"ناسازگاری دفتر اقتصاد","detail":f"{negatives} رکورد با مانده منفی پیدا شد.","action":"ledger"})
    crisis_count=sum(1 for x in countries_rows if x["crisis"])
    if crisis_count:
        alerts.append({"severity":"warning","domain":"world","title":"بحران فعال در جهان","detail":f"{crisis_count} کشور درگیر بحران فعال است.","action":"countries"})
    if not alerts:
        alerts.append({"severity":"info","domain":"system","title":"وضعیت پایدار","detail":"در این لحظه رخداد قابل‌اقدام بحرانی ثبت نشده است.","action":"operations"})
    order={"critical":0,"warning":1,"info":2};alerts.sort(key=lambda x:order[str(x["severity"])])
    await persist_incidents(alerts)
    durable=[dict(x) for x in await incident_rows(30)]
    return {"overview":dict(overview) if overview else {},"operations":ops,"integrity":integrity,
      "alerts":durable,"countries":[dict(x) for x in countries_rows],
      "summary":{"critical":sum(a["severity"]=="critical" and a["status"]!='resolved' for a in durable),"warning":sum(a["severity"]=="warning" and a["status"]!='resolved' for a in durable),"crises":crisis_count}}

async def persist_incidents(items:list[dict[str,object]])->list[dict[str,object]]:
    """Upsert observations while preserving acknowledgement and ownership."""
    import hashlib
    seen=[]
    for item in items:
        fingerprint=hashlib.sha256(f"{item['domain']}|{item['title']}".encode()).hexdigest()[:32]
        row=await db.fetchrow("""INSERT INTO admin_incidents(fingerprint,severity,domain,title,detail,action_view,metadata)
          VALUES($1,$2,$3,$4,$5,$6,$7)
          ON CONFLICT(fingerprint) DO UPDATE SET severity=EXCLUDED.severity,detail=EXCLUDED.detail,
          action_view=EXCLUDED.action_view,last_seen_at=now(),occurrences=admin_incidents.occurrences+1,
          status=CASE WHEN admin_incidents.status='resolved' THEN 'open' ELSE admin_incidents.status END,
          resolved_at=CASE WHEN admin_incidents.status='resolved' THEN NULL ELSE admin_incidents.resolved_at END
          RETURNING *""",fingerprint,item['severity'],item['domain'],item['title'],item['detail'],item['action'],item)
        seen.append(dict(row))
    return seen

async def incident_rows(limit:int=100)->list[asyncpg.Record]:
    return await db.fetch("""SELECT * FROM admin_incidents ORDER BY
      CASE severity WHEN 'critical' THEN 0 WHEN 'warning' THEN 1 ELSE 2 END,
      CASE status WHEN 'open' THEN 0 WHEN 'investigating' THEN 1 WHEN 'acknowledged' THEN 2 ELSE 3 END,
      last_seen_at DESC LIMIT $1""",limit)

async def update_incident(incident_id:int,status:str,actor:str,note:str|None)->asyncpg.Record|None:
    return await db.fetchrow("""UPDATE admin_incidents SET status=$2,assigned_to=CASE WHEN $2 IN ('acknowledged','investigating') THEN $3 ELSE assigned_to END,
      acknowledged_at=CASE WHEN $2 IN ('acknowledged','investigating') THEN COALESCE(acknowledged_at,now()) ELSE acknowledged_at END,
      resolved_at=CASE WHEN $2='resolved' THEN now() ELSE NULL END,resolution_note=CASE WHEN $2='resolved' THEN $4 ELSE resolution_note END
      WHERE id=$1 RETURNING *""",incident_id,status,actor,note)

async def global_search(query:str,limit:int=8)->dict[str,list[dict[str,object]]]:
    q=query.strip();like=f"%{q}%"
    if not q:return {"players":[],"countries":[],"incidents":[],"audit":[]}
    players=await db.fetch("""SELECT id,first_name,username,telegram_id,level,is_banned FROM players
      WHERE first_name ILIKE $1 OR COALESCE(username,'') ILIKE $1 OR id::text=$2 OR telegram_id::text=$2 ORDER BY last_seen_at DESC LIMIT $3""",like,q,limit)
    countries=await db.fetch("SELECT id,name,status,treasury_toman FROM countries WHERE name ILIKE $1 OR id::text=$2 ORDER BY name LIMIT $3",like,q,limit)
    incidents=await db.fetch("SELECT id,title,severity,status,action_view FROM admin_incidents WHERE title ILIKE $1 OR detail ILIKE $1 ORDER BY last_seen_at DESC LIMIT $2",like,limit)
    audits=await db.fetch("SELECT id,admin_actor,action,created_at FROM admin_audit_log WHERE action ILIKE $1 OR admin_actor ILIKE $1 ORDER BY created_at DESC LIMIT $2",like,limit)
    return {"players":[dict(x) for x in players],"countries":[dict(x) for x in countries],"incidents":[dict(x) for x in incidents],"audit":[dict(x) for x in audits]}

async def anomaly_rows(limit:int=100)->list[dict[str,object]]:
    rows=await db.fetch("""WITH flow AS (
      SELECT player_id,count(*) tx_count,COALESCE(sum(abs(amount)),0) volume,
       count(*) FILTER(WHERE reason='level_up' OR reason LIKE '%xp%') xp_related
      FROM ledger WHERE created_at>=now()-interval '24 hours' AND player_id IS NOT NULL GROUP BY player_id
    ), wealth AS (SELECT id,first_name,username,wallet_toman+savings_toman wealth FROM players)
    SELECT w.id,w.first_name,w.username,w.wealth,COALESCE(f.tx_count,0) tx_count,COALESCE(f.volume,0) volume,
      CASE WHEN COALESCE(f.tx_count,0)>250 THEN 'transaction_burst'
           WHEN COALESCE(f.volume,0)>GREATEST(w.wealth*5,50000000) THEN 'volume_spike'
           WHEN w.wealth>1000000000 THEN 'wealth_outlier' END anomaly
    FROM wealth w LEFT JOIN flow f ON f.player_id=w.id
    WHERE COALESCE(f.tx_count,0)>250 OR COALESCE(f.volume,0)>GREATEST(w.wealth*5,50000000) OR w.wealth>1000000000
    ORDER BY volume DESC,wealth DESC LIMIT $1""",limit)
    return [dict(x) for x in rows]

async def register_undo(actor:str,action_type:str,target_key:str,inverse:dict[str,object],request_id:str)->int:
    return int(await db.fetchval("""INSERT INTO admin_reversible_actions(admin_actor,action_type,target_key,inverse_payload,source_request_id,expires_at)
      VALUES($1,$2,$3,$4,$5,now()+interval '10 minutes') RETURNING id""",actor,action_type,target_key,inverse,request_id))

async def undo_action(action_id:int,actor:str)->bool:
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT * FROM admin_reversible_actions WHERE id=$1 FOR UPDATE",action_id)
        if not row or row['undone_at'] or row['expires_at']<=await conn.fetchval('SELECT now()'):raise ValueError('undo_unavailable')
        data=dict(row['inverse_payload']);kind=str(row['action_type'])
        if kind=='feature_toggle':
            await set_flag(conn,str(data['key']),bool(data['enabled']),actor)
        elif kind=='market_price':
            await conn.execute("UPDATE market_prices SET current_price_toman=$2,updated_by=$3,updated_at=now() WHERE asset_code=$1",data['asset'],int(data['price']),actor)
            await conn.execute("INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at) VALUES($1,$2,date_trunc('minute',now())) ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman",data['asset'],int(data['price']))
        elif kind=='country_asset':
            country_id=int(data['country_id']);asset=str(data['asset']);delta=int(data['delta'])
            if asset=='IRT':
                balance=await conn.fetchval("UPDATE countries SET treasury_toman=treasury_toman+$2 WHERE id=$1 AND treasury_toman+$2>=0 RETURNING treasury_toman",country_id,delta)
            else:
                balance=await conn.fetchval("UPDATE country_resources SET quantity=quantity+$3 WHERE country_id=$1 AND asset_code=$2 AND quantity+$3>=0 RETURNING quantity",country_id,asset,delta)
            if balance is None:raise ValueError('undo_insufficient_balance')
            await conn.execute("INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,asset_code,account,amount,balance_after,metadata) VALUES(NULL,$1,$2,'admin_undo',$3,$3,'treasury',$4,$5,$6)",country_id,f"admin-undo:{action_id}",asset,delta,int(balance),{'admin_actor':actor,'source_action_id':action_id})
        else:raise ValueError('undo_unsupported')
        await conn.execute("UPDATE admin_reversible_actions SET undone_at=now(),undone_by=$2 WHERE id=$1",action_id,actor)
        await audit(conn,actor,'undo',f"undo:{action_id}",{'source_action_id':action_id})
        return True


async def available_undos(limit:int=50)->list[asyncpg.Record]:
    return await db.fetch("""SELECT id,admin_actor,action_type,target_key,expires_at,created_at
      FROM admin_reversible_actions WHERE undone_at IS NULL AND expires_at>now() ORDER BY created_at DESC LIMIT $1""",limit)
