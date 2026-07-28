"""Stable Persian labels for internal product codes shown to users."""
from __future__ import annotations

GOVERNMENT_NAMES: dict[str, str] = {
    "republic": "جمهوری",
    "presidential": "جمهوری ریاستی",
    "parliamentary": "نظام پارلمانی",
    "semi_presidential": "نظام نیمه‌ریاستی",
    "monarchy": "پادشاهی مطلقه",
    "constitutional_monarchy": "پادشاهی مشروطه",
    "dictatorship": "دیکتاتوری",
    "federal": "نظام فدرال",
    "council": "نظام شورایی",
    "direct_democracy": "دموکراسی مستقیم",
    "theocracy": "حکومت دینی",
    "military_junta": "شورای نظامی",
    "oligarchy": "الیگارشی",
}

def government_name(code: object) -> str:
    """Never leak an English government code into a user-facing surface."""
    return GOVERNMENT_NAMES.get(str(code), "نوع حکومت نامشخص")