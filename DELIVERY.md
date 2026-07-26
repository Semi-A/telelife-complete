# TeleLife Phase 5 Delivery

This repository is reconstructed from the supplied TeleLife Phase 2 dump and includes the integrated country/group layer.

## Included

- Forward-only `0003_country_layer.sql`
- YAML-driven country, economy, jobs, elections, projects, missions, news, and daily events
- Repository-only SQL for all new domains
- Atomic shared-ledger service for money/resources
- Lazy production with capacity cap, proportional XP threshold, and checkpoint-before-upgrade
- Country missions instantiated from eligible actions
- Elections, secret one-vote ballots, polls, presidential permissions
- One-time national storage project
- Transactional outbox with retry lease
- Idempotent daily events and country-economy catch-up
- Audited admin APIs
- TeleWorld command handlers and scheduler integration
- Phase 5 documentation and security/config tests

## Run

1. Copy `.env.example` to `.env` and set database/bot/admin secrets.
2. Install dependencies from `requirements.txt` in Python 3.13.
3. Run `pytest`.
4. Start services with `SERVICE=telelife|teleworld|scheduler|admin python run.py`.

Migrations are applied automatically at service startup.
