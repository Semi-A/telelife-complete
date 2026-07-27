-- Admin command center: authoritative market board and historical snapshots.
CREATE TABLE IF NOT EXISTS market_prices (
    asset_code          TEXT PRIMARY KEY,
    title_fa            TEXT NOT NULL,
    current_price_toman BIGINT NOT NULL CHECK (current_price_toman > 0),
    updated_by          TEXT NOT NULL DEFAULT 'system',
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (length(asset_code) BETWEEN 1 AND 64)
);

CREATE TABLE IF NOT EXISTS market_price_snapshots (
    asset_code  TEXT NOT NULL REFERENCES market_prices(asset_code) ON DELETE RESTRICT,
    price_toman BIGINT NOT NULL CHECK (price_toman > 0),
    captured_at TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (asset_code, captured_at)
);

CREATE INDEX IF NOT EXISTS idx_market_snapshots_time
    ON market_price_snapshots (captured_at DESC, asset_code);

INSERT INTO market_prices (asset_code, title_fa, current_price_toman)
VALUES
    ('USD', 'دلار', 85000),
    ('oil', 'نفت', 720000),
    ('food', 'غذا', 85000),
    ('minerals', 'مواد معدنی', 310000),
    ('energy', 'انرژی', 190000),
    ('technology', 'فناوری', 950000)
ON CONFLICT (asset_code) DO NOTHING;

INSERT INTO market_price_snapshots (asset_code, price_toman, captured_at)
SELECT asset_code, current_price_toman, date_trunc('minute', now())
FROM market_prices
ON CONFLICT DO NOTHING;
