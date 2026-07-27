"""Phase 4 USD market: bounded price impact, spread, fees and daily limits."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

@dataclass(frozen=True,slots=True)
class MarketView:
    price:int; buy_price:int; sell_price:int; health:int; volume_cents:int; frozen:bool

@dataclass(frozen=True,slots=True)
class TradeResult:
    applied:bool; side:str; cents:int; toman:int; fee:int; price:int; price_after:int

def _quote(price:int,side:str)->int:
    spread=get_config().int_("market.usd.spread_basis_points")
    return max(1,(price*(10000+(spread if side=="buy" else -spread)))//10000)

async def view()->MarketView:
    row=await db.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE")
    if row is None: raise ValueError("market_not_initialized")
    frozen=bool(await db.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"))
    p=int(row["reference_price_toman"])
    return MarketView(p,_quote(p,"buy"),_quote(p,"sell"),int(row["health"]),int(row["volume_cents"]),frozen)

async def trade(player_id:int,side:str,cents:int,key:str)->TradeResult:
    cfg=get_config()
    if side not in {"buy","sell"}: raise ValueError("invalid_side")
    if not cfg.int_("market.usd.minimum_trade_cents")<=cents<=cfg.int_("market.usd.maximum_trade_cents"): raise ValueError("amount_out_of_bounds")
    today=clock.game_today()
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        if int(player["level"])<cfg.int_("market.usd.min_level"): raise ValueError("market_locked")
        if await ledger_repo.economy_frozen(conn) or await conn.fetchval("SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='usd_market_frozen'),FALSE)"): raise ValueError("market_frozen")
        state=await conn.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if await conn.fetchval("SELECT 1 FROM usd_trades WHERE idempotency_key=$1",key):
            return TradeResult(False,side,cents,0,0,int(state["reference_price_toman"]),int(state["reference_price_toman"]))
        await conn.execute("INSERT INTO usd_daily_limits(player_id,trade_date) VALUES($1,$2) ON CONFLICT DO NOTHING",player_id,today)
        limits=await conn.fetchrow("SELECT * FROM usd_daily_limits WHERE player_id=$1 AND trade_date=$2 FOR UPDATE",player_id,today)
        used=int(limits["bought_cents"] if side=="buy" else limits["sold_cents"])
        maximum=cfg.int_(f"market.usd.daily_{side}_limit_cents")
        if used+cents>maximum: raise ValueError("daily_limit")
        reference=int(state["reference_price_toman"]); price=_quote(reference,side)
        gross=(price*cents+99)//100
        fee=(gross*cfg.int_("market.usd.fee_basis_points")+9999)//10000
        wallet_delta=-(gross+fee) if side=="buy" else gross-fee
        usd_delta=cents if side=="buy" else -cents
        changed=await conn.fetchrow("""UPDATE players SET wallet_toman=wallet_toman+$2::bigint,usd_cents=usd_cents+$3::bigint
          WHERE id=$1::bigint AND wallet_toman+$2::bigint>=0 AND usd_cents+$3::bigint>=0 RETURNING wallet_toman,usd_cents""",player_id,wallet_delta,usd_delta)
        if changed is None: raise ValueError("insufficient_balance")
        steps=max(1,cents//cfg.int_("market.usd.impact_cents_per_step")); move=min(cfg.int_("market.usd.max_trade_move_basis_points"),steps*cfg.int_("market.usd.impact_basis_points_per_step"))
        candidate=(reference*(10000+(move if side=="buy" else -move)))//10000
        open_price=int(state["open_price_toman"]); band=cfg.int_("market.usd.daily_band_basis_points")
        low=open_price*(10000-band)//10000; high=open_price*(10000+band)//10000; after=max(low,min(high,max(1,candidate)))
        net=int(state["net_flow_cents"])+(cents if side=="buy" else -cents); volume=int(state["volume_cents"])+cents
        health=max(0,100-min(100,abs(net)*100//max(volume,1)))
        await conn.execute("UPDATE usd_market_state SET reference_price_toman=$1,net_flow_cents=$2,volume_cents=$3,health=$4,updated_at=now() WHERE singleton=TRUE",after,net,volume,health)
        col="bought_cents" if side=="buy" else "sold_cents"
        await conn.execute(f"UPDATE usd_daily_limits SET {col}={col}+$3 WHERE player_id=$1 AND trade_date=$2",player_id,today,cents)
        await conn.execute("""INSERT INTO usd_trades(player_id,idempotency_key,side,usd_cents,gross_toman,fee_toman,price_toman,price_after_toman)
          VALUES($1,$2,$3,$4,$5,$6,$7,$8)""",player_id,key,side,cents,gross,fee,price,after)
        ok1=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:irt",reason=f"usd_{side}",asset="IRT",account="wallet",amount=wallet_delta,balance=int(changed["wallet_toman"]),metadata={"fee":fee,"price":price})
        ok2=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:usd",reason=f"usd_{side}",asset="USD",account="usd",amount=usd_delta,balance=int(changed["usd_cents"]),metadata={"price":price})
        if not(ok1 and ok2): raise RuntimeError("market_ledger_conflict")
        await conn.execute("""UPDATE market_prices SET current_price_toman=$1,updated_by='market-engine',updated_at=now() WHERE asset_code='USD'""",after)
        await conn.execute("""INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at) VALUES('USD',$1,date_trunc('minute',now())) ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman""",after)
        return TradeResult(True,side,cents,gross,fee,price,after)

async def stabilize()->int:
    cfg=get_config()
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT * FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if row is None:return 0
        current=int(row["reference_price_toman"]); target=int(row["open_price_toman"]); bp=cfg.int_("market.usd.stabilization_basis_points_per_minute")
        step=max(1,current*bp//10000); after=current-step if current>target else current+step if current<target else current
        if (current-target)*(after-target)<0:after=target
        await conn.execute("UPDATE usd_market_state SET reference_price_toman=$1,updated_at=now() WHERE singleton=TRUE",after)
        await conn.execute("UPDATE market_prices SET current_price_toman=$1,updated_by='stabilizer',updated_at=now() WHERE asset_code='USD'",after)
        return after

async def daily_rollover()->None:
    async with db.transaction() as conn:
        row=await conn.fetchrow("SELECT reference_price_toman,market_date FROM usd_market_state WHERE singleton=TRUE FOR UPDATE")
        if row and row["market_date"]!=clock.game_today():
            await conn.execute("UPDATE usd_market_state SET open_price_toman=reference_price_toman,net_flow_cents=0,volume_cents=0,health=100,market_date=$1,updated_at=now() WHERE singleton=TRUE",clock.game_today())