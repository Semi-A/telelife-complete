from pathlib import Path
import ast, re, yaml
ROOT=Path(__file__).parents[1]
def test_python_syntax():
 for p in ROOT.rglob('*.py'): ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
def test_yaml_valid():
 for p in (ROOT/'packages/core/config/data').glob('*.yaml'): yaml.safe_load(p.read_text(encoding='utf-8'))
def test_world_is_message_and_button_driven():
 src=(ROOT/'apps/teleworld_bot/handlers/world.py').read_text()
 assert 'CommandHandler' not in src
 assert 'MessageHandler(filters.TEXT,text)' in src
 assert "pattern=r'^tw:'" in src
 assert all(x not in src for x in ["a=='jobs'","a.startswith('job:')","a=='jcollect'","a.startswith('jup:')"])
def test_personal_jobs_stay_in_life():
 life=(ROOT/'apps/telelife_bot/keyboards/main.py').read_text()
 world=(ROOT/'apps/teleworld_bot/keyboards.py').read_text()
 for label in ['کشاورز','معدن‌کار','برنامه‌نویس','بازرگان','مهندس','پزشک','روزنامه‌نگار']: assert label in life
 assert 'شغل شخصی' not in world
def test_no_slash_help_in_bot_texts():
 for root in ['apps/telelife_bot','apps/teleworld_bot']:
  for p in (ROOT/root).rglob('*.py'):
   assert not re.search(r'["\']/(start|help|job|country|profile|daily)',p.read_text(),re.I)
