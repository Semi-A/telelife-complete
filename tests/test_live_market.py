import math
import pytest
from packages.core.services.live_market import extract_price
@pytest.mark.parametrize(("payload","expected"),[
 ({"price":91234},91234),({"data":{"price":"91,234"}},91234),
 ({"result":[{"last":91234.4}]},91234),
])
def test_extract_zipodo_price(payload,expected):assert extract_price(payload)==expected
@pytest.mark.parametrize("payload",[{}, {"price":True},{"price":"nan"},{"price":12},{"price":999999999999}])
def test_rejects_invalid_or_implausible_price(payload):
 with pytest.raises(ValueError):extract_price(payload)