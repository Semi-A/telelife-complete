# گزارش تحویل Release C — تجارت و تعامل کشورها

تاریخ: ۲۰۲۶-۰۷-۲۷

## ممیزی پیش از پیاده‌سازی

- Commerce موجود فقط تبلیغات و Telegram Stars را مدیریت می‌کرد و بدون تغییر حفظ شد.
- کشور، خزانه، منابع، Ledger، Outbox، سمت‌های Release B و بحران‌ها قابل استفاده مجدد بودند.
- تداخل اصلی نام «تجارت» بود؛ تجارت کشورها در سرویس و جداول مستقل ساخته شد.
- ریسک‌های اصلی: Double-spend، پذیرش هم‌زمان، انقضای هم‌زمان با پذیرش، deadlock قراردادهای معکوس، ازبین‌رفتن Escrow، دورزدن تحریم و Callback بدون Permission.
- کنترل ریسک: قفل کشورها با ترتیب ثابت، قفل قرارداد و Escrow، تراکنش واحد، کلیدهای idempotency، Ledger چندشاخه، Outbox و Scheduler محدود.

## امکانات Release C

1. قرارداد تجاری مستقیم بین دو کشور با پیشنهادهای محدود و Config-driven.
2. انتقال فوری دارایی پیشنهاددهنده به Escrow.
3. پذیرش اتمیک قرارداد و جلوگیری از Double-spend.
4. بازپرداخت Escrow در لغو یا انقضای ۱۲ساعته.
5. سقف قرارداد باز بر اساس اعتبار بین‌المللی.
6. نرخ مرجع بر اساس تاریخچه معاملات واقعی تکمیل‌شده.
7. روابط رسمی دوطرفه: دوست، شریک تجاری و متحد دفاعی.
8. تعرفه واقعی بر اساس رابطه؛ روابط بهتر هزینه تجارت را کم می‌کنند.
9. تحریم مستقیم با هزینه اعتباری برای کشور تحریم‌کننده.
10. اعتبار بین‌المللی با اثر قرارداد موفق، لغو، کمک و تحریم.
11. کمک اضطراری غذا، انرژی و خزانه فقط به کشور دارای بحران فعال.
12. Permission برای رئیس‌جمهور، وزیر اقتصاد و وزیر خارجه.
13. Audit دیپلماسی و اعلان پیشنهاد با Outbox.
14. رابط فارسی تجارت، قراردادهای ورودی/خروجی، روابط، کمک و نرخ مرجع.
15. Scheduler محدود برای انقضای قرارداد و پیشنهاد دیپلماتیک.

## فایل‌های جدید

- `migrations/0018_country_trade_diplomacy_release_c.sql`
- `packages/core/config/data/country_trade.yaml`
- `packages/core/services/country_trade_rules.py`
- `packages/core/services/country_trade.py`
- `tests/test_country_trade_release_c.py`
- `RELEASE_C_REPORT_FA.md`

## فایل‌های تغییرکرده

- `apps/teleworld_bot/handlers/world.py`
- `apps/teleworld_bot/keyboards.py`
- `apps/scheduler/main.py`

## تست

- Compile کل پروژه: موفق.
- تست مستقیم Release C به همراه رگرسیون A/B: **۱۸ Passed / ۰ Failed / ۰ Skipped**.
- migrationهای `0001` تا `0017` با artifact مبنای Release B مقایسه شدند و بدون تغییرند.
- اجرای مجموعه کامل pytest ممکن نبود، چون executable/package مربوط به pytest در محیط ساخت موجود نبود.
- تست واقعی PostgreSQL/asyncpg، Telegram API و Render/Supabase در این محیط انجام نشد؛ پیش از انتشار عمومی باید روی staging اجرا شود.

## Deploy

1. از دیتابیس production بکاپ منطقی بگیرید.
2. ZIP را روی staging با کپی داده production اجرا کنید.
3. migration افزایشی `0018` را اجرا کنید؛ هیچ migration قبلی را تغییر ندهید.
4. Smoke test: ساخت قرارداد، مشاهده Escrow، پذیرش، لغو، انقضا، رابطه دوطرفه، تحریم و کمک به بحران.
5. Ledger هر دو کشور و عدم منفی‌شدن منابع را بررسی کنید.
6. همان artifact تأییدشده را روی Render منتشر کنید.
7. متغیر محیطی جدیدی لازم نیست.

## Rollback بدون حذف داده

- کد را به Release B برگردانید و جدول‌های `0018` را نگه دارید.
- Scheduler قدیمی jobهای Release C را اجرا نمی‌کند و داده‌ها بی‌اثر می‌مانند.
- پیش از rollback، قراردادهای باز را از رابط لغو کنید تا Escrow بازپرداخت شود.
- جدول، Ledger یا Audit را Drop نکنید.

## محدودیت صادقانه

این artifact یک Production Candidate است و «بدون باگ» نامیده نمی‌شود. تست concurrency واقعی شامل پذیرش هم‌زمان، پذیرش هم‌زمان با انقضا و قراردادهای معکوس روی PostgreSQL staging الزامی است.