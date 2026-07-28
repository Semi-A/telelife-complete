"""Pure Release-C trade and diplomacy rules."""
from __future__ import annotations
from packages.core.config import get_config

RELATIONS={"neutral","friend","trade_partner","defensive_ally","rival","hostile"}

def pair(a:int,b:int)->tuple[int,int]:
 if a==b:raise ValueError("same_country")
 return (a,b) if a<b else (b,a)

def tariff_bp(status:str)->int:
 if status not in RELATIONS:status="neutral"
 return get_config().int_(f"country_trade.tariffs.{status}_bp")

def net_after_tariff(amount:int,bp:int)->tuple[int,int]:
 if amount<=0:raise ValueError("amount_must_be_positive")
 fee=min(amount-1,max(0,amount*max(0,bp)//10000)) if amount>1 else 0
 return amount-fee,fee

def open_limit(reputation:int)->int:
 cfg=get_config();bonus=max(0,min(cfg.int_("country_trade.contracts.max_open_reputation_bonus"),reputation//25))
 return cfg.int_("country_trade.contracts.max_open_base")+bonus
