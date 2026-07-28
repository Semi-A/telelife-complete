"""Contextual guidance and previews for the active TeleLife panel."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from html import escape
from typing import Any

from packages.core.config import get_config
from packages.core.repositories import production_repo
from packages.core.services import daily, missions, personal_economy, production, usd_market
from packages.core.utils import fmt

HOUSING_FA = {"room": "اتاق", "apartment": "آپارتمان", "villa": "ویلا"}


@dataclass(frozen=True, slots=True)
class TodayView:
    text: str
    actions: tuple[str, ...]


async def today_view(player: Any) -> TodayView:
    """Show one clear next action, then compact supporting status."""
    streak, _, last_claim = await daily.state(player.id)
    ready_daily = daily.claimable(last_claim)
    items = await missions.ensure_today(player.id, max(1, player.level))
    completed = sum(1 for item in items if item.done)
    claimable = sum(1 for item in items if item.done and not item.claimed)
    economy = await personal_economy.view(player.id)
    job = await production_repo.get(player.id)
    accrual = production.accrue(job, datetime.now(UTC)) if job else None

    if ready_daily:
        next_action, next_label = "daily", "🎁 هدیه آماده‌ات را بگیر"
        why = "پول و تجربه می‌گیری و زنجیره حضورت حفظ می‌شود."
    elif claimable:
        next_action, next_label = "missions", "🎯 پاداش کار کامل‌شده را بگیر"
        why = "پاداش آماده است؛ دریافتش سطحت را جلو می‌برد."
    elif not job:
        next_action, next_label = "jobs", "💼 یک شغل انتخاب کن"
        why = "درآمد شغل با گذشت زمان جمع می‌شود و مهارت می‌سازد."
    elif accrual and accrual.stored > 0:
        next_action, next_label = "jobs", "💰 نتیجه شیفت را دریافت کن"
        why = "درآمد، تجربه و اثر کارت روی کشور ثبت می‌شود."
    elif economy.living_due:
        next_action, next_label = "economy", "🧾 هزینه زندگی را بررسی کن"
        why = "پرداخت منظم از جمع‌شدن بدهی جلوگیری می‌کند."
    else:
        next_action, next_label = "missions", "🎯 یکی از کارهای امروز را جلو ببر"
        why = "سریع‌ترین راه دریافت تجربه و بازکردن امکانات تازه است."

    job_status = "شغل نداری" if not job else (f"{fmt.number(accrual.stored)} واحد درآمد آماده" if accrual and accrual.stored else "درآمد در حال جمع‌شدن")
    rows = [
        "☀️ <b>امروز من</b>", "",
        "🎯 <b>بهترین کار الان</b>", next_label, why, "",
        "<b>وضعیت کوتاه</b>",
        f"🎁 هدیه: {'آماده' if ready_daily else 'گرفته شده'} · زنجیره {fmt.number(streak)} روز",
        f"🎯 کارها: {fmt.number(completed)} از {fmt.number(len(items))} کامل" + (f" · {fmt.number(claimable)} پاداش آماده" if claimable else ""),
        f"💼 شغل: {job_status}",
        f"🧾 هزینه زندگی: {fmt.toman(economy.living_due) if economy.living_due else 'تسویه'}",
        "", "روزانه چند دقیقه کافی است؛ اول دکمه رنگی را بزن.",
    ]
    extras = [a for a in ("daily" if ready_daily else None, "missions" if claimable else None, "jobs" if job else None, "economy" if economy.living_due else None) if a and a != next_action]
    return TodayView("\n".join(rows), tuple([next_action, *extras[:2]]))


def upgrade_preview(row: Any, kind: str, wallet: int) -> str:
    cfg = get_config()
    current = int(row[f"{kind}_level"])
    target = current + 1
    section = "jobs.storage.upgrade_cost_toman" if kind == "storage" else "jobs.production_levels.upgrade_cost_toman"
    if not cfg.has(f"{section}.{target}"):
        raise ValueError("max_level_reached")
    cost = cfg.int_(f"{section}.{target}")
    title = "ظرفیت انبار" if kind == "storage" else "بازده تولید"
    extra = "ساعت بیشتری پیش از پرشدن انبار فرصت داری." if kind == "storage" else "سرعت درآمد شغل افزایش می‌یابد."
    return (f"⚙️ <b>پیش‌نمایش ارتقای {title}</b>\n\n"
            f"سطح فعلی: <b>{fmt.number(current)}</b>\nسطح جدید: <b>{fmt.number(target)}</b>\n"
            f"هزینه: <b>{fmt.toman(cost)}</b>\nموجودی پس از ارتقا: <b>{fmt.toman(wallet-cost)}</b>\n\n{extra}")


def housing_preview(player: Any, code: str, tenure: str) -> str:
    spec = get_config().section("phase3.housing.options").get(code)
    if not spec:
        raise ValueError("invalid_housing")
    cost = int(spec["weekly_rent_toman"] if tenure == "rent" else spec["purchase_toman"])
    title = escape(str(spec.get("title") or HOUSING_FA.get(code, code)))
    mode = "اجاره هفت‌روزه" if tenure == "rent" else "خرید دائمی"
    return (f"🏠 <b>پیش‌نمایش {mode} {title}</b>\n\nهزینه: <b>{fmt.toman(cost)}</b>\n"
            f"هزینه زندگی روزانه: <b>{fmt.toman(int(spec.get('daily_living_toman',0)))}</b>\n"
            f"حداقل سطح: <b>{fmt.number(spec['min_level'])}</b>\n"
            f"موجودی پس از پرداخت: <b>{fmt.toman(player.wallet_toman-cost)}</b>\n\n"
            "با تأیید، خانه فعلی جایگزین می‌شود و اثر شادی آن اعمال خواهد شد.")


async def market_preview(player: Any, side: str, cents: int) -> str:
    view = await usd_market.view()
    unit = view.buy_price if side == "buy" else view.sell_price
    toman = unit * cents // 100
    fee_bp = get_config().int_("market.usd.fee_basis_points")
    fee = toman * fee_bp // 10_000
    total = toman + fee if side == "buy" else toman - fee
    after_wallet = player.wallet_toman - total if side == "buy" else player.wallet_toman + total
    after_usd = player.usd_cents + cents if side == "buy" else player.usd_cents - cents
    verb = "خرید" if side == "buy" else "فروش"
    return (f"💵 <b>پیش‌نمایش {verb} {fmt.usd(cents)}</b>\n\nنرخ محاسبه: <b>{fmt.toman(unit)}</b>\n"
            f"ارزش معامله: <b>{fmt.toman(toman)}</b>\nکارمزد: <b>{fmt.toman(fee)}</b>\n"
            f"دریافت/پرداخت نهایی: <b>{fmt.toman(total)}</b>\n\n"
            f"کیف پول پس از معامله: <b>{fmt.toman(after_wallet)}</b>\nدلار پس از معامله: <b>{fmt.usd(after_usd)}</b>")


def actionable_error(code: str, *, player: Any | None = None) -> str:
    messages = {
        "insufficient_balance": "❌ <b>موجودی کافی نیست</b>\n\nمبلغ لازم بیشتر از کیف پول فعلی است. درآمد شغل را دریافت کن، مبلغ کمتری انتخاب کن یا از پس‌انداز برداشت کن.",
        "insufficient_player_balance": "❌ <b>موجودی کافی نیست</b>\n\nابتدا درآمد آماده را دریافت کن یا موجودی کیف پول را افزایش بده.",
        "housing_locked": "🔒 <b>این خانه هنوز باز نشده است</b>\n\nدر صفحه مرکز پیشرفت، سطح لازم و بهترین مسیر رسیدن به آن را ببین.",
        "market_locked": "🔒 <b>بازار ارز از سطح ۱۰ باز می‌شود</b>\n\nمأموریت‌ها و نتیجه شیفت‌ها سریع‌ترین مسیر دریافت تجربه‌اند.",
        "job_not_found": "💼 <b>هنوز شغلی نداری</b>\n\nابتدا یک شغل انتخاب کن تا درآمد با گذشت زمان جمع شود.",
        "max_level_reached": "✅ <b>این بخش در بالاترین سطح است</b>\n\nنیازی به ارتقای بیشتر نیست؛ روی دارایی یا هدف بعدی تمرکز کن.",
        "market_frozen": "⏸ <b>بازار موقتاً متوقف است</b>\n\nقیمت‌ها قابل مشاهده‌اند، اما معامله تا بازشدن بازار انجام نمی‌شود.",
    }
    return messages.get(code, "❌ عملیات کامل نشد. صفحه را تازه کن و شرایط نمایش‌داده‌شده را دوباره بررسی کن.")
