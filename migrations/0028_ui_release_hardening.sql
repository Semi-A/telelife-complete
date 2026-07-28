-- 0028 — UI release hardening.
-- Additive and idempotent only: index creation, nothing destructive.
-- Every statement is safe to re-run on a database that already has 0001..0027.

-- The rebuilt TeleLife panel reads the active citizenship on nearly every page
-- render. player_id is the primary key, but the active-row predicate is what
-- the planner actually filters on, so give it a partial index.
CREATE INDEX IF NOT EXISTS idx_citizenships_active_player
    ON citizenships (player_id)
    WHERE is_active;

-- Country page lists candidate destinations ordered by citizen count.
CREATE INDEX IF NOT EXISTS idx_citizenships_active_country
    ON citizenships (country_id)
    WHERE is_active;

-- The home panel resolves onboarding step and the live message on each tap.
CREATE INDEX IF NOT EXISTS idx_player_ui_state_player
    ON player_ui_state (player_id);

-- Migration status banner on the country page.
CREATE INDEX IF NOT EXISTS idx_migration_requests_player_pending
    ON migration_requests (player_id, expires_at)
    WHERE status = 'pending';
