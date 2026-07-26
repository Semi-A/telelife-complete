from packages.core.utils import fmt


def test_toman_grouping():
    assert fmt.toman(500000, persian=False) == "500\u066c000 \u062a\u0648\u0645\u0627\u0646"


def test_usd_cents():
    assert fmt.usd(2550, persian=False) == "25.50$"
    assert fmt.usd(0, persian=False) == "0.00$"


def test_progress_bar_bounds():
    assert fmt.progress_bar(0, 100) == "\u25b1" * 10
    assert fmt.progress_bar(100, 100) == "\u25b0" * 10
    assert len(fmt.progress_bar(37, 100)) == 10
    assert fmt.progress_bar(5, 0) == "\u25b1" * 10


def test_persian_digits_applied():
    assert "5" not in fmt.number(12345)