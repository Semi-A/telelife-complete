"""Daily country objective driven by real work claims."""
from __future__ import annotations
from dataclasses import dataclass
from packages.core import db

@dataclass(frozen=True,slots=True)
class Objective:
    target:int
    progress:int
    contributors:int
    complete:bool

async def today(country_id:int)->Objective:
    citizens=int(await db.fetchval("SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active",country_id) or 0)
    target=max(3,citizens*2)
    row=await db.fetchrow("""SELECT count(*) claims,count(DISTINCT player_id) people FROM work_claims
      WHERE country_id=$1 AND claimed_at>=date_trunc('day',now() AT TIME ZONE 'UTC') AT TIME ZONE 'UTC'""",country_id)
    progress=int(row['claims'] or 0);people=int(row['people'] or 0)
    return Objective(target,min(progress,target),people,progress>=target)
