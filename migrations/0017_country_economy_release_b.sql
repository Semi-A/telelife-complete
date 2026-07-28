-- Release B: bounded country consumption, budgets, satisfaction, crises and offices.
-- Additive/forward-only; no existing data is removed.

CREATE TABLE IF NOT EXISTS country_budget_allocations (
 country_id BIGINT PRIMARY KEY REFERENCES countries(id) ON DELETE CASCADE,
 welfare_bp INTEGER NOT NULL DEFAULT 2000 CHECK(welfare_bp BETWEEN 0 AND 10000),
 production_bp INTEGER NOT NULL DEFAULT 2500 CHECK(production_bp BETWEEN 0 AND 10000),
 technology_bp INTEGER NOT NULL DEFAULT 1500 CHECK(technology_bp BETWEEN 0 AND 10000),
 defense_bp INTEGER NOT NULL DEFAULT 1000 CHECK(defense_bp BETWEEN 0 AND 10000),
 intelligence_bp INTEGER NOT NULL DEFAULT 500 CHECK(intelligence_bp BETWEEN 0 AND 10000),
 diplomacy_bp INTEGER NOT NULL DEFAULT 500 CHECK(diplomacy_bp BETWEEN 0 AND 10000),
 emergency_bp INTEGER NOT NULL DEFAULT 2000 CHECK(emergency_bp BETWEEN 0 AND 10000),
 version BIGINT NOT NULL DEFAULT 1,
 updated_by_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK(welfare_bp+production_bp+technology_bp+defense_bp+intelligence_bp+diplomacy_bp+emergency_bp=10000)
);
INSERT INTO country_budget_allocations(country_id)
SELECT id FROM countries ON CONFLICT(country_id) DO NOTHING;

CREATE TABLE IF NOT EXISTS country_economy_state (
 country_id BIGINT PRIMARY KEY REFERENCES countries(id) ON DELETE CASCADE,
 satisfaction INTEGER NOT NULL DEFAULT 70 CHECK(satisfaction BETWEEN 0 AND 100),
 food_shortage_bp INTEGER NOT NULL DEFAULT 0 CHECK(food_shortage_bp BETWEEN 0 AND 10000),
 energy_shortage_bp INTEGER NOT NULL DEFAULT 0 CHECK(energy_shortage_bp BETWEEN 0 AND 10000),
 production_modifier_bp INTEGER NOT NULL DEFAULT 10000 CHECK(production_modifier_bp BETWEEN 5000 AND 15000),
 welfare_level INTEGER NOT NULL DEFAULT 50 CHECK(welfare_level BETWEEN 0 AND 100),
 defense_readiness INTEGER NOT NULL DEFAULT 20 CHECK(defense_readiness BETWEEN 0 AND 100),
 last_settled_date DATE,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO country_economy_state(country_id)
SELECT id FROM countries ON CONFLICT(country_id) DO NOTHING;

CREATE TABLE IF NOT EXISTS country_resource_daily (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 economy_date DATE NOT NULL,
 citizens INTEGER NOT NULL CHECK(citizens>=0),
 food_needed BIGINT NOT NULL CHECK(food_needed>=0),
 food_consumed BIGINT NOT NULL CHECK(food_consumed>=0),
 energy_needed BIGINT NOT NULL CHECK(energy_needed>=0),
 energy_consumed BIGINT NOT NULL CHECK(energy_consumed>=0),
 budget_spent_toman BIGINT NOT NULL CHECK(budget_spent_toman>=0),
 satisfaction_before INTEGER NOT NULL CHECK(satisfaction_before BETWEEN 0 AND 100),
 satisfaction_after INTEGER NOT NULL CHECK(satisfaction_after BETWEEN 0 AND 100),
 production_modifier_bp INTEGER NOT NULL,
 ledger_key TEXT NOT NULL UNIQUE,
 details JSONB NOT NULL DEFAULT '{}'::jsonb,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,economy_date)
);
CREATE INDEX IF NOT EXISTS idx_country_resource_daily_date ON country_resource_daily(economy_date DESC,country_id);

CREATE TABLE IF NOT EXISTS country_crises (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 crisis_code TEXT NOT NULL CHECK(crisis_code IN ('food_shortage','energy_shortage','treasury_stress')),
 status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active','resolved')),
 severity INTEGER NOT NULL CHECK(severity BETWEEN 1 AND 100),
 started_on DATE NOT NULL,
 resolved_on DATE,
 details JSONB NOT NULL DEFAULT '{}'::jsonb,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_country_crisis_active ON country_crises(country_id,crisis_code) WHERE status='active';
CREATE INDEX IF NOT EXISTS idx_country_crises_status ON country_crises(status,country_id,started_on DESC);

CREATE TABLE IF NOT EXISTS country_offices (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 role_code TEXT NOT NULL CHECK(role_code IN ('economy_minister','industry_minister','foreign_minister','army_commander','intelligence_chief')),
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 appointed_by_player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 appointed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,role_code),
 UNIQUE(country_id,player_id)
);

CREATE TABLE IF NOT EXISTS country_governance_audit (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 actor_player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
 action_code TEXT NOT NULL,
 idempotency_key TEXT NOT NULL UNIQUE,
 payload JSONB NOT NULL DEFAULT '{}'::jsonb,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_country_governance_audit_country ON country_governance_audit(country_id,created_at DESC);
