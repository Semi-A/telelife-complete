"""Contracts for the readable admin UI, truthful health and 30-minute market tape."""
from pathlib import Path


def test_market_api_builds_real_thirty_minute_ohlc() -> None:
    source = Path("packages/core/repositories/admin_repo.py").read_text(encoding="utf-8")
    assert "date_bin(interval '30 minutes'" in source
    for field in ("'open'", "'high'", "'low'", "'close'", "'samples'"):
        assert field in source
    assert "FROM market_price_snapshots" in source


def test_transient_health_failure_does_not_restart_bot() -> None:
    source = Path("packages/core/supervisor.py").read_text(encoding="utf-8")
    assert "consecutive_health_failures < 3" in source
    assert "service health check failed repeatedly" in source
    assert "item.last_error = None" in source


def test_health_endpoint_does_not_treat_reconnect_as_admin_failure() -> None:
    source = Path("apps/admin/main.py").read_text(encoding="utf-8")
    assert '{"starting", "healthy", "degraded"}' in source
    assert "Bot lifecycle states remain" in source


def test_admin_chart_is_interactive_and_snapshot_driven() -> None:
    js = Path("apps/admin/static/admin.js").read_text(encoding="utf-8")
    html = Path("apps/admin/templates/dashboard.html").read_text(encoding="utf-8")
    assert "data.candles" not in js  # rows expose candles directly per asset
    assert "selected.candles" in js
    assert "chart-cross-x" in js and "chart-tooltip" in js
    assert "setInterval" in js and "30000" in js
    assert "کندل‌های واقعی" in html and "تایم‌فریم ۳۰ دقیقه" in html


def test_admin_design_keeps_accessibility_basics() -> None:
    html = Path("apps/admin/templates/dashboard.html").read_text(encoding="utf-8")
    css = Path("apps/admin/static/admin.css").read_text(encoding="utf-8")
    assert 'aria-live="polite"' in html
    assert 'aria-label="تازه‌سازی داده‌ها"' in html
    assert "focus-visible" in css
    assert "prefers-reduced-motion" in css