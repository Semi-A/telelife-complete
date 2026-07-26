"""Country lifecycle and deterministic initial-resource allocation."""

from __future__ import annotations

import hashlib
import random

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, group_repo


def _resources(chat_id: int, name: str) -> dict[str, int]:
    """Split the national endowment deterministically across assets.

    Same (chat_id, name) always yields the same split, so a retry of country
    creation can never hand out a different starting position.
    """
    spec = get_config().section("country.resources")
    codes = sorted(str(code) for code in spec["asset_codes"])
    total = int(spec["country_total"])
    low = int(spec["minimum_share"])
    high = int(spec["maximum_share"])

    if not codes:
        raise ValueError("no_asset_codes_configured")
    if low > high:
        raise ValueError("minimum_share_above_maximum_share")
    if not low * len(codes) <= total <= high * len(codes):
        raise ValueError("country_total_outside_share_bounds")

    digest = hashlib.sha256(
        f"{spec['allocation_seed_namespace']}:{chat_id}:{name}".encode()
    ).digest()
    rng = random.Random(int.from_bytes(digest[:8], "big"))

    values = dict.fromkeys(codes, low)
    remaining = total - low * len(codes)

    while remaining > 0:
        headroom = [code for code in codes if values[code] < high]
        if not headroom:  # Unreachable given the bounds check, but never spin.
            break
        code = rng.choice(headroom)
        take = min(remaining, high - values[code], rng.randint(1, remaining))
        values[code] += take
        remaining -= take

    return values


async def create_country(
    *,
    chat_id: int,
    chat_title: str,
    player_id: int,
    name: str,
    government: str,
    description: str,
) -> asyncpg.Record:
    cfg = get_config()

    if government not in set(cfg.get("country.government_types")):
        raise ValueError("invalid_government")

    name = name.strip()
    description = description.strip()
    rules = cfg.section("country.validation")
    if not (
        int(rules["name_min_length"]) <= len(name) <= int(rules["name_max_length"])
    ):
        raise ValueError("invalid_name")
    if not (
        int(rules["description_min_length"])
        <= len(description)
        <= int(rules["description_max_length"])
    ):
        raise ValueError("invalid_description")

    if await country_repo.by_chat(chat_id) is not None:
        raise ValueError("country_already_exists")

    group = await group_repo.get_or_create(chat_id, chat_title)

    async with db.transaction() as conn:
        return await country_repo.create(
            conn,
            group.id,
            player_id,
            name,
            government,
            description,
            cfg.int_("country.creation.protection_days"),
            _resources(chat_id, name),
        )


async def join_country(*, chat_id: int, player_id: int) -> bool:
    """Become a citizen. False means the player was already a citizen."""
    country = await country_repo.by_chat(chat_id)
    if country is None:
        raise ValueError("country_not_found")
    async with db.transaction() as conn:
        return await country_repo.join(conn, player_id, int(country["id"]))