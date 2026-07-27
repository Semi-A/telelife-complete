"""Lazy-production row locking and materialisation queries."""

from __future__ import annotations

from datetime import datetime

import asyncpg

from packages.core import db

# Whitelist: the column name is interpolated into SQL, so it can never come
# straight from a caller.
_LEVEL_COLUMNS = {"storage": "storage_level", "production": "production_level"}


async def get(player_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM player_jobs WHERE player_id = $1", player_id
    )


async def choose(player_id: int, job: str, asset: str) -> bool:
    """Pick a job once. False means the player already has one."""
    chosen = await db.fetchval(
        """
        INSERT INTO player_jobs
            (player_id, job_code, output_asset_code, production_updated_at)
        VALUES ($1, $2, $3, now())
        ON CONFLICT DO NOTHING
        RETURNING player_id
        """,
        player_id,
        job,
        asset,
    )
    return chosen is not None


async def lock(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow(
        "SELECT * FROM player_jobs WHERE player_id = $1 FOR UPDATE", player_id
    )


async def checkpoint(
    conn: asyncpg.Connection, player_id: int, stored: int, at: datetime
) -> None:
    await conn.execute(
        "UPDATE player_jobs SET stored_amount = $2, production_updated_at = $3 "
        "WHERE player_id = $1",
        player_id,
        stored,
        at,
    )


async def clear(conn: asyncpg.Connection, player_id: int, at: datetime) -> None:
    await conn.execute(
        "UPDATE player_jobs SET stored_amount = 0, production_updated_at = $2 "
        "WHERE player_id = $1",
        player_id,
        at,
    )


async def level_up(conn: asyncpg.Connection, player_id: int, kind: str) -> None:
    column = _LEVEL_COLUMNS.get(kind)
    if column is None:
        raise ValueError(f"unknown_level_kind: {kind}")
    await conn.execute(
        f"UPDATE player_jobs SET {column} = {column} + 1 WHERE player_id = $1",  # noqa: S608
        player_id,
    )

async def set_shift_mode(conn: asyncpg.Connection, player_id: int, mode: str) -> None:
    await conn.execute(
        "UPDATE player_jobs SET shift_mode=$2,updated_at=now() WHERE player_id=$1",
        player_id, mode,
    )


async def country_for_player(conn: asyncpg.Connection, player_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow(
        """SELECT c.id,c.name FROM citizenships cs JOIN countries c ON c.id=cs.country_id
        WHERE cs.player_id=$1 AND cs.is_active FOR SHARE OF c""", player_id
    )
