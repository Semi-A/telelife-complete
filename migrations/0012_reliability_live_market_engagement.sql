-- Reliability, live market provenance, and group engagement. Additive and rollback-safe.
DO $$
DECLARE constraint_name text;
BEGIN
  SELECT c.conname INTO constraint_name
  FROM pg_constraint c
  WHERE c.conrelid='ad_requests'::regclass AND c.contype='c'
    AND pg_get_constraintdef(c.oid) ILIKE '%price_stars%';
  IF constraint_name IS NOT NULL THEN
    EXECUTE format('ALTER TABLE ad_requests DROP CONSTRAINT %I', constraint_name);
  END IF;
END $$;
ALTER TABLE ad_requests ADD CONSTRAINT ad_requests_price_stars_check
  CHECK (price_stars BETWEEN 1 AND 10000) NOT VALID;
ALTER TABLE ad_requests VALIDATE CONSTRAINT ad_requests_price_stars_check;


-- 0010 used a fixed 10-star round, while application pricing scales to 75 stars.
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_collected_stars_check;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_target_stars_check
  CHECK(target_stars BETWEEN 1 AND 1000) NOT VALID;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_collected_stars_check
  CHECK(collected_stars BETWEEN 0 AND target_stars) NOT VALID;
ALTER TABLE subscription_rounds VALIDATE CONSTRAINT subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds VALIDATE CONSTRAINT subscription_rounds_collected_stars_check;

ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source TEXT NOT NULL DEFAULT 'internal';
ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source_checked_at TIMESTAMPTZ;
ALTER TABLE market_prices ADD COLUMN IF NOT EXISTS source_error TEXT;

CREATE TABLE IF NOT EXISTS scheduler_job_runs (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 job_name TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN ('running','succeeded','failed')),
 started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 finished_at TIMESTAMPTZ,
 duration_ms INTEGER,
 result JSONB NOT NULL DEFAULT '{}'::jsonb,
 error_type TEXT,
 error_message TEXT
);
CREATE INDEX IF NOT EXISTS idx_scheduler_job_runs_name_time
 ON scheduler_job_runs(job_name,started_at DESC);

CREATE TABLE IF NOT EXISTS group_engagement_state (
 group_id BIGINT PRIMARY KEY REFERENCES groups(id) ON DELETE CASCADE,
 streak INTEGER NOT NULL DEFAULT 0 CHECK(streak>=0),
 best_streak INTEGER NOT NULL DEFAULT 0 CHECK(best_streak>=0),
 last_active_date DATE,
 last_digest_date DATE,
 last_event_at TIMESTAMPTZ,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS group_live_events (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
 event_code TEXT NOT NULL,
 title TEXT NOT NULL,
 payload JSONB NOT NULL DEFAULT '{}'::jsonb,
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','resolved','expired')),
 starts_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 ends_at TIMESTAMPTZ NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_group_open_event
 ON group_live_events(group_id) WHERE status='open';