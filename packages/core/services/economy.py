"""Single atomic funnel for every money/resource mutation."""

from __future__ import annotations

from dataclasses import dataclass

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo


@dataclass(frozen=True, slots=True)
class TransferResult:
    applied: bool
    duplicate: bool
    source_balance: int
    target_balance: int


def _validate_amount(asset: str, amount: int) -> None:
    if amount <= 0:
        raise ValueError("invalid_amount")
    cfg = get_config()
    if asset == "IRT":
        lo = cfg.int_("economy.limits.min_transaction_toman")
        hi = cfg.int_("economy.limits.max_transaction_toman")
    else:
        lo = cfg.int_("economy.limits.min_resource_transaction")
        hi = cfg.int_("economy.limits.max_resource_transaction")
    if not lo <= amount <= hi:
        raise ValueError("amount_out_of_range")


async def transfer(
    *,
    player_id: int,
    country_id: int,
    asset: str,
    amount: int,
    reason: str,
    idempotency_key: str,
) -> TransferResult:
    """Move `amount` of `asset` from a player to a country treasury, atomically."""
    _validate_amount(asset, amount)

    debit_key = f"{idempotency_key}:debit"
    credit_key = f"{idempotency_key}:credit"

    async with db.transaction() as conn:
        if await ledger_repo.economy_frozen(conn):
            raise RuntimeError("economy_frozen")
        if await ledger_repo.idempotency_exists(conn, debit_key):
            return TransferResult(False, True, 0, 0)

        # Always lock in the same order (player, then country) to avoid deadlocks.
        await ledger_repo.lock_player(conn, player_id)
        await ledger_repo.lock_country(conn, country_id)

        source = await ledger_repo.change_player(conn, player_id, asset, -amount)
        target = await ledger_repo.change_country(conn, country_id, asset, amount)

        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=debit_key,
            reason=reason,
            asset=asset,
            account=ledger_repo.player_account(asset),
            amount=-amount,
            balance=source,
            metadata={"country_id": country_id},
        )
        await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=credit_key,
            reason=reason,
            asset=asset,
            account=ledger_repo.country_account(asset),
            amount=amount,
            balance=target,
            metadata={"player_id": player_id},
        )
        return TransferResult(True, False, source, target)


async def country_adjust(
    *,
    country_id: int,
    asset: str,
    amount: int,
    reason: str,
    key: str,
    allow_frozen: bool = False,
) -> bool:
    """Signed treasury adjustment used by scheduled country economics."""
    async with db.transaction() as conn:
        if not allow_frozen and await ledger_repo.economy_frozen(conn):
            raise RuntimeError("economy_frozen")
        if await ledger_repo.idempotency_exists(conn, key):
            return False
        await ledger_repo.lock_country(conn, country_id)
        balance = await ledger_repo.change_country(conn, country_id, asset, amount)
        return await ledger_repo.insert(
            conn,
            player_id=None,
            country_id=country_id,
            key=key,
            reason=reason,
            asset=asset,
            account=ledger_repo.country_account(asset),
            amount=amount,
            balance=balance,
        )
