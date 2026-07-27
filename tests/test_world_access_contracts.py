"""Static contracts that require no Telegram or PostgreSQL service."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def test_my_chat_member_is_registered():
    source = text("apps/teleworld_bot/handlers/access.py")
    main = text("apps/teleworld_bot/main.py")
    assert "ChatMemberHandler.MY_CHAT_MEMBER" in source
    assert "access.register(application)" in main

def test_permission_policy_is_minimal():
    source = text("packages/core/services/world_access.py")
    assert "can_delete_messages" in source
    for dangerous in ("can_promote_members", "can_change_info", "can_restrict_members"):
        assert dangerous not in source

def test_all_world_mutations_pass_gate():
    source = text("apps/teleworld_bot/handlers/world.py")
    assert "is_mutating(action)" in source
    assert "if not access.ready" in source

def test_financial_callback_key_is_stable():
    source = text("apps/teleworld_bot/handlers/world.py")
    assert 'world-donate:{p.id}:{query.id}' in source
    assert 'world-project:{p.id}:{query.id}' in source
    assert 'idempotency_key=f"world:{p.id}:{uuid4().hex}"' not in source

def test_migration_is_non_destructive_and_repeatable():
    sql = text("migrations/0008_world_access_lifecycle.sql").upper()
    assert sql.count("CREATE TABLE IF NOT EXISTS") == 2
    assert "DROP TABLE" not in sql and "TRUNCATE" not in sql

def test_callback_payload_literals_fit_limit():
    files = [text("apps/teleworld_bot/keyboards.py"), text("apps/telelife_bot/keyboards/main.py")]
    for source in files:
        for value in re.findall(r'callback_data\s*=\s*f?["\']([^"\']+)', source):
            assert len(value.encode("utf-8")) <= 64

def test_privacy_mode_is_documented_honestly():
    guide = text("docs/DEPLOYMENT_FA.md")
    assert "Privacy Mode" in guide
    assert "قابل تشخیص مستقیم نیست" in guide
    assert "BotFather" in guide