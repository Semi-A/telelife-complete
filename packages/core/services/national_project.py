"""One-time national project with atomic, idempotent contributions.

Money and asset movement happens only through the ledger, inside a single
transaction, keyed by a deterministic idempotency key per leg.
"""

from __future__ import annotations

from typing import Any

import asyncpg

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, ledger_repo, project_repo
from packages.core.services import xp, migration

_IRT = "IRT"


def _account_for(asset: str) -> str:
    """Wallet holds currency; everything else lives in inventory."""
    return "wallet" if asset == _IRT else "inventory"


async def start(
    country_id: int,
    player_id: int,
    key: str = "national_storage",
) -> asyncpg.Record:
    """Open a national project. Only the sitting president may start one."""
    if await migration.political_hold(player_id):raise PermissionError("migrant_political_hold")
    country = await country_repo.by_id(country_id)
    if country is None:
        raise ValueError("country_not_found")

    president = country["president_player_id"]
    if president is not None:
        if int(president) != player_id:
            raise PermissionError("president_required")
    elif not await db.fetchval(
        "SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2 AND is_active",
        country_id, player_id,
    ):
        raise PermissionError("citizen_required")

    projects=get_config().section("national_project.projects")
    if key not in projects:raise ValueError("invalid_project")
    requirements: dict[str, Any] = get_config().section(
        f"national_project.projects.{key}.requirements"
    )
    parsed = {asset: int(amount) for asset, amount in requirements.items()}

    async with db.transaction() as conn:
        return await project_repo.start(conn, country_id, player_id, key, parsed)


async def contribute(
    project_id: int,
    player_id: int,
    asset: str,
    amount: int,
    key: str,
) -> tuple[int, bool]:
    """Contribute to a project. Returns (amount_accepted, project_completed).

    Exactly-once is guaranteed by the UNIQUE constraint on
    project_contributions.idempotency_key, not by a pre-flight lookup: a
    read-then-write check leaves a race window open under concurrent taps.
    """
    if amount <= 0:
        raise ValueError("amount_must_be_positive")

    completed = False
    accepted = 0
    project_key = "national_storage"

    async with db.transaction() as conn:
        project = await project_repo.lock(conn, project_id)
        if project is None or project["status"] != "active":
            raise ValueError("project_not_active")
        project_key = str(project["project_key"])

        is_citizen = await conn.fetchval(
            "SELECT EXISTS(SELECT 1 FROM citizenships "
            "WHERE player_id = $1 AND country_id = $2 AND is_active)",
            player_id,
            project["country_id"],
        )
        if not is_citizen:
            raise PermissionError("citizen_required")

        remaining = await project_repo.remaining(conn, project_id, asset)
        if remaining is None:
            raise ValueError("asset_not_required")

        accepted = min(amount, remaining)
        if accepted <= 0:
            return 0, False

        # Claim the idempotency slot FIRST. If this returns False the work was
        # already done by an earlier (or concurrent) call: nothing to replay.
        claimed = await project_repo.contribution(
            conn, project_id, player_id, asset, accepted, key
        )
        if not claimed:
            return 0, False

        balance = await ledger_repo.change_player(conn, player_id, asset, -accepted)
        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=f"{key}:debit",
            reason="project_contribution",
            asset=asset,
            account=_account_for(asset),
            amount=-accepted,
            balance=balance,
            metadata={"project_id": project_id},
        )

        completed = await project_repo.complete_if_ready(conn, project_id)

    if completed:
        completion=get_config().section(f"national_project.projects.{project_key}.completion")
        async with db.transaction() as conn:
            project=await project_repo.lock(conn,project_id)
            await project_repo.apply_effect(conn,project_id,int(project["country_id"]),str(completion["effect_code"]),str(completion.get("effect_asset") or "all"),int(completion["magnitude_basis_points"]))
            people=await project_repo.contributors(conn,project_id)
        reward=int(completion["contributor_reward_xp"])
        for contributor in people:
            await xp.grant(contributor,"national_project",idempotency_key=f"project:{project_id}:xp:{contributor}",amount=reward)
    if accepted:
        from packages.core.services import missions
        await missions.report_progress(player_id,"project_contribution")
    return accepted, completed

async def treasury_contribute(project_id:int,player_id:int,asset:str,amount:int,key:str)->tuple[int,bool]:
    if amount<=0:raise ValueError("amount_must_be_positive")
    async with db.transaction() as conn:
        project=await project_repo.lock(conn,project_id)
        if not project or project["status"]!="active":raise ValueError("project_not_active")
        country=await ledger_repo.lock_country(conn,int(project["country_id"]))
        if not country or int(country["president_player_id"] or 0)!=player_id:raise PermissionError("president_required")
        remaining=await project_repo.remaining(conn,project_id,asset)
        if remaining is None:raise ValueError("asset_not_required")
        accepted=min(amount,remaining)
        if accepted<=0:return 0,False
        if not await project_repo.claim_country_funding(conn,project_id,player_id,asset,accepted,key):return 0,False
        balance=await ledger_repo.change_country(conn,int(project["country_id"]),asset,-accepted)
        await ledger_repo.insert(conn,player_id=player_id,country_id=int(project["country_id"]),key=f"{key}:country",reason="project_treasury_funding",asset=asset,account=ledger_repo.country_account(asset),amount=-accepted,balance=balance,metadata={"project_id":project_id})
        completed=await project_repo.complete_if_ready(conn,project_id)
    if completed:
        completion=get_config().section(f"national_project.projects.{project['project_key']}.completion")
        async with db.transaction() as conn:
            await project_repo.apply_effect(conn,project_id,int(project["country_id"]),str(completion["effect_code"]),str(completion.get("effect_asset") or "all"),int(completion["magnitude_basis_points"]))
    return accepted,completed

async def available(country_id:int)->list[tuple[str,str]]:
    projects=get_config().section("national_project.projects");done=await project_repo.completed_keys(country_id)
    return [(key,str(spec["title"])) for key,spec in projects.items() if key not in done]