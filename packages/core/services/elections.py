"""Election and poll business rules with idempotent resolution."""

from __future__ import annotations

from datetime import timedelta

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, election_repo
from packages.core.utils import clock


async def start(country_id: int, player_id: int) -> asyncpg.Record:
    """Open an election. One per country at a time."""
    country = await country_repo.by_id(country_id)
    if country is None:
        raise ValueError("country_not_found")

    president = country["president_player_id"]
    if president is not None and int(president) != player_id:
        raise PermissionError("president_required")

    if get_config().bool_("elections.election.one_open_per_country", True):
        if await election_repo.open_for_country(country_id) is not None:
            raise ValueError("election_already_open")

    cfg = get_config()
    now = clock.utcnow()
    nominations_end = now + timedelta(
        hours=cfg.int_("elections.election.nomination_duration_hours")
    )
    voting_end = nominations_end + timedelta(
        hours=cfg.int_("elections.election.voting_duration_hours")
    )

    async with db.transaction() as conn:
        return await election_repo.start(
            conn, country_id, player_id, nominations_end, voting_end
        )


async def create_poll(
    country_id: int,
    player_id: int,
    question: str,
    options: list[str],
) -> asyncpg.Record:
    """Create a poll after validating the question and the option list."""
    cfg = get_config()

    question = question.strip()
    q_min = cfg.int_("elections.poll.question_min_length")
    q_max = cfg.int_("elections.poll.question_max_length")
    if not q_min <= len(question) <= q_max:
        raise ValueError("invalid_question")

    cleaned = [text.strip() for text in options if text.strip()]
    if len(cleaned) != len(set(cleaned)):
        raise ValueError("duplicate_options")

    lo = cfg.int_("elections.poll.minimum_options")
    hi = cfg.int_("elections.poll.maximum_options")
    if not lo <= len(cleaned) <= hi:
        raise ValueError("invalid_options")

    o_min = cfg.int_("elections.poll.option_min_length")
    o_max = cfg.int_("elections.poll.option_max_length")
    if any(not o_min <= len(text) <= o_max for text in cleaned):
        raise ValueError("invalid_option_length")

    closes = clock.utcnow() + timedelta(
        hours=cfg.int_("elections.poll.duration_hours")
    )
    async with db.transaction() as conn:
        return await election_repo.create_poll(
            conn, country_id, player_id, question, closes, cleaned
        )


async def resolve_due() -> dict[str, int]:
    """Advance or close everything that is due. Safe to run concurrently:
    rows are claimed with FOR UPDATE SKIP LOCKED."""
    cfg = get_config()
    batch = cfg.int_("elections.scheduler.claim_batch_size")
    stats = {"elections": 0, "polls": 0}

    async with db.transaction() as conn:
        for row in await election_repo.claim_due(conn, batch):
            if row["status"] == "nominations":
                await election_repo.advance(conn, row["id"])
            else:
                await election_repo.resolve(conn, row["id"])
            stats["elections"] += 1

        for row in await election_repo.claim_due_polls(conn, batch):
            await election_repo.resolve_poll(conn, row["id"])
            stats["polls"] += 1

    return stats