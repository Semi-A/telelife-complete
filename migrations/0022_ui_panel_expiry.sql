-- Persist panel expiry so stale callbacks remain invalid after restart/replicas.
ALTER TABLE player_ui_state ADD COLUMN IF NOT EXISTS life_expires_at TIMESTAMPTZ;
ALTER TABLE world_ui_state ADD COLUMN IF NOT EXISTS expires_at TIMESTAMPTZ;
CREATE INDEX IF NOT EXISTS idx_player_ui_expiry ON player_ui_state(life_expires_at);
CREATE INDEX IF NOT EXISTS idx_world_ui_expiry ON world_ui_state(expires_at);