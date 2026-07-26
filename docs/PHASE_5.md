# Phase 5 — Country and Group Layer

**Status:** integrated implementation

## Delivered
Countries/citizenship, shared economic ledger, five resources, seven lazy-production jobs, proportional collection XP, checkpoint-before-upgrade, country missions and effects, elections, secret one-vote ballots, presidential permissions, one-time national storage project, anti-spam polls, transactional news outbox, deterministic daily events, scheduler resolution, and audited admin operations.

## Security invariants
- Telegram numeric IDs are identity; group-admin API is used only for country registration.
- Every asset mutation is transactional and receives a unique ledger key.
- Collection XP is proportional and suppressed below the configured minimum fraction.
- Upgrade locks and checkpoints the old rate/capacity before changing level.
- Vote, contribution, reward, scheduler, outbox, and daily-event retries are idempotent.
- Admin audit and ledger are append-only.

## Issues found/fixed
| Issue | Fix |
|---|---|
| Fine-grained collection XP farming | Proportional XP plus minimum fraction |
| Retroactive upgrade production | Locked checkpoint before level update |
| Missions appearing only on view | Instantiation during eligible action |
| Duplicate votes/contributions | Database uniqueness and idempotency keys |
| Competing schedulers | `FOR UPDATE SKIP LOCKED` plus outbox leases |
| Untracked privileged changes | Append-only admin audit log |

## Metrics
- Eight Phase 5 YAML config files
- Schema migration remains below 400 lines
- Repository/service files remain below 400 lines
- Seven job definitions and five national resources
