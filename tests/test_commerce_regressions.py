from packages.core.services.commerce import ad_price

def test_all_channel_adjusted_prices_are_positive_and_schema_safe():
 for package in ("economy","standard","campaign","featured"):
  for channel in ("life","world","both"):
   assert 1 <= ad_price(package,channel) <= 10_000

def test_world_campaign_regression_price():assert ad_price("campaign","world")==180
def test_both_featured_price():assert ad_price("featured","both")==440