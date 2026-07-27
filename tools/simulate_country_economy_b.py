"""Offline 30-day Release-B balance simulation; never imported by production."""
from __future__ import annotations
from dataclasses import dataclass
from statistics import mean
from packages.core.services.country_economy_rules import calculate_daily

PRESETS={
 "balanced":{"welfare":2000,"production":2500,"technology":1500,"defense":1000,"intelligence":500,"diplomacy":500,"emergency":2000},
 "growth":{"welfare":1200,"production":3500,"technology":2500,"defense":700,"intelligence":300,"diplomacy":300,"emergency":1500},
}
@dataclass
class Nation:
 name:str;citizens:int;active_ratio:float;treasury:int;food:int;energy:int;satisfaction:int=70

def run(n:Nation,preset:str="balanced",days:int=30):
 mods=[];shortages=0;initial=n.treasury
 for day in range(days):
  active=max(1,int(n.citizens*n.active_ratio))
  n.food+=active*3;n.energy+=active*2;n.treasury+=active*55_000
  plan=calculate_daily(citizens=n.citizens,food=n.food,energy=n.energy,treasury=n.treasury,satisfaction=n.satisfaction,budget=PRESETS[preset],completed_projects=day//12)
  n.food-=plan.food_used;n.energy-=plan.energy_used;n.treasury-=plan.budget_spend;n.satisfaction=plan.satisfaction;mods.append(plan.production_modifier_bp)
  shortages+=int(plan.food_shortage_bp>0 or plan.energy_shortage_bp>0)
 return {"name":n.name,"citizens":n.citizens,"treasury_growth":n.treasury-initial,"satisfaction":n.satisfaction,"shortage_days":shortages,"avg_modifier_bp":round(mean(mods)),"project_days_estimate":round(2_500_000/max(1,(n.treasury-initial)/days),1)}

def main():
 rows=[run(Nation("کشور کوچک",8,.5,3_000_000,100,80)),run(Nation("کشور متوسط",40,.35,8_000_000,300,250)),run(Nation("کشور بزرگ",180,.25,25_000_000,900,700),"growth")]
 print("name,citizens,treasury_growth,satisfaction,shortage_days,avg_modifier_bp,project_days_estimate")
 for r in rows:print(",".join(str(r[k]) for k in r))
if __name__=="__main__":main()