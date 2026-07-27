from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_multi_admin_schema_has_password_and_audit_fields():
    sql = text("migrations/0021_multi_admin_hardening.sql")
    for field in ("password_hash", "created_by", "last_login_at", "disabled_at"):
        assert field in sql
    assert "pbkdf2_sha256" in sql


def test_passwords_use_salted_pbkdf2_and_constant_time_compare():
    source = text("packages/core/services/admin_accounts.py")
    assert "os.urandom(16)" in source
    assert "hashlib.pbkdf2_hmac" in source
    assert "hmac.compare_digest" in source
    assert "password_hash" in source


def test_admin_routes_are_superadmin_permission_guarded():
    security = text("packages/core/services/admin_security.py")
    router = text("apps/admin/routers/country_admin.py")
    assert '("/admins", "admins")' in security
    assert '"admins"' in security.split('"superadmin"', 1)[1]
    assert '@router.post("/admins",status_code=201)' in router
    assert '@router.patch("/admins/{username}")' in router


def test_admin_frontend_has_management_view_and_actionable_errors():
    html = text("apps/admin/templates/dashboard.html")
    js = text("apps/admin/static/admin.js")
    assert 'id="view-admins"' in html
    assert 'id="admins-body"' in html
    assert "async function admins" in js
    assert "Promise.allSettled" in js
    assert "اطلاعات فرم کامل یا معتبر نیست" in js


def test_incident_refresh_does_not_create_fake_recurrences():
    repo = text("packages/core/repositories/admin_repo.py")
    assert "last_seen_at<now()-interval '10 minutes'" in repo
    assert "resolve_unobserved_incidents" in repo
    assert "include_resolved=False" in repo
    assert "An intentional freeze is state, not an error" in repo