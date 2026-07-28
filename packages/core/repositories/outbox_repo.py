"""Transactional outbox and deterministic daily-event queries."""

from __future__ import annotations

from datetime import date
from typing import Any
from uuid import UUID

import asyncpg


async def enqueue(
    conn: asyncpg.Connection,
    key: str,
    event_type: str,
    payload: dict[str, Any],
    destination: int | None,
) -> bool:
    """Queue one message. False means this key was already queued."""
    queued = await conn.fetchval(
        """
        INSERT INTO news_outbox
            (idempotency_key, event_type, payload, destination_chat_id)
        VALUES ($1, $2, $3, $4)
        ON CONFLICT (idempotency_key) DO NOTHING
        RETURNING id
        """,
        key,
        event_type,
        payload,
        destination,
    )
    return queued is not None


async def claim(
    conn: asyncpg.Connection,
    token: UUID,
    limit: int,
    lease: int,
    max_attempts: int,
) -> list[asyncpg.Record]:
    """Lease a batch of due messages. Concurrent workers never collide."""
    return list(
        await conn.fetch(
            """
            WITH picked AS (
                SELECT id FROM news_outbox
                WHERE published_at IS NULL
                  AND attempts < $3
                  AND available_at <= now()
                  AND (processing_until IS NULL OR processing_until < now())
                ORDER BY created_at, id
                FOR UPDATE SKIP LOCKED
                LIMIT $2
            )
            UPDATE news_outbox n SET
                processing_token = $1,
                processing_until = now() + ($4::double precision * interval '1 second'),
                attempts = attempts + 1
            FROM picked
            WHERE n.id = picked.id
            RETURNING n.*
            """,
            token,
            limit,
            max_attempts,
            lease,
        )
    )


async def published(conn: asyncpg.Connection, row_id: int, token: UUID) -> None:
    await conn.execute(
        """
        UPDATE news_outbox SET
            published_at = now(), processing_token = NULL, processing_until = NULL
        WHERE id = $1 AND processing_token = $2
        """,
        row_id,
        token,
    )


async def failed(
    conn: asyncpg.Connection,
    row_id: int,
    token: UUID,
    error: str,
    delay: int,
) -> None:
    """Release the lease and schedule a retry."""
    await conn.execute(
        """
        UPDATE news_outbox SET
            processing_token = NULL,
            processing_until = NULL,
            last_error_code  = $3,
            available_at     = now() + ($4::double precision * interval '1 second')
        WHERE id = $1 AND processing_token = $2
        """,
        row_id,
        token,
        error,
        delay,
    )


async def create_event(
    conn: asyncpg.Connection, day: date, code: str, effect: dict[str, Any]
) -> bool:
    """Record the day's event once. False means the day already had one."""
    created = await conn.fetchval(
        """
        INSERT INTO daily_events (event_date, event_code, effect_payload)
        VALUES ($1, $2, $3)
        ON CONFLICT (event_date) DO NOTHING
        RETURNING event_date
        """,
        day,
        code,
        effect,
    )
    return created is not None
