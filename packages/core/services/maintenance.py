"""Bounded retention and stale-run recovery suitable for free database plans."""
from __future__ import annotations
from packages.core import db

async def minute_tick() -> dict[str,int]:
    stale=await db.execute("""UPDATE scheduler_job_runs SET status='failed',finished_at=now(),
      error_type='StaleRun',error_message='Recovered after process interruption'
      WHERE status='running' AND started_at < now()-interval '20 minutes'""")
    # Small deletes avoid long locks and cap growth without a paid monitoring stack.
    jobs=await db.execute("""DELETE FROM scheduler_job_runs WHERE id IN (
      SELECT id FROM scheduler_job_runs WHERE started_at < now()-interval '30 days'
      ORDER BY started_at LIMIT 200)""")
    outbox=await db.execute("""DELETE FROM telegram_action_outbox WHERE id IN (
      SELECT id FROM telegram_action_outbox WHERE completed_at < now()-interval '30 days'
      ORDER BY completed_at LIMIT 200)""")
    def count(tag:str)->int:
        try:return int(tag.rsplit(' ',1)[-1])
        except (ValueError,IndexError):return 0
    return {"stale_runs":count(stale),"jobs_pruned":count(jobs),"actions_pruned":count(outbox)}
