from pathlib import Path


def source(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_advertising_has_one_open_invoice_and_state_bound_precheckout():
    migration = source("migrations/0027_production_integrity_hardening.sql")
    commerce = source("packages/core/services/commerce.py")
    assert "uq_open_advertisement_invoice" in migration
    assert "ad_status" in commerce and "approved_unpaid" in commerce
    assert "duplicate_payment_charge" in commerce


def test_refund_uses_durable_claim_before_external_call():
    commerce = source("packages/core/services/commerce.py")
    router = source("apps/admin/routers/country_admin.py")
    assert "refund_pending" in commerce
    assert "begin_refund" in router and "finish_refund" in router
    assert router.index("begin_refund") < router.index("refund_star_payment")


def test_social_cash_help_writes_two_ledger_legs():
    social = source("packages/core/services/social.py")
    assert 'f"{key}:debit"' in social
    assert 'f"{key}:credit"' in social
    assert "citizen_help_ledger_conflict" in social


def test_daily_jobs_are_independently_guarded():
    scheduler = source("apps/scheduler/main.py")
    assert '("daily_reset", daily_reset.run)' in scheduler
    assert "await scheduler_ops.run(name, job)" in scheduler


def test_admin_authentication_is_throttled():
    migration = source("migrations/0027_production_integrity_hardening.sql")
    auth = source("apps/admin/auth.py")
    assert "admin_auth_throttle" in migration
    assert "authentication_blocked" in auth
    assert "status_code=429" in auth


def test_subscription_invoices_reserve_remaining_round_capacity():
    commerce = source("packages/core/services/commerce.py")
    assert "reserved=int(await conn.fetchval" in commerce
    assert "round_fully_reserved" in commerce


def test_delivery_claim_prevents_refund_send_race():
    migration = source("migrations/0027_production_integrity_hardening.sql")
    jobs = source("apps/scheduler/jobs/country_jobs.py")
    commerce = source("packages/core/services/commerce.py")
    assert "'sending'" in migration
    assert "SET status='sending'" in jobs
    assert "status IN ('sending','sent')" in commerce
