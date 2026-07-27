# Phase 2 — Identity & Progression (DELIVERED)

**Status:** complete, tested, runnable
**New in this phase:** the glass button system (Bot API 9.4 styles)

---

## 1. Glass buttons — what Telegram actually shipped

Bot API **9.4** (9 Feb 2026) added `style` to `InlineKeyboardButton` and
`KeyboardButton`. Supported in python-telegram-bot **22.7+**.

| Value | Colour | Our rule |
|---|---|---|
| *(omitted)* | translucent glass | **default for everything** |
| `primary` | blue | the one action we want tapped — **max one per keyboard** |
| `success` | green | a reward is waiting to be collected |
| `danger` | red | destructive / irreversible only |

`icon_custom_emoji_id` is also available for custom emoji on buttons.

### Colour policy (enforced in code, not by discipline)

`Keyboard.build()` **raises** if a keyboard contains more than one `primary`
button. Colour everywhere means colour nowhere; if every button shouts, the
player's eye has nothing to follow.

Colour is emphasis, never meaning. Old clients silently ignore `style`, so
every layout must read perfectly with zero colour. Button text always stands
on its own.