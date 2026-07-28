"""Retry-safe delivery of Telegram actions without extra infrastructure."""
from __future__ import annotations
from html import escape
import logging
from typing import Any
from uuid import uuid4
from telegram import Bot, LabeledPrice
from packages.core import db
from packages.core.repositories import action_outbox_repo
logger = logging.getLogger(__name__)

async def enqueue(key: str, bot_name: str, action: str, chat_id: int,
                  payload: dict[str, Any], *, conn=None) -> bool:
    if conn is not None:
        return await action_outbox_repo.enqueue(conn,key,bot_name,action,chat_id,payload)
    async with db.transaction() as owned:
        return await action_outbox_repo.enqueue(owned,key,bot_name,action,chat_id,payload)

async def deliver_batch(life_bot: Bot, world_bot: Bot) -> dict[str,int]:
    token=uuid4(); stats={"delivered":0,"failed":0}
    async with db.transaction() as conn:
        rows=await action_outbox_repo.claim(conn,token)
    for row in rows:
        try:
            bot=life_bot if row["bot_name"]=="telelife" else world_bot
            payload=row["payload"]
            if row["action"]=="send_message":
                await bot.send_message(chat_id=row["chat_id"],text=escape(str(payload["text"])))
            elif row["action"]=="send_invoice":
                await bot.send_invoice(chat_id=row["chat_id"],title=str(payload["title"]),
                    description=str(payload["description"]),payload=str(payload["invoice_payload"]),
                    currency="XTR",prices=[LabeledPrice(str(payload["label"]),int(payload["stars"]))],
                    provider_token="")
            else: raise ValueError("unsupported_action")
        except Exception as exc:
            logger.warning("telegram action delivery failed",extra={"extra_fields":{"row_id":row["id"],"error":type(exc).__name__}})
            delay=min(3600,30*(2**min(int(row["attempts"])-1,7)))
            async with db.transaction() as conn:
                await action_outbox_repo.failed(conn,row["id"],token,type(exc).__name__,delay)
            stats["failed"]+=1
        else:
            async with db.transaction() as conn:
                await action_outbox_repo.completed(conn,row["id"],token)
            stats["delivered"]+=1
    return stats
