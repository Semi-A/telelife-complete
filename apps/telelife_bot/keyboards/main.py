"""Glass keyboards for TeleLife.

Colour policy, applied consistently everywhere:
  PRIMARY (blue)  - the single action we want tapped. Max one per keyboard.
  SUCCESS (green) - a reward is waiting to be collected. Earned, not decorative.
  DANGER  (red)   - destructive or irreversible. Never used for navigation.
  GLASS           - everything else. Default translucent Telegram look.
"""

from __future__ import annotations

from telegram import InlineKeyboardMarkup

from apps.telelife_bot.texts import fa
from packages.core.ui import Keyboard, Style, button, cb

NS = "tl"


def profile_panel(owner_id: int, *, daily_ready: bool, missions_unlocked: bool) -> InlineKeyboardMarkup:
    kb = Keyboard()
    kb.row(
        button(
            fa.BTN_DAILY_READY if daily_ready else fa.BTN_DAILY,
            cb(NS, "daily", owner_id),
            style=Style.SUCCESS if daily_ready else Style.GLASS,
        )
    )
    second = [button(fa.BTN_UNLOCKS, cb(NS, "unlocks", owner_id))]
    if missions_unlocked:
        second.insert(0, button(fa.BTN_MISSIONS, cb(NS, "missions", owner_id)))
    kb.row(*second)
    kb.row(button(fa.BTN_REFRESH, cb(NS, "profile", owner_id)))
    return kb.build()


def daily_panel(owner_id: int, *, claimable: bool) -> InlineKeyboardMarkup:
    kb = Keyboard()
    if claimable:
        kb.row(button(fa.BTN_CLAIM, cb(NS, "claim", owner_id), style=Style.PRIMARY))
    kb.row(
        button(fa.BTN_MISSIONS, cb(NS, "missions", owner_id)),
        button(fa.BTN_BACK, cb(NS, "profile", owner_id)),
    )
    return kb.build()


def missions_panel(owner_id: int, claimable_keys: list[str]) -> InlineKeyboardMarkup:
    kb = Keyboard()
    kb.grid(
        [
            button(
                f"{fa.BTN_CLAIM} {i + 1}",
                cb(NS, "mclaim", owner_id, key),
                style=Style.SUCCESS,
            )
            for i, key in enumerate(claimable_keys)
        ],
        per_row=2,
    )
    kb.row(
        button(fa.BTN_REFRESH, cb(NS, "missions", owner_id)),
        button(fa.BTN_BACK, cb(NS, "profile", owner_id)),
    )
    return kb.build()


def unlocks_panel(owner_id: int) -> InlineKeyboardMarkup:
    return Keyboard().row(button(fa.BTN_BACK, cb(NS, "profile", owner_id))).build()


def level_up_panel(owner_id: int) -> InlineKeyboardMarkup:
    return (
        Keyboard()
        .row(button(fa.BTN_PROFILE, cb(NS, "profile", owner_id), style=Style.PRIMARY))
        .build()
    )
