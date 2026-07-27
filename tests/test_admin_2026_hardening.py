"""Regression contracts for the 2026 command-centre hardening."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_admin_mutations_have_origin_guard() -> None:
    text = (ROOT / "apps/admin/main.py").read_text(encoding="utf-8")
    assert 'request.method not in {"GET", "HEAD", "OPTIONS"}' in text
    assert "درخواست از مبدأ نامعتبر رد شد" in text


def test_admin_emergency_flags_are_allowlisted() -> None:
    text = (ROOT / "apps/admin/routers/country_admin.py").read_text(encoding="utf-8")
    for key in ("economy_frozen", "usd_market_frozen", "ads_frozen", "registrations_frozen"):
        assert key in text
    assert "if key not in allowed" in text


def test_daily_credit_requires_ledger_leg() -> None:
    text = (ROOT / "packages/core/services/daily.py").read_text(encoding="utf-8")
    assert "daily_ledger_conflict" in text
    assert "DO NOTHING RETURNING id" in text


def test_admin_has_retention_audit_and_ledger_views() -> None:
    html = (ROOT / "apps/admin/templates/dashboard.html").read_text(encoding="utf-8")
    js = (ROOT / "apps/admin/static/admin.js").read_text(encoding="utf-8")
    for view in ("engagement", "ledger", "audit", "controls"):
        assert f'id="view-{view}"' in html
        assert f"async function {view}" in js
    assert "prompt(" not in js


def test_forwarded_headers_are_not_globally_trusted() -> None:
    text = (ROOT / "run.py").read_text(encoding="utf-8")
    assert 'forwarded_allow_ips="*"' not in text
