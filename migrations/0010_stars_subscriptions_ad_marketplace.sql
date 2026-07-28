-- Telegram Stars subscriptions, collaborative funding, moderated ad marketplace.
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ad_free_until TIMESTAMPTZ;
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ads_delivered_today INTEGER NOT NULL DEFAULT 0;
ALTER TABLE groups ADD COLUMN IF NOT EXISTS ads_delivery_day DATE;

CREATE TABLE IF NOT EXISTS subscription_rounds (
 id BIGSERIAL PRIMARY KEY, group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE,
 target_stars INTEGER NOT NULL DEFAULT 10 CHECK(target_stars=10), collected_stars INTEGER NOT NULL DEFAULT 0 CHECK(collected_stars BETWEEN 0 AND 10),
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','completed','expired','cancelled')),
 expires_at TIMESTAMPTZ NOT NULL DEFAULT now()+interval '7 days', completed_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE UNIQUE INDEX IF NOT EXISTS uq_subscription_open_round ON subscription_rounds(group_id) WHERE status='open';
CREATE TABLE IF NOT EXISTS star_payments (
 id BIGSERIAL PRIMARY KEY, purpose TEXT NOT NULL CHECK(purpose IN ('subscription','advertisement')),
 reference_id BIGINT NOT NULL, payer_telegram_id BIGINT NOT NULL, stars INTEGER NOT NULL CHECK(stars>0),
 invoice_payload TEXT NOT NULL UNIQUE, telegram_charge_id TEXT UNIQUE, provider_charge_id TEXT,
 status TEXT NOT NULL DEFAULT 'invoiced' CHECK(status IN ('invoiced','paid','refunded','expired','cancelled')),
 expires_at TIMESTAMPTZ NOT NULL, paid_at TIMESTAMPTZ, refunded_at TIMESTAMPTZ, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_star_payment_lookup ON star_payments(invoice_payload,status);
CREATE TABLE IF NOT EXISTS group_subscription_events (
 id BIGSERIAL PRIMARY KEY, group_id BIGINT NOT NULL REFERENCES groups(id), source TEXT NOT NULL CHECK(source IN ('stars','treasury','admin')),
 stars INTEGER, treasury_toman BIGINT, starts_at TIMESTAMPTZ NOT NULL, ends_at TIMESTAMPTZ NOT NULL,
 actor_player_id BIGINT REFERENCES players(id), created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS ad_requests (
 id BIGSERIAL PRIMARY KEY, requester_player_id BIGINT NOT NULL REFERENCES players(id),
 package_code TEXT NOT NULL CHECK(package_code IN ('economy','standard','campaign','featured')),
 title TEXT NOT NULL CHECK(length(title) BETWEEN 3 AND 120), description TEXT NOT NULL CHECK(length(description) BETWEEN 10 AND 2000),
 target_url TEXT NOT NULL CHECK(length(target_url) BETWEEN 8 AND 1000), image_bytes BYTEA, image_mime TEXT,
 requested_start_at TIMESTAMPTZ, status TEXT NOT NULL DEFAULT 'pending_review' CHECK(status IN ('draft','pending_review','changes_requested','approved_unpaid','paid','active','paused','completed','rejected','cancelled','refunded','payment_expired')),
 price_stars INTEGER NOT NULL CHECK(price_stars IN (25,60,120,200)), impressions_planned INTEGER NOT NULL,
 campaign_hours INTEGER NOT NULL, priority INTEGER NOT NULL DEFAULT 0, admin_note TEXT, approved_by TEXT,
 approved_at TIMESTAMPTZ, payment_expires_at TIMESTAMPTZ, paid_at TIMESTAMPTZ, first_delivery_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(), updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_ad_requests_admin ON ad_requests(status,created_at DESC);
CREATE TABLE IF NOT EXISTS ad_deliveries (
 id BIGSERIAL PRIMARY KEY, ad_request_id BIGINT NOT NULL REFERENCES ad_requests(id) ON DELETE CASCADE,
 group_id BIGINT NOT NULL REFERENCES groups(id) ON DELETE CASCADE, slot_no INTEGER NOT NULL,
 scheduled_at TIMESTAMPTZ NOT NULL, status TEXT NOT NULL DEFAULT 'scheduled' CHECK(status IN ('scheduled','queued','sent','failed','cancelled')),
 outbox_key TEXT UNIQUE, sent_at TIMESTAMPTZ, error_code TEXT, created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(ad_request_id,group_id,slot_no)
);
CREATE INDEX IF NOT EXISTS idx_ad_delivery_due ON ad_deliveries(status,scheduled_at) WHERE status='scheduled';
