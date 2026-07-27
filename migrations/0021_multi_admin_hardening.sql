-- Database-backed admin accounts and reliable incident lifecycle.
ALTER TABLE admin_identities ADD COLUMN IF NOT EXISTS password_hash TEXT;
ALTER TABLE admin_identities ADD COLUMN IF NOT EXISTS created_by TEXT;
ALTER TABLE admin_identities ADD COLUMN IF NOT EXISTS last_login_at TIMESTAMPTZ;
ALTER TABLE admin_identities ADD COLUMN IF NOT EXISTS disabled_at TIMESTAMPTZ;

CREATE INDEX IF NOT EXISTS idx_admin_identities_enabled_role
    ON admin_identities(role, username) WHERE enabled;

-- Existing rows created by the earlier RBAC migration have no credential and
-- intentionally remain unable to authenticate until a superadmin sets one.
ALTER TABLE admin_identities DROP CONSTRAINT IF EXISTS admin_identity_password_shape;
ALTER TABLE admin_identities ADD CONSTRAINT admin_identity_password_shape
    CHECK (password_hash IS NULL OR password_hash LIKE 'pbkdf2_sha256$%');