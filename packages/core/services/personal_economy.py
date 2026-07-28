"""Phase 3 personal economy: atomic savings, housing, rent and living costs."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import timedelta
from typing import Any
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo
from packages.core.utils import clock

@dataclass(frozen=True,slots=True)
class EconomyView:
    wallet:int; savings:int; housing:dict[str,Any]|None; living_due:int; living_days:int

async def view(player_id:int)->EconomyView:
    player=await db.fetchrow("SELECT wallet_toman,savings_toman FROM players WHERE id=$1",player_id)
    if player is None: raise ValueError("player_not_found")
    house=await db.fetchrow("SELECT * FROM player_housing WHERE player_id=$1",player_id)
    today=clock.game_today()
    if house and house["tenure"] == "rent" and (house["rent_paid_until"] is None or house["rent_paid_until"] < today):
        house=None
    state=await db.fetchrow("SELECT last_living_charge_date FROM player_life_economy WHERE player_id=$1",player_id)
    last=state["last_living_charge_date"] if state else None
    days=1 if last is None else max(0,min((today-last).days,get_config().int_("phase3.living.max_catch_up_days")))
    daily=get_config().int_("phase3.living.base_daily_cost_toman")
    if house: daily+=get_config().int_(f"phase3.housing.options.{house['housing_code']}.daily_living_toman")
    assets=await db.fetch("SELECT asset_code FROM player_assets WHERE player_id=$1",player_id)
    specs=get_config().section("life_progression.assets")
    daily+=sum(int(specs[str(a["asset_code"])].get("maintenance_daily_toman",0)) for a in assets if str(a["asset_code"]) in specs)
    return EconomyView(int(player["wallet_toman"]),int(player["savings_toman"]),dict(house) if house else None,daily*days,days)

async def savings_transfer(player_id:int,amount:int,direction:str,key:str)->tuple[int,int]:
    cfg=get_config(); lo=cfg.int_("phase3.savings.minimum_transfer_toman"); hi=cfg.int_("phase3.savings.maximum_transfer_toman")
    if direction not in {"deposit","withdraw"}: raise ValueError("invalid_direction")
    if not lo<=amount<=hi: raise ValueError("amount_out_of_bounds")
    async with db.transaction() as conn:
        row=await ledger_repo.lock_player(conn,player_id)
        if row is None: raise ValueError("player_not_found")
        if await ledger_repo.idempotency_exists(conn,f"{key}:wallet"): return int(row["wallet_toman"]),int(row["savings_toman"])
        wallet_delta=-amount if direction=="deposit" else amount
        savings_delta=amount if direction=="deposit" else -amount
        changed=await conn.fetchrow("""UPDATE players SET wallet_toman=wallet_toman+$2,savings_toman=savings_toman+$3
          WHERE id=$1 AND wallet_toman+$2>=0 AND savings_toman+$3>=0 RETURNING wallet_toman,savings_toman""",player_id,wallet_delta,savings_delta)
        if changed is None: raise ValueError("insufficient_balance")
        a=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:wallet",reason=f"savings_{direction}",asset="IRT",account="wallet",amount=wallet_delta,balance=int(changed["wallet_toman"]))
        b=await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:savings",reason=f"savings_{direction}",asset="IRT",account="savings",amount=savings_delta,balance=int(changed["savings_toman"]))
        if not(a and b): raise RuntimeError("savings_ledger_conflict")
        return int(changed["wallet_toman"]),int(changed["savings_toman"])

async def acquire_housing(player_id:int,code:str,tenure:str,key:str)->dict[str,Any]:
    cfg=get_config(); options=cfg.section("phase3.housing.options")
    if code not in options or tenure not in {"rent","owned"}: raise ValueError("invalid_housing")
    spec=options[code]; cost=int(spec["weekly_rent_toman"] if tenure=="rent" else spec["purchase_toman"])
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        if int(player["level"])<int(spec["min_level"]): raise ValueError("housing_locked")
        if await ledger_repo.idempotency_exists(conn,key):
            row=await conn.fetchrow("SELECT * FROM player_housing WHERE player_id=$1",player_id); return dict(row)
        previous=await conn.fetchrow("SELECT housing_code FROM player_housing WHERE player_id=$1 FOR UPDATE",player_id)
        previous_bonus=int(options[str(previous["housing_code"])].get("happiness_bonus",0)) if previous and str(previous["housing_code"]) in options else 0
        new_bonus=int(spec.get("happiness_bonus",0))
        balance=await ledger_repo.change_player(conn,player_id,"IRT",-cost)
        until=clock.game_today()+timedelta(days=cfg.int_("phase3.housing.rent_period_days")) if tenure=="rent" else None
        row=await conn.fetchrow("""INSERT INTO player_housing(player_id,housing_code,tenure,rent_paid_until,purchased_at)
          VALUES($1,$2,$3,$4,CASE WHEN $3='owned' THEN now() END)
          ON CONFLICT(player_id) DO UPDATE SET housing_code=$2,tenure=$3,rent_paid_until=$4,
          purchased_at=CASE WHEN $3='owned' THEN now() END,updated_at=now() RETURNING *""",player_id,code,tenure,until)
        if not await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason=f"housing_{tenure}",asset="IRT",account="wallet",amount=-cost,balance=balance,metadata={"housing":code}): raise RuntimeError("housing_ledger_conflict")
        await conn.execute("UPDATE players SET happiness=GREATEST(0,LEAST(100,happiness+$2)) WHERE id=$1",player_id,new_bonus-previous_bonus)
        return dict(row)

async def pay_living(player_id:int,key:str)->tuple[int,int]:
    cfg=get_config(); today=clock.game_today()
    async with db.transaction() as conn:
        player=await ledger_repo.lock_player(conn,player_id)
        if player is None: raise ValueError("player_not_found")
        await conn.execute("INSERT INTO player_life_economy(player_id) VALUES($1) ON CONFLICT DO NOTHING",player_id)
        state=await conn.fetchrow("SELECT * FROM player_life_economy WHERE player_id=$1 FOR UPDATE",player_id)
        last=state["last_living_charge_date"]; days=1 if last is None else max(0,min((today-last).days,cfg.int_("phase3.living.max_catch_up_days")))
        if days==0:return 0,int(player["wallet_toman"])
        house=await conn.fetchrow("SELECT housing_code,tenure,rent_paid_until FROM player_housing WHERE player_id=$1 FOR UPDATE",player_id)
        # Expired rentals stop adding housing costs and are removed atomically.
        if house and house["tenure"] == "rent" and (house["rent_paid_until"] is None or house["rent_paid_until"] < today):
            await conn.execute("DELETE FROM player_housing WHERE player_id=$1", player_id)
            house = None
        daily=cfg.int_("phase3.living.base_daily_cost_toman")+(cfg.int_(f"phase3.housing.options.{house['housing_code']}.daily_living_toman") if house else 0)
        assets=await conn.fetch("SELECT asset_code FROM player_assets WHERE player_id=$1",player_id)
        specs=cfg.section("life_progression.assets")
        daily+=sum(int(specs[str(a["asset_code"])].get("maintenance_daily_toman",0)) for a in assets if str(a["asset_code"]) in specs)
        amount=daily*days
        if int(player["wallet_toman"])<amount: raise ValueError("insufficient_balance")
        balance=await ledger_repo.change_player(conn,player_id,"IRT",-amount)
        await conn.execute("UPDATE player_life_economy SET last_living_charge_date=$2,total_living_paid=total_living_paid+$3,missed_living_days=0,updated_at=now() WHERE player_id=$1",player_id,today,amount)
        if not await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=key,reason="living_cost",asset="IRT",account="wallet",amount=-amount,balance=balance,metadata={"days":days}): raise RuntimeError("living_ledger_conflict")
        return amount,balance