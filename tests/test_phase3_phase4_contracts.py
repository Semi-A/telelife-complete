from pathlib import Path

def test_phase_3_4_migration_contract():
    text=Path("migrations/0006_phase3_phase4_complete.sql").read_text()
    for table in ("player_housing","player_life_economy","usd_market_state","usd_trades","usd_daily_limits"):
        assert table in text

def test_user_bots_only_register_start_command():
    roots=[Path("apps/telelife_bot"),Path("apps/teleworld_bot")]
    registrations=[]
    for root in roots:
        for p in root.rglob("*.py"):
            for line in p.read_text().splitlines():
                if "add_handler(CommandHandler" in line: registrations.append(line)
    assert registrations and all('"start"' in line for line in registrations)

def test_market_is_bounded_and_idempotent():
    text=Path("packages/core/services/usd_market.py").read_text()
    assert "daily_band_basis_points" in text
    assert "idempotency_key" in text
    assert "FOR UPDATE" in text
    assert "daily_limit" in text

def test_phase3_money_uses_transactions_and_ledger():
    text=Path("packages/core/services/personal_economy.py").read_text()
    assert "db.transaction()" in text
    assert "ledger_repo.insert" in text
    assert "FOR UPDATE" in text
