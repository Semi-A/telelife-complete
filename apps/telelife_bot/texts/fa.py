"""All player-facing Persian copy for TeleLife. No text belongs in logic files."""

from __future__ import annotations

# ---------- onboarding ----------
WELCOME_NEW = (
    "🌆 <b>به تله‌لایف خوش اومدی، {name}!</b>\n\n"
    "از همین لحظه یه زندگی دوم داری. حسابت باز شد و {wallet} توش نشسته.\n\n"
    "کارِت اینه که بسازیش: کار کن، پس‌انداز کن، سرمایه‌گذاری کن، بالا برو.\n"
    "هر روزی که بیای، جلوتری از دیروز."
)

WELCOME_BACK = (
    "👋 <b>برگشتی {name}!</b>\n\n"
    "سطح {level} · {wallet}\n"
    "زندگیت همون‌جا که گذاشتیش منتظرته."
)

# ---------- profile ----------
PROFILE = (
    "🪪 <b>{name}</b>\n"
    "<code>─────────────────</code>\n"
    "🎚 سطح <b>{level}</b>{prestige_tag}  ·  رتبه {rank}\n"
    "{xp_bar}\n"
    "<i>{xp} از {xp_needed} XP تا سطح بعد</i>\n\n"
    "💵 کیف پول    <b>{wallet}</b>\n"
    "🏦 پس‌انداز    <b>{savings}</b>\n"
    "💲 دلار        <b>{usd}</b>\n"
    "<code>─────────────────</code>\n"
    "😊 شادی {happiness}٪   ⭐️ شهرت {reputation}\n"
    "🔥 استریک {streak} روز\n\n"
    "<i>ثروت خالص: {net_worth}</i>"
)

PRESTIGE_TAG = " · پرستیژ {prestige}"

# ---------- daily ----------
DAILY_CLAIMED = (
    "🎁 <b>جایزه امروز گرفته شد!</b>\n"
    "<code>─────────────────</code>\n"
    "💰 <b>+{reward}</b>\n"
    "✨ +{xp} XP\n\n"
    "🔥 استریک: <b>{streak} روز</b>\n"
    "{next_line}"
)

DAILY_MILESTONE = (
    "\n\n🏅 <b>{label}</b>\n"
    "پاداش ویژه: <b>+{bonus}</b>\n"
    "<i>ادامه بده، بعدی سنگین‌تره.</i>"
)

DAILY_NEXT = "فردا بیای: <b>{amount}</b>"
DAILY_NEXT_MILESTONE = "🎯 {days} روز دیگه تا نشان بعدی"

DAILY_READY = (
    "🎁 <b>جایزه امروزت آماده‌ست</b>\n"
    "<code>─────────────────</code>\n"
    "🔥 استریک فعلی: <b>{streak} روز</b>\n"
    "🏆 رکوردت: {best} روز\n\n"
    "💰 امروز می‌گیری: <b>{amount}</b>\n"
    "{next_line}"
)

DAILY_READY_NEXT = "<i>فردا می‌شه {amount} — استریکو نشکون.</i>"

DAILY_ALREADY = (
    "⏳ <b>امروز رو گرفتی</b>\n\n"
    "🔥 استریک: <b>{streak} روز</b>\n"
    "فردا برگرد، <b>{tomorrow}</b> منتظرته.\n\n"
    "<i>یه روز غیبت، استریکت برمی‌گرده سر خونه اول.</i>"
)

# ---------- missions ----------
MISSIONS_HEADER = (
    "🎯 <b>ماموریت‌های امروز</b>\n"
    "<code>─────────────────</code>\n"
    "{body}\n"
    "<code>─────────────────</code>\n"
    "<i>نصف‌شب ریست می‌شن. جا نمونی.</i>"
)

MISSION_ROW_DONE = "✅ <s>{title}</s>  <b>+{reward}</b>"
MISSION_ROW_READY = "🎁 <b>{title}</b>  ({progress}/{target})  <b>+{reward}</b>"
MISSION_ROW_OPEN = "▫️ {title}  ({progress}/{target})  +{reward}"

MISSION_CLAIMED = "✅ <b>{title}</b>\nگرفتی: <b>+{reward}</b> و +{xp} XP"
MISSION_NOT_READY = "هنوز تمومش نکردی."
MISSIONS_LOCKED = "🔒 ماموریت‌های روزانه از سطح ۲ باز می‌شن.\nیه کم دیگه بمون."
MISSIONS_EMPTY = "فعلاً ماموریتی برات نیست. فردا سر بزن."

# ---------- level up ----------
LEVEL_UP = (
    "🎉 <b>سطح {level}!</b>\n"
    "<code>─────────────────</code>\n"
    "🎁 پاداش ارتقا: <b>+{reward}</b>\n"
    "{unlock_line}"
)

LEVEL_UP_UNLOCK = "🔓 باز شد: <b>{icon} {title}</b>"
LEVEL_UP_NEXT = "<i>سطح {level}: {icon} {title}</i>"

# ---------- unlocks panel ----------
UNLOCKS_HEADER = (
    "🗺 <b>نقشه پیشرفت</b>\n"
    "<code>─────────────────</code>\n"
    "{body}\n"
    "<code>─────────────────</code>\n"
    "<i>سطح {level} · بعدی تو سطح {next_level}</i>"
)

UNLOCK_ROW_OPEN = "✅ {icon} {title}"
UNLOCK_ROW_LOCKED = "🔒 {icon} {title} <i>— سطح {level}</i>"
UNLOCK_ROW_NEXT = "➡️ <b>{icon} {title}</b> <i>— سطح {level}</i>"
UNLOCKS_ALL_DONE = "همه‌چیز باز شده. افسانه‌ای."

# ---------- buttons ----------
BTN_DAILY = "🎁 جایزه روزانه"
BTN_DAILY_READY = "🎁 جایزه امروز آماده‌ست"
BTN_MISSIONS = "🎯 ماموریت‌ها"
BTN_PROFILE = "🪪 پروفایل"
BTN_UNLOCKS = "🗺 نقشه پیشرفت"
BTN_BACK = "◀️ برگرد"
BTN_REFRESH = "🔄 تازه‌سازی"
BTN_CLAIM = "🎁 بگیر"

# ---------- system ----------
BANNED = "⛔️ حسابت مسدوده.\nدلیل: {reason}"
FROZEN = "🧊 حسابت موقتاً فریز شده."
ERROR = "😵‍💫 یه چیزی این وسط قاطی کرد. چند لحظه دیگه دوباره امتحان کن."
NOT_YOUR_PANEL = "این پنل مال تو نیست 😐"
PANEL_EXPIRED = "این پنل منقضی شده. دوباره بازش کن."
NO_REASON = "نامشخص"
XP_CAPPED = "\n\n<i>سقف XP امروزت پر شد. فردا تازه می‌شه.</i>"

HELP = (
    "🧭 <b>راهنمای تله‌لایف</b>\n"
    "<code>─────────────────</code>\n"
    "/profile — پروفایل و وضعیت زندگیت\n"
    "/daily — جایزه روزانه و استریک\n"
    "/missions — ماموریت‌های امروز\n"
    "/unlocks — نقشه پیشرفت\n"
    "/help — همین صفحه\n\n"
    "<i>تو گروه‌ها هم می‌تونی فارسی حرف بزنی: پول، سطح، روزانه…</i>"
)
