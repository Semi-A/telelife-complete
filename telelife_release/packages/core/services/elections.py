"""Election and poll business rules with citizenship authorization."""
from __future__ import annotations
from datetime import timedelta
import asyncpg
from packages.core import db
from packages.core.config import get_config
from packages.core.repositories import country_repo, election_repo
from packages.core.services import country as country_service
from packages.core.utils import clock

async def _active_citizen(country_id:int, player_id:int)->bool:
    return bool(await db.fetchval("SELECT 1 FROM citizenships WHERE country_id=$1 AND player_id=$2 AND is_active",country_id,player_id))

async def start(country_id:int, player_id:int)->asyncpg.Record:
    country=await country_repo.by_id(country_id)
    if country is None: raise ValueError("country_not_found")
    if not await _active_citizen(country_id,player_id): raise PermissionError("citizen_required")
    president=country["president_player_id"]
    if president is not None and int(president)!=player_id: raise PermissionError("president_required")
    cfg=get_config(); now=clock.utcnow()
    nom=now+timedelta(hours=cfg.int_("elections.election.nomination_duration_hours"))
    vote=nom+timedelta(hours=cfg.int_("elections.election.voting_duration_hours"))
    try:
        async with db.transaction() as conn:
            await conn.fetchrow("SELECT id FROM countries WHERE id=$1 FOR UPDATE",country_id)
            if await conn.fetchval("SELECT 1 FROM elections WHERE country_id=$1 AND status IN ('nominations','voting')",country_id):
                raise ValueError("election_already_open")
            return await election_repo.start(conn,country_id,player_id,nom,vote)
    except asyncpg.UniqueViolationError as exc:
        raise ValueError("election_already_open") from exc

async def nominate(election_id:int, player_id:int, chat_id:int|None, message_id:int|None)->bool:
    row=await db.fetchrow("SELECT country_id FROM elections WHERE id=$1",election_id)
    if row is None: raise ValueError("election_not_found")
    if not await _active_citizen(int(row["country_id"]),player_id): raise PermissionError("citizen_required")
    return await election_repo.nominate(election_id,player_id,chat_id,message_id)

async def vote(election_id:int, voter:int, candidate:int)->bool:
    row=await db.fetchrow("SELECT country_id FROM elections WHERE id=$1",election_id)
    if row is None: raise ValueError("election_not_found")
    cid=int(row["country_id"])
    if not await _active_citizen(cid,voter) or not await _active_citizen(cid,candidate):
        raise PermissionError("citizen_required")
    return await election_repo.vote(election_id,voter,candidate)

async def create_poll(country_id:int,player_id:int,question:str,options:list[str])->asyncpg.Record:
    if not await _active_citizen(country_id,player_id): raise PermissionError("citizen_required")
    cfg=get_config(); question=question.strip()
    if not cfg.int_("elections.poll.question_min_length")<=len(question)<=cfg.int_("elections.poll.question_max_length"): raise ValueError("invalid_question")
    cleaned=[x.strip() for x in options if x.strip()]
    if len(cleaned)!=len(set(cleaned)): raise ValueError("duplicate_options")
    if not cfg.int_("elections.poll.minimum_options")<=len(cleaned)<=cfg.int_("elections.poll.maximum_options"): raise ValueError("invalid_options")
    if any(not cfg.int_("elections.poll.option_min_length")<=len(x)<=cfg.int_("elections.poll.option_max_length") for x in cleaned): raise ValueError("invalid_option_length")
    closes=clock.utcnow()+timedelta(hours=cfg.int_("elections.poll.duration_hours"))
    async with db.transaction() as conn:return await election_repo.create_poll(conn,country_id,player_id,question,closes,cleaned)

async def resolve_due()->dict[str,int]:
    cfg=get_config(); stats={"elections":0,"polls":0}; touched=set()
    async with db.transaction() as conn:
        for row in await election_repo.claim_due(conn,cfg.int_("elections.scheduler.claim_batch_size")):
            if row["status"]=="nominations": await election_repo.advance(conn,row["id"])
            else:
                await election_repo.resolve(conn,row["id"]); touched.add(int(row["country_id"]))
            stats["elections"]+=1
        for row in await election_repo.claim_due_polls(conn,cfg.int_("elections.scheduler.claim_batch_size")):
            await election_repo.resolve_poll(conn,row["id"]);stats["polls"]+=1
    for cid in touched: await country_service.refresh_status(cid)
    return stats
