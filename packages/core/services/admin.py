"""Audited privileged operations; mutation and audit commit atomically."""
from __future__ import annotations

from packages.core import db
from packages.core.repositories import admin_repo, outbox_repo
from packages.core.services import xp
from packages.core.services.xp import XPResult

async def ban(actor: str, player_id: int, banned: bool, reason: str | None,
              request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "ban" if banned else "unban",
                                      request_id, {"reason": reason}, player_id):
            return False
        await admin_repo.set_ban(conn, player_id, banned, reason)
        return True

async def feature(actor: str, key: str, enabled: bool, request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "feature_toggle", request_id,
                                      {"key": key, "enabled": enabled}):
            return False
        await admin_repo.set_flag(conn, key, enabled, actor)
        return True

async def grant_xp(actor: str, player_id: int, amount: int,
                   request_id: str) -> XPResult | None:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "grant_xp", request_id,
                                      {"amount": amount}, player_id):
            return None
        return await xp.grant(player_id, "admin_grant",
                              idempotency_key=f"admin-xp:{request_id}", amount=amount, conn=conn)

async def set_market_price(actor: str, asset: str, price: int, request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "market_price", request_id,
                                      {"asset": asset, "price": price}):
            return False
        changed = await conn.fetchval("""
            UPDATE market_prices SET current_price_toman=$2,updated_by=$3,updated_at=now()
            WHERE asset_code=$1 RETURNING asset_code
        """, asset, price, actor)
        if changed is None:
            raise ValueError("asset_not_found")
        await conn.execute("""
            INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
            VALUES($1,$2,date_trunc('minute',now()))
            ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman
        """, asset, price)
        return True

async def adjust_country_asset(actor: str, country_id: int, asset: str, delta: int,
                               request_id: str) -> int:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "country_asset_adjust", request_id,
                                      {"asset": asset, "delta": delta}, country_id=country_id):
            return 0
        exists = await conn.fetchval("SELECT 1 FROM countries WHERE id=$1 FOR UPDATE", country_id)
        if not exists:
            raise ValueError("country_not_found")
        if asset == "IRT":
            value = await conn.fetchval("""
                UPDATE countries SET treasury_toman=treasury_toman+$2
                WHERE id=$1 AND treasury_toman+$2>=0 RETURNING treasury_toman
            """, country_id, delta)
        else:
            value = await conn.fetchval("""
                INSERT INTO country_resources(country_id,asset_code,quantity) VALUES($1,$2,$3)
                ON CONFLICT(country_id,asset_code) DO UPDATE
                SET quantity=country_resources.quantity+$3,updated_at=now()
                WHERE country_resources.quantity+$3>=0 RETURNING quantity
            """, country_id, asset, delta)
        if value is None:
            raise ValueError("insufficient_balance")
        await conn.execute("""
            INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,
                               asset_code,account,amount,balance_after,metadata)
            VALUES(NULL,$1,$2,'admin_adjustment',$3,$3,'treasury',$4,$5,$6)
        """, country_id, f"admin-country:{request_id}", asset, delta, value,
             {"admin_actor": actor})
        return int(value)

async def set_president(actor: str, country_id: int, player_id: int | None,
                        request_id: str) -> bool:
    async with db.transaction() as conn:
        if player_id is not None:
            citizen = await conn.fetchval(
                "SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2",
                country_id, player_id,
            )
            if not citizen:
                raise ValueError("president_must_be_citizen")
        if not await admin_repo.audit(conn, actor, "set_president", request_id,
                                      {"player_id": player_id}, player_id, country_id):
            return False
        result = await conn.execute(
            "UPDATE countries SET president_player_id=$2 WHERE id=$1", country_id, player_id
        )
        if result == "UPDATE 0":
            raise ValueError("country_not_found")
        return True

async def enqueue_news(actor: str, text: str, destination: int,
                       request_id: str) -> bool:
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "enqueue_news", request_id,
                                      {"destination": destination, "text": text[:200]}):
            return False
        return await outbox_repo.enqueue(conn, f"admin-news:{request_id}",
                                         "admin_announcement", {"text": text}, destination)

async def create_ad(actor: str, title: str, text: str, destination: int,
                    scheduled_at, repeat_minutes: int | None, request_id: str) -> int:
    from packages.core.services.content_filter import require_clean
    require_clean(title, "name"); require_clean(text, "description")
    status = "scheduled" if scheduled_at else "draft"
    async with db.transaction() as conn:
        if not await admin_repo.audit(conn, actor, "create_ad", request_id,
                                      {"title": title, "destination": destination}): return 0
        return int(await conn.fetchval("""INSERT INTO ad_campaigns
          (title,body,destination_chat_id,status,scheduled_at,repeat_minutes,created_by)
          VALUES($1,$2,$3,$4,$5,$6,$7) RETURNING id""",
          title,text,destination,status,scheduled_at,repeat_minutes,actor))

async def queue_ad(actor: str, ad_id: int, request_id: str) -> bool:
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT * FROM ad_campaigns WHERE id=$1 FOR UPDATE",ad_id)
        if row is None: raise ValueError("ad_not_found")
        if not await admin_repo.audit(conn,actor,"queue_ad",request_id,{"ad_id":ad_id}): return False
        queued=await outbox_repo.enqueue(conn,f"ad:{ad_id}:{request_id}","advertisement",
                                         {"text":row["body"],"ad_id":ad_id},row["destination_chat_id"])
        if queued: await conn.execute("UPDATE ad_campaigns SET status='queued',last_queued_at=now(),updated_at=now() WHERE id=$1",ad_id)
        return queued
