from packages.core.services import progression


def test_curve_is_monotonic():
    values = [progression.xp_required(lvl) for lvl in range(1, 50)]
    assert values == sorted(values)
    assert all(v > 0 for v in values)


def test_level_progress_returns_pair():
    current, needed = progression.level_progress(1, 40)
    assert current == 40
    assert needed == progression.xp_required(1)


def test_max_level_caps_progress():
    top = progression.max_level()
    current, needed = progression.level_progress(top, 999)
    assert current == needed == 999