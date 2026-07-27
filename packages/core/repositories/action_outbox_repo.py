"""Transactional Telegram action outbox used by admin workflows."""
from __future__ import annotations
from typing import Any
from uuid import UUID
import asyncpg

async def enqueue(conn: asyncpg.Connection, key: str, bot_name: str, action: str,
                  chat_id: int, payload: dict[str, Any]) -> bool:
    row = await conn.fetchval("""
        INSERT INTO telegram_action_outbox
          (idempotency_key, bot_name, action, chat_id, payload)
        VALUES ($1,$2,$3,$4,$5)
        ON CONFLICT (idempotency_key) DO NOTHING RETURNING id
    """, key, bot_name, action, chat_id, payload)
    return row is not None

async def claim(conn: asyncpg.Connection, token: UUID, limit: int = 20,
                lease: int = 90, max_attempts: int = 8) -> list[asyncpg.Record]:
    return list(await conn.fetch("""
        WITH picked AS (
          SELECT id FROM telegram_action_outbox
          WHERE completed_at IS NULL AND attempts < $3 AND available_at <= now()
            AND (processing_until IS NULL OR processing_until < now())
          ORDER BY created_at,id FOR UPDATE SKIP LOCKED LIMIT $2
        )
        UPDATE telegram_action_outbox o SET processing_token=$1,
          processing_until=now()+($4::double precision*interval '1 second'),
          attempts=attempts+1
        FROM picked WHERE o.id=picked.id RETURNING o.*
    """, token, limit, max_attempts, lease))

async def completed(conn: asyncpg.Connection, row_id: int, token: UUID) -> None:
    await conn.execute("""UPDATE telegram_action_outbox SET completed_at=now(),
      processing_token=NULL,processing_until=NULL,last_error_code=NULL
      WHERE id=$1 AND processing_token=$2""", row_id, token)

async def failed(conn: asyncpg.Connection, row_id: int, token: UUID,
                 error: str, delay: int) -> None:
    await conn.execute("""UPDATE telegram_action_outbox SET processing_token=NULL,
      processing_until=NULL,last_error_code=$3,
      available_at=now()+($4::double precision*interval '1 second')
      WHERE id=$1 AND processing_token=$2""", row_id, token, error[:64], delay)