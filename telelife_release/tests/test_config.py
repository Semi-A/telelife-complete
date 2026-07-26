import pytest

from packages.core.config import ConfigError, get_config


def test_required_sections_present():
    cfg = get_config()
    assert cfg.int_("economy.starting_balance.wallet_toman") > 0
    assert cfg.int_("progression.xp_curve.base") > 0
    assert cfg.bool_("core.menu_cleanup.enabled") is True


def test_missing_key_raises():
    with pytest.raises(ConfigError):
        get_config().get("economy.does.not.exist")


def test_default_is_returned():
    assert get_config().get("nope.nope", "fallback") == "fallback"


def test_explicit_none_default_is_supported():
    assert get_config().get("missing.optional.value", None) is None


def test_numeric_yaml_keys_support_dotted_access():
    assert get_config().int_("jobs.storage.levels.1.capacity_hours") == 6