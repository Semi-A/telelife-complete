-- Free-tier operational hardening. Additive, idempotent and safe for live data.

-- Keep only one useful row per Telegram/provider charge and speed reconciliation.
CREATE UNIQUE INDEX IF NOT EXISTS uq_star_payments_provider_charge
    ON star_payments(provider_charge_id)
    WHERE provider_charge_id IS NOT NULL AND provider_charge_id <> '';
CREATE INDEX IF NOT EXISTS idx_star_payments_reconcile
    ON star_payments(status, created_at DESC);

-- Queue admin-to-user Telegram actions transactionally instead of performing
-- remote calls inside the HTTP request.
CREATE TABLE IF NOT EXISTS telegram_action_outbox (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    idempotency_key TEXT NOT NULL UNIQUE,
    bot_name TEXT NOT NULL CHECK (bot_name IN ('telelife','teleworld')),
    action TEXT NOT NULL CHECK (action IN ('send_message','send_invoice')),
    chat_id BIGINT NOT NULL,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb,
    attempts INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    available_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    processing_token UUID,
    processing_until TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    last_error_code TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (jsonb_typeof(payload) = 'object')
);
CREATE INDEX IF NOT EXISTS idx_telegram_action_outbox_claim
    ON telegram_action_outbox(available_at, created_at)
    WHERE completed_at IS NULL;

-- Cheap operational queries on the existing scheduler table.
CREATE INDEX IF NOT EXISTS idx_scheduler_job_runs_status_time
    ON scheduler_job_runs(status, started_at DESC);

-- Prevent unbounded growth on free PostgreSQL plans. Cleanup is performed by
-- the existing minute scheduler and keeps recent operational history.
