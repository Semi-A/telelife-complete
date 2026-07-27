"""Timezone-aware game clock utilities.

All domain dates are derived from the configured IANA timezone. Keeping this in
one module prevents UTC/local-date drift around midnight and makes time policy
explicit for every service.
"""

from __future__ import annotations

from datetime import UTC, date, datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from packages.core.config import ConfigError, get_config


def game_timezone() -> ZoneInfo:
    """Return the configured game timezone, raising a clear config error."""
    name = str(get_config().get("core.timezone"))
    try:
        return ZoneInfo(name)
    except ZoneInfoNotFoundError as exc:
        raise ConfigError(f"Invalid IANA timezone in core.timezone: {name}") from exc


def utcnow() -> datetime:
    """Return an aware UTC timestamp."""
    return datetime.now(UTC)


def game_today(now: datetime | None = None) -> date:
    """Return the calendar date in the configured game timezone."""
    current = now or utcnow()
    if current.tzinfo is None:
        raise ValueError("game_today requires a timezone-aware datetime")
    return current.astimezone(game_timezone()).date()


def day_stamp(now: datetime | None = None) -> str:
    """Return the ISO game date used in idempotency keys."""
    return game_today(now).isoformat()
