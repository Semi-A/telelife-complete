-- TeleLife action-based skill and useful personal-asset progression.
CREATE TABLE IF NOT EXISTS player_skills (
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 skill_code TEXT NOT NULL CHECK (length(skill_code) BETWEEN 1 AND 32),
 level INTEGER NOT NULL DEFAULT 1 CHECK (level BETWEEN 1 AND 20),
 xp INTEGER NOT NULL DEFAULT 0 CHECK (xp >= 0),
 total_xp BIGINT NOT NULL DEFAULT 0 CHECK (total_xp >= 0),
 actions_count BIGINT NOT NULL DEFAULT 0 CHECK (actions_count >= 0),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(player_id,skill_code)
);
CREATE TABLE IF NOT EXISTS skill_events (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 idempotency_key TEXT NOT NULL UNIQUE,
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 skill_code TEXT NOT NULL,
 amount INTEGER NOT NULL CHECK (amount >= 0),
 level_after INTEGER NOT NULL CHECK (level_after >= 1),
 source TEXT NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_skill_events_player_time ON skill_events(player_id,created_at DESC);
CREATE TABLE IF NOT EXISTS player_assets (
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 asset_code TEXT NOT NULL CHECK (length(asset_code) BETWEEN 1 AND 40),
 acquired_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 purchase_price_toman BIGINT NOT NULL CHECK (purchase_price_toman >= 0),
 PRIMARY KEY(player_id,asset_code)
);
CREATE INDEX IF NOT EXISTS idx_player_assets_player ON player_assets(player_id,acquired_at DESC);
