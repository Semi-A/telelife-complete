"""Regression coverage for the exclusive ledger owner invariant."""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

from packages.core.repositories import ledger_repo


class NoQueryConnection:
    async def fetchval(self, *args: object) -> object:
        raise AssertionError("invalid ownership must be rejected before SQL executes")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("player_id", "country_id"),
    [(None, None), (7, 11)],
)
async def test_insert_rejects_zero_or_two_owners(player_id: int | None, country_id: int | None) -> None:
    with pytest.raises(ValueError, match="ledger_requires_exactly_one_owner"):
        await ledger_repo.insert(
            NoQueryConnection(),  # type: ignore[arg-type]
            player_id=player_id,
            country_id=country_id,
            key="owner-test",
            reason="test",
            asset="IRT",
            account="wallet",
            amount=1,
            balance=1,
        )


def test_all_static_ledger_calls_have_one_explicit_owner() -> None:
    """Keep country balance legs from accidentally carrying the actor as owner."""
    for root in (Path("packages"), Path("apps")):
        for path in root.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                func = node.func
                if not (
                    isinstance(func, ast.Attribute)
                    and func.attr == "insert"
                    and isinstance(func.value, ast.Name)
                    and func.value.id == "ledger_repo"
                ):
                    continue
                keywords = {item.arg: item.value for item in node.keywords if item.arg}
                player = keywords.get("player_id")
                country = keywords.get("country_id")
                assert player is not None and country is not None, f"owners missing at {path}:{node.lineno}"
                player_none = isinstance(player, ast.Constant) and player.value is None
                country_none = isinstance(country, ast.Constant) and country.value is None
                assert player_none != country_none, f"ambiguous owners at {path}:{node.lineno}"
