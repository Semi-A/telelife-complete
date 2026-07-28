"""Persian-first formatting helpers. Numbers must always look native."""

from __future__ import annotations

_FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def group_digits(value: int) -> str:
    return f"{value:,}".replace(",", "٬")


def fa_digits(text: str) -> str:
    return text.translate(_FA_DIGITS)


def toman(amount: int, *, persian: bool = True) -> str:
    out = f"{group_digits(amount)} تومان"
    return fa_digits(out) if persian else out


def usd(cents: int, *, persian: bool = True) -> str:
    whole, frac = divmod(abs(cents), 100)
    sign = "-" if cents < 0 else ""
    out = f"{sign}{group_digits(whole)}.{frac:02d}$"
    return fa_digits(out) if persian else out


def number(value: int, *, persian: bool = True) -> str:
    out = group_digits(value)
    return fa_digits(out) if persian else out


def progress_bar(current: int, total: int, width: int = 10) -> str:
    if total <= 0:
        return "▱" * width
    filled = max(0, min(width, round(current / total * width)))
    return "▰" * filled + "▱" * (width - filled)