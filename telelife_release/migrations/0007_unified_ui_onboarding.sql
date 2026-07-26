-- Persistent single-panel navigation and an actionable new-player journey.
CREATE TABLE IF NOT EXISTS player_ui_state (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE CASCADE,
    life_chat_id BIGINT,
    life_message_id BIGINT,
    onboarding_step SMALLINT NOT NULL DEFAULT 0 CHECK (onboarding_step BETWEEN 0 AND 4),
    onboarding_completed_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS world_ui_state (
    chat_id BIGINT PRIMARY KEY,
    message_id BIGINT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
