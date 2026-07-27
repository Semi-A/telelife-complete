"""/start and /help for TeleLife."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from apps.telelife_bot.handlers.common import resolve
from apps.telelife_bot.keyboards import main as kb
from apps.telelife_bot.texts import fa
from packages.core.config import get_config
from packages.core.repositories import player_repo
from packages.core.services import daily
from packages.core.utils import fmt


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if user is None:
        return
    existing = await player_repo.get_by_telegram_id(user.id)

    ctx = await resolve(update)
    if ctx is None:
        return

    if existing is None:
        cfg = get_config()
        text = fa.WELCOME_NEW.format(
            name=ctx.player.first_name,
            wallet=fmt.toman(cfg.int_("economy.starting_balance.wallet_toman")),
        )
    else:
        text = fa.WELCOME_BACK.format(
            name=ctx.player.first_name,
            level=fmt.number(ctx.player.level),
            wallet=fmt.toman(ctx.player.wallet_toman),
        )

    _, _, last_claim = await daily.state(ctx.player.id)
    await ctx.message.reply_text(
        text,
        reply_markup=kb.profile_panel(
            ctx.telegram_id,
            daily_ready=daily.claimable(last_claim),
            missions_unlocked=ctx.player.level >= 2,
        ),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(fa.HELP)


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("start", start))