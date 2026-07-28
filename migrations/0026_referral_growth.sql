-- Referral growth: reward activation, never raw sign-up.
CREATE TABLE IF NOT EXISTS player_referrals (
 id BIGSERIAL PRIMARY KEY,
 inviter_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
 invited_player_id BIGINT NOT NULL UNIQUE REFERENCES players(id) ON DELETE CASCADE,
 referral_code TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','qualified','rewarded','rejected')),
 qualified_at TIMESTAMPTZ,
 rewarded_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(inviter_player_id<>invited_player_id)
);
CREATE INDEX IF NOT EXISTS ix_player_referrals_inviter ON player_referrals(inviter_player_id,status,created_at DESC);
CREATE UNIQUE INDEX IF NOT EXISTS uq_player_referral_pair ON player_referrals(inviter_player_id,invited_player_id);

CREATE TABLE IF NOT EXISTS referral_milestone_rewards (
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
 milestone INTEGER NOT NULL CHECK(milestone IN (1,3,5,10,20,50)),
 reward_toman BIGINT NOT NULL CHECK(reward_toman>=0),
 claimed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(player_id,milestone)
);