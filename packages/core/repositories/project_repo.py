"""National project persistence."""

from __future__ import annotations

from collections.abc import Mapping

import asyncpg

from packages.core import db


async def start(
    conn: asyncpg.Connection,
    country_id: int,
    player_id: int,
    key: str,
    requirements: Mapping[str, int],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO national_projects (country_id, project_key, started_by_player_id)
        VALUES ($1, $2, $3)
        RETURNING *
        """,
        country_id,
        key,
        player_id,
    )
    if row is None:
        raise RuntimeError("project_insert_returned_nothing")
    await conn.executemany(
        """
        INSERT INTO project_requirements (project_id, asset_code, required_amount)
        VALUES ($1, $2, $3)
        """,
        [(row["id"], asset, amount) for asset, amount in requirements.items()],
    )
    return row


async def active(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM national_projects WHERE country_id = $1 AND status = 'active'",
        country_id,
    )


async def status(project_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT * FROM project_requirements WHERE project_id = $1 ORDER BY asset_code",
        project_id,
    )


async def lock(conn: asyncpg.Connection, project_id: int) -> asyncpg.Record | None:
    return await conn.fetchrow(
        "SELECT * FROM national_projects WHERE id = $1 FOR UPDATE", project_id
    )


async def remaining(
    conn: asyncpg.Connection, project_id: int, asset: str
) -> int | None:
    """Outstanding amount for one asset, with the requirement row locked."""
    value = await conn.fetchval(
        """
        SELECT required_amount - contributed_amount
        FROM project_requirements
        WHERE project_id = $1 AND asset_code = $2
        FOR UPDATE
        """,
        project_id,
        asset,
    )
    return int(value) if value is not None else None


async def contribution(
    conn: asyncpg.Connection,
    project_id: int,
    player_id: int,
    asset: str,
    amount: int,
    key: str,
) -> bool:
    """Record a contribution once. False means the key was already used."""
    added = await conn.fetchval(
        """
        INSERT INTO project_contributions
            (project_id, player_id, asset_code, amount, idempotency_key)
        VALUES ($1, $2, $3, $4, $5)
        ON CONFLICT (idempotency_key) DO NOTHING
        RETURNING id
        """,
        project_id,
        player_id,
        asset,
        amount,
        key,
    )
    if added is None:
        return False
    await conn.execute(
        """
        UPDATE project_requirements
        SET contributed_amount = LEAST(required_amount, contributed_amount + $3)
        WHERE project_id = $1 AND asset_code = $2
        """,
        project_id,
        asset,
        amount,
    )
    return True


async def complete_if_ready(conn: asyncpg.Connection, project_id: int) -> bool:
    """Mark complete only when every requirement is met, exactly once."""
    pending = await conn.fetchval(
        """
        SELECT EXISTS(
            SELECT 1 FROM project_requirements
            WHERE project_id = $1 AND contributed_amount < required_amount
        )
        """,
        project_id,
    )
    if pending:
        return False
    # RETURNING is the reliable "did this row change" signal. Parsing the
    # command tag with endswith('1') also matches "UPDATE 11".
    completed = await conn.fetchval(
        """
        UPDATE national_projects
        SET status = 'completed', completed_at = now()
        WHERE id = $1 AND status = 'active'
        RETURNING id
        """,
        project_id,
    )
    return completed is not None
async def completed_keys(country_id: int) -> set[str]:
    rows=await db.fetch("SELECT project_key FROM national_projects WHERE country_id=$1",country_id)
    return {str(row["project_key"]) for row in rows}

async def contributors(conn: asyncpg.Connection, project_id: int) -> list[int]:
    rows=await conn.fetch("SELECT DISTINCT player_id FROM project_contributions WHERE project_id=$1 ORDER BY player_id",project_id)
    return [int(row["player_id"]) for row in rows]

async def claim_country_funding(conn: asyncpg.Connection, project_id: int, actor: int,
                                asset: str, amount: int, key: str) -> bool:
    value=await conn.fetchval("""INSERT INTO country_project_funding(project_id,actor_player_id,asset_code,amount,idempotency_key)
      VALUES($1,$2,$3,$4,$5) ON CONFLICT(idempotency_key) DO NOTHING RETURNING id""",project_id,actor,asset,amount,key)
    if value is None:return False
    await conn.execute("""UPDATE project_requirements SET contributed_amount=LEAST(required_amount,contributed_amount+$3)
      WHERE project_id=$1 AND asset_code=$2""",project_id,asset,amount)
    return True

async def apply_effect(conn: asyncpg.Connection, project_id: int, country_id: int,
                       code: str, asset: str | None, magnitude: int) -> None:
    await conn.execute("""INSERT INTO national_project_effects(country_id,project_id,effect_code,asset_code,magnitude_basis_points)
      VALUES($1,$2,$3,$4,$5) ON CONFLICT(project_id) DO NOTHING""",country_id,project_id,code,asset,magnitude)
