"""Regression guards for the 2026-07-27 clean rebuild."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def source(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_ledger_economic_parameters_have_explicit_bigint_types() -> None:
    text = source("packages/core/repositories/ledger_repo.py")
    assert "wallet_toman+$2::bigint" in text
    assert "usd_cents+$2::bigint" in text
    assert "SELECT $1::bigint,$2::text,$3::bigint" in text
    assert "quantity=player_resources.quantity+$3::bigint" in text
    assert "quantity=country_resources.quantity+$3::bigint" in text


def test_usd_trade_deltas_have_explicit_bigint_types() -> None:
    text = source("packages/core/services/usd_market.py")
    assert "wallet_toman=wallet_toman+$2::bigint" in text
    assert "usd_cents=usd_cents+$3::bigint" in text


def test_telelife_market_is_text_only() -> None:
    text = source("apps/telelife_bot/handlers/life.py")
    market = text[text.index("async def market(ctx,c):"):text.index("async def unlock_page")]
    assert "send_photo" not in market
    assert "InputFile" not in market
    assert "market_chart" not in market
    assert "قیمت خرید" in market
    assert "قیمت فروش" in market
    assert "شاخص سلامت" in market


def test_job_is_user_selected_from_level_one() -> None:
    config = source("packages/core/config/data/jobs.yaml")
    keyboard = source("apps/telelife_bot/keyboards/main.py")
    text = source("apps/telelife_bot/texts/fa.py")
    assert "available_from_level: 1" in config
    for code in ("farmer", "miner", "programmer", "trader", "engineer", "doctor", "journalist"):
        assert f'"{code}"' in keyboard
    assert "از همان سطح ۱ شغلت را خودت انتخاب کن" in text
    assert "سطح ۵ شغل" not in text