-- Safe, consent-first social life inside country groups.
CREATE TABLE IF NOT EXISTS social_relationships (
 id BIGSERIAL PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 kind TEXT NOT NULL CHECK(kind IN ('friendship','marriage')),
 player_low_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
 player_high_id BIGINT NOT NULL REFERENCES players(id) ON DELETE CASCADE,
 status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','active','rejected','ended','cancelled')),
 proposed_by BIGINT NOT NULL REFERENCES players(id),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), accepted_at TIMESTAMPTZ, ended_at TIMESTAMPTZ,
 cooldown_until TIMESTAMPTZ, CHECK(player_low_id < player_high_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_social_pair_open ON social_relationships(kind,player_low_id,player_high_id)
 WHERE status IN ('pending','active');
CREATE INDEX IF NOT EXISTS idx_social_active_marriage_low ON social_relationships(player_low_id) WHERE kind='marriage' AND status='active';
CREATE INDEX IF NOT EXISTS idx_social_active_marriage_high ON social_relationships(player_high_id) WHERE kind='marriage' AND status='active';
CREATE INDEX IF NOT EXISTS idx_social_relationship_target ON social_relationships(proposed_by,status,created_at DESC);

CREATE TABLE IF NOT EXISTS citizen_help_events (
 id BIGSERIAL PRIMARY KEY, country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 helper_id BIGINT NOT NULL REFERENCES players(id), recipient_id BIGINT NOT NULL REFERENCES players(id),
 amount_toman BIGINT NOT NULL CHECK(amount_toman BETWEEN 10000 AND 200000),
 reputation_awarded INT NOT NULL DEFAULT 0 CHECK(reputation_awarded BETWEEN 0 AND 3),
 idempotency_key TEXT NOT NULL UNIQUE, created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(helper_id<>recipient_id)
);
CREATE INDEX IF NOT EXISTS idx_help_daily ON citizen_help_events(helper_id,created_at DESC);

CREATE TABLE IF NOT EXISTS social_competitions (
 id BIGSERIAL PRIMARY KEY, country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 challenger_id BIGINT NOT NULL REFERENCES players(id), opponent_id BIGINT NOT NULL REFERENCES players(id),
 status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','active','completed','rejected','expired')),
 challenger_score INT NOT NULL DEFAULT 0, opponent_score INT NOT NULL DEFAULT 0,
 round_no SMALLINT NOT NULL DEFAULT 0 CHECK(round_no BETWEEN 0 AND 3),
 turn_player_id BIGINT REFERENCES players(id), winner_id BIGINT REFERENCES players(id),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), expires_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '24 hours',
 resolved_at TIMESTAMPTZ, CHECK(challenger_id<>opponent_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_competition_pair_open ON social_competitions(country_id,LEAST(challenger_id,opponent_id),GREATEST(challenger_id,opponent_id)) WHERE status IN ('pending','active');

CREATE TABLE IF NOT EXISTS citizen_cases (
 id BIGSERIAL PRIMARY KEY, country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 plaintiff_id BIGINT NOT NULL REFERENCES players(id), defendant_id BIGINT NOT NULL REFERENCES players(id),
 category TEXT NOT NULL CHECK(category IN ('harassment','fraud','threat','spam','other')),
 summary TEXT NOT NULL CHECK(length(summary) BETWEEN 10 AND 500),
 status TEXT NOT NULL DEFAULT 'review' CHECK(status IN ('review','voting','resolved','dismissed')),
 opened_at TIMESTAMPTZ NOT NULL DEFAULT now(), voting_ends_at TIMESTAMPTZ,
 guilty_votes INT NOT NULL DEFAULT 0, not_guilty_votes INT NOT NULL DEFAULT 0,
 verdict TEXT CHECK(verdict IN ('guilty','not_guilty','dismissed')), resolved_at TIMESTAMPTZ,
 CHECK(plaintiff_id<>defendant_id)
);
CREATE INDEX IF NOT EXISTS idx_cases_country_open ON citizen_cases(country_id,status,opened_at DESC);
CREATE TABLE IF NOT EXISTS citizen_case_votes (
 case_id BIGINT NOT NULL REFERENCES citizen_cases(id) ON DELETE CASCADE,
 voter_id BIGINT NOT NULL REFERENCES players(id), vote TEXT NOT NULL CHECK(vote IN ('guilty','not_guilty')),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), PRIMARY KEY(case_id,voter_id)
);

CREATE TABLE IF NOT EXISTS citizen_reports (
 id BIGSERIAL PRIMARY KEY, country_id BIGINT NOT NULL REFERENCES countries(id),
 reporter_id BIGINT NOT NULL REFERENCES players(id), target_id BIGINT NOT NULL REFERENCES players(id),
 category TEXT NOT NULL CHECK(category IN ('harassment','fraud','threat','spam','other')),
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','reviewed','closed')),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), CHECK(reporter_id<>target_id)
);
CREATE INDEX IF NOT EXISTS idx_reports_open ON citizen_reports(country_id,status,created_at DESC);