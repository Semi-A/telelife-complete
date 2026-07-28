-- Group-to-group council: local vote first, counterparty approval second.
CREATE TABLE IF NOT EXISTS country_council_proposals (
 id BIGSERIAL PRIMARY KEY,
 proposer_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 target_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 created_by_player_id BIGINT NOT NULL REFERENCES players(id),
 action_code TEXT NOT NULL CHECK(action_code IN ('friend','trade_partner','defensive_ally','aid_food','aid_energy','aid_irt')),
 status TEXT NOT NULL DEFAULT 'local_voting' CHECK(status IN ('local_voting','remote_voting','approved','rejected','expired','failed')),
 local_yes INTEGER NOT NULL DEFAULT 0,
 local_no INTEGER NOT NULL DEFAULT 0,
 remote_yes INTEGER NOT NULL DEFAULT 0,
 remote_no INTEGER NOT NULL DEFAULT 0,
 local_closes_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '24 hours',
 remote_closes_at TIMESTAMPTZ,
 executed_at TIMESTAMPTZ,
 failure_code TEXT,
 idempotency_key TEXT NOT NULL UNIQUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(proposer_country_id<>target_country_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_country_council_one_open_pair_action
 ON country_council_proposals(proposer_country_id,target_country_id,action_code)
 WHERE status IN ('local_voting','remote_voting');
CREATE INDEX IF NOT EXISTS ix_country_council_target_status ON country_council_proposals(target_country_id,status,created_at DESC);
CREATE INDEX IF NOT EXISTS ix_country_council_proposer_status ON country_council_proposals(proposer_country_id,status,created_at DESC);

CREATE TABLE IF NOT EXISTS country_council_votes (
 proposal_id BIGINT NOT NULL REFERENCES country_council_proposals(id) ON DELETE CASCADE,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
 vote TEXT NOT NULL CHECK(vote IN ('yes','no')),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(proposal_id,country_id,player_id)
);