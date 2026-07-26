"""Profile, daily, missions and the unlock map - commands plus glass callbacks."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CallbackQueryHandler, ContextTypes

from apps.telelife_bot.handlers.common import Ctx, guard_callback, resolve, send_panel
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from apps.telelife_bot.views import render
from packages.core.repositories import player_repo, progression_repo
from packages.core.services import daily, missions, progression, xp
from packages.core.utils import fmt

MISSIONS_UNLOCK_LEVEL = 2


async def _announce_level_up(ctx: Ctx, result: xp.XPResult) -> None:
    if not result.leveled_up:
        return
    await ctx.message.reply_text(
        render.level_up(result), reply_markup=kb.level_up_panel(ctx.telegram_id)
    )


async def _render_profile(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    result = await xp.grant(
        ctx.player.id, "profile_view", idempotency_key=xp.day_key("profile", ctx.player.id)
    )
    player = await player_repo.get_by_telegram_id(ctx.telegram_id) or ctx.player

    streak, _, last_claim = await daily.state(player.id)
    rank = await progression_repo.rank_by_level(player.id)
    _, needed = progression.level_progress(player.level, player.xp)

    text = render.profile(player, rank=rank, streak=streak, xp_needed=needed)
    markup = kb.profile_panel(
        ctx.telegram_id,
        daily_ready=daily.claimable(last_claim),
        missions_unlocked=player.level >= MISSIONS_UNLOCK_LEVEL,
    )
    await send_panel(context, ctx.message, text, markup, "profile", edit=edit)
    await missions.report_progress(player.id, "check_profile")
    await _announce_level_up(ctx, result)


async def _render_daily(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    streak, best, last_claim = await daily.state(ctx.player.id)
    can_claim = daily.claimable(last_claim)
    if can_claim:
        text = render.daily_ready(streak, best)
    else:
        text = render.daily_already(streak, daily.tomorrow_preview(streak))
    await send_panel(
        context,
        ctx.message,
        text,
        kb.daily_panel(ctx.telegram_id, claimable=can_claim),
        "profile",
        edit=edit,
    )


async def _render_missions(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    if ctx.player.level < MISSIONS_UNLOCK_LEVEL:
        await ctx.message.reply_text(fa.MISSIONS_LOCKED)
        return
    items = await missions.ensure_today(ctx.player.id, ctx.player.level)
    ready = [m.key for m in items if m.done and not m.claimed]
    await send_panel(
        context, ctx.message, render.missions(items),
        kb.missions_panel(ctx.telegram_id, ready), "profile", edit=edit,
    )


async def _render_unlocks(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, *, edit: bool) -> None:
    await send_panel(
        context, ctx.message, render.unlocks_map(ctx.player.level),
        kb.unlocks_panel(ctx.telegram_id), "profile", edit=edit,
    )


# ---------------- commands ----------------

async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_profile(ctx, context, edit=False)


async def cmd_daily(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_daily(ctx, context, edit=False)


async def cmd_missions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_missions(ctx, context, edit=False)


async def cmd_unlocks(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    ctx = await resolve(update)
    if ctx:
        await _render_unlocks(ctx, context, edit=False)


# ---------------- callbacks ----------------

async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    parsed = await guard_callback(update)
    query = update.callback_query
    if parsed is None or query is None:
        return
    ctx = await resolve(update)
    if ctx is None:
        await query.answer()
        return

    action = parsed.action
    if action == "profile":
        await query.answer()
        await _render_profile(ctx, context, edit=True)
    elif action == "daily":
        await query.answer()
        await _render_daily(ctx, context, edit=True)
    elif action == "missions":
        await query.answer()
        await _render_missions(ctx, context, edit=True)
    elif action == "unlocks":
        await query.answer()
        await _render_unlocks(ctx, context, edit=True)
    elif action == "claim":
        await _do_claim(ctx, context, update)
    elif action == "mclaim":
        await _do_mission_claim(ctx, context, update, parsed.arg)
    else:
        await query.answer()


async def _do_claim(ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, update: Update) -> None:
    query = update.callback_query
    assert query is not None

    result = await daily.claim(ctx.player.id)
    if result.already_claimed:
        await query.answer(fa.MISSION_NOT_READY, show_alert=False)
        await _render_daily(ctx, context, edit=True)
        return

    xp_result = await xp.grant(
        ctx.player.id,
        "daily_claim",
        idempotency_key=xp.day_key("daily", ctx.player.id),
        amount=result.reward_xp,
    )
    await missions.report_progress(ctx.player.id, "claim_daily")
    await missions.report_progress(ctx.player.id, "streak_keeper")

    text = render.daily_claimed(result)
    if xp_result.capped:
        text += fa.XP_CAPPED

    await query.answer()
    await send_panel(
        context, ctx.message, text,
        kb.daily_panel(ctx.telegram_id, claimable=False), "profile", edit=True,
    )
    await _announce_level_up(ctx, xp_result)


async def _do_mission_claim(
    ctx: Ctx, context: ContextTypes.DEFAULT_TYPE, update: Update, mission_key: str
) -> None:
    query = update.callback_query
    assert query is not None

    claimed = await missions.claim(ctx.player.id, mission_key)
    if claimed is None:
        await query.answer(fa.MISSION_NOT_READY, show_alert=True)
        return

    xp_result = await xp.grant(
        ctx.player.id,
        "mission_complete",
        idempotency_key=f"mission:{ctx.player.id}:{mission_key}:{xp.day_key('d', 0)}",
        amount=claimed.reward_xp,
    )
    await query.answer(
        fa.MISSION_CLAIMED.format(
            title=claimed.title,
            reward=fmt.toman(claimed.reward_toman),
            xp=fmt.number(claimed.reward_xp),
        ).replace("<b>", "").replace("</b>", "").replace("\n", " "),
        show_alert=True,
    )
    await _render_missions(ctx, context, edit=True)
    await _announce_level_up(ctx, xp_result)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CallbackQueryHandler(on_callback, pattern=r"^tl:"))