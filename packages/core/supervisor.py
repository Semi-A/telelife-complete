"""Fault-isolating asyncio supervisor for all long-running application services."""
from __future__ import annotations

import asyncio
import inspect
import logging
import resource
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass

from packages.core.runtime_status import state

logger = logging.getLogger(__name__)
Runner = Callable[[asyncio.Event], Awaitable[None]]
HealthCheck = Callable[[], bool | Awaitable[bool]]


@dataclass(frozen=True, slots=True)
class ServiceSpec:
    name: str
    runner: Runner
    healthcheck: HealthCheck


class ServiceSupervisor:
    """Runs isolated service tasks and restarts only the failed/unhealthy service."""

    def __init__(
        self,
        specs: list[ServiceSpec],
        *,
        health_interval: float = 15.0,
        restart_base: float = 1.0,
        restart_cap: float = 60.0,
        memory_warning_mb: int = 450,
    ) -> None:
        self.specs = specs
        self.health_interval = health_interval
        self.restart_base = restart_base
        self.restart_cap = restart_cap
        self.memory_warning_mb = memory_warning_mb
        self.stop = asyncio.Event()
        self._tasks: dict[str, asyncio.Task[None]] = {}
        self._monitor: asyncio.Task[None] | None = None

    async def run(self) -> None:
        for spec in self.specs:
            self._tasks[spec.name] = asyncio.create_task(
                self._supervise(spec), name=f"supervisor:{spec.name}"
            )
        self._monitor = asyncio.create_task(self._monitor_loop(), name="supervisor:monitor")
        await self.stop.wait()
        await self.shutdown()

    async def _supervise(self, spec: ServiceSpec) -> None:
        failures = 0
        item = state(spec.name)
        while not self.stop.is_set():
            local_stop = asyncio.Event()
            item.status = "starting"
            item.last_started_monotonic = time.monotonic()
            item.consecutive_health_failures = 0
            service_task = asyncio.create_task(spec.runner(local_stop), name=f"service:{spec.name}")
            try:
                while not self.stop.is_set():
                    stop_waiter = asyncio.create_task(self.stop.wait())
                    done, _ = await asyncio.wait(
                        {service_task, stop_waiter}, timeout=self.health_interval,
                        return_when=asyncio.FIRST_COMPLETED,
                    )
                    if not stop_waiter.done():
                        stop_waiter.cancel()
                    await asyncio.gather(stop_waiter, return_exceptions=True)
                    if stop_waiter in done:
                        local_stop.set()
                        try:
                            await asyncio.wait_for(service_task, timeout=20.0)
                        except TimeoutError:
                            service_task.cancel()
                            await asyncio.gather(service_task, return_exceptions=True)
                        return
                    if service_task.done():
                        exc = service_task.exception()
                        if exc:
                            raise exc
                        raise RuntimeError("service exited unexpectedly")
                    healthy = spec.healthcheck()
                    if inspect.isawaitable(healthy):
                        healthy = await healthy
                    if not healthy:
                        # A single polling/updater sample can be false during a
                        # harmless Telegram reconnect. Require three consecutive
                        # failed probes before restarting the service.
                        item.consecutive_health_failures += 1
                        item.status = "degraded"
                        if item.consecutive_health_failures < 3:
                            continue
                        raise RuntimeError("service health check failed repeatedly")
                    item.consecutive_health_failures = 0
                    item.status = "healthy"
                    item.last_error = None
                    item.last_healthy_monotonic = time.monotonic()
                    if time.monotonic() - (item.last_started_monotonic or 0) >= 300:
                        failures = 0
            except asyncio.CancelledError:
                local_stop.set()
                service_task.cancel()
                await asyncio.gather(service_task, return_exceptions=True)
                raise
            except Exception as exc:  # service boundary intentionally catches everything
                item.status = "restarting"
                item.last_error = f"{type(exc).__name__}: {exc}"
                item.restarts += 1
                failures += 1
                logger.exception("service %s failed; restart scheduled", spec.name)
                local_stop.set()
                service_task.cancel()
                await asyncio.gather(service_task, return_exceptions=True)
                delay = min(self.restart_cap, self.restart_base * (2 ** min(failures - 1, 8)))
                try:
                    await asyncio.wait_for(self.stop.wait(), timeout=delay)
                except TimeoutError:
                    pass
            finally:
                local_stop.set()
        item.status = "stopped"

    async def _monitor_loop(self) -> None:
        while not self.stop.is_set():
            rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
            if rss_mb >= self.memory_warning_mb:
                logger.warning("high process memory watermark: %.1f MiB", rss_mb)
            logger.info(
                "supervisor heartbeat rss_mb=%.1f tasks=%d services=%d",
                rss_mb, len(asyncio.all_tasks()), len(self._tasks),
            )
            try:
                await asyncio.wait_for(self.stop.wait(), timeout=60)
            except TimeoutError:
                pass

    async def shutdown(self) -> None:
        self.stop.set()
        for task in self._tasks.values():
            task.cancel()
        if self._monitor:
            self._monitor.cancel()
        await asyncio.gather(*self._tasks.values(), return_exceptions=True)
        if self._monitor:
            await asyncio.gather(self._monitor, return_exceptions=True)
        for spec in self.specs:
            state(spec.name).status = "stopped"