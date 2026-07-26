from __future__ import annotations
import asyncio
from typing import Any
from uuid import uuid4
from packages.core.repositories import outbox_repo

class FakeConnection:
    def __init__(self) -> None:
        self.query = ""
        self.args: tuple[Any, ...] = ()
    async def fetch(self, query: str, *args: Any) -> list[Any]:
        self.query, self.args = query, args
        return []
    async def execute(self, query: str, *args: Any) -> str:
        self.query, self.args = query, args
        return "UPDATE 1"

def test_claim_uses_numeric_interval_expression() -> None:
    conn = FakeConnection()
    asyncio.run(outbox_repo.claim(conn, uuid4(), 20, 60, 5))  # type: ignore[arg-type]
    assert "$4::double precision * interval '1 second'" in conn.query
    assert conn.args[3] == 60

def test_failed_uses_numeric_interval_expression() -> None:
    conn = FakeConnection()
    asyncio.run(outbox_repo.failed(conn, 1, uuid4(), "telegram_error", 120))  # type: ignore[arg-type]
    assert "$4::double precision * interval '1 second'" in conn.query
    assert conn.args[3] == 120
