"""Single entrypoint for all four services. One image, four Render services."""

from __future__ import annotations

import os
import sys

from packages.core.settings import Service


def main() -> None:
    raw = os.getenv("SERVICE", Service.TELELIFE.value).strip().lower()
    try:
        service = Service(raw)
    except ValueError:
        sys.exit(f"Unknown SERVICE={raw!r}. Expected: {[s.value for s in Service]}")

    if service is Service.TELELIFE:
        from apps.telelife_bot.main import main as run_service

        run_service()
    elif service is Service.TELEWORLD:
        from apps.teleworld_bot.main import main as run_service

        run_service()
    elif service is Service.SCHEDULER:
        from apps.scheduler.main import main as run_service

        run_service()
    else:
        import uvicorn

        from packages.core.settings import get_settings

        settings = get_settings()
        uvicorn.run(
            "apps.admin.main:app",
            host=settings.host,
            port=settings.port,
            log_config=None,
            access_log=False,
        )


if __name__ == "__main__":
    main()