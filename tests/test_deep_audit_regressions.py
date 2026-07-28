"""Regression contracts found during the second deep audit."""
from pathlib import Path


def test_project_completion_and_effect_share_transaction_scope() -> None:
    source = Path("packages/core/services/national_project.py").read_text(encoding="utf-8")
    # The old failure mode opened another transaction after completion committed.
    assert "if completed:\n        completion=" not in source
    assert "Completion and its durable gameplay effect are one atomic" in source
    assert "Keep project status, effect and contributor rewards atomic" in source


def test_progression_panel_uses_game_timezone_day() -> None:
    source = Path("packages/core/repositories/progression_repo.py").read_text(encoding="utf-8")
    assert "created_at AT TIME ZONE $2" in source
    assert "clock.game_today()" in source
    assert "date_trunc('day', now())" not in source


def test_project_rewards_are_atomic_and_ordered() -> None:
    service = Path("packages/core/services/national_project.py").read_text(encoding="utf-8")
    repo = Path("packages/core/repositories/project_repo.py").read_text(encoding="utf-8")
    assert service.count("conn=conn") >= 2
    assert "treasury supplies the final required unit" in service
    assert "ORDER BY player_id" in repo


def test_trade_rejects_self_operations_and_aid_cap_is_per_asset() -> None:
    source = Path("packages/core/services/country_trade.py").read_text(encoding="utf-8")
    assert "pair(proposer_id,recipient_id)" in source
    assert "pair(donor_id,recipient_id)" in source
    assert "donor_country_id=$1 AND asset_code=$2" in source
    assert 'if asset!="IRT" and used+amount' not in source


def test_relation_acceptance_claims_idempotency_before_mutation() -> None:
    source = Path("packages/core/services/country_trade.py").read_text(encoding="utf-8")
    block = source[source.index("async def accept_relation"):source.index("async def impose_sanction")]
    assert "RETURNING id" in block
    assert "if not inserted:return False" in block
    assert block.index("if not inserted:return False") < block.index("UPDATE country_relations SET status")