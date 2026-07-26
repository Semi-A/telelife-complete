"""Glass keyboard system (Bot API 9.4 button styles).

Telegram exposes exactly three styles: primary / success / danger.
No style = the default translucent "glass" background - our neutral default.

Rules enforced here:
- Colour is emphasis, never meaning. Button text must stand alone.
- At most ONE primary per keyboard. Colour everywhere = colour nowhere.
- Old clients silently ignore `style`, so layouts must read fine uncoloured.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Self

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Style(StrEnum):
    """Bot API 9.4 button styles. GLASS means: send no style field at all."""

    GLASS = "glass"
    PRIMARY = "primary"
    SUCCESS = "success"
    DANGER = "danger"


def button(
    text: str,
    callback_data: str,
    *,
    style: Style = Style.GLASS,
    icon_custom_emoji_id: str | None = None,
) -> InlineKeyboardButton:
    """Build one button. GLASS omits `style` so the client uses its default."""
    kwargs: dict[str, object] = {"text": text, "callback_data": callback_data}
    if style is not Style.GLASS:
        kwargs["style"] = style.value
    if icon_custom_emoji_id:
        kwargs["icon_custom_emoji_id"] = icon_custom_emoji_id
    return InlineKeyboardButton(**kwargs)  # type: ignore[arg-type]


def url_button(text: str, url: str, *, style: Style = Style.GLASS) -> InlineKeyboardButton:
    kwargs: dict[str, object] = {"text": text, "url": url}
    if style is not Style.GLASS:
        kwargs["style"] = style.value
    return InlineKeyboardButton(**kwargs)  # type: ignore[arg-type]


class Keyboard:
    """Small fluent builder. Keeps handlers free of nested list noise."""

    __slots__ = ("_rows",)

    def __init__(self) -> None:
        self._rows: list[list[InlineKeyboardButton]] = []

    def row(self, *buttons: InlineKeyboardButton) -> Self:
        if buttons:
            self._rows.append(list(buttons))
        return self

    def add(
        self,
        text: str,
        callback_data: str,
        *,
        style: Style = Style.GLASS,
        icon_custom_emoji_id: str | None = None,
    ) -> Self:
        return self.row(
            button(text, callback_data, style=style, icon_custom_emoji_id=icon_custom_emoji_id)
        )

    def grid(self, buttons: list[InlineKeyboardButton], per_row: int = 2) -> Self:
        for i in range(0, len(buttons), per_row):
            self.row(*buttons[i : i + per_row])
        return self

    def build(self) -> InlineKeyboardMarkup:
        self._assert_single_primary()
        return InlineKeyboardMarkup(self._rows)

    def _assert_single_primary(self) -> None:
        primaries = sum(
            1
            for row in self._rows
            for b in row
            if getattr(b, "style", None) == Style.PRIMARY.value
        )
        if primaries > 1:
            raise ValueError(
                f"Keyboard has {primaries} primary buttons. Exactly one action leads."
            )