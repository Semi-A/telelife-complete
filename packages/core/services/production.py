"""Capacity-capped lazy production with proportional anti-farm XP."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from math import floor

from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import ledger_repo, production_repo
from packages.core.services import xp, life_progression

UPGRADE_KINDS = frozenset({"storage", "production"})


@dataclass(frozen=True, slots=True)
class Accrual:
    stored: int
    capacity: int
    rate: float


def _max_level(kind: str) -> int:
    cfg = get_config()
    if kind == "storage":
        return max(int(k) for k in cfg.section("jobs.storage.levels"))
    return cfg.int_("jobs.production_levels.maximum")


def _upgrade_cost(kind: str, target: int) -> int:
    section = "jobs.storage.upgrade_cost_toman" if kind == "storage" \
        else "jobs.production_levels.upgrade_cost_toman"
    cfg = get_config()
    path = f"{section}.{target}"
    if not cfg.has(path):
        raise ValueError("max_level_reached")
    return cfg.int_(path)


def accrue(row, at: datetime) -> Accrual:  # type: ignore[no-untyped-def]
    """Compute what the player's job has produced since the last checkpoint."""
    cfg = get_config()
    job = cfg.section(f"jobs.jobs.{row['job_code']}")
    rate = float(job["base_rate_per_hour"]) * (
        1 + (int(row["production_level"]) - 1)
        * cfg.float_("jobs.production.production_multiplier_per_level")
    )

    since = row["production_updated_at"]
    if since.tzinfo is None:
        since = since.replace(tzinfo=UTC)
    if at.tzinfo is None:
        at = at.replace(tzinfo=UTC)

    # Clock skew must never mint resources, and never destroy stored ones.
    skew = cfg.int_("jobs.production.max_accrual_clock_skew_seconds")
    elapsed = (at - since).total_seconds()
    if elapsed < -skew:
        elapsed = 0.0
    hours = max(0.0, elapsed) / cfg.int_("jobs.production.time_unit_seconds")

    capacity_hours = cfg.int_(f"jobs.storage.levels.{row['storage_level']}.capacity_hours")
    cap = floor(rate * capacity_hours)
    stored = min(cap, int(row["stored_amount"]) + floor(rate * hours))
    return Accrual(max(0, stored), max(0, cap), rate)


async def choose(player_id: int, job: str) -> bool:
    player = await db.fetchrow("SELECT level FROM players WHERE id=$1", player_id)
    if player is None:
        raise ValueError("player_not_found")
    if int(player["level"]) < get_config().int_("jobs.purpose_loop.available_from_level"):
        raise ValueError("job_locked")
    jobs = get_config().section("jobs.jobs")
    if job not in jobs:
        raise ValueError("invalid_job")
    return await production_repo.choose(player_id, job, str(jobs[job]["output_asset"]))


async def collect(player_id: int, key: str, at: datetime | None = None) -> tuple[int, int]:
    """Bank stored production. Returns (amount, xp_awarded)."""
    now = at or datetime.now(UTC)
    cfg = get_config()

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")
        # The player_jobs lock serializes double taps; re-check idempotency only after it.
        if await ledger_repo.idempotency_exists(conn, key):
            return 0, 0
        accrual = accrue(row, now)
        amount = accrual.stored
        if amount < cfg.int_("jobs.production.minimum_collection_amount"):
            return 0, 0
        asset = row["output_asset_code"]
        balance = await ledger_repo.change_player(conn, player_id, asset, amount)
        if not await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason="production_collect",
            asset=asset,
            account=ledger_repo.player_account(asset),
            amount=amount,
            balance=balance,
            metadata={"job": row["job_code"]},
        ):
            return 0, 0
        await production_repo.clear(conn, player_id, now)

    fraction = amount / accrual.capacity if accrual.capacity else 0.0
    minimum = cfg.float_("jobs.production.minimum_collection_fraction_for_xp")
    award = (
        floor(cfg.int_("jobs.production.collection_xp_at_full_capacity") * fraction)
        if fraction >= minimum
        else 0
    )
    if award:
        result = await xp.grant(
            player_id, "production_collect", idempotency_key=f"{key}:xp", amount=award
        )
        award = result.granted
    return amount, award


async def upgrade(player_id: int, kind: str, key: str, at: datetime | None = None) -> int:
    """Upgrade storage or production. Old rate is checkpointed first."""
    if kind not in UPGRADE_KINDS:
        raise ValueError("invalid_upgrade")
    now = at or datetime.now(UTC)

    async with db.transaction() as conn:
        row = await production_repo.lock(conn, player_id)
        if not row:
            raise ValueError("job_not_found")

        current = int(row[f"{kind}_level"])
        target = current + 1
        if target > _max_level(kind):
            raise ValueError("max_level_reached")

        # Duplicate request: stop before touching balances or levels.
        if await ledger_repo.idempotency_exists(conn, key):
            return current

        cost = _upgrade_cost(kind, target)

        # Freeze production at the OLD rate before the level changes, so the
        # upgrade never applies retroactively to hours already elapsed.
        accrual = accrue(row, now)
        await production_repo.checkpoint(conn, player_id, accrual.stored, now)

        balance = await ledger_repo.change_player(conn, player_id, "IRT", -cost)
        await ledger_repo.insert(
            conn,
            player_id=player_id,
            country_id=None,
            key=key,
            reason=f"{kind}_upgrade",
            asset="IRT",
            account="wallet",
            amount=-cost,
            balance=balance,
            metadata={"kind": kind, "level": target},
        )
        await production_repo.level_up(conn, player_id, kind)
        return target
@dataclass(frozen=True, slots=True)
class WorkReceipt:
    amount: int
    xp: int
    asset: str
    tax_toman: int
    country_amount: int
    country_asset: str | None
    country_name: str | None
    shift_mode: str
    skill_code: str | None = None
    skill_level: int = 1
    skill_xp: int = 0
    skill_needed: int = 1


def shift_modes() -> dict[str, dict[str, object]]:
    return get_config().section("jobs.purpose_loop.shift_modes")


async def choose_shift(player_id: int, mode: str) -> str:
    modes=shift_modes()
    if mode not in modes:raise ValueError("invalid_shift")
    async with db.transaction() as conn:
        row=await production_repo.lock(conn,player_id)
        if not row:raise ValueError("job_not_found")
        accrual=accrue(row,datetime.now(UTC))
        await production_repo.checkpoint(conn,player_id,accrual.stored,datetime.now(UTC))
        await production_repo.set_shift_mode(conn,player_id,mode)
    return mode


async def collect_purposeful(player_id: int, key: str, at: datetime | None = None) -> WorkReceipt:
    """Claim one accumulated shift and atomically split its impact."""
    now=at or datetime.now(UTC);cfg=get_config()
    async with db.transaction() as conn:
        row=await production_repo.lock(conn,player_id)
        if not row:raise ValueError("job_not_found")
        existing=await conn.fetchrow("SELECT * FROM work_claims WHERE idempotency_key=$1",key)
        if existing:
            return WorkReceipt(0,0,str(existing['asset_code']),0,0,None,None,str(existing['shift_mode']))
        accrual=accrue(row,now);gross=accrual.stored
        asset_bonus=await life_progression.asset_bonus_bp(conn,player_id,'work_bonus_bp')
        gross=floor(gross*(10000+asset_bonus)/10000)
        if gross<cfg.int_("jobs.production.minimum_collection_amount"):
            return WorkReceipt(0,0,str(row['output_asset_code']),0,0,None,None,str(row.get('shift_mode') or 'balanced'))
        mode=str(row.get('shift_mode') or 'balanced');spec=cfg.section(f"jobs.purpose_loop.shift_modes.{mode}")
        asset=str(row['output_asset_code']);country=await production_repo.country_for_player(conn,player_id)
        player_pct=int(spec['player_percent']);country_pct=int(spec['country_percent']) if country else 0
        if country:
            bonus=int(await conn.fetchval("""SELECT COALESCE(sum(magnitude_basis_points),0) FROM national_project_effects
              WHERE country_id=$1 AND effect_code='work_output_bonus' AND (asset_code=$2 OR asset_code='all')""",int(country['id']),asset) or 0)
            economy_modifier=int(await conn.fetchval(
              "SELECT production_modifier_bp FROM country_economy_state WHERE country_id=$1",
              int(country['id']),
            ) or 10000)
            # National projects and Release-B shortages/budgets both affect real work output.
            gross=floor(gross*(10000+min(bonus,5000))/10000)
            gross=max(1,floor(gross*max(5000,min(15000,economy_modifier))/10000))
        player_amount=max(1,floor(gross*player_pct/100));country_amount=max(0,floor(gross*country_pct/100))
        tax=0;country_asset=asset if country else None
        if asset=='IRT':
            tax=floor(player_amount*cfg.int_("jobs.purpose_loop.tax_percent")/100) if country else 0
            player_amount-=tax
            country_asset=str(cfg.get("jobs.purpose_loop.national_output_asset_for_irt_jobs")) if country else None
            country_amount=floor(gross*cfg.int_("jobs.purpose_loop.national_output_percent_for_irt_jobs")/100) if country else 0
        balance=await ledger_repo.change_player(conn,player_id,asset,player_amount)
        await ledger_repo.insert(conn,player_id=player_id,country_id=None,key=f"{key}:player",reason="purposeful_work_player",asset=asset,account=ledger_repo.player_account(asset),amount=player_amount,balance=balance,metadata={"job":row['job_code'],"shift":mode,"gross":gross})
        if country and tax:
            treasury=await ledger_repo.change_country(conn,int(country['id']),'IRT',tax)
            await ledger_repo.insert(conn,player_id=None,country_id=int(country['id']),key=f"{key}:tax",reason="work_tax",asset='IRT',account='treasury',amount=tax,balance=treasury,metadata={"job":row['job_code'],"shift":mode})
        if country and country_amount and country_asset:
            national=await ledger_repo.change_country(conn,int(country['id']),country_asset,country_amount)
            await ledger_repo.insert(conn,player_id=None,country_id=int(country['id']),key=f"{key}:country",reason="national_work_output",asset=country_asset,account=ledger_repo.country_account(country_asset),amount=country_amount,balance=national,metadata={"job":row['job_code'],"shift":mode})
        fraction=gross/accrual.capacity if accrual.capacity else 0
        award=floor(cfg.int_("jobs.production.collection_xp_at_full_capacity")*fraction*int(spec['xp_percent'])/100) if fraction>=cfg.float_("jobs.production.minimum_collection_fraction_for_xp") else 0
        await conn.execute("""INSERT INTO work_claims(idempotency_key,player_id,country_id,job_code,shift_mode,asset_code,gross_amount,player_amount,country_amount,tax_toman,xp_awarded)
          VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11)""",key,player_id,int(country['id']) if country else None,row['job_code'],mode,asset,gross,player_amount,country_amount,tax,award)
        await conn.execute("""UPDATE player_jobs SET stored_amount=0,production_updated_at=$2,last_claim_at=$2,total_claims=total_claims+1,
          total_tax_toman=total_tax_toman+$3,total_country_output=total_country_output+$4,updated_at=now() WHERE player_id=$1""",player_id,now,tax,country_amount)
        skill=await life_progression.record_work(conn,player_id,str(row['job_code']),f"{key}:skill",fraction)
    if award:
        result=await xp.grant(player_id,"purposeful_work",idempotency_key=f"{key}:xp",amount=award);award=result.granted
        await db.execute("UPDATE work_claims SET xp_awarded=$2 WHERE idempotency_key=$1",key,award)
    from packages.core.services import missions
    await missions.report_progress(player_id,"work_shift")
    if country_amount:await missions.report_progress(player_id,"national_output")
    if tax:await missions.report_progress(player_id,"pay_work_tax")
    if award:await missions.report_progress(player_id,"earn_xp_100",award)
    return WorkReceipt(player_amount,award,asset,tax,country_amount,country_asset,str(country['name']) if country else None,mode,skill.code,skill.level,skill.xp,skill.needed)