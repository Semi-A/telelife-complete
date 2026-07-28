-- Multiple useful national projects, treasury funding and durable completion effects.
CREATE TABLE IF NOT EXISTS country_project_funding (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 project_id BIGINT NOT NULL REFERENCES national_projects(id) ON DELETE RESTRICT,
 actor_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 asset_code TEXT NOT NULL,
 amount BIGINT NOT NULL CHECK(amount>0),
 idempotency_key TEXT NOT NULL UNIQUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_country_project_funding_project ON country_project_funding(project_id,created_at DESC);

CREATE TABLE IF NOT EXISTS national_project_effects (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE RESTRICT,
 project_id BIGINT NOT NULL UNIQUE REFERENCES national_projects(id) ON DELETE RESTRICT,
 effect_code TEXT NOT NULL,
 asset_code TEXT,
 magnitude_basis_points INTEGER NOT NULL CHECK(magnitude_basis_points BETWEEN 1 AND 10000),
 activated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_national_project_effects_country ON national_project_effects(country_id,effect_code,asset_code);
