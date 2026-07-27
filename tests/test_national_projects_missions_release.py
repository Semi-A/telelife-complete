from pathlib import Path
from packages.core.config import get_config
from packages.core.services import missions

def test_four_useful_projects_have_real_effects():
    projects=get_config().section('national_project.projects')
    assert set(projects)=={'national_storage','power_grid','research_university','food_network'}
    for spec in projects.values():
        assert spec['requirements'] and int(spec['completion']['magnitude_basis_points'])>0

def test_missions_are_action_based_not_navigation_based():
    keys={x['key'] for x in get_config().get('missions.pool')}
    assert {'work_shift','national_output','pay_work_tax','project_contribution'}<=keys
    assert 'check_profile' not in keys

def test_daily_selection_remains_deterministic():
    from datetime import date
    a=[x['key'] for x in missions.select_for(42,1,date(2026,7,27))]
    b=[x['key'] for x in missions.select_for(42,1,date(2026,7,27))]
    assert a==b and len(a)==3

def test_migration_is_additive_and_release_declared():
    sql=Path('migrations/0016_national_projects_and_missions.sql').read_text()
    assert 'DROP TABLE' not in sql and 'DROP COLUMN' not in sql
    assert 'national_project_effects' in sql and 'country_project_funding' in sql
    assert Path('RELEASE_NATIONAL_PROJECTS_MISSIONS_FA.md').exists()
