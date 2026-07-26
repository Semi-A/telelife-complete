"""Container entrypoint dispatching exactly one configured service."""

from __future__ import annotations

import os


def main() -> None:
    service = os.getenv("SERVICE", "telelife").strip().lower()
    if service == "telelife":
        from apps.telelife_bot.main import main as target
    elif service == "teleworld":
        from apps.teleworld_bot.main import main as target
    elif service == "scheduler":
        from apps.scheduler.main import main as target
    elif service == "admin":
        import uvicorn
        from packages.core.settings import get_settings

        settings = get_settings()
        uvicorn.run(
            "apps.admin.main:app",
            host=settings.host,
            port=settings.port,
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
        return
    else:
        raise SystemExit(f"Unknown SERVICE value: {service!r}")
    target()


if __name__ == "__main__":
    main()
