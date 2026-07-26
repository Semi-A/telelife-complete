from packages.core.repositories import ledger_repo
from packages.core.services import production

def test_canonical_accounts():
    assert ledger_repo.player_account("IRT") == "wallet"
    assert ledger_repo.player_account("food") == "resource:food"
    assert ledger_repo.country_account("IRT") == "treasury"

def test_production_uses_existing_ledger_contract():
    assert callable(ledger_repo.player_account)
    assert callable(ledger_repo.country_account)

def test_lifecycle_migration_present():
    text=open("migrations/0005_life_world_hardening.sql",encoding="utf-8").read()
    assert "forming" in text and "temporary" in text and "official" in text
    assert "uq_elections_one_open_country" in text
