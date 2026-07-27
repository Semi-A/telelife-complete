"""Unicode-aware Persian content moderation with bounded obfuscation detection.

The matcher is deliberately boundary-aware: it catches separators and repeated letters
inside a blocked token, but does not reject a longer innocent word merely because it
contains the same substring.
"""
from __future__ import annotations
from dataclasses import dataclass
import re
import unicodedata

@dataclass(frozen=True, slots=True)
class ModerationResult:
    allowed: bool
    category: str | None = None

# Keep the public response generic; never echo an offensive value back to a group.
TERMS: dict[str, tuple[str, ...]] = {
    "sexual": ("کون", "کس", "کیر", "جنده", "پورن", "سکس"),
    "insult": ("حرومزاده", "بی ناموس", "مادر قحبه", "کصخل"),
    "political_extremism": ("داعش", "نازی", "فاشیست"),
}
_CHAR_MAP = str.maketrans({"ي":"ی", "ى":"ی", "ك":"ک", "ة":"ه", "ۀ":"ه", "ؤ":"و", "إ":"ا", "أ":"ا"})
_SEP = r"[\s\-_.ـ‌‍]*"
_WORD = r"\w"

def normalize(text: str) -> str:
    value = unicodedata.normalize("NFKC", text).translate(_CHAR_MAP).casefold()
    value = "".join(ch for ch in value if unicodedata.category(ch) not in {"Mn", "Cf"})
    return value

def _pattern(term: str) -> re.Pattern[str]:
    chars = [c for c in normalize(term) if c.isalnum()]
    body = _SEP.join(re.escape(c) + "+" for c in chars)
    # Persian has no case distinction; Unicode word boundaries prevent false positives
    # such as the blocked token being only the prefix of a longer name.
    return re.compile(rf"(?<!{_WORD}){body}(?!{_WORD})", re.UNICODE)

_PATTERNS = [(category, _pattern(term)) for category, terms in TERMS.items() for term in terms]

def inspect(text: str) -> ModerationResult:
    value = normalize(text)
    for category, pattern in _PATTERNS:
        if pattern.search(value):
            return ModerationResult(False, category)
    return ModerationResult(True)

def require_clean(text: str, field: str = "content") -> None:
    result = inspect(text)
    if not result.allowed:
        raise ValueError(f"inappropriate_{field}")
