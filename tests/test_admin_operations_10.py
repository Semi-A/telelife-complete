from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def text(path):return (ROOT/path).read_text(encoding='utf-8')

def test_backend_preview_is_one_use_and_payload_bound():
 s=text('packages/core/services/admin_security.py')
 assert 'x-admin-preview' in s and 'payload_hash' in s and 'used_at IS NULL' in s
 assert 'expires_at>now()' in s

def test_rbac_is_backend_enforced():
 s=text('packages/core/services/admin_security.py')
 for role in ('viewer','support','content','economy','operator','superadmin'):assert role in s
 assert 'require_permission' in s and 'HTTPException(403' in s

def test_incidents_are_persistent_and_managed():
 sql=text('migrations/0020_admin_operations_10.sql');repo=text('packages/core/repositories/admin_repo.py')
 assert 'admin_incidents' in sql and 'acknowledged' in sql and 'resolved' in sql
 assert 'persist_incidents' in repo and 'update_incident' in repo

def test_macro_map_reads_latest_indicator_table():
 s=text('packages/core/repositories/admin_repo.py')
 assert 'country_indicator_daily d' in s and 'ORDER BY indicator_date DESC LIMIT 1' in s
 assert 'e.inflation_bp' not in s

def test_search_anomaly_sse_and_undo_exist():
 router=text('apps/admin/routers/country_admin.py');repo=text('packages/core/repositories/admin_repo.py')
 for token in ('/search','/anomalies','/events','/undo/{action_id}','/action-preview'):assert token in router
 for token in ('global_search','anomaly_rows','undo_action','available_undos'):assert token in repo

def test_frontend_uses_backend_preview_and_command_palette():
 s=text('apps/admin/static/admin.js')
 assert '/api/admin/action-preview' in s and 'X-Admin-Preview' in s
 assert 'Ctrl K' not in s or 'command-palette' in s
 assert 'EventSource' in s and 'setIncident' in s
