"""Atomic, idempotent movement of player and country assets."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo

@dataclass(slots=True, frozen=True)
class TransferResult:
    applied: bool
    source_balance: int
    target_balance: int


def _validate_amount(asset: str, amount: int) -> None:
    cfg = get_config()
    if amount <= 0:
        raise ValueError("invalid_amount")
    if asset == "IRT":
        low = cfg.int_("economy.limits.min_transaction_toman")
        high = cfg.int_("economy.limits.max_transaction_toman")
    else:
        low = cfg.int_("economy.limits.min_resource_transaction")
        high = cfg.int_("economy.limits.max_resource_transaction")
    if not low <= amount <= high:
        raise ValueError("amount_out_of_bounds")


async def transfer(player_id: int, country_id: int, asset: str, amount: int, *,
                   reason: str, idempotency_key: str) -> TransferResult:
    _validate_amount(asset, amount)
    cfg = get_config()
    debit_key = f"{idempotency_key}:{cfg.get('economy.ledger.transfer_legs.debit_suffix')}"
    credit_key = f"{idempotency_key}:{cfg.get('economy.ledger.transfer_legs.credit_suffix')}"
    async with db.transaction() as conn:
        if await ledger_repo.economy_frozen(conn):
            raise ValueError("economy_frozen")
        player = await ledger_repo.lock_player(conn, player_id)
        country = await ledger_repo.lock_country(conn, country_id)
        if player is None:
            raise ValueError("player_not_found")
        if country is None:
            raise ValueError("country_not_found")
        # The ownership locks serialize retries. Re-check only after both locks.
        if await ledger_repo.idempotency_exists(conn, debit_key):
            return TransferResult(False, 0, 0)
        source = await ledger_repo.change_player(conn, player_id, asset, -amount)
        target = await ledger_repo.change_country(conn, country_id, asset, amount)
        debit_ok = await ledger_repo.insert(
            conn, player_id=player_id, country_id=None, key=debit_key,
            reason=reason, asset=asset, account=ledger_repo.player_account(asset),
            amount=-amount, balance=source, metadata={"country_id": country_id},
        )
        credit_ok = await ledger_repo.insert(
            conn, player_id=None, country_id=country_id, key=credit_key,
            reason=reason, asset=asset, account=ledger_repo.country_account(asset),
            amount=amount, balance=target, metadata={"player_id": player_id},
        )
        if not (debit_ok and credit_ok):
            raise RuntimeError("ledger_transfer_conflict")
        return TransferResult(True, source, target)


async def country_adjust(country_id: int, asset: str, amount: int, *, reason: str,
                         idempotency_key: str, allow_frozen: bool = False) -> int:
    if amount == 0:
        raise ValueError("invalid_amount")
    _validate_amount(asset, abs(amount))
    async with db.transaction() as conn:
        if not allow_frozen and await ledger_repo.economy_frozen(conn):
            raise ValueError("economy_frozen")
        row = await ledger_repo.lock_country(conn, country_id)
        if row is None:
            raise ValueError("country_not_found")
        if await ledger_repo.idempotency_exists(conn, idempotency_key):
            return 0
        balance = await ledger_repo.change_country(conn, country_id, asset, amount)
        inserted = await ledger_repo.insert(
            conn, player_id=None, country_id=country_id, key=idempotency_key,
            reason=reason, asset=asset, account=ledger_repo.country_account(asset),
            amount=amount, balance=balance,
        )
        if not inserted:
            raise RuntimeError("ledger_adjust_conflict")
        return balance