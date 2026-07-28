"""Safe plain-text rendering for Telegram messages.

The bots intentionally use no HTML parse mode. This sanitizer prevents legacy
formatting tags stored in old text or database content from appearing raw.
"""
from __future__ import annotations
import re

_TELEGRAM_TAG = re.compile(
    r"</?(?:b|strong|i|em|u|ins|s|strike|del|code|pre|blockquote|tg-spoiler)(?:\s[^>]*)?>",
    re.IGNORECASE,
)

def plain_text(value: object) -> str:
    """Return readable Telegram text with legacy formatting tags removed."""
    return _TELEGRAM_TAG.sub("", str(value))