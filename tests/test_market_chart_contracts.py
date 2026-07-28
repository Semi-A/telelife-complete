from datetime import UTC,datetime
from packages.core.services.market_chart import Candle,render

def test_market_chart_is_png():
 rows=[Candle(datetime.now(UTC),90000,91000,89500,90500,2)]
 assert render(rows).read(8)==b"\\x89PNG\\r\\n\\x1a\\n"
