from pathlib import Path
from packages.core.utils.message_text import plain_text


def test_legacy_html_tags_are_removed():
    assert plain_text('سلام <b>دوست</b>؛ <i>خوش آمدی</i>') == 'سلام دوست؛ خوش آمدی'


def test_bot_sources_do_not_ship_html_formatting_tags():
    tags=(' <b>','</b>','<i>','</i>','<code>','</code>')
    for root in (Path('apps/telelife_bot'),Path('apps/teleworld_bot')):
        for path in root.rglob('*.py'):
            source=path.read_text()
            assert not any(tag in source for tag in tags), path


def test_admin_web_html_is_not_affected():
    assert Path('apps/admin/templates/dashboard.html').exists()