-- Purposeful work loop: level-one jobs, shift choices, tax and national output.
-- Additive and safe for existing player_jobs rows.
ALTER TABLE player_jobs ADD COLUMN IF NOT EXISTS shift_mode TEXT NOT NULL DEFAULT 'balanced';
ALTER TABLE player_jobs ADD COLUMN IF NOT EXISTS last_claim_at TIMESTAMPTZ;
ALTER TABLE player_jobs ADD COLUMN IF NOT EXISTS total_claims BIGINT NOT NULL DEFAULT 0;
ALTER TABLE player_jobs ADD COLUMN IF NOT EXISTS total_tax_toman BIGINT NOT NULL DEFAULT 0;
ALTER TABLE player_jobs ADD COLUMN IF NOT EXISTS total_country_output BIGINT NOT NULL DEFAULT 0;

ALTER TABLE player_jobs DROP CONSTRAINT IF EXISTS player_jobs_shift_mode_check;
ALTER TABLE player_jobs ADD CONSTRAINT player_jobs_shift_mode_check
  CHECK (shift_mode IN ('safe','balanced','national','private'));

CREATE TABLE IF NOT EXISTS work_claims (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 idempotency_key TEXT NOT NULL UNIQUE,
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 country_id BIGINT REFERENCES countries(id) ON DELETE SET NULL,
 job_code TEXT NOT NULL,
 shift_mode TEXT NOT NULL CHECK (shift_mode IN ('safe','balanced','national','private')),
 asset_code TEXT NOT NULL,
 gross_amount BIGINT NOT NULL CHECK (gross_amount > 0),
 player_amount BIGINT NOT NULL CHECK (player_amount >= 0),
 country_amount BIGINT NOT NULL DEFAULT 0 CHECK (country_amount >= 0),
 tax_toman BIGINT NOT NULL DEFAULT 0 CHECK (tax_toman >= 0),
 xp_awarded INTEGER NOT NULL DEFAULT 0 CHECK (xp_awarded >= 0),
 claimed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_work_claims_player_time ON work_claims(player_id,claimed_at DESC);
CREATE INDEX IF NOT EXISTS idx_work_claims_country_time ON work_claims(country_id,claimed_at DESC) WHERE country_id IS NOT NULL;
