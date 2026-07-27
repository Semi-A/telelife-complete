-- Release C: country trade escrow, diplomacy, reputation, sanctions and emergency aid.
-- Additive and forward-only. Existing commerce/Stars tables are intentionally untouched.

CREATE TABLE IF NOT EXISTS country_international_reputation (
 country_id BIGINT PRIMARY KEY REFERENCES countries(id) ON DELETE CASCADE,
 score INTEGER NOT NULL DEFAULT 50 CHECK(score BETWEEN 0 AND 100),
 fulfilled_contracts INTEGER NOT NULL DEFAULT 0 CHECK(fulfilled_contracts>=0),
 cancelled_contracts INTEGER NOT NULL DEFAULT 0 CHECK(cancelled_contracts>=0),
 aid_sent BIGINT NOT NULL DEFAULT 0 CHECK(aid_sent>=0),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO country_international_reputation(country_id)
SELECT id FROM countries ON CONFLICT(country_id) DO NOTHING;

CREATE TABLE IF NOT EXISTS country_relations (
 country_low_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 country_high_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 status TEXT NOT NULL DEFAULT 'neutral' CHECK(status IN ('neutral','friend','trade_partner','defensive_ally','rival','hostile')),
 proposed_status TEXT CHECK(proposed_status IN ('friend','trade_partner','defensive_ally')),
 proposed_by_country_id BIGINT REFERENCES countries(id) ON DELETE SET NULL,
 proposal_expires_at TIMESTAMPTZ,
 changed_by_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_low_id,country_high_id),
 CHECK(country_low_id<country_high_id)
);
CREATE INDEX IF NOT EXISTS idx_country_relations_proposal ON country_relations(proposed_by_country_id,proposal_expires_at) WHERE proposed_status IS NOT NULL;

CREATE TABLE IF NOT EXISTS country_sanctions (
 imposing_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 target_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active','lifted')),
 imposed_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 imposed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 lifted_at TIMESTAMPTZ,
 reason TEXT NOT NULL DEFAULT 'محدودیت تجاری',
 PRIMARY KEY(imposing_country_id,target_country_id),
 CHECK(imposing_country_id<>target_country_id)
);
CREATE INDEX IF NOT EXISTS idx_country_sanctions_active ON country_sanctions(target_country_id) WHERE status='active';

CREATE TABLE IF NOT EXISTS country_trade_contracts (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 proposer_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
 recipient_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
 offered_asset TEXT NOT NULL,
 offered_amount BIGINT NOT NULL CHECK(offered_amount>0),
 requested_asset TEXT NOT NULL,
 requested_amount BIGINT NOT NULL CHECK(requested_amount>0),
 tariff_bp INTEGER NOT NULL DEFAULT 500 CHECK(tariff_bp BETWEEN 0 AND 5000),
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','accepted','cancelled','expired')),
 created_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 accepted_by_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
 idempotency_key TEXT NOT NULL UNIQUE,
 expires_at TIMESTAMPTZ NOT NULL,
 accepted_at TIMESTAMPTZ,
 cancelled_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(proposer_country_id<>recipient_country_id),
 CHECK(length(offered_asset) BETWEEN 1 AND 32),
 CHECK(length(requested_asset) BETWEEN 1 AND 32)
);
CREATE INDEX IF NOT EXISTS idx_country_trade_open_recipient ON country_trade_contracts(recipient_country_id,expires_at,id) WHERE status='open';
CREATE INDEX IF NOT EXISTS idx_country_trade_open_proposer ON country_trade_contracts(proposer_country_id,expires_at,id) WHERE status='open';

CREATE TABLE IF NOT EXISTS country_trade_escrow (
 contract_id BIGINT PRIMARY KEY REFERENCES country_trade_contracts(id) ON DELETE RESTRICT,
 asset_code TEXT NOT NULL,
 amount BIGINT NOT NULL CHECK(amount>0),
 status TEXT NOT NULL DEFAULT 'held' CHECK(status IN ('held','released','refunded')),
 released_at TIMESTAMPTZ,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS country_humanitarian_aid (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 donor_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
 recipient_country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
 asset_code TEXT NOT NULL CHECK(asset_code IN ('food','energy','IRT')),
 amount BIGINT NOT NULL CHECK(amount>0),
 crisis_id BIGINT REFERENCES country_crises(id) ON DELETE SET NULL,
 sent_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 idempotency_key TEXT NOT NULL UNIQUE,
 sent_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(donor_country_id<>recipient_country_id)
);
CREATE INDEX IF NOT EXISTS idx_country_aid_daily ON country_humanitarian_aid(donor_country_id,sent_at DESC);

CREATE TABLE IF NOT EXISTS country_diplomacy_audit (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 counterparty_country_id BIGINT REFERENCES countries(id) ON DELETE SET NULL,
 actor_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
 action_code TEXT NOT NULL,
 idempotency_key TEXT NOT NULL UNIQUE,
 payload JSONB NOT NULL DEFAULT '{}'::jsonb,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_country_diplomacy_audit_country ON country_diplomacy_audit(country_id,created_at DESC);
