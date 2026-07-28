"""Player resource inventory, fixed-price sales and social transfers."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo

ASSETS=frozenset({"food","minerals","technology","energy"})

@dataclass(frozen=True,slots=True)
class SaleReceipt:
 asset:str;amount:int;gross:int;fee:int;net:int;resource_balance:int;wallet:int

@dataclass(frozen=True,slots=True)
class TransferReceipt:
 asset:str;amount:int;balance:int;reputation:int;country_id:int;recipient_id:int|None

def spec(asset:str)->dict[str,object]:
 if asset not in ASSETS:raise ValueError("invalid_asset")
 return get_config().section(f"resource_economy.assets.{asset}")

def allowed_amount(amount:int,*,social:bool=False)->None:
 path="resource_economy.social.allowed_amounts" if social else "resource_economy.market.allowed_amounts"
 if amount not in {int(x) for x in get_config().get(path)}:raise ValueError("invalid_amount")

async def inventory(player_id:int)->list[dict[str,object]]:
 rows=await db.fetch("SELECT asset_code,quantity FROM player_resources WHERE player_id=$1 AND quantity>0 ORDER BY asset_code",player_id)
 values={str(r["asset_code"]):int(r["quantity"]) for r in rows}
 return [{"asset":a,"title":str(spec(a)["title"]),"quantity":values.get(a,0),"sell_price":int(spec(a)["sell_toman_per_unit"])} for a in sorted(ASSETS)]

async def sell(player_id:int,asset:str,amount:int,key:str)->SaleReceipt:
 allowed_amount(amount);cfg=get_config();item=spec(asset)
 async with db.transaction() as conn:
  if await ledger_repo.economy_frozen(conn):raise ValueError("economy_frozen")
  old=await conn.fetchrow("SELECT * FROM player_resource_sales WHERE idempotency_key=$1",key)
  if old:
   wallet=int(await conn.fetchval("SELECT wallet_toman FROM players WHERE id=$1",player_id) or 0)
   balance=int(await conn.fetchval("SELECT quantity FROM player_resources WHERE player_id=$1 AND asset_code=$2",player_id,asset) or 0)
   return SaleReceipt(asset,int(old['amount']),int(old['gross_toman']),int(old['fee_toman']),int(old['net_toman']),balance,wallet)
  used=int(await conn.fetchval("SELECT COALESCE(sum(amount),0) FROM player_resource_sales WHERE player_id=$1 AND created_at>=date_trunc('day',now())",player_id) or 0)
  if used+amount>cfg.int_("resource_economy.market.daily_sell_units"):raise ValueError("resource_sell_daily_limit")
  unit=int(item["sell_toman_per_unit"]);gross=amount*unit;fee=gross*cfg.int_("resource_economy.market.fee_percent")//100;net=gross-fee
  resource_balance=await ledger_repo.change_player(conn,player_id,asset,-amount)
  wallet=await ledger_repo.change_player(conn,player_id,"IRT",net)
  await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:asset",reason="resource_sale",asset=asset,account=ledger_repo.player_account(asset),amount=-amount,balance=resource_balance,metadata={"unit_price":unit,"gross":gross,"fee":fee})
  await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:cash",reason="resource_sale_income",asset="IRT",account="wallet",amount=net,balance=wallet,metadata={"asset":asset,"units":amount,"gross":gross,"fee":fee})
  await conn.execute("INSERT INTO player_resource_sales(player_id,asset_code,amount,unit_price_toman,gross_toman,fee_toman,net_toman,idempotency_key) VALUES($1,$2,$3,$4,$5,$6,$7,$8)",player_id,asset,amount,unit,gross,fee,net,key)
  return SaleReceipt(asset,amount,gross,fee,net,resource_balance,wallet)

async def _country(conn,player_id:int)->int:
 value=await conn.fetchval("SELECT country_id FROM citizenships WHERE player_id=$1 AND is_active",player_id)
 if not value:raise PermissionError("citizen_required")
 return int(value)

async def transfer(actor:int,asset:str,amount:int,key:str,*,recipient:int|None=None)->TransferReceipt:
 allowed_amount(amount,social=True);spec(asset);cfg=get_config();kind="gift" if recipient else "country_donation"
 async with db.transaction() as conn:
  if await ledger_repo.economy_frozen(conn):raise ValueError("economy_frozen")
  old=await conn.fetchrow("SELECT * FROM citizen_resource_transfers WHERE idempotency_key=$1",key)
  if old:
   balance=int(await conn.fetchval("SELECT quantity FROM player_resources WHERE player_id=$1 AND asset_code=$2",actor,asset) or 0)
   return TransferReceipt(asset,int(old['amount']),balance,int(old['reputation_awarded']),int(old['country_id']),old['recipient_id'])
  country=await _country(conn,actor)
  if recipient:
   if recipient==actor:raise ValueError("self_interaction")
   peer=await _country(conn,recipient)
   if peer!=country:raise PermissionError("same_country_required")
   used=int(await conn.fetchval("SELECT COALESCE(sum(amount),0) FROM citizen_resource_transfers WHERE actor_id=$1 AND transfer_type='gift' AND created_at>=date_trunc('day',now())",actor) or 0)
   if used+amount>cfg.int_("resource_economy.social.daily_gift_units"):raise ValueError("resource_gift_daily_limit")
  else:
   used=int(await conn.fetchval("SELECT COALESCE(sum(amount),0) FROM citizen_resource_transfers WHERE actor_id=$1 AND transfer_type='country_donation' AND created_at>=date_trunc('day',now())",actor) or 0)
   if used+amount>cfg.int_("resource_economy.social.daily_country_donation_units"):raise ValueError("resource_donation_daily_limit")
  balance=await ledger_repo.change_player(conn,actor,asset,-amount)
  await ledger_repo.insert(conn,player_id=actor,country_id=None,key=f"{key}:debit",reason=f"resource_{kind}",asset=asset,account=ledger_repo.player_account(asset),amount=-amount,balance=balance,metadata={"country_id":country,"recipient_id":recipient})
  if recipient:
   target_balance=await ledger_repo.change_player(conn,recipient,asset,amount)
   await ledger_repo.insert(conn,player_id=recipient,country_id=None,key=f"{key}:credit",reason="resource_gift_received",asset=asset,account=ledger_repo.player_account(asset),amount=amount,balance=target_balance,metadata={"sender_id":actor,"country_id":country})
  else:
   target_balance=await ledger_repo.change_country(conn,country,asset,amount)
   await ledger_repo.insert(conn,player_id=None,country_id=country,key=f"{key}:credit",reason="citizen_resource_donation",asset=asset,account=ledger_repo.country_account(asset),amount=amount,balance=target_balance,metadata={"actor_id":actor})
  count=int(await conn.fetchval("SELECT count(*) FROM citizen_resource_transfers WHERE actor_id=$1 AND created_at>=date_trunc('day',now())",actor) or 0)
  rep=1 if count<cfg.int_("resource_economy.social.reputation_first_transfers") else 0
  if rep:await conn.execute("UPDATE players SET reputation=LEAST(1000,reputation+$2) WHERE id=$1",actor,rep)
  await conn.execute("INSERT INTO citizen_resource_transfers(country_id,actor_id,recipient_id,transfer_type,asset_code,amount,reputation_awarded,idempotency_key) VALUES($1,$2,$3,$4,$5,$6,$7,$8)",country,actor,recipient,kind,asset,amount,rep,key)
  return TransferReceipt(asset,amount,balance,rep,country,recipient)
