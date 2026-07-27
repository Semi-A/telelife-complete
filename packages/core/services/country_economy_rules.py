"""Pure Release-B formulas; importable by tests and the offline simulator."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from packages.core.config import get_config

@dataclass(frozen=True,slots=True)
class DailyPlan:
 food_needed:int; energy_needed:int; food_used:int; energy_used:int
 food_shortage_bp:int; energy_shortage_bp:int; budget_spend:int
 satisfaction:int; production_modifier_bp:int; welfare:int; defense:int

def shortage_bp(needed:int,available:int)->int:
 if needed<=0:return 0
 return max(0,min(10000,10000-(min(needed,max(0,available))*10000//needed)))

def calculate_daily(*,citizens:int,food:int,energy:int,treasury:int,satisfaction:int,budget:Mapping[str,int],completed_projects:int=0)->DailyPlan:
 cfg=get_config();count=min(max(0,citizens),cfg.int_("country_economy_b.consumption.maximum_citizens_counted"))
 food_needed=cfg.int_("country_economy_b.consumption.base_food_daily")+count*cfg.int_("country_economy_b.consumption.food_per_citizen_daily")
 energy_needed=cfg.int_("country_economy_b.consumption.base_energy_daily")+count*cfg.int_("country_economy_b.consumption.energy_per_citizen_daily")
 food_used=min(max(0,food),food_needed);energy_used=min(max(0,energy),energy_needed)
 fs=shortage_bp(food_needed,food_used);es=shortage_bp(energy_needed,energy_used)
 spend=max(0,min(cfg.int_("country_economy_b.budget.daily_spend_cap_toman"),treasury*cfg.int_("country_economy_b.budget.treasury_spend_bp")//10000))
 if treasury and spend<cfg.int_("country_economy_b.budget.minimum_operating_spend_toman"):spend=min(treasury,cfg.int_("country_economy_b.budget.minimum_operating_spend_toman"))
 welfare_share=int(budget["welfare"]);emergency=int(budget["emergency"])
 mitigation=min(cfg.int_("country_economy_b.crisis.emergency_mitigation_bp_max"),emergency*3//2)
 effective_shortage=max(0,fs-mitigation)+max(0,es-mitigation)
 delta=(cfg.int_("country_economy_b.satisfaction.full_food_bonus") if fs==0 else 0)+(cfg.int_("country_economy_b.satisfaction.full_energy_bonus") if es==0 else 0)
 delta+=min(cfg.int_("country_economy_b.satisfaction.welfare_bonus_max"),welfare_share//1000)
 delta+=min(cfg.int_("country_economy_b.satisfaction.completed_project_bonus_max"),completed_projects)
 delta-=min(cfg.int_("country_economy_b.satisfaction.crisis_penalty_max"),effective_shortage//1500)
 max_change=cfg.int_("country_economy_b.satisfaction.daily_max_change");delta=max(-max_change,min(max_change,delta))
 sat=max(0,min(100,satisfaction+delta))
 modifier=10000-(fs+es)//5-min(cfg.int_("country_economy_b.production.low_satisfaction_penalty_bp_max"),max(0,50-sat)*30)
 modifier+=min(cfg.int_("country_economy_b.production.production_budget_bonus_bp_max"),int(budget["production"])//4)
 modifier+=min(cfg.int_("country_economy_b.production.technology_budget_bonus_bp_max"),int(budget["technology"])//4)
 modifier=max(cfg.int_("country_economy_b.production.minimum_modifier_bp"),min(cfg.int_("country_economy_b.production.maximum_modifier_bp"),modifier))
 welfare=max(0,min(100,40+welfare_share//100-fs//500))
 defense=max(0,min(100,10+int(budget["defense"])//100+int(budget["intelligence"])//200))
 return DailyPlan(food_needed,energy_needed,food_used,energy_used,fs,es,spend,sat,modifier,welfare,defense)