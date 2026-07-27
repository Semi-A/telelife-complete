-- Country identity, central-bank policy, macro indicators, shocks and national newspaper.
ALTER TABLE countries ADD COLUMN IF NOT EXISTS interest_rate_bp INTEGER NOT NULL DEFAULT 1200 CHECK(interest_rate_bp BETWEEN 0 AND 10000);
ALTER TABLE countries ADD COLUMN IF NOT EXISTS fx_reserve_cents BIGINT NOT NULL DEFAULT 0 CHECK(fx_reserve_cents>=0);
ALTER TABLE countries ADD COLUMN IF NOT EXISTS inflation_target_bp INTEGER NOT NULL DEFAULT 800 CHECK(inflation_target_bp BETWEEN 0 AND 5000);

CREATE TABLE IF NOT EXISTS country_indicator_daily (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 indicator_date DATE NOT NULL,
 inflation_bp INTEGER NOT NULL CHECK(inflation_bp BETWEEN -5000 AND 100000),
 unemployment_bp INTEGER NOT NULL CHECK(unemployment_bp BETWEEN 0 AND 10000),
 satisfaction INTEGER NOT NULL CHECK(satisfaction BETWEEN 0 AND 100),
 growth_bp INTEGER NOT NULL CHECK(growth_bp BETWEEN -10000 AND 10000),
 gdp_toman BIGINT NOT NULL CHECK(gdp_toman>=0),
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,indicator_date)
);
CREATE TABLE IF NOT EXISTS country_shocks (
 id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 shock_code TEXT NOT NULL CHECK(shock_code IN ('sanctions','drought','export_boom')),
 title TEXT NOT NULL,
 effects JSONB NOT NULL DEFAULT '{}'::jsonb,
 starts_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 ends_at TIMESTAMPTZ NOT NULL,
 announced_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 UNIQUE(country_id,shock_code,starts_at)
);
CREATE INDEX IF NOT EXISTS idx_country_shocks_active ON country_shocks(country_id,ends_at) WHERE announced_at IS NOT NULL;
CREATE TABLE IF NOT EXISTS country_newspapers (
 country_id BIGINT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
 issue_date DATE NOT NULL,
 headline TEXT NOT NULL,
 body TEXT NOT NULL,
 indicators JSONB NOT NULL DEFAULT '{}'::jsonb,
 shock_id BIGINT REFERENCES country_shocks(id) ON DELETE SET NULL,
 published_at TIMESTAMPTZ,
 created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
 PRIMARY KEY(country_id,issue_date)
);
