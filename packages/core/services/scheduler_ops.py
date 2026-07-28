"""Isolated, observable execution for scheduler jobs."""
from __future__ import annotations
import logging, time
from typing import Awaitable, Callable, TypeVar
from packages.core import db
logger=logging.getLogger(__name__)
T=TypeVar("T")
async def run(name:str, fn:Callable[[],Awaitable[T]])->T|None:
    started=time.perf_counter()
    row_id=await db.fetchval("INSERT INTO scheduler_job_runs(job_name,status) VALUES($1,'running') RETURNING id",name)
    try:
        result=await fn()
        payload=result if isinstance(result,dict) else {"value":result} if result is not None else {}
        await db.execute("UPDATE scheduler_job_runs SET status='succeeded',finished_at=now(),duration_ms=$2,result=$3 WHERE id=$1",row_id,round((time.perf_counter()-started)*1000),payload)
        return result
    except Exception as exc:
        await db.execute("UPDATE scheduler_job_runs SET status='failed',finished_at=now(),duration_ms=$2,error_type=$3,error_message=$4 WHERE id=$1",row_id,round((time.perf_counter()-started)*1000),type(exc).__name__,str(exc)[:1000])
        logger.exception("scheduler job failed",extra={"job_name":name})
        return None
