-- ============================================================
-- Phase 2 | Identity & Progression
-- Daily rewards, streaks, missions, unlocks, XP events.
-- ============================================================

-- ---------- daily claim state (one row per player) ----------
CREATE TABLE IF NOT EXISTS daily_state (
    player_id        BIGINT      PRIMARY KEY REFERENCES players(id) ON DELETE CASCADE,
    streak           INTEGER     NOT NULL DEFAULT 0 CHECK (streak >= 0),
    best_streak      INTEGER     NOT NULL DEFAULT 0 CHECK (best_streak >= 0),
    last_claim_date  DATE,
    total_claims     INTEGER     NOT NULL DEFAULT 0 CHECK (total_claims >= 0),
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ---------- daily missions ----------
-- One row per player per mission per day. The PK makes progress writes
-- idempotent and lets the daily reset be a single ranged DELETE.
CREATE TABLE IF NOT EXISTS daily_missions (
    player_id     BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    mission_date  DATE        NOT NULL,
    mission_key   TEXT        NOT NULL,
    progress      INTEGER     NOT NULL DEFAULT 0 CHECK (progress >= 0),
    target        INTEGER     NOT NULL CHECK (target > 0),
    claimed_at    TIMESTAMPTZ,
    PRIMARY KEY (player_id, mission_date, mission_key)
);

CREATE INDEX IF NOT EXISTS idx_missions_date ON daily_missions (mission_date);
CREATE INDEX IF NOT EXISTS idx_missions_open
    ON daily_missions (player_id, mission_date)
    WHERE claimed_at IS NULL;

-- ---------- unlocks earned by the player ----------
CREATE TABLE IF NOT EXISTS player_unlocks (
    player_id    BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    unlock_key   TEXT        NOT NULL,
    unlocked_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (player_id, unlock_key)
);

-- ---------- xp audit trail ----------
-- Mirrors the ledger philosophy: XP is currency, so it gets the same
-- idempotency guarantee. This is what makes anti-farming enforceable.
CREATE TABLE IF NOT EXISTS xp_events (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id        BIGINT      NOT NULL REFERENCES players(id) ON DELETE CASCADE,
    idempotency_key  TEXT        NOT NULL,
    source           TEXT        NOT NULL,
    amount           INTEGER     NOT NULL,
    level_after      INTEGER     NOT NULL,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX IF NOT EXISTS uq_xp_idempotency ON xp_events (idempotency_key);
CREATE INDEX IF NOT EXISTS idx_xp_player_time ON xp_events (player_id, created_at DESC);

-- Daily XP ceiling per player is enforced by this covering index.
CREATE INDEX IF NOT EXISTS idx_xp_daily_cap
    ON xp_events (player_id, created_at) INCLUDE (amount);

DROP TRIGGER IF EXISTS trg_daily_state_touch ON daily_state;
CREATE TRIGGER trg_daily_state_touch
    BEFORE UPDATE ON daily_state
    FOR EACH ROW EXECUTE FUNCTION touch_updated_at();
