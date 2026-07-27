"""Domain service package.

Submodules are intentionally not eagerly imported. Python resolves explicit
``from packages.core.services import xp`` imports lazily, avoiding package-level
cycles while preserving the public import style.
"""

__all__ = [
    "admin",
    "country",
    "country_economy",
    "country_missions",
    "daily",
    "economy",
    "elections",
    "missions",
    "national_project",
    "news",
    "production",
    "progression",
    "unlocks",
    "xp",
]