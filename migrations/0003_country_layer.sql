-- ============================================================
-- TeleLife / TeleWorld | Phase 5 country and group layer schema
-- Forward-only. Existing identities, balances, and ledger rows are preserved.
-- Game balance values and durations belong in YAML, not in this migration.
-- ============================================================

-- ---------- extend the shared ledger ----------
-- The Phase 1 ledger only supported player IRT/USD accounts. Phase 5 keeps
-- that table as the single economic journal and expands its ownership/assets.
ALTER TABLE ledger
    ADD COLUMN IF NOT EXISTS country_id BIGINT,
    ADD COLUMN IF NOT EXISTS asset_code TEXT;

UPDATE ledger
SET asset_code = currency
WHERE asset_code IS NULL;

-- Keep legacy Phase 1/2 writers compatible during the expansion window.
-- A trigger copies currency into asset_code when an older writer omits it.
CREATE OR REPLACE FUNCTION ledger_fill_asset_code() RETURNS TRIGGER AS $$
BEGIN
    NEW.asset_code := COALESCE(NEW.asset_code, NEW.currency);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_ledger_fill_asset_code ON ledger;
CREATE TRIGGER trg_ledger_fill_asset_code
    BEFORE INSERT ON ledger
    FOR EACH ROW EXECUTE FUNCTION ledger_fill_asset_code();

ALTER TABLE ledger
    ALTER COLUMN asset_code SET NOT NULL,
    ALTER COLUMN player_id DROP NOT NULL,
    ALTER COLUMN currency DROP NOT NULL;

ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_currency_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_account_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_owner_check;
ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_balance_after_check;

ALTER TABLE ledger
    ADD CONSTRAINT ledger_owner_check CHECK (
        (player_id IS NOT NULL AND country_id IS NULL)
        OR (player_id IS NULL AND country_id IS NOT NULL)
    ),
    ADD CONSTRAINT ledger_balance_after_check CHECK (balance_after >= 0),
    ADD CONSTRAINT ledger_asset_code_check CHECK (length(asset_code) BETWEEN 1 AND 64),
    ADD CONSTRAINT ledger_account_check CHECK (length(account) BETWEEN 1 AND 64);

CREATE INDEX IF NOT EXISTS idx_ledger_country_time
    ON ledger (country_id, created_at DESC)
    WHERE country_id IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_ledger_asset_time
    ON ledger (asset_code, created_at DESC);

COMMENT ON TABLE ledger IS
    'Append-only source of truth for every player and country asset mutation.';
COMMENT ON COLUMN ledger.idempotency_key IS
    'Unique mutation-leg key; multi-leg operations use deterministic leg suffixes.';

-- ---------- countries and citizenship ----------
CREATE TABLE IF NOT EXISTS countries (
    id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    group_id            BIGINT NOT NULL UNIQUE REFERENCES groups(id) ON DELETE RESTRICT,
    name                TEXT NOT NULL UNIQUE,
    government_type     TEXT NOT NULL,
    description         TEXT NOT NULL,
    flag_file_id        TEXT,
    flag_file_unique_id TEXT,
    protection_until    TIMESTAMPTZ NOT NULL,
    president_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
    treasury_toman      BIGINT NOT NULL DEFAULT 0 CHECK (treasury_toman >= 0),
    daily_income_toman  BIGINT NOT NULL DEFAULT 0 CHECK (daily_income_toman >= 0),
    daily_expense_toman BIGINT NOT NULL DEFAULT 0 CHECK (daily_expense_toman >= 0),
    created_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(name) BETWEEN 1 AND 80),
    CHECK (length(government_type) BETWEEN 1 AND 32),
    CHECK (length(description) BETWEEN 1 AND 500)
);

ALTER TABLE ledger DROP CONSTRAINT IF EXISTS ledger_country_id_fkey;
ALTER TABLE ledger
    ADD CONSTRAINT ledger_country_id_fkey
    FOREIGN KEY (country_id) REFERENCES countries(id) ON DELETE RESTRICT;

CREATE INDEX IF NOT EXISTS idx_countries_protection
    ON countries (protection_until);
CREATE INDEX IF NOT EXISTS idx_countries_president
    ON countries (president_player_id)
    WHERE president_player_id IS NOT NULL;

CREATE TABLE IF NOT EXISTS citizenships (
    player_id  BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    joined_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_citizenships_country
    ON citizenships (country_id, joined_at);

CREATE TABLE IF NOT EXISTS country_resources (
    country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    asset_code TEXT NOT NULL,
    quantity   BIGINT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (country_id, asset_code),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

-- ---------- player resources and lazy production ----------
CREATE TABLE IF NOT EXISTS player_resources (
    player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    asset_code TEXT NOT NULL,
    quantity   BIGINT NOT NULL DEFAULT 0 CHECK (quantity >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (player_id, asset_code),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS player_jobs (
    player_id             BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    job_code              TEXT NOT NULL,
    output_asset_code     TEXT NOT NULL,
    production_level      INTEGER NOT NULL DEFAULT 1 CHECK (production_level > 0),
    storage_level         INTEGER NOT NULL DEFAULT 1 CHECK (storage_level > 0),
    stored_amount         BIGINT NOT NULL DEFAULT 0 CHECK (stored_amount >= 0),
    production_updated_at TIMESTAMPTZ NOT NULL,
    selected_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at            TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(job_code) BETWEEN 1 AND 32),
    CHECK (length(output_asset_code) BETWEEN 1 AND 64)
);

CREATE INDEX IF NOT EXISTS idx_player_jobs_checkpoint
    ON player_jobs (production_updated_at);

-- ---------- elections ----------
CREATE TABLE IF NOT EXISTS elections (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id         BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    started_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    status             TEXT NOT NULL,
    nominations_end_at TIMESTAMPTZ NOT NULL,
    voting_end_at      TIMESTAMPTZ NOT NULL,
    winner_player_id   BIGINT REFERENCES players(id) ON DELETE SET NULL,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at        TIMESTAMPTZ,
    CHECK (status IN ('nominations', 'voting', 'completed', 'cancelled')),
    CHECK (voting_end_at > nominations_end_at)
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_elections_country_open
    ON elections (country_id)
    WHERE status IN ('nominations', 'voting');
CREATE INDEX IF NOT EXISTS idx_elections_due
    ON elections (status, nominations_end_at, voting_end_at);

CREATE TABLE IF NOT EXISTS election_candidates (
    election_id BIGINT NOT NULL REFERENCES elections(id) ON DELETE RESTRICT,
    player_id   BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    message_chat_id BIGINT,
    message_id  BIGINT,
    nominated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (election_id, player_id)
);

CREATE TABLE IF NOT EXISTS election_votes (
    election_id        BIGINT NOT NULL REFERENCES elections(id) ON DELETE RESTRICT,
    voter_player_id    BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    candidate_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    voted_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (election_id, voter_player_id),
    FOREIGN KEY (election_id, candidate_player_id)
        REFERENCES election_candidates(election_id, player_id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_election_votes_tally
    ON election_votes (election_id, candidate_player_id);

-- ---------- national projects ----------
CREATE TABLE IF NOT EXISTS national_projects (
    id                   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id           BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    project_key          TEXT NOT NULL,
    started_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    status               TEXT NOT NULL DEFAULT 'active',
    created_at           TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at         TIMESTAMPTZ,
    UNIQUE (country_id, project_key),
    CHECK (status IN ('active', 'completed', 'cancelled')),
    CHECK (length(project_key) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS project_requirements (
    project_id         BIGINT NOT NULL REFERENCES national_projects(id) ON DELETE RESTRICT,
    asset_code         TEXT NOT NULL,
    required_amount    BIGINT NOT NULL CHECK (required_amount > 0),
    contributed_amount BIGINT NOT NULL DEFAULT 0 CHECK (contributed_amount >= 0),
    PRIMARY KEY (project_id, asset_code)
);

CREATE TABLE IF NOT EXISTS project_contributions (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id      BIGINT NOT NULL REFERENCES national_projects(id) ON DELETE RESTRICT,
    player_id       BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    asset_code      TEXT NOT NULL,
    amount          BIGINT NOT NULL CHECK (amount > 0),
    idempotency_key TEXT NOT NULL UNIQUE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_project_contributions_project
    ON project_contributions (project_id, created_at DESC);

-- ---------- country polls ----------
CREATE TABLE IF NOT EXISTS polls (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id         BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    creator_player_id  BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    question           TEXT NOT NULL,
    status             TEXT NOT NULL DEFAULT 'active',
    closes_at          TIMESTAMPTZ NOT NULL,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    resolved_at        TIMESTAMPTZ,
    CHECK (status IN ('active', 'completed', 'cancelled')),
    CHECK (length(question) BETWEEN 1 AND 200)
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_polls_creator_active
    ON polls (creator_player_id)
    WHERE status = 'active';
CREATE INDEX IF NOT EXISTS idx_polls_due
    ON polls (status, closes_at);

CREATE TABLE IF NOT EXISTS poll_options (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    poll_id     BIGINT NOT NULL REFERENCES polls(id) ON DELETE RESTRICT,
    option_text TEXT NOT NULL,
    UNIQUE (poll_id, id),
    UNIQUE (poll_id, option_text),
    CHECK (length(option_text) BETWEEN 1 AND 100)
);

CREATE TABLE IF NOT EXISTS poll_votes (
    poll_id         BIGINT NOT NULL REFERENCES polls(id) ON DELETE RESTRICT,
    voter_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    option_id       BIGINT NOT NULL,
    voted_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (poll_id, voter_player_id),
    FOREIGN KEY (poll_id, option_id)
        REFERENCES poll_options(poll_id, id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_poll_votes_tally
    ON poll_votes (poll_id, option_id);

-- ---------- country missions and effects ----------
CREATE TABLE IF NOT EXISTS country_missions (
    country_id        BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    mission_date      DATE NOT NULL,
    mission_key       TEXT NOT NULL,
    metric_key        TEXT NOT NULL,
    target_amount     BIGINT NOT NULL CHECK (target_amount > 0),
    progress_amount   BIGINT NOT NULL DEFAULT 0 CHECK (progress_amount >= 0),
    reward_asset_code TEXT NOT NULL,
    reward_amount     BIGINT NOT NULL CHECK (reward_amount > 0),
    completed_at      TIMESTAMPTZ,
    rewarded_at       TIMESTAMPTZ,
    PRIMARY KEY (country_id, mission_date, mission_key)
);

CREATE INDEX IF NOT EXISTS idx_country_missions_open
    ON country_missions (country_id, mission_date)
    WHERE completed_at IS NULL;

CREATE TABLE IF NOT EXISTS country_effects (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id  BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    effect_code TEXT NOT NULL,
    magnitude   BIGINT NOT NULL,
    starts_at   TIMESTAMPTZ NOT NULL,
    ends_at     TIMESTAMPTZ NOT NULL,
    source_type TEXT NOT NULL,
    source_key  TEXT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (country_id, source_type, source_key, effect_code),
    CHECK (ends_at > starts_at)
);

CREATE INDEX IF NOT EXISTS idx_country_effects_active
    ON country_effects (country_id, effect_code, ends_at);

-- ---------- daily economy and events ----------
CREATE TABLE IF NOT EXISTS country_economy_daily (
    country_id       BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
    economy_date     DATE NOT NULL,
    income_toman     BIGINT NOT NULL DEFAULT 0 CHECK (income_toman >= 0),
    expense_toman    BIGINT NOT NULL DEFAULT 0 CHECK (expense_toman >= 0),
    closing_treasury BIGINT NOT NULL CHECK (closing_treasury >= 0),
    ledger_key       TEXT NOT NULL UNIQUE,
    processed_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (country_id, economy_date)
);

CREATE TABLE IF NOT EXISTS daily_events (
    event_date      DATE PRIMARY KEY,
    event_code      TEXT NOT NULL,
    effect_payload  JSONB NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    announced_at    TIMESTAMPTZ,
    CHECK (jsonb_typeof(effect_payload) = 'object')
);

-- ---------- transactional news outbox ----------
CREATE TABLE IF NOT EXISTS news_outbox (
    id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    idempotency_key   TEXT NOT NULL UNIQUE,
    event_type        TEXT NOT NULL,
    destination_chat_id BIGINT,
    payload           JSONB NOT NULL,
    attempts          INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    available_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    processing_token  UUID,
    processing_until  TIMESTAMPTZ,
    published_at      TIMESTAMPTZ,
    last_error_code   TEXT,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (jsonb_typeof(payload) = 'object')
);

CREATE INDEX IF NOT EXISTS idx_news_outbox_claim
    ON news_outbox (available_at, created_at)
    WHERE published_at IS NULL;
CREATE INDEX IF NOT EXISTS idx_news_outbox_lease
    ON news_outbox (processing_until)
    WHERE published_at IS NULL AND processing_token IS NOT NULL;

-- ---------- global feature flags and privileged audit ----------
CREATE TABLE IF NOT EXISTS feature_flags (
    key           TEXT PRIMARY KEY,
    enabled       BOOLEAN NOT NULL DEFAULT FALSE,
    updated_by    TEXT NOT NULL,
    updated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(key) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS admin_audit_log (
    id                 BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    admin_actor        TEXT NOT NULL,
    action             TEXT NOT NULL,
    target_player_id   BIGINT REFERENCES players(id) ON DELETE RESTRICT,
    target_country_id  BIGINT REFERENCES countries(id) ON DELETE RESTRICT,
    request_id         TEXT NOT NULL UNIQUE,
    details            JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at         TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (jsonb_typeof(details) = 'object')
);

CREATE INDEX IF NOT EXISTS idx_admin_audit_time
    ON admin_audit_log (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_admin_audit_action_time
    ON admin_audit_log (action, created_at DESC);

-- ---------- append-only database guards ----------
CREATE OR REPLACE FUNCTION reject_append_only_mutation() RETURNS TRIGGER AS $$
BEGIN
    RAISE EXCEPTION 'append-only table cannot be updated or deleted';
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_ledger_append_only ON ledger;
CREATE TRIGGER trg_ledger_append_only
    BEFORE UPDATE OR DELETE ON ledger
    FOR EACH ROW EXECUTE FUNCTION reject_append_only_mutation();

DROP TRIGGER IF EXISTS trg_admin_audit_append_only ON admin_audit_log;
CREATE TRIGGER trg_admin_audit_append_only
    BEFORE UPDATE OR DELETE ON admin_audit_log
    FOR EACH ROW EXECUTE FUNCTION reject_append_only_mutation();

DROP TRIGGER IF EXISTS trg_countries_touch ON countries;
CREATE TRIGGER trg_countries_touch
    BEFORE UPDATE ON countries
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();

DROP TRIGGER IF EXISTS trg_player_jobs_touch ON player_jobs;
CREATE TRIGGER trg_player_jobs_touch
    BEFORE UPDATE ON player_jobs
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();