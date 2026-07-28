-- Production integrity hardening. Forward-only; do not edit migrations 0001..0026.

-- Allow a durable refund claim before the external Telegram call.
ALTER TABLE ad_requests DROP CONSTRAINT IF EXISTS ad_requests_status_check;
ALTER TABLE ad_requests ADD CONSTRAINT ad_requests_status_check CHECK (
 status IN ('draft','pending_review','changes_requested','approved_unpaid','paid','active',
            'paused','completed','rejected','cancelled','refund_pending','refunded','payment_expired')
);
ALTER TABLE ad_requests
 ADD COLUMN IF NOT EXISTS refund_previous_status TEXT,
 ADD COLUMN IF NOT EXISTS refund_requested_at TIMESTAMPTZ,
 ADD COLUMN IF NOT EXISTS refund_requested_by TEXT;

-- Keep only the newest unpaid invoice per advertisement, then enforce the rule.
WITH ranked AS (
 SELECT id, row_number() OVER (PARTITION BY reference_id ORDER BY created_at DESC,id DESC) AS rn
 FROM star_payments
 WHERE purpose='advertisement' AND status='invoiced'
)
UPDATE star_payments SET status='cancelled'
WHERE id IN (SELECT id FROM ranked WHERE rn>1);
CREATE UNIQUE INDEX IF NOT EXISTS uq_open_advertisement_invoice
 ON star_payments(reference_id)
 WHERE purpose='advertisement' AND status='invoiced';

-- Persistent, bounded authentication throttling for the HTTP Basic admin entrypoint.
CREATE TABLE IF NOT EXISTS admin_auth_throttle (
 throttle_key TEXT PRIMARY KEY,
 failures INTEGER NOT NULL DEFAULT 0 CHECK(failures>=0),
 first_failed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 blocked_until TIMESTAMPTZ,
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_admin_auth_throttle_cleanup
 ON admin_auth_throttle(updated_at);


-- A delivery is claimed before the external Telegram call. Refunds cannot race a claimed send.
ALTER TABLE ad_deliveries DROP CONSTRAINT IF EXISTS ad_deliveries_status_check;
ALTER TABLE ad_deliveries ADD CONSTRAINT ad_deliveries_status_check CHECK (
 status IN ('scheduled','queued','sending','sent','failed','cancelled')
);

-- Old open subscription invoices did not reserve the round's remaining capacity.
-- Invalidate them once; users can request a fresh, correctly bounded invoice.
UPDATE star_payments SET status='cancelled'
WHERE purpose='subscription' AND status='invoiced';
