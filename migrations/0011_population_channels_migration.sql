-- Population-priced subscriptions, channel-specific ads and controlled migration.
ALTER TABLE subscription_rounds DROP CONSTRAINT IF EXISTS subscription_rounds_target_stars_check;
ALTER TABLE subscription_rounds ADD CONSTRAINT subscription_rounds_target_stars_check CHECK(target_stars IN (10,15,30,50,75));
ALTER TABLE ad_requests ADD COLUMN IF NOT EXISTS channel TEXT NOT NULL DEFAULT 'world' CHECK(channel IN ('life','world','both'));
ALTER TABLE ad_deliveries ADD COLUMN IF NOT EXISTS destination_type TEXT NOT NULL DEFAULT 'world' CHECK(destination_type IN ('life','world'));
ALTER TABLE ad_deliveries ADD COLUMN IF NOT EXISTS destination_telegram_id BIGINT;
ALTER TABLE ad_deliveries ALTER COLUMN group_id DROP NOT NULL;
ALTER TABLE ad_deliveries DROP CONSTRAINT IF EXISTS ad_deliveries_ad_request_id_group_id_slot_no_key;
CREATE UNIQUE INDEX IF NOT EXISTS uq_ad_delivery_destination ON ad_deliveries(ad_request_id,destination_type,destination_telegram_id,slot_no);
DROP INDEX IF EXISTS idx_ad_delivery_due;
CREATE INDEX IF NOT EXISTS idx_ad_delivery_due ON ad_deliveries(status,scheduled_at,destination_type) WHERE status='scheduled';

ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS migrant_until TIMESTAMPTZ;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS political_hold_until TIMESTAMPTZ;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS last_migrated_at TIMESTAMPTZ;
CREATE TABLE IF NOT EXISTS migration_requests (
 id BIGSERIAL PRIMARY KEY, player_id BIGINT NOT NULL REFERENCES players(id),
 origin_country_id BIGINT NOT NULL REFERENCES countries(id), destination_country_id BIGINT NOT NULL REFERENCES countries(id),
 exit_fee_toman BIGINT NOT NULL CHECK(exit_fee_toman BETWEEN 500000 AND 50000000),
 status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending','approved','rejected','expired','cancelled')),
 reviewed_by_player_id BIGINT REFERENCES players(id), review_note TEXT,
 expires_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '72 hours', created_at TIMESTAMPTZ NOT NULL DEFAULT now(), resolved_at TIMESTAMPTZ,
 CHECK(origin_country_id<>destination_country_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_migration_pending ON migration_requests(player_id) WHERE status='pending';
CREATE INDEX IF NOT EXISTS idx_migration_destination_pending ON migration_requests(destination_country_id,expires_at) WHERE status='pending';