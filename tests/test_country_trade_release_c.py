from pathlib import Path
from packages.core.config import get_config
from packages.core.services.country_trade_rules import pair,tariff_bp,net_after_tariff,open_limit

def test_country_pair_is_canonical_and_rejects_self():
 assert pair(9,2)==(2,9)
 try:pair(4,4)
 except ValueError as exc:assert str(exc)=="same_country"
 else:raise AssertionError("self relation accepted")

def test_relations_change_real_tariffs():
 assert tariff_bp("trade_partner")<tariff_bp("neutral")<tariff_bp("hostile")

def test_tariff_never_creates_negative_delivery():
 assert net_after_tariff(1,5000)==(1,0)
 net,fee=net_after_tariff(1000,500)
 assert net==950 and fee==50

def test_reputation_increases_contract_capacity_with_a_cap():
 assert open_limit(0)>=3
 assert open_limit(100)>open_limit(0)
 assert open_limit(10000)==open_limit(100)

def test_contract_presets_are_bounded_and_distinct_assets():
 cfg=get_config();maximum=cfg.int_("country_trade.contracts.max_amount")
 for spec in cfg.section("country_trade.contracts.presets").values():
  assert 0<int(spec["offered_amount"])<=maximum
  assert 0<int(spec["requested_amount"])<=maximum
  assert spec["offered_asset"]!=spec["requested_asset"]

def test_release_c_migration_is_additive_and_isolated_from_stars_commerce():
 text=Path("migrations/0018_country_trade_diplomacy_release_c.sql").read_text(encoding="utf-8")
 assert "DROP TABLE" not in text.upper() and "DROP COLUMN" not in text.upper()
 for name in ("country_trade_contracts","country_trade_escrow","country_relations","country_sanctions","country_humanitarian_aid"):
  assert name in text
 assert "ad_requests" not in text and "star_payments" not in text

def test_acceptance_and_expiry_are_connected_to_atomic_service_and_scheduler():
 service=Path("packages/core/services/country_trade.py").read_text(encoding="utf-8")
 scheduler=Path("apps/scheduler/main.py").read_text(encoding="utf-8")
 assert "async with db.transaction()" in service
 assert "FOR UPDATE" in service
 assert "country_trade_escrow" in service
 assert '"country_trade_expiry"' in scheduler

def test_ui_exposes_trade_relations_aid_and_reference_history():
 world=Path("apps/teleworld_bot/handlers/world.py").read_text(encoding="utf-8")
 for token in ('action == "trade"','action == "relations"','action == "aid"','action == "traderef"'):
  assert token in world
