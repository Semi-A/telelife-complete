"""Economic persistence primitives. Business rules live in services."""
from __future__ import annotations
from typing import Any
import asyncpg


def player_account(asset: str) -> str:
    """Canonical ledger account for a player-owned asset."""
    return "wallet" if asset == "IRT" else "usd" if asset == "USD" else f"resource:{asset}"


def country_account(asset: str) -> str:
    """Canonical ledger account for a country-owned asset."""
    return "treasury" if asset == "IRT" else f"resource:{asset}"


async def idempotency_exists(conn: asyncpg.Connection, key: str) -> bool:
    return bool(await conn.fetchval("SELECT EXISTS(SELECT 1 FROM ledger WHERE idempotency_key=$1)", key))


async def lock_player(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM players WHERE id=$1 FOR UPDATE", player_id)


async def lock_country(conn: asyncpg.Connection, country_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow("SELECT * FROM countries WHERE id=$1 FOR UPDATE", country_id)


async def player_resource(conn: asyncpg.Connection, player_id: int, asset: str) -> int:
    value = await conn.fetchval(
        "SELECT quantity FROM player_resources WHERE player_id=$1 AND asset_code=$2 FOR UPDATE",
        player_id, asset,
    )
    return int(value or 0)


async def change_player(conn: asyncpg.Connection, player_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value = await conn.fetchval(
            "UPDATE players SET wallet_toman=wallet_toman+$2::bigint WHERE id=$1::bigint AND wallet_toman+$2::bigint>=0 RETURNING wallet_toman",
            player_id, delta,
        )
    elif asset == "USD":
        value = await conn.fetchval(
            "UPDATE players SET usd_cents=usd_cents+$2::bigint WHERE id=$1::bigint AND usd_cents+$2::bigint>=0 RETURNING usd_cents",
            player_id, delta,
        )
    else:
        value = await conn.fetchval(
            """INSERT INTO player_resources(player_id,asset_code,quantity)
            SELECT $1::bigint,$2::text,$3::bigint WHERE $3::bigint>=0
            ON CONFLICT(player_id,asset_code) DO UPDATE SET quantity=player_resources.quantity+$3::bigint,updated_at=now()
            WHERE player_resources.quantity+$3::bigint>=0 RETURNING quantity""",
            player_id, asset, delta,
        )
    if value is None:
        raise ValueError("insufficient_player_balance")
    return int(value)


async def change_country(conn: asyncpg.Connection, country_id: int, asset: str, delta: int) -> int:
    if asset == "IRT":
        value = await conn.fetchval(
            "UPDATE countries SET treasury_toman=treasury_toman+$2::bigint WHERE id=$1::bigint AND treasury_toman+$2::bigint>=0 RETURNING treasury_toman",
            country_id, delta,
        )
    else:
        value = await conn.fetchval(
            """INSERT INTO country_resources(country_id,asset_code,quantity)
            SELECT $1::bigint,$2::text,$3::bigint WHERE $3::bigint>=0
            ON CONFLICT(country_id,asset_code) DO UPDATE SET quantity=country_resources.quantity+$3::bigint,updated_at=now()
            WHERE country_resources.quantity+$3::bigint>=0 RETURNING quantity""",
            country_id, asset, delta,
        )
    if value is None:
        raise ValueError("insufficient_country_balance")
    return int(value)


async def insert(
    conn: asyncpg.Connection, *, player_id: int | None, country_id: int | None,
    key: str, reason: str, asset: str, account: str, amount: int,
    balance: int, metadata: dict[str, Any] | None = None,
) -> bool:
    # A ledger leg belongs to exactly one balance owner. Actor/citizen IDs must
    # live in metadata; setting both owners violates ledger_owner_check and can
    # roll back an otherwise valid economic transaction.
    if (player_id is None) == (country_id is None):
        raise ValueError("ledger_requires_exactly_one_owner")
    row = await conn.fetchval(
        """INSERT INTO ledger(player_id,country_id,idempotency_key,reason,currency,asset_code,account,amount,balance_after,metadata)
        VALUES($1,$2,$3,$4,$5,$5,$6,$7,$8,$9)
        ON CONFLICT(idempotency_key) DO NOTHING RETURNING id""",
        player_id, country_id, key, reason, asset, account, amount, balance, metadata or {},
    )
    return row is not None


async def economy_frozen(conn: asyncpg.Connection) -> bool:
    return bool(await conn.fetchval(
        "SELECT COALESCE((SELECT enabled FROM feature_flags WHERE key='economy_frozen'),false)"
    ))