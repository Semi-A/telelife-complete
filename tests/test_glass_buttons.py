"""Glass keyboard contract tests.

Bot API 9.4 added `style` (primary/success/danger). Omitting it yields the
default translucent look, which is our neutral state.
"""

import pytest

from packages.core.ui.buttons import Keyboard, Style, button


def test_glass_omits_style_field():
    b = button("سلام", "tl:x:1")
    assert getattr(b, "style", None) is None


def test_styles_are_the_three_telegram_values():
    assert {s.value for s in Style} == {"glass", "primary", "success", "danger"}
    for style in (Style.PRIMARY, Style.SUCCESS, Style.DANGER):
        b = button("t", "tl:x:1", style=style)
        assert b.style == style.value


def test_only_one_primary_allowed():
    kb = Keyboard()
    kb.add("یک", "tl:a:1", style=Style.PRIMARY)
    kb.add("دو", "tl:b:1", style=Style.PRIMARY)
    with pytest.raises(ValueError, match="primary"):
        kb.build()


def test_many_success_buttons_are_fine():
    kb = Keyboard()
    for i in range(3):
        kb.add(f"بگیر {i}", f"tl:c:1:{i}", style=Style.SUCCESS)
    assert len(kb.build().inline_keyboard) == 3


def test_grid_wraps_rows():
    kb = Keyboard().grid([button(str(i), f"tl:g:1:{i}") for i in range(5)], per_row=2)
    rows = kb.build().inline_keyboard
    assert [len(r) for r in rows] == [2, 2, 1]
