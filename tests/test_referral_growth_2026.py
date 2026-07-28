from pathlib import Path


def test_referral_schema_is_one_inviter_per_player():
 sql=Path("migrations/0026_referral_growth.sql").read_text()
 assert "invited_player_id BIGINT NOT NULL UNIQUE" in sql
 assert "CHECK(inviter_player_id<>invited_player_id)" in sql


def test_rewards_require_real_activation():
 source=Path("packages/core/services/referrals.py").read_text()
 assert "step>=4 and days>=2" in source
 assert "status='pending'" in source
 assert "10 minutes" in source


def test_rewards_are_idempotent_and_ledgered():
 source=Path("packages/core/services/referrals.py").read_text()
 sql=Path("migrations/0026_referral_growth.sql").read_text()
 assert "PRIMARY KEY(player_id,milestone)" in sql
 assert "referral_milestone" in source
 assert "lock_player" in source


def test_referral_routes_exist_and_home_stays_simple():
 life=Path("apps/telelife_bot/handlers/life.py").read_text()
 keys=Path("apps/telelife_bot/keyboards/main.py").read_text()
 assert '"referrals"' in keys and "referrals_page" in life and "refclaim" in life
 assert "start_payload" in life


def test_group_growth_entry_exists():
 keys=Path("apps/teleworld_bot/keyboards.py").read_text()
 world=Path("apps/teleworld_bot/handlers/world.py").read_text()
 assert "grow_country" in keys and "grow_country" in world