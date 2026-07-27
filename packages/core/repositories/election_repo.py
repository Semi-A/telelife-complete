"""Election and poll queries, including SKIP LOCKED scheduler claims."""

from __future__ import annotations

from datetime import datetime

import asyncpg

from packages.core import db


async def start(
    conn: asyncpg.Connection,
    country_id: int,
    player_id: int,
    nom_end: datetime,
    vote_end: datetime,
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO elections
            (country_id, started_by_player_id, status, nominations_end_at, voting_end_at)
        VALUES ($1, $2, 'nominations', $3, $4)
        RETURNING *
        """,
        country_id,
        player_id,
        nom_end,
        vote_end,
    )
    if row is None:  # `assert` disappears under `python -O`.
        raise RuntimeError("election_insert_returned_nothing")
    return row


async def nominate(
    election_id: int,
    player_id: int,
    chat_id: int | None,
    message_id: int | None,
) -> bool:
    """Register a candidate. Only while the election accepts nominations."""
    accepted = await db.fetchval(
        """
        INSERT INTO election_candidates
            (election_id, player_id, message_chat_id, message_id)
        SELECT $1, $2, $3, $4
        WHERE EXISTS (
            SELECT 1 FROM elections
            WHERE id = $1 AND status = 'nominations' AND nominations_end_at > now()
        )
        ON CONFLICT DO NOTHING
        RETURNING player_id
        """,
        election_id,
        player_id,
        chat_id,
        message_id,
    )
    return accepted is not None


async def vote(election_id: int, voter: int, candidate: int) -> bool:
    """Cast a vote. Rejected unless voting is open and the candidate is real."""
    accepted = await db.fetchval(
        """
        INSERT INTO election_votes
            (election_id, voter_player_id, candidate_player_id)
        SELECT $1, $2, $3
        WHERE EXISTS (
            SELECT 1 FROM elections
            WHERE id = $1 AND status = 'voting' AND voting_end_at > now()
        )
        AND EXISTS (
            SELECT 1 FROM election_candidates
            WHERE election_id = $1 AND player_id = $3
        )
        ON CONFLICT DO NOTHING
        RETURNING voter_player_id
        """,
        election_id,
        voter,
        candidate,
    )
    return accepted is not None


async def open_for_country(country_id: int) -> asyncpg.Record | None:
    return await db.fetchrow(
        "SELECT * FROM elections "
        "WHERE country_id = $1 AND status IN ('nominations', 'voting')",
        country_id,
    )


async def claim_due(conn: asyncpg.Connection, limit: int) -> list[asyncpg.Record]:
    return list(
        await conn.fetch(
            """
            SELECT * FROM elections
            WHERE (status = 'nominations' AND nominations_end_at <= now())
               OR (status = 'voting'      AND voting_end_at      <= now())
            ORDER BY id
            FOR UPDATE SKIP LOCKED
            LIMIT $1
            """,
            limit,
        )
    )


async def advance(conn: asyncpg.Connection, election_id: int) -> None:
    """Nominations -> voting. Cancels the election when nobody stood."""
    await conn.execute(
        """
        UPDATE elections SET status = CASE
            WHEN EXISTS (SELECT 1 FROM election_candidates WHERE election_id = $1)
            THEN 'voting' ELSE 'cancelled' END,
            resolved_at = CASE
            WHEN EXISTS (SELECT 1 FROM election_candidates WHERE election_id = $1)
            THEN NULL ELSE now() END
        WHERE id = $1 AND status = 'nominations'
        """,
        election_id,
    )


async def resolve(conn: asyncpg.Connection, election_id: int) -> int | None:
    """Close voting and seat the winner. Ties break on earliest nomination."""
    winner = await conn.fetchval(
        """
        SELECT v.candidate_player_id
        FROM election_votes v
        JOIN election_candidates c
          ON c.election_id = v.election_id AND c.player_id = v.candidate_player_id
        WHERE v.election_id = $1
        GROUP BY v.candidate_player_id, c.created_at
        ORDER BY count(*) DESC, c.created_at, v.candidate_player_id
        LIMIT 1
        """,
        election_id,
    )

    # Only seat the winner if THIS call is the one that closed the election.
    # Without the RETURNING guard a concurrent worker could seat twice.
    closed = await conn.fetchval(
        """
        UPDATE elections
        SET status = 'completed', winner_player_id = $2, resolved_at = now()
        WHERE id = $1 AND status = 'voting'
        RETURNING country_id
        """,
        election_id,
        winner,
    )
    if closed is None:
        return None

    if winner is not None:
        await conn.execute(
            "UPDATE countries SET president_player_id = $2 WHERE id = $1",
            int(closed),
            int(winner),
        )
        return int(winner)
    return None


async def create_poll(
    conn: asyncpg.Connection,
    country_id: int,
    creator: int,
    question: str,
    closes: datetime,
    options: list[str],
) -> asyncpg.Record:
    row = await conn.fetchrow(
        """
        INSERT INTO polls (country_id, creator_player_id, question, closes_at)
        VALUES ($1, $2, $3, $4)
        RETURNING *
        """,
        country_id,
        creator,
        question,
        closes,
    )
    if row is None:
        raise RuntimeError("poll_insert_returned_nothing")
    await conn.executemany(
        "INSERT INTO poll_options (poll_id, option_text) VALUES ($1, $2)",
        [(row["id"], text) for text in options],
    )
    return row


async def poll_vote(poll_id: int, voter: int, option_id: int) -> bool:
    """Cast a poll vote. The option must belong to this open poll."""
    accepted = await db.fetchval(
        """
        INSERT INTO poll_votes (poll_id, voter_player_id, option_id)
        SELECT $1, $2, $3
        WHERE EXISTS (
            SELECT 1 FROM polls
            WHERE id = $1 AND status = 'active' AND closes_at > now()
        )
        AND EXISTS (
            SELECT 1 FROM poll_options WHERE id = $3 AND poll_id = $1
        )
        ON CONFLICT DO NOTHING
        RETURNING voter_player_id
        """,
        poll_id,
        voter,
        option_id,
    )
    return accepted is not None


async def polls(country_id: int) -> list[asyncpg.Record]:
    return await db.fetch(
        "SELECT * FROM polls WHERE country_id = $1 ORDER BY created_at DESC LIMIT 20",
        country_id,
    )


async def claim_due_polls(
    conn: asyncpg.Connection, limit: int
) -> list[asyncpg.Record]:
    return list(
        await conn.fetch(
            """
            SELECT * FROM polls
            WHERE status = 'active' AND closes_at <= now()
            ORDER BY id
            FOR UPDATE SKIP LOCKED
            LIMIT $1
            """,
            limit,
        )
    )


async def resolve_poll(conn: asyncpg.Connection, poll_id: int) -> None:
    await conn.execute(
        "UPDATE polls SET status = 'completed', resolved_at = now() "
        "WHERE id = $1 AND status = 'active'",
        poll_id,
    )