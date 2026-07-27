from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_purchase_page_lists_all_benefits():
 text=(ROOT/'apps/teleworld_bot/handlers/world.py').read_text()
 for phrase in ('حذف تبلیغات عمومی','گزارش اقتصادی و سیاسی کامل‌تر','یادآوری هوشمند','بدون افزایش درآمد'):
  assert phrase in text
def test_subscription_is_group_scoped_and_30_days():
 text=(ROOT/'packages/core/services/commerce.py').read_text()
 assert "UPDATE groups SET ad_free_until=" in text
 assert "interval '30 days'" in text
def test_ads_skip_subscribed_world_groups():
 text=(ROOT/'packages/core/services/commerce.py').read_text()
 assert "ad_free_until IS NULL OR ad_free_until<=now()" in text
def test_stars_settlement_is_idempotent():
 text=(ROOT/'packages/core/services/commerce.py').read_text()
 assert "if payment[\"status\"]=='paid':return payment[\"purpose\"]" in text
def test_no_gameplay_power_is_granted():
 migration=(ROOT/'migrations/0010_stars_subscriptions_ad_marketplace.sql').read_text()
 assert 'ad_free_until' in migration
 assert 'production_modifier' not in migration
