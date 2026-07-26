from packages.core.services import unlocks


def test_catalogue_is_sorted_by_level():
    levels = [u.level for u in unlocks.catalogue()]
    assert levels == sorted(levels)


def test_progression_never_stalls_too_long():
    """Promise to the player: something new every few levels."""
    levels = [u.level for u in unlocks.catalogue()]
    gaps = [b - a for a, b in zip(levels, levels[1:], strict=False)]
    assert max(gaps) <= 10, f"a {max(gaps)}-level dead zone kills motivation"


def test_next_unlock_moves_forward():
    nxt = unlocks.next_unlock(1)
    assert nxt is not None and nxt.level == 2


def test_top_level_has_nothing_left():
    assert unlocks.next_unlock(999) is None


def test_available_grows_with_level():
    assert len(unlocks.available(1)) < len(unlocks.available(50))