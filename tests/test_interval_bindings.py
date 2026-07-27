from pathlib import Path

def test_integer_intervals_use_numeric_bind_casts() -> None:
    targets = [
        Path("packages/core/repositories/country_repo.py"),
        Path("packages/core/repositories/mission_repo.py"),
        Path("packages/core/repositories/player_repo.py"),
        Path("apps/scheduler/jobs/daily_reset.py"),
    ]
    text = "\n".join(path.read_text() for path in targets)
    assert "::text || ' days'" not in text
    assert "::text || ' hours'" not in text
    assert "$1 || ' days'" not in text
    assert "interval '1 day'" in text