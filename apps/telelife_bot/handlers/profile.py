"""/profile - the first screen that must feel premium."""

from __future__ import annotations

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from apps.telelife_bot.texts import fa
from packages.core.repositories import player_repo
from packages.core.services import progression
from packages.core.utils import fmt


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = update.effective_message
    if user is None or message is None:
        return

    player = await player_repo.get_or_create(
        user.id,
        username=user.username,
        first_name=user.first_name or "رفیق",
        language_code=user.language_code or "fa",
    )

    if not player.playable:
        text = (
            fa.BANNED.format(reason=player.ban_reason or fa.NO_REASON)
            if player.is_banned
            else fa.FROZEN
        )
        await message.reply_text(text)
        return

    current_xp, needed = progression.level_progress(player.level, player.xp)

    await message.reply_text(
        fa.PROFILE.format(
            name=player.first_name,
            level=fmt.number(player.level),
            prestige=fmt.number(player.prestige),
            xp_bar=fmt.progress_bar(current_xp, needed),
            xp=fmt.number(current_xp),
            xp_needed=fmt.number(needed),
            wallet=fmt.toman(player.wallet_toman),
            savings=fmt.toman(player.savings_toman),
            usd=fmt.usd(player.usd_cents),
            happiness=fmt.number(player.happiness),
            reputation=fmt.number(player.reputation),
            net_worth=fmt.toman(player.net_worth_toman),
        )
    )


def register(application) -> None:  # type: ignore[no-untyped-def]
    application.add_handler(CommandHandler("profile", profile))