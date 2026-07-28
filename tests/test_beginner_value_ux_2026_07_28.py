"""Beginner comprehension and value-proposition regression contracts."""
from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_home_explains_the_game_and_one_next_action():
    copy = read("apps/telelife_bot/texts/fa.py")
    assert "اینجا چه کار می‌کنی؟" in copy
    assert "الان فقط این کار" in copy
    assert "کار کن ← پاداش بگیر ← قوی‌تر شو" in copy


def test_home_menu_is_beginner_first():
    keyboard = read("apps/telelife_bot/keyboards/main.py")
    for label in ("قدم بعدی من", "کار و درآمد", "چرا بازی کنم؟", "راهنمای یک‌دقیقه‌ای"):
        assert label in keyboard
    home = keyboard[keyboard.index("def home("):keyboard.index("def journey(")]
    assert "بازار ارز" not in home
    assert "خانه و زندگی" not in home


def test_onboarding_teaches_benefits_not_only_features():
    life = read("apps/telelife_bot/handlers/life.py")
    assert "فایده این قدم" in read("apps/telelife_bot/texts/fa.py")
    assert "درآمد شغل با گذشت زمان جمع می‌شود" in life
    assert "if step==3:await jobs(ctx,c)" in life


def test_today_view_names_one_best_action():
    ux = read("apps/telelife_bot/handlers/ux.py")
    assert "بهترین کار الان" in ux
    assert "next_action" in ux
    assert "روزانه چند دقیقه کافی است" in ux


def test_world_explains_shared_group_value():
    copy = read("apps/teleworld_bot/texts/fa.py")
    assert "کشور زنده گروه شما" in copy
    assert "تصمیم‌های اعضا واقعی‌اند" in copy
    assert "ماموریت فعلی گروه" in copy