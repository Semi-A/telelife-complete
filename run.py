"""Single-container entrypoint supervising both bots, scheduler and FastAPI."""
from __future__ import annotations

import asyncio
import logging
import signal

import uvicorn

from apps.scheduler.main import SchedulerService
from apps.telelife_bot.main import register as register_telelife
from apps.teleworld_bot.main import register as register_teleworld
from packages.core import db
from packages.core.bot import PollingService
from packages.core.db.migrator import migrate
from packages.core.logging import setup_logging
from packages.core.settings import Service, get_settings
from packages.core.supervisor import ServiceSpec, ServiceSupervisor

logger = logging.getLogger(__name__)


class AdminService:
    def __init__(self, settings) -> None:  # type: ignore[no-untyped-def]
        config = uvicorn.Config(
            "apps.admin.main:app", host=settings.host, port=settings.port,
            log_level=settings.log_level.lower(), proxy_headers=True,
            forwarded_allow_ips="127.0.0.1", lifespan="on", access_log=True,
        )
        self.server = uvicorn.Server(config)

    def healthy(self) -> bool:
        return bool(self.server.started and not self.server.should_exit)

    async def run(self, stop: asyncio.Event) -> None:
        self.server.should_exit = False
        serve = asyncio.create_task(self.server.serve(), name="admin:uvicorn")
        stop_waiter = asyncio.create_task(stop.wait(), name="admin:stop")
        done, _ = await asyncio.wait({serve, stop_waiter}, return_when=asyncio.FIRST_COMPLETED)
        if stop_waiter in done:
            self.server.should_exit = True
            await serve
        else:
            stop_waiter.cancel()
            await asyncio.gather(stop_waiter, return_exceptions=True)
            await serve


async def amain() -> None:
    settings = get_settings()
    setup_logging("supervisor", settings.log_level)
    await db.create_pool(settings)
    await migrate()

    telelife = PollingService(settings, Service.TELELIFE, register_telelife)
    teleworld = PollingService(settings, Service.TELEWORLD, register_teleworld)
    scheduler = SchedulerService(settings)
    admin = AdminService(settings)
    supervisor = ServiceSupervisor([
        ServiceSpec("telelife", telelife.run, telelife.healthy),
        ServiceSpec("teleworld", teleworld.run, teleworld.healthy),
        ServiceSpec("scheduler", scheduler.run, scheduler.healthy),
        ServiceSpec("admin", admin.run, admin.healthy),
    ], memory_warning_mb=settings.memory_warning_mb)

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, supervisor.stop.set)
        except NotImplementedError:
            pass
    try:
        await supervisor.run()
    finally:
        await db.close_pool()
        logger.info("process shutdown complete")


def main() -> None:
    asyncio.run(amain())


if __name__ == "__main__":
    main()
