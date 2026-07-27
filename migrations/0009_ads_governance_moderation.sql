-- Advertising campaigns and governance controls.
CREATE TABLE IF NOT EXISTS ad_campaigns (
 id BIGSERIAL PRIMARY KEY,
 title TEXT NOT NULL CHECK(length(title) BETWEEN 3 AND 120),
 body TEXT NOT NULL CHECK(length(body) BETWEEN 3 AND 4000),
 destination_chat_id BIGINT NOT NULL,
 status TEXT NOT NULL DEFAULT 'draft' CHECK(status IN ('draft','scheduled','queued','cancelled')),
 scheduled_at TIMESTAMPTZ,
 repeat_minutes INTEGER CHECK(repeat_minutes IS NULL OR repeat_minutes >= 15),
 last_queued_at TIMESTAMPTZ,
 created_by TEXT NOT NULL,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_ad_campaign_due ON ad_campaigns(status,scheduled_at) WHERE status='scheduled';
