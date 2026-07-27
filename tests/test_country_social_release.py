from pathlib import Path
import ast

def text(path): return Path(path).read_text(encoding='utf-8')

def test_url_button_is_publicly_exported():
    ui=text('packages/core/ui/__init__.py')
    assert '"url_button"' in ui
    assert '"button", "url_button"' in ui

def test_social_schema_and_consent_contracts():
    sql=text('migrations/0023_country_social_life.sql')
    service=text('packages/core/services/social.py')
    for table in ('social_relationships','citizen_help_events','social_competitions','citizen_cases','citizen_case_votes','citizen_reports'):
        assert f'CREATE TABLE IF NOT EXISTS {table}' in sql
    assert 'request_target_required' in service
    assert 'same_country_required' in service
    assert 'help_daily_limit' in service
    assert 'case_party_cannot_vote' in service

def test_social_world_routes_exist():
    world=text('apps/teleworld_bot/handlers/world.py')
    keys=text('apps/teleworld_bot/keyboards.py')
    for token in ('society_page','social_people_page','shelp:','socaccept:','compplay:','casevote:','divorceok'):
        assert token in world
    for fn in ('society_home','social_people','help_amount','competition','court_cases','court_vote','divorce_confirm'):
        assert f'def {fn}' in keys

def test_all_sources_parse():
    for path in Path('.').rglob('*.py'):
        ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
