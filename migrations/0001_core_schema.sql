-- ============================================================
-- TeleLife / TeleWorld  |  Phase 1 core schema
-- Money is BIGINT minor units. NEVER float.
-- ============================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ---------- players : one identity across both bots ----------
CREATE TABLE IF NOT EXISTS players (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    telegram_id     BIGINT      NOT NULL UNIQUE,
    username        TEXT,
    first_name      TEXT        NOT NULL DEFAULT '',
    language_code   TEXT        NOT NULL DEFAULT 'fa',

    level           INTEGER     NOT NULL DEFAULT 1  CHECK (level >= 1),
    xp              BIGINT      NOT NULL DEFAULT 0  CHECK (xp >= 0),
    reputation      INTEGER     NOT NULL DEFAULT 0,
    happiness       SMALLINT    NOT NULL DEFAULT 70 CHECK (happiness BETWEEN 0 AND 100),
    prestige        SMALLINT    NOT NULL DEFAULT 0  CHECK (prestige >= 0),

    wallet_toman    BIGINT      NOT NULL DEFAULT 0  CHECK (wallet_toman >= 0),
    savings_toman   BIGINT      NOT NULL DEFAULT 0  CHECK (savings_toman >= 0),
    usd_cents       BIGINT      NOT NULL DEFAULT 0  CHECK (usd_cents >= 0),

    is_banned       BOOLEAN     NOT NULL DEFAULT FALSE,
    is_frozen       BOOLEAN     NOT NULL DEFAULT FALSE,
    ban_reason      TEXT,

    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_players_last_seen  ON players (last_seen_at DESC);
CREATE INDEX IF NOT EXISTS idx_players_level_xp   ON players (level DESC, xp DESC);
CREATE INDEX IF NOT EXISTS idx_players_wealth     ON players ((wallet_toman + savings_toman) DESC);
CREATE INDEX IF NOT EXISTS idx_players_active     ON players (id) WHERE NOT is_banned AND NOT is_frozen;

-- ---------- groups : TeleWorld territories ----------
CREATE TABLE IF NOT EXISTS groups (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    telegram_id     BIGINT      NOT NULL UNIQUE,
    title           TEXT        NOT NULL DEFAULT '',
    is_active       BOOLEAN     NOT NULL DEFAULT TRUE,
    member_count    INTEGER     NOT NULL DEFAULT 0,
    settings        JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_active_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_groups_active ON groups (last_active_at DESC) WHERE is_active;

-- ---------- group_members ----------
CREATE TABLE IF NOT EXISTS group_members (
    group_id        BIGINT      NOT NULL REFERENCES groups(id)  ON DELETE CASCADE,
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    joined_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_active_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (group_id, player_id)
);

CREATE INDEX IF NOT EXISTS idx_group_members_player ON group_members (player_id);

-- ---------- ledger : the ONLY source of truth for money movement ----------
CREATE TABLE IF NOT EXISTS ledger (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    idempotency_key TEXT        NOT NULL,
    reason          TEXT        NOT NULL,
    currency        TEXT        NOT NULL CHECK (currency IN ('IRT','USD')),
    account         TEXT        NOT NULL CHECK (account IN ('wallet','savings','usd')),
    amount          BIGINT      NOT NULL,
    balance_after   BIGINT      NOT NULL,
    metadata        JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- The single most important constraint in the project:
-- it makes double-clicks, Telegram retries and races economically harmless.
CREATE UNIQUE INDEX IF NOT EXISTS uq_ledger_idempotency ON ledger (idempotency_key);
CREATE INDEX IF NOT EXISTS idx_ledger_player_time ON ledger (player_id, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_ledger_reason_time ON ledger (reason, created_at DESC);

-- ---------- cooldowns ----------
CREATE TABLE IF NOT EXISTS cooldowns (
    player_id       BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    action          TEXT        NOT NULL,
    expires_at      TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (player_id, action)
);

CREATE INDEX IF NOT EXISTS idx_cooldowns_expiry ON cooldowns (expires_at);

-- ---------- audit_log ----------
CREATE TABLE IF NOT EXISTS audit_log (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    actor       TEXT        NOT NULL,
    action      TEXT        NOT NULL,
    target_id   BIGINT,
    payload     JSONB       NOT NULL DEFAULT '{}'::jsonb,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_audit_time ON audit_log (created_at DESC);

-- ---------- updated_at trigger ----------
CREATE OR REPLACE FUNCTION touch_updated_at() RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at := now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_players_touch ON players;
CREATE TRIGGER trg_players_touch
    BEFORE UPDATE ON players
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();
