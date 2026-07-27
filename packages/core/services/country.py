"""Country lifecycle, membership and deterministic initial-resource allocation."""
from __future__ import annotations
import hashlib, random
import asyncpg
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, group_repo, ledger_repo
from packages.core.services.content_filter import require_clean


def _resources(chat_id: int, name: str) -> dict[str, int]:
    spec = get_config().section("country.resources")
    codes = sorted(str(c) for c in spec["asset_codes"])
    total, low, high = int(spec["country_total"]), int(spec["minimum_share"]), int(spec["maximum_share"])
    if not codes: raise ValueError("no_asset_codes_configured")
    if low > high: raise ValueError("minimum_share_above_maximum_share")
    if not low * len(codes) <= total <= high * len(codes): raise ValueError("country_total_outside_share_bounds")
    digest = hashlib.sha256(f"{spec['allocation_seed_namespace']}:{chat_id}:{name}".encode()).digest()
    rng = random.Random(int.from_bytes(digest[:8], "big")); values = dict.fromkeys(codes, low)
    remaining = total - low * len(codes)
    while remaining:
        choices = [c for c in codes if values[c] < high]
        code = rng.choice(choices); take = min(remaining, high-values[code], rng.randint(1, remaining))
        values[code] += take; remaining -= take
    return values


async def _refresh_status(conn: asyncpg.Connection, country_id: int) -> str:
    cfg = get_config(); row = await conn.fetchrow(
        """SELECT c.status, c.president_player_id,
                  count(cs.player_id) FILTER (WHERE cs.is_active) AS citizens
           FROM countries c LEFT JOIN citizenships cs ON cs.country_id=c.id
           WHERE c.id=$1 GROUP BY c.id""", country_id)
    if row is None: raise ValueError("country_not_found")
    citizens = int(row["citizens"] or 0)
    temporary_min = cfg.int_("country.lifecycle.temporary_min_citizens")
    official_min = cfg.int_("country.lifecycle.official_min_citizens")
    leader_ok = row["president_player_id"] is not None or not cfg.bool_("country.lifecycle.require_elected_leader_for_official", True)
    target = "official" if citizens >= official_min and leader_ok else "temporary" if citizens >= temporary_min else "forming"
    await conn.execute(
        """UPDATE countries SET status=$2,
           temporary_at=CASE WHEN $2 IN ('temporary','official') THEN COALESCE(temporary_at,now()) ELSE temporary_at END,
           official_at=CASE WHEN $2='official' THEN COALESCE(official_at,now()) ELSE NULL END
           WHERE id=$1""", country_id, target)
    return target


async def refresh_status(country_id: int) -> str:
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE", country_id)
        return await _refresh_status(conn, country_id)


async def create_country(*, chat_id: int, chat_title: str, player_id: int,
                         name: str, government: str, description: str) -> asyncpg.Record:
    cfg=get_config(); name=name.strip(); description=description.strip()
    if government not in set(cfg.get("country.government_types")): raise ValueError("invalid_government")
    require_clean(name, "name")
    require_clean(description, "description")
    rules=cfg.section("country.validation")
    if not int(rules["name_min_length"]) <= len(name) <= int(rules["name_max_length"]): raise ValueError("invalid_name")
    if not int(rules["description_min_length"]) <= len(description) <= int(rules["description_max_length"]): raise ValueError("invalid_description")
    group=await group_repo.get_or_create(chat_id,chat_title)
    resources=_resources(chat_id,name)
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM groups WHERE id=$1 FOR UPDATE",group.id)
        if await conn.fetchval("SELECT 1 FROM countries WHERE group_id=$1",group.id): raise ValueError("country_already_exists")
        current=await conn.fetchrow("SELECT country_id,is_active FROM citizenships WHERE player_id=$1 FOR UPDATE",player_id)
        if current and current["is_active"]: raise ValueError("already_citizen_elsewhere")
        row=await country_repo.create(conn,group.id,player_id,name,government,description,
                                      cfg.int_("country.creation.protection_days"),resources)
        for asset,qty in resources.items():
            ok=await ledger_repo.insert(conn,player_id=None,country_id=int(row["id"]),
                key=f"country-genesis:{row['id']}:{asset}",reason="country_genesis",
                asset=asset,account=ledger_repo.country_account(asset),amount=qty,balance=qty,
                metadata={"created_by":player_id})
            if not ok: raise RuntimeError("country_genesis_ledger_conflict")
        await _refresh_status(conn,int(row["id"]))
        return await conn.fetchrow("SELECT * FROM countries WHERE id=$1",row["id"])


async def join_country(*, chat_id: int, player_id: int) -> bool:
    country=await country_repo.by_chat(chat_id)
    if country is None: raise ValueError("country_not_found")
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country["id"])
        current=await conn.fetchrow("SELECT country_id,is_active FROM citizenships WHERE player_id=$1 FOR UPDATE",player_id)
        if current and current["is_active"]:
            if int(current["country_id"]) == int(country["id"]): return False
            raise ValueError("migration_required")
        if current:
            await conn.execute("UPDATE citizenships SET country_id=$2,is_active=TRUE,left_at=NULL,joined_at=now() WHERE player_id=$1",player_id,country["id"])
            joined=True
        else:
            joined=await country_repo.join(conn,player_id,int(country["id"]))
        await _refresh_status(conn,int(country["id"]))
        return joined


async def leave_country(*, chat_id: int, player_id: int) -> bool:
    country=await country_repo.by_chat(chat_id)
    if country is None: return False
    async with db.transaction() as conn:
        await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country["id"])
        changed=await conn.fetchval("""UPDATE citizenships SET is_active=FALSE,left_at=now()
          WHERE player_id=$1 AND country_id=$2 AND is_active RETURNING player_id""",player_id,country["id"])
        if changed:
            await conn.execute("UPDATE countries SET president_player_id=NULL WHERE id=$1 AND president_player_id=$2",country["id"],player_id)
            await _refresh_status(conn,int(country["id"]))
        return changed is not None
