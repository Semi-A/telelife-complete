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