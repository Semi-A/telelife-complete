"""Level-gated unlock catalogue. Pure config reads - no I/O."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from packages.core.config import get_config


@dataclass(slots=True, frozen=True)
class Unlock:
    level: int
    key: str
    title: str
    icon: str
    phase: int


@lru_cache(maxsize=1)
def catalogue() -> tuple[Unlock, ...]:
    levels = get_config().section("unlocks.levels")
    items = [
        Unlock(int(lvl), str(s["key"]), str(s["title"]), str(s["icon"]), int(s["phase"]))
        for lvl, s in levels.items()
    ]
    return tuple(sorted(items, key=lambda u: u.level))


def unlocked_at(level: int) -> tuple[Unlock, ...]:
    return tuple(u for u in catalogue() if u.level == level)


def available(level: int) -> tuple[Unlock, ...]:
    return tuple(u for u in catalogue() if u.level <= level)


def next_unlock(level: int) -> Unlock | None:
    return next((u for u in catalogue() if u.level > level), None)