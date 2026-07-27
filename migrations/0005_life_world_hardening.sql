-- TeleLife/TeleWorld hardening: country lifecycle, membership validity and election safety.
ALTER TABLE countries ADD COLUMN IF NOT EXISTS status TEXT;
ALTER TABLE countries ADD COLUMN IF NOT EXISTS temporary_at TIMESTAMPTZ;
ALTER TABLE countries ADD COLUMN IF NOT EXISTS official_at TIMESTAMPTZ;
UPDATE countries SET status = 'temporary', temporary_at = COALESCE(temporary_at, created_at)
WHERE status IS NULL;
ALTER TABLE countries ALTER COLUMN status SET DEFAULT 'forming';
ALTER TABLE countries ALTER COLUMN status SET NOT NULL;
ALTER TABLE countries DROP CONSTRAINT IF EXISTS countries_status_check;
ALTER TABLE countries ADD CONSTRAINT countries_status_check
    CHECK (status IN ('forming','temporary','official'));

ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE;
ALTER TABLE citizenships ADD COLUMN IF NOT EXISTS left_at TIMESTAMPTZ;
CREATE INDEX IF NOT EXISTS idx_citizenships_active_country
    ON citizenships(country_id, joined_at) WHERE is_active;

-- Existing primary-key semantics retain one-country-per-player. Only active rows count.
CREATE UNIQUE INDEX IF NOT EXISTS uq_elections_one_open_country
    ON elections(country_id) WHERE status IN ('nominations','voting');

-- A president must be an active citizen of the country. The trigger protects admin
-- tools and future writers in addition to the service layer.
CREATE OR REPLACE FUNCTION validate_country_president() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.president_player_id IS NOT NULL AND NOT EXISTS (
        SELECT 1 FROM citizenships cs
        WHERE cs.player_id = NEW.president_player_id
          AND cs.country_id = NEW.id AND cs.is_active
    ) THEN
        RAISE EXCEPTION 'president_must_be_active_citizen';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS trg_validate_country_president ON countries;
CREATE CONSTRAINT TRIGGER trg_validate_country_president
    AFTER INSERT OR UPDATE OF president_player_id ON countries
    DEFERRABLE INITIALLY DEFERRED
    FOR EACH ROW EXECUTE FUNCTION validate_country_president();