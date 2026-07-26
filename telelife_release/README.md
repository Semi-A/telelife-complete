# TeleLife / TeleWorld

استقرار تک‌پردازه شامل دو ربات Telegram، زمان‌بند و پنل FastAPI است.

## معماری اجرا

`run.py` یک pool مشترک asyncpg و migrationها را راه‌اندازی می‌کند و `ServiceSupervisor` چهار سرویس زیر را به‌صورت taskهای مستقل اجرا می‌کند:

- TeleLife polling bot
- TeleWorld polling bot
- Scheduler (minute/daily loops)
- FastAPI Admin (تنها listener روی `PORT`)

خرابی هر سرویس در مرز Supervisor مهار و با exponential backoff همان سرویس restart می‌شود. `SIGTERM` و `SIGINT` باعث graceful shutdown همه taskها، Telegram applications، Uvicorn و pool دیتابیس می‌شوند.

## استقرار Render

1. repository را به GitHub push کنید.
2. در Render یک Blueprint از `render.yaml` بسازید؛ فقط یک Web Service Free تعریف می‌شود.
3. secretها را وارد کنید: `DATABASE_URL`، هر دو bot token، و اطلاعات admin.
4. برای Supabase Transaction Pooler از port `6543`، `sslmode=require` و `DB_STATEMENT_CACHE_SIZE=0` استفاده کنید.
5. migrationها هنگام startup و پیش از سرویس‌ها، تحت advisory lock اجرا می‌شوند.

Health: `/healthz` — Readiness: `/readyz` — داشبورد و API مدیریت با HTTP Basic محافظت شده‌اند.

## اجرا و تست
