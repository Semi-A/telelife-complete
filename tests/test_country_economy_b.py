from datetime import date
from pathlib import Path
from packages.core.config import get_config
from packages.core.services.country_economy_rules import calculate_daily,shortage_bp

B={"welfare":2000,"production":2500,"technology":1500,"defense":1000,"intelligence":500,"diplomacy":500,"emergency":2000}

def test_shortage_formula_is_bounded():
 assert shortage_bp(100,0)==10000
 assert shortage_bp(100,50)==5000
 assert shortage_bp(100,150)==0
 assert shortage_bp(0,0)==0

def test_full_supply_preserves_players_and_improves_satisfaction():
 p=calculate_daily(citizens=20,food=1000,energy=1000,treasury=10_000_000,satisfaction=60,budget=B,completed_projects=1)
 assert p.food_shortage_bp==0 and p.energy_shortage_bp==0
 assert p.satisfaction>60
 assert p.production_modifier_bp>=10000

def test_shortage_degrades_but_never_destroys_production():
 p=calculate_daily(citizens=100,food=0,energy=0,treasury=0,satisfaction=30,budget=B)
 assert p.satisfaction>=0
 assert get_config().int_("country_economy_b.production.minimum_modifier_bp")<=p.production_modifier_bp
 assert p.production_modifier_bp<=10000

def test_budget_is_bounded_by_treasury():
 p=calculate_daily(citizens=5,food=100,energy=100,treasury=1000,satisfaction=70,budget=B)
 assert 0<=p.budget_spend<=1000

def test_release_b_migration_is_additive_and_numbered_after_release_a():
 text=Path("migrations/0017_country_economy_release_b.sql").read_text(encoding="utf-8")
 assert "DROP TABLE" not in text.upper()
 assert "country_budget_allocations" in text
 assert "country_economy_state" in text
 assert "country_crises" in text
 assert "country_offices" in text

def test_scheduler_and_production_are_connected():
 scheduler=Path("apps/scheduler/main.py").read_text(encoding="utf-8")
 production=Path("packages/core/services/production.py").read_text(encoding="utf-8")
 assert '("country_economy_b", country_economy_b.catch_up)' in scheduler
 assert 'await scheduler_ops.run(name, job)' in scheduler
 assert "production_modifier_bp" in production
