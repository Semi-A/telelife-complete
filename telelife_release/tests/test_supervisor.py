from __future__ import annotations
import asyncio
from packages.core.supervisor import ServiceSpec, ServiceSupervisor

async def test_crashed_service_restarts_without_stopping_peer():
    crashes = 0
    peer_ticks = 0
    async def flaky(stop: asyncio.Event) -> None:
        nonlocal crashes
        crashes += 1
        if crashes == 1:
            raise RuntimeError("boom")
        await stop.wait()
    async def peer(stop: asyncio.Event) -> None:
        nonlocal peer_ticks
        while not stop.is_set():
            peer_ticks += 1
            await asyncio.sleep(0.005)
    supervisor = ServiceSupervisor(
        [ServiceSpec("flaky-test", flaky, lambda: True), ServiceSpec("peer-test", peer, lambda: True)],
        health_interval=0.01, restart_base=0.01, restart_cap=0.02,
    )
    task = asyncio.create_task(supervisor.run())
    await asyncio.sleep(0.08)
    supervisor.stop.set()
    await task
    assert crashes >= 2
    assert peer_ticks > 2