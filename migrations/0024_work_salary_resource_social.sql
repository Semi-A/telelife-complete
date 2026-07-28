-- Cash wages for resource jobs and auditable citizen resource transfers.
ALTER TABLE work_claims ADD COLUMN IF NOT EXISTS salary_gross_toman BIGINT NOT NULL DEFAULT 0 CHECK(salary_gross_toman>=0);
ALTER TABLE work_claims ADD COLUMN IF NOT EXISTS salary_net_toman BIGINT NOT NULL DEFAULT 0 CHECK(salary_net_toman>=0);

CREATE TABLE IF NOT EXISTS citizen_resource_transfers (
 id BIGSERIAL PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 actor_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 recipient_id BIGINT REFERENCES players(id) ON DELETE RESTRICT,
 transfer_type TEXT NOT NULL CHECK(transfer_type IN ('gift','country_donation')),
 asset_code TEXT NOT NULL CHECK(asset_code IN ('food','minerals','technology','energy')),
 amount BIGINT NOT NULL CHECK(amount>0),
 reputation_awarded INT NOT NULL DEFAULT 0 CHECK(reputation_awarded BETWEEN 0 AND 3),
 idempotency_key TEXT NOT NULL UNIQUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 CHECK((transfer_type='gift' AND recipient_id IS NOT NULL AND recipient_id<>actor_id)
    OR (transfer_type='country_donation' AND recipient_id IS NULL))
);
CREATE INDEX IF NOT EXISTS idx_resource_transfer_actor_day ON citizen_resource_transfers(actor_id,created_at DESC);
CREATE INDEX IF NOT EXISTS idx_resource_transfer_country_time ON citizen_resource_transfers(country_id,created_at DESC);

CREATE TABLE IF NOT EXISTS player_resource_sales (
 id BIGSERIAL PRIMARY KEY,
 player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
 asset_code TEXT NOT NULL CHECK(asset_code IN ('food','minerals','technology','energy')),
 amount BIGINT NOT NULL CHECK(amount>0),
 unit_price_toman BIGINT NOT NULL CHECK(unit_price_toman>0),
 gross_toman BIGINT NOT NULL CHECK(gross_toman>0),
 fee_toman BIGINT NOT NULL CHECK(fee_toman>=0),
 net_toman BIGINT NOT NULL CHECK(net_toman>0),
 idempotency_key TEXT NOT NULL UNIQUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_resource_sales_player_day ON player_resource_sales(player_id,created_at DESC);
