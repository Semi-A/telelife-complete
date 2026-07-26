"""Country, citizenship and national-resource queries."""

from __future__ import annotations

from collections.abc import Mapping

import asyncpg

from packages.core import db


async def by_chat(chat_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        """
        SELECT c.*, g.telegram_id, g.title
        FROM countries c
        JOIN groups g ON g.id = c.group_id
        WHERE g.telegram_id = $1
        """,
        chat_id,
    )


async def by_id(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow("SELECT * FROM countries WHERE id = $1", country_id)


async def citizenship(player_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        """
        SELECT cs.*, c.name
        FROM citizenships cs
        JOIN countries c ON c.id = cs.country_id
        WHERE cs.player_id = $1
        """,
        player_id,
    )


async def create(
    conn: asyncpg.Connection,
    group_id: int,
    player_id: int,
    name: str,
    government: str,
    description: str,
    protection_days: int,
    resources: Mapping[str, int],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO countries
            (group_id, name, government_type, description,
             protection_until, created_by_player_id)
        VALUES ($1, $2, $3, $4, now() + ($5::text || ' days')::interval, $6)
        RETURNING *
        """,
        group_id,
        name,
        government,
        description,
        protection_days,
        player_id,
    )
    if row is None:
        raise RuntimeError("country_insert_returned_nothing")
    await conn.execute(
        "INSERT INTO citizenships (player_id, country_id) VALUES ($1, $2) "
        "ON CONFLICT DO NOTHING",
        player_id,
        row["id"],
    )
    await conn.executemany(
        """
        INSERT INTO country_resources (country_id, asset_code, quantity)
        VALUES ($1, $2, $3)
        """,
        [(row["id"], asset, qty) for asset, qty in resources.items()],
    )
    return row


async def join(conn: asyncpg.Connection, player_id: int, country_id: int) -> bool:
    joined = await conn.fetchval(
        "INSERT INTO citizenships (player_id, country_id) VALUES ($1, $2) "
        "ON CONFLICT DO NOTHING RETURNING player_id",
        player_id,
        country_id,
    )
    return joined is not None


async def set_flag(
    country_id: int, player_id: int, file_id: str, unique_id: str | None
) -> bool:
    """Only the president can change the flag. False means: not allowed."""
    updated = await db.fetchval(
        """
        UPDATE countries SET flag_file_id = $3, flag_file_unique_id = $4
        WHERE id = $1 AND president_player_id = $2
        RETURNING id
        """,
        country_id,
        player_id,
        file_id,
        unique_id,
    )
    return updated is not None


async def is_president(country_id: int, player_id: int) -> bool:
    return bool(
        await db.fetchval(
            "SELECT president_player_id = $2 FROM countries WHERE id = $1",
            country_id,
            player_id,
        )
    )


async def resources(country_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT asset_code, quantity FROM country_resources "
        "WHERE country_id = $1 ORDER BY asset_code",
        country_id,
    )


async def citizens(country_id: int) -> list[int]:
    rows = await db.fetch(
        "SELECT player_id FROM citizenships WHERE country_id = $1 ORDER BY player_id",
        country_id,
    )
    return [int(row["player_id"]) for row in rows]