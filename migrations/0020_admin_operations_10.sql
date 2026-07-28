-- Persistent incidents, backend previews, RBAC identities and reversible operations.
CREATE TABLE IF NOT EXISTS admin_identities (
 username TEXT PRIMARY KEY,
 role TEXT NOT NULL CHECK(role IN ('viewer','support','content','economy','operator','superadmin')),
 enabled BOOLEAN NOT NULL DEFAULT TRUE,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS admin_action_previews (
 token_hash TEXT PRIMARY KEY,
 admin_actor TEXT NOT NULL,
 method TEXT NOT NULL,
 path TEXT NOT NULL,
 payload_hash TEXT NOT NULL,
 expires_at TIMESTAMPTZ NOT NULL,
 used_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_admin_preview_expiry ON admin_action_previews(expires_at) WHERE used_at IS NULL;
CREATE TABLE IF NOT EXISTS admin_incidents (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 fingerprint TEXT NOT NULL UNIQUE,
 severity TEXT NOT NULL CHECK(severity IN ('critical','warning','info')),
 domain TEXT NOT NULL,
 title TEXT NOT NULL,
 detail TEXT NOT NULL,
 action_view TEXT NOT NULL,
 status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open','acknowledged','investigating','resolved')),
 assigned_to TEXT,
 first_seen_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 last_seen_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 acknowledged_at TIMESTAMPTZ,
 resolved_at TIMESTAMPTZ,
 resolution_note TEXT,
 occurrences BIGINT NOT NULL DEFAULT 1 CHECK(occurrences > 0),
 metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);
CREATE INDEX IF NOT EXISTS idx_admin_incidents_queue ON admin_incidents(status,severity,last_seen_at DESC);
CREATE TABLE IF NOT EXISTS admin_reversible_actions (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 admin_actor TEXT NOT NULL,
 action_type TEXT NOT NULL,
 target_key TEXT NOT NULL,
 inverse_payload JSONB NOT NULL,
 source_request_id TEXT NOT NULL UNIQUE,
 expires_at TIMESTAMPTZ NOT NULL,
 undone_at TIMESTAMPTZ,
 undone_by TEXT,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_admin_undo_available ON admin_reversible_actions(expires_at) WHERE undone_at IS NULL;
