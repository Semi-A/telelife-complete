-- Phase 3: personal economy, housing and living costs.
CREATE TABLE IF NOT EXISTS player_housing (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    housing_code TEXT NOT NULL,
    tenure TEXT NOT NULL CHECK (tenure IN ('rent','owned')),
    rent_paid_until DATE,
    purchased_at TIMESTAMPTZ,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(housing_code) BETWEEN 1 AND 32)
);

CREATE TABLE IF NOT EXISTS player_life_economy (
    player_id BIGINT PRIMARY KEY REFERENCES players(id) ON DELETE RESTRICT,
    last_living_charge_date DATE,
    total_living_paid BIGINT NOT NULL DEFAULT 0 CHECK (total_living_paid >= 0),
    missed_living_days INTEGER NOT NULL DEFAULT 0 CHECK (missed_living_days >= 0),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Phase 4: auditable USD market state and per-player daily limits.
CREATE TABLE IF NOT EXISTS usd_market_state (
    singleton BOOLEAN PRIMARY KEY DEFAULT TRUE CHECK (singleton),
    reference_price_toman BIGINT NOT NULL CHECK (reference_price_toman > 0),
    open_price_toman BIGINT NOT NULL CHECK (open_price_toman > 0),
    net_flow_cents BIGINT NOT NULL DEFAULT 0,
    volume_cents BIGINT NOT NULL DEFAULT 0 CHECK (volume_cents >= 0),
    health SMALLINT NOT NULL DEFAULT 100 CHECK (health BETWEEN 0 AND 100),
    market_date DATE NOT NULL DEFAULT current_date,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
INSERT INTO usd_market_state(singleton,reference_price_toman,open_price_toman)
SELECT TRUE,current_price_toman,current_price_toman FROM market_prices WHERE asset_code='USD'
ON CONFLICT(singleton) DO NOTHING;

CREATE TABLE IF NOT EXISTS usd_trades (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    idempotency_key TEXT NOT NULL UNIQUE,
    side TEXT NOT NULL CHECK (side IN ('buy','sell')),
    usd_cents BIGINT NOT NULL CHECK (usd_cents > 0),
    gross_toman BIGINT NOT NULL CHECK (gross_toman > 0),
    fee_toman BIGINT NOT NULL CHECK (fee_toman >= 0),
    price_toman BIGINT NOT NULL CHECK (price_toman > 0),
    price_after_toman BIGINT NOT NULL CHECK (price_after_toman > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_usd_trades_player_time ON usd_trades(player_id,created_at DESC);
CREATE INDEX IF NOT EXISTS idx_usd_trades_time ON usd_trades(created_at DESC);

CREATE TABLE IF NOT EXISTS usd_daily_limits (
    player_id BIGINT NOT NULL REFERENCES players(id) ON DELETE RESTRICT,
    trade_date DATE NOT NULL,
    bought_cents BIGINT NOT NULL DEFAULT 0 CHECK (bought_cents >= 0),
    sold_cents BIGINT NOT NULL DEFAULT 0 CHECK (sold_cents >= 0),
    PRIMARY KEY(player_id,trade_date)
);

INSERT INTO feature_flags(key,enabled,updated_by)
VALUES ('usd_market_frozen',FALSE,'migration-0006') ON CONFLICT(key) DO NOTHING;