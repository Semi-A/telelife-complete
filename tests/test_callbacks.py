from packages.core.ui.callbacks import Callback, cb


def test_roundtrip():
    packed = cb("tl", "claim", 12345, "mission_a")
    parsed = Callback.parse(packed)
    assert parsed == Callback("tl", "claim", 12345, "mission_a")


def test_ownership_check_needs_no_database():
    parsed = Callback.parse(cb("tl", "profile", 777))
    assert parsed is not None
    assert parsed.owned_by(777)
    assert not parsed.owned_by(778)


def test_rejects_garbage():
    assert Callback.parse("nope") is None
    assert Callback.parse("tl:x:notanumber") is None


def test_enforces_telegram_64_byte_limit():
    import pytest

    with pytest.raises(ValueError, match="64-byte"):
        cb("tl", "action", 123456789, "x" * 80)