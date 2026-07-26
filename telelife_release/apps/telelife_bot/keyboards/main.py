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
    kb.row(button(fa.BTN_ECONOMY, cb(NS,"economy",owner_id), style=Style.PRIMARY), button(fa.BTN_JOBS, cb(NS,"jobs",owner_id)))
    kb.row(button(fa.BTN_MARKET, cb(NS,"market",owner_id)), button(fa.BTN_REFRESH, cb(NS, "profile", owner_id)))
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

def economy_panel(owner_id: int) -> InlineKeyboardMarkup:
    return (Keyboard()
        .row(button(fa.BTN_SAVINGS, cb(NS,"savings",owner_id), style=Style.PRIMARY), button(fa.BTN_HOUSING, cb(NS,"housing",owner_id)))
        .row(button("🧾 پرداخت هزینه زندگی",cb(NS,"living",owner_id),style=Style.SUCCESS),button(fa.BTN_BACK,cb(NS,"profile",owner_id)))
        .build())

def savings_panel(owner_id:int)->InlineKeyboardMarkup:
    return (Keyboard()
      .row(button("واریز ۵۰ هزار",cb(NS,"deposit",owner_id,"50000"),style=Style.PRIMARY),button("برداشت ۵۰ هزار",cb(NS,"withdraw",owner_id,"50000")))
      .row(button("واریز ۲۰۰ هزار",cb(NS,"deposit",owner_id,"200000")),button("برداشت ۲۰۰ هزار",cb(NS,"withdraw",owner_id,"200000")))
      .row(button(fa.BTN_BACK,cb(NS,"economy",owner_id))).build())

def housing_panel(owner_id:int)->InlineKeyboardMarkup:
    return (Keyboard()
      .row(button("اجاره اتاق",cb(NS,"hrent",owner_id,"room"),style=Style.PRIMARY),button("خرید اتاق",cb(NS,"hbuy",owner_id,"room")))
      .row(button("اجاره آپارتمان",cb(NS,"hrent",owner_id,"apartment")),button("خرید آپارتمان",cb(NS,"hbuy",owner_id,"apartment")))
      .row(button("خرید ویلا",cb(NS,"hbuy",owner_id,"villa")),button(fa.BTN_BACK,cb(NS,"economy",owner_id))).build())

def jobs_panel(owner_id:int,has_job:bool)->InlineKeyboardMarkup:
    kb=Keyboard()
    if has_job:
      kb.row(button(fa.BTN_COLLECT_JOB,cb(NS,"jcollect",owner_id),style=Style.SUCCESS))
      kb.row(button(fa.BTN_UPGRADE_PRODUCTION,cb(NS,"jupgrade",owner_id,"production"),style=Style.PRIMARY),button(fa.BTN_UPGRADE_STORAGE,cb(NS,"jupgrade",owner_id,"storage")))
    else:
      kb.row(button("کشاورز",cb(NS,"jchoose",owner_id,"farmer"),style=Style.PRIMARY),button("برنامه‌نویس",cb(NS,"jchoose",owner_id,"programmer")))
      kb.row(button("بازرگان",cb(NS,"jchoose",owner_id,"trader")),button("مهندس",cb(NS,"jchoose",owner_id,"engineer")))
      kb.row(button("پزشک",cb(NS,"jchoose",owner_id,"doctor")),button("روزنامه‌نگار",cb(NS,"jchoose",owner_id,"journalist")))
    kb.row(button(fa.BTN_BACK,cb(NS,"profile",owner_id)))
    return kb.build()

def market_panel(owner_id:int)->InlineKeyboardMarkup:
    return (Keyboard()
      .row(button("خرید ۱۰ دلار",cb(NS,"mbuy",owner_id,"1000"),style=Style.PRIMARY),button("فروش ۱۰ دلار",cb(NS,"msell",owner_id,"1000")))
      .row(button("خرید ۵۰ دلار",cb(NS,"mbuy",owner_id,"5000")),button("فروش ۵۰ دلار",cb(NS,"msell",owner_id,"5000")))
      .row(button(fa.BTN_REFRESH,cb(NS,"market",owner_id)),button(fa.BTN_BACK,cb(NS,"profile",owner_id))).build())
