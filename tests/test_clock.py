from datetime import UTC, datetime

import pytest

from packages.core.utils import clock


def test_game_date_uses_configured_timezone():
    instant = datetime(2026, 7, 25, 21, 0, tzinfo=UTC)
    assert clock.game_today(instant).isoformat() == "2026-07-26"


def test_naive_datetimes_are_rejected():
    with pytest.raises(ValueError, match="timezone-aware"):
        clock.game_today(datetime(2026, 7, 26))