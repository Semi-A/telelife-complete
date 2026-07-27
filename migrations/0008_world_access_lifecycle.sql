-- TeleWorld group lifecycle, permission gate and deduplicated product audit.
CREATE TABLE IF NOT EXISTS world_group_access (
    chat_id BIGINT PRIMARY KEY,
    chat_title TEXT NOT NULL DEFAULT '',
    membership_status TEXT NOT NULL DEFAULT 'unknown',
    is_active BOOLEAN NOT NULL DEFAULT FALSE,
    welcomed_at TIMESTAMPTZ,
    welcome_message_id BIGINT,
    status_message_id BIGINT,
    is_administrator BOOLEAN NOT NULL DEFAULT FALSE,
    can_delete_messages BOOLEAN NOT NULL DEFAULT FALSE,
    missing_permissions TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
    last_checked_at TIMESTAMPTZ,
    last_warning_at TIMESTAMPTZ,
    last_warning_fingerprint TEXT,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_world_group_access_active
    ON world_group_access (is_active, updated_at DESC);

CREATE TABLE IF NOT EXISTS product_audit_log (
    id BIGSERIAL PRIMARY KEY,
    event_key TEXT NOT NULL UNIQUE,
    event_type TEXT NOT NULL,
    chat_id BIGINT,
    player_id BIGINT REFERENCES players(id) ON DELETE SET NULL,
    country_id BIGINT REFERENCES countries(id) ON DELETE SET NULL,
    details JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_product_audit_time
    ON product_audit_log (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_product_audit_chat_time
    ON product_audit_log (chat_id, created_at DESC);
