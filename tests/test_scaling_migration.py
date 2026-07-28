from packages.core.services.commerce import subscription_stars,treasury_price,ad_price
from packages.core.services.migration import exit_fee

def test_subscription_population_tiers():
 assert subscription_stars(1)==10 and subscription_stars(20)==10
 assert subscription_stars(21)==15 and subscription_stars(100)==15
 assert subscription_stars(101)==30 and subscription_stars(500)==30
 assert subscription_stars(501)==50 and subscription_stars(1000)==50
 assert subscription_stars(1001)==75

def test_treasury_population_formula():
 assert treasury_price(0,1)==20_000_000
 assert treasury_price(250_000_000,100)==150_000_000
 assert treasury_price(10_000_000_000,1000)==1_000_000_000

def test_channel_prices_round_up():
 assert ad_price('economy','life')==25
 assert ad_price('economy','world')==38
 assert ad_price('economy','both')==55
 assert ad_price('standard','world')==90
 assert ad_price('standard','both')==132

def test_migration_fee_bounds():
 assert exit_fee(1)==500_000
 assert exit_fee(100_000_000)==5_000_000
 assert exit_fee(2_000_000_000)==50_000_000