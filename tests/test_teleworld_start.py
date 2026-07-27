from __future__ import annotations
from apps.teleworld_bot.handlers import status


def test_teleworld_registers_start_and_menu_callbacks() -> None:
    class App:
        def __init__(self) -> None:
            self.handlers = []
        def add_handler(self, handler) -> None:  # type: ignore[no-untyped-def]
            self.handlers.append(handler)
    app = App()
    status.register(app)
    commands = {
        command
        for handler in app.handlers
        for command in getattr(handler, "commands", set())
    }
    assert {"start", "status", "help"} <= commands
    assert any(getattr(handler, "pattern", None) for handler in app.handlers)