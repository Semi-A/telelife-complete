from pathlib import Path

def test_country_identity_is_used_at_outbox_delivery_boundary():
 text=Path("apps/scheduler/jobs/country_jobs.py").read_text()
 assert "country_identity.destination" in text
 assert "country_identity.masthead" in text

def test_group_engagement_uses_country_not_telegram_title():
 text=Path("packages/core/services/engagement.py").read_text()
 assert "c.name country_name" in text
 assert "row['title']" not in text

def test_realism_schema_is_additive():
 text=Path("migrations/0013_country_identity_candles_realism.sql").read_text()
 for table in ("country_indicator_daily","country_shocks","country_newspapers"):
  assert f"CREATE TABLE IF NOT EXISTS {table}" in text