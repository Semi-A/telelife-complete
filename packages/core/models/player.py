"""Domain models. Plain dataclasses - no ORM, no magic."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import asyncpg


@dataclass(slots=True, frozen=True)
class Player:
    id: int
    telegram_id: int
    username: str | None
    first_name: str
    language_code: str
    level: int
    xp: int
    reputation: int
    happiness: int
    prestige: int
    wallet_toman: int
    savings_toman: int
    usd_cents: int
    is_banned: bool
    is_frozen: bool
    ban_reason: str | None
    created_at: datetime
    updated_at: datetime
    last_seen_at: datetime

    @classmethod
    def from_record(cls, row: asyncpg.Record) -> Player:
        return cls(**dict(row))

    @property
    def net_worth_toman(self) -> int:
        return self.wallet_toman + self.savings_toman

    @property
    def playable(self) -> bool:
        return not self.is_banned and not self.is_frozen


@dataclass(slots=True, frozen=True)
class Group:
    id: int
    telegram_id: int
    title: str
    is_active: bool
    member_count: int
    settings: dict[str, Any]
    created_at: datetime
    last_active_at: datetime

    @classmethod
    def from_record(cls, row: asyncpg.Record) -> Group:
        return cls(**dict(row))
