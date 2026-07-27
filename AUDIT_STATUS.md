# Production Readiness Audit

## اصلاحات تکمیل‌شده

- ورودی چهار-service قدیمی با یک process supervisor جایگزین شد.
- دو bot در polling mode، scheduler و FastAPI همزمان اجرا می‌شوند.
- فقط Uvicorn/FastAPI روی `PORT` listen می‌کند.
- crash boundary، auto-restart با exponential backoff، health registry، heartbeat، memory watermark و graceful shutdown افزوده شد.
- lifecycle دیتابیس process-level شد تا یک pool مشترک asyncpg با سقف ۴ connection استفاده شود.
- Supabase transaction pooler با statement cache صفر، TLS در DSN نمونه و inactive lifetime محدود پیکربندی شد.
- migration runner با PostgreSQL advisory transaction lock ایمن شد.
- health/readiness endpoints و security headers افزوده شدند.
- Render Blueprint به یک Free Web Service کاهش یافت؛ هیچ feature، route، table یا game service حذف نشد.
- تمام فایل‌های Python با AST و compileall بررسی شدند؛ fragment تولیدی خراب در source پیدا نشد.
- تست crash isolation افزوده شد.

## محدودیت اعتبارسنجی محیط ممیزی

اجرای کامل pytest و integration test زنده با Supabase/Telegram در sandbox آفلاین ممکن نبود، زیرا runtime dependencyهای پروژه و credentialهای واقعی موجود نبودند. Dockerfile نصب dependencyها و compile check را در build انجام می‌دهد. پیش از production، تست‌های integration باید در CI با database آزمایشی و tokenهای اختصاصی اجرا شوند.
