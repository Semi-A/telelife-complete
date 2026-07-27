from packages.core.db import migrator


def test_migrations_discovered_and_ordered():
    files = migrator.discover()
    assert files, "no migration files found"
    names = [p.name for p in files]
    assert names == sorted(names)
    assert names[0].startswith("0001")


def test_checksum_is_stable():
    a = migrator._checksum("SELECT 1;")
    b = migrator._checksum("SELECT 1;")
    assert a == b and len(a) == 16

def test_only_pre_normalization_migrations_are_legacy_compatible():
    assert migrator.LEGACY_CHECKSUM_VERSIONS == {
        "0001_core_schema", "0002_progression", "0003_country_layer",
        "0004_admin_command_center", "0005_life_world_hardening",
        "0006_phase3_phase4_complete", "0007_unified_ui_onboarding",
        "0008_world_access_lifecycle", "0009_ads_governance_moderation",
        "0010_stars_subscriptions_ad_marketplace",
        "0011_population_channels_migration",
        "0012_reliability_live_market_engagement",
        "0013_country_identity_candles_realism",
        "0014_free_tier_hardening",
    }
    assert "0015_future_migration" not in migrator.LEGACY_CHECKSUM_VERSIONS


def test_new_migrations_remain_checksum_strict():
    source = (migrator.Path(migrator.__file__)).read_text(encoding="utf-8")
    assert "if version in LEGACY_CHECKSUM_VERSIONS" in source
    assert "Create a new migration instead of editing history" in source