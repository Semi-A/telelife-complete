"""Pure text builders. No Telegram, no I/O - just data in, string out."""

from __future__ import annotations

from apps.telelife_bot.texts import fa
from packages.core.models import Player
from packages.core.services import unlocks as unlock_svc
from packages.core.services.daily import DailyResult
from packages.core.services.missions import Mission
from packages.core.services.xp import XPResult
from packages.core.utils import fmt


def profile(player: Player, *, rank: int, streak: int, xp_needed: int) -> str:
    prestige_tag = (
        fa.PRESTIGE_TAG.format(prestige=fmt.number(player.prestige))
        if player.prestige
        else ""
    )
    return fa.PROFILE.format(
        name=player.first_name,
        level=fmt.number(player.level),
        prestige_tag=prestige_tag,
        rank=fmt.number(rank),
        xp_bar=fmt.progress_bar(player.xp, xp_needed, width=14),
        xp=fmt.number(player.xp),
        xp_needed=fmt.number(xp_needed),
        wallet=fmt.toman(player.wallet_toman),
        savings=fmt.toman(player.savings_toman),
        usd=fmt.usd(player.usd_cents),
        happiness=fmt.number(player.happiness),
        reputation=fmt.number(player.reputation),
        streak=fmt.number(streak),
        net_worth=fmt.toman(player.net_worth_toman),
    )


def daily_claimed(result: DailyResult) -> str:
    if result.next_milestone:
        remaining = result.next_milestone - result.streak
        next_line = fa.DAILY_NEXT_MILESTONE.format(days=fmt.number(remaining))
    else:
        next_line = ""

    text = fa.DAILY_CLAIMED.format(
        reward=fmt.toman(result.reward_toman),
        xp=fmt.number(result.reward_xp),
        streak=fmt.number(result.streak),
        next_line=next_line,
    )
    if result.milestone_label:
        text += fa.DAILY_MILESTONE.format(
            label=result.milestone_label, bonus=fmt.toman(result.milestone_toman)
        )
    return text


def daily_ready(streak: int, best: int) -> str:
    from packages.core.services import daily as daily_svc  # noqa: PLC0415

    today_amount = daily_svc.preview(streak + 1)
    tomorrow_amount = daily_svc.preview(streak + 2)
    return fa.DAILY_READY.format(
        streak=fmt.number(streak),
        best=fmt.number(best),
        amount=fmt.toman(today_amount),
        next_line=fa.DAILY_READY_NEXT.format(amount=fmt.toman(tomorrow_amount)),
    )


def daily_already(streak: int, tomorrow: int) -> str:
    return fa.DAILY_ALREADY.format(
        streak=fmt.number(streak), tomorrow=fmt.toman(tomorrow)
    )


def missions(items: list[Mission]) -> str:
    if not items:
        return fa.MISSIONS_EMPTY
    rows: list[str] = []
    for m in items:
        reward = fmt.toman(m.reward_toman)
        if m.claimed:
            rows.append(fa.MISSION_ROW_DONE.format(title=m.title, reward=reward))
        elif m.done:
            rows.append(
                fa.MISSION_ROW_READY.format(
                    title=m.title,
                    progress=fmt.number(m.progress),
                    target=fmt.number(m.target),
                    reward=reward,
                )
            )
        else:
            rows.append(
                fa.MISSION_ROW_OPEN.format(
                    title=m.title,
                    progress=fmt.number(m.progress),
                    target=fmt.number(m.target),
                    reward=reward,
                )
            )
    return fa.MISSIONS_HEADER.format(body="\n".join(rows))


def unlocks_map(level: int) -> str:
    catalogue = unlock_svc.catalogue()
    nxt = unlock_svc.next_unlock(level)
    rows: list[str] = []
    for u in catalogue:
        if u.level <= level:
            rows.append(fa.UNLOCK_ROW_OPEN.format(icon=u.icon, title=u.title))
        elif nxt and u.key == nxt.key:
            rows.append(
                fa.UNLOCK_ROW_NEXT.format(
                    icon=u.icon, title=u.title, level=fmt.number(u.level)
                )
            )
        else:
            rows.append(
                fa.UNLOCK_ROW_LOCKED.format(
                    icon=u.icon, title=u.title, level=fmt.number(u.level)
                )
            )
    return fa.UNLOCKS_HEADER.format(
        body="\n".join(rows),
        level=fmt.number(level),
        next_level=fmt.number(nxt.level) if nxt else fmt.number(level),
    )


def level_up(result: XPResult) -> str:
    opened = unlock_svc.unlocked_at(result.level_after)
    if opened:
        unlock_line = "\n".join(
            fa.LEVEL_UP_UNLOCK.format(icon=u.icon, title=u.title) for u in opened
        )
    else:
        nxt = unlock_svc.next_unlock(result.level_after)
        unlock_line = (
            fa.LEVEL_UP_NEXT.format(
                level=fmt.number(nxt.level), icon=nxt.icon, title=nxt.title
            )
            if nxt
            else ""
        )
    return fa.LEVEL_UP.format(
        level=fmt.number(result.level_after),
        reward=fmt.toman(result.reward_toman),
        unlock_line=unlock_line,
    )