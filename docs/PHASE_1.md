# Phase 1 — Core Skeleton (DELIVERED)

**Status:** complete and runnable
**Scope discipline:** everything listed below works. Nothing beyond it exists yet, by design.

## What Phase 1 delivers

| Area | Delivered |
|---|---|
| Settings | env-driven, validated by pydantic-settings, Supabase-pooler safe |
| Logging | structured JSON, one line per event, noisy libraries muted |
| Database | asyncpg pool, jsonb codec, transaction helper, healthcheck |
| Migrations | forward-only SQL runner with checksum tamper detection |
| Schema | players, groups, group_members, ledger, cooldowns, audit_log |
| Game config | YAML-driven, dotted access, zero hardcoded game numbers |
| Bot runtime | shared bootstrap; polling AND webhook from one code path |
| TeleLife | /start, /profile, /help |
| TeleWorld | /status, /help, group + member sync |
| Scheduler | independent worker, cooldown cleanup, graceful shutdown |
| Admin | HTTP Basic auth, dark dashboard, HTMX live refresh, /healthz |
| Deploy | one Dockerfile, four Render services via the SERVICE env var |
| Tests | config, formatting, progression curve, migration runner |

## Running locally
