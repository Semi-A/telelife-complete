"""Scheduler: minute resolution/outbox and idempotent daily maintenance."""
from __future__ import annotations
import asyncio,contextlib,logging,signal
from datetime import UTC,datetime,timedelta
from telegram import Bot
from apps.scheduler.jobs import country_jobs,daily_reset
from packages.core import db
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import Service,get_settings
logger=logging.getLogger(__name__)
async def minute(stop:asyncio.Event,bot:Bot)->None:
 while not stop.is_set():
  try:
   await db.execute('DELETE FROM cooldowns WHERE expires_at<now()');await country_jobs.resolve_due();await country_jobs.publish_news(bot)
  except Exception:logger.exception('minute jobs failed')
  with contextlib.suppress(TimeoutError):await asyncio.wait_for(stop.wait(),timeout=60)
def until_daily()->float:
 now=datetime.now(UTC);n=(now+timedelta(days=1)).replace(hour=0,minute=10,second=0,microsecond=0);return (n-now).total_seconds()
async def daily(stop:asyncio.Event)->None:
 await country_jobs.daily_events()
 while not stop.is_set():
  with contextlib.suppress(TimeoutError):await asyncio.wait_for(stop.wait(),timeout=until_daily())
  if stop.is_set():return
  try:await daily_reset.run();await country_jobs.daily_events()
  except Exception:logger.exception('daily jobs failed')
async def run()->None:
 s=get_settings();setup_logging(Service.SCHEDULER.value,s.log_level);await db.create_pool(s);await migrate();stop=asyncio.Event();loop=asyncio.get_running_loop()
 for sig in (signal.SIGINT,signal.SIGTERM):
  with contextlib.suppress(NotImplementedError):loop.add_signal_handler(sig,stop.set)
 bot=Bot(s.teleworld_bot_token);await asyncio.gather(minute(stop,bot),daily(stop));await db.close_pool()
def main()->None:asyncio.run(run())
if __name__=='__main__':main()
