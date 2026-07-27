from packages.core.services.commerce import PACKAGES,treasury_price,valid_url,ad_price

def test_package_base_prices_and_delivery_counts():
 assert PACKAGES['economy'][:3]==(25,1,1)
 assert PACKAGES['standard'][:3]==(60,3,24)
 assert PACKAGES['campaign'][:3]==(120,6,72)
 assert PACKAGES['featured'][:3]==(200,8,168)
def test_dynamic_treasury_price_is_population_aware_and_bounded():
 assert treasury_price(1,0)==20_000_000
 assert treasury_price(250_000_000,100)==150_000_000
 assert treasury_price(10_000_000_000,1000)==1_000_000_000
def test_channel_price():
 assert ad_price('economy','life')==25
 assert ad_price('economy','world')==38
 assert ad_price('economy','both')==55
def test_only_http_links():
 assert valid_url('https://example.com/x')
 assert not valid_url('javascript:alert(1)')
