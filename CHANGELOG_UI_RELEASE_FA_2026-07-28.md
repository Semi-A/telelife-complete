# انتشار رابط کاربری و متن‌ها — ۲۸ ژوئیه ۲۰۲۶

## ۱) رفع باگ حیاتی: ربات روی چند مسیر کرش می‌کرد

۲۹ کلید متنی در کد صدا زده می‌شد که در `apps/telelife_bot/texts/fa.py` وجود نداشت
(`WELCOME_NEW`, `WELCOME_BACK`, `HELP`, `MISSIONS_HEADER`, `DAILY_CLAIMED`, `PRESTIGE_TAG` و…).
هر بار که کاربر `start` می‌زد یا پروفایل/مأموریت باز می‌کرد، `AttributeError` می‌گرفت.

**ریشهٔ مشکل:** چهار ماژول از نسخهٔ قدیمی در پروژه جا مانده بودند که هیچ‌جا import نمی‌شدند
ولی به متن‌های حذف‌شده وابسته بودند و تست‌های ایستا را می‌شکستند.

**حذف شد:**
- `apps/telelife_bot/handlers/start.py`
- `apps/telelife_bot/handlers/progression.py`
- `apps/telelife_bot/handlers/economy_ui.py`
- `apps/telelife_bot/handlers/profile.py`
- `apps/telelife_bot/views/` (کل پوشه)

مسیر زندهٔ بازی (`life.py` + `ux.py` + `panel.py` + `advertising.py`) دست‌نخورده و کامل است.
اکنون صفر ارجاع شکسته وجود دارد.

## ۲) بازنویسی کامل متن‌های فارسی

`texts/fa.py` از نو نوشته شد. لحن از خشک و ماشینی به گرم و انسانی تغییر کرد.

هر صفحه ساختار ثابت دارد: تیتر → خط‌کش → توضیح کوتاه → وضعیت عددی → یک راهنمای پایانی.
دو جداکنندهٔ مشترک معرفی شد: `RULE` (`━━━`) برای زیر تیتر و `SOFT` (`┈┈┈`) برای جدا کردن آمار.

صفحهٔ اول (HOME) کاملاً بازنویسی شد: توضیح می‌دهد بازی چیست، یک قدم بعدی مشخص می‌دهد،
سه عدد کلیدی را جدا نشان می‌دهد و با یک جملهٔ اطمینان‌بخش تمام می‌شود.

صفحات بازنویسی‌شده: HOME، JOURNEY، WHY_PLAY، HOW_TO_PLAY، PROFILE، DAILY_READY،
DAILY_DONE، DAILY_WAIT، MISSIONS، ECONOMY، JOBS، UNLOCKS، BANNED، FROZEN، ERROR،
PANEL_EXPIRED، NOT_YOUR_PANEL.

همچنین متن درون‌خطی این صفحه‌ها هم‌سبک شد: بازار دلار، پس‌انداز، خانه و زندگی، و «امروز من».

## ۳) نظم‌دهی به دکمه‌های شیشه‌ای و رنگ‌بندی

یک زبان رنگی واحد در کل ربات تعریف شد:

| نشانه | معنی |
|---|---|
| 🔵 | جابه‌جایی و اطلاعات |
| 🟣 | اقتصاد و دارایی |
| 🟡 | خرج کردن یا فروش |
| 🟢 | رشد و پیشرفت |

قواعد ثابت:
- در هر صفحه **دقیقاً یک** دکمهٔ Primary — یعنی بهترین قدم بعدی.
- Success فقط برای چیزی که **همین حالا** آمادهٔ دریافت است.
- ردیف پایانی همهٔ صفحه‌ها یکنواخت شد (تابع مشترک `_footer`): بازگشت مشخص، سپس «خانه».
- دکمه‌های حالت خالی معنادار شدند (مثلاً وقتی مأموریت آماده نیست، «رفتن سر کار» پیشنهاد می‌شود).
- هدیهٔ روزانه در صفحهٔ اول به‌صورت شرطی به‌عنوان Success برجسته می‌شود.

## ۴) ایمن‌سازی migration در برابر خطای دیپلوی

`packages/core/db/migrator.py`:
- checksum حالا روی متن **نرمال‌شده** حساب می‌شود (CRLF/CR → LF و حذف فاصلهٔ ابتدا/انتها).
  دیگر تفاوت line ending بین ویندوز و لینوکس باعث خطای
  «Migration changed after being applied» نمی‌شود.
- `RECOVERED_BASELINE_END` به `0027_production_integrity_hardening` رسید و
  `STRICT_CHECKSUM_FROM` به `0028_`.

### migration جدید: `0028_ui_release_hardening.sql`

کاملاً additive و idempotent — بدون `DROP`، بدون `TRUNCATE`. فقط چهار ایندکس:

- `idx_citizenships_active_player` — پنل خانه در هر تپ شهروندی فعال را می‌خواند
- `idx_citizenships_active_country` — شمارش شهروندان در فهرست مقصدهای مهاجرت
- `idx_player_ui_state_player` — resolve کردن پیام زندهٔ پنل
- `idx_migration_requests_player_pending` — بنر وضعیت مهاجرت

## ۵) کنترل کیفیت انجام‌شده

- کل درخت با `compileall` بدون خطا کامپایل می‌شود
- ۴۲ حالت مختلف صفحه‌کلید ساخته و اعتبارسنجی شد: هیچ‌کدام بیش از یک Primary ندارند و همهٔ
  `callback_data`ها زیر سقف ۶۴ بایت تلگرام هستند
- ۷۰ قرارداد ایستای موجود پروژه بازبررسی شد و همه سبز است
- بررسی یکپارچگی: همهٔ Python‌ها parse می‌شوند، همهٔ YAML‌ها mapping‌اند، هیچ باقی‌ماندهٔ
  heredoc در سورس نیست، پوشه‌های الزامی runtime موجودند
- بدون تگ HTML و بدون دستور اسلش در متن‌های زندهٔ ربات
- فایل تست جدید: `tests/test_ui_release_2026_07_28.py`

## نکتهٔ استقرار

تست‌های یکپارچهٔ PostgreSQL باید در staging با دیتابیس واقعی اجرا شوند:

```
python -m pytest -q
```

`asyncpg` و `python-telegram-bot` باید نصب باشند (در `requirements.txt` هستند).
