# Conventions — non-negotiable

## Code
- Python 3.13 target, forward-compatible with 3.14.
- `from __future__ import annotations` at the top of every module.
- Full type hints on every public function.
- Fully async. No blocking I/O in the event loop, ever.
- Max 400 lines per file. Split before exceeding.
- Ruff and mypy strict must pass.

## Money
- Always BIGINT minor units. Never float.
- Every mutation goes through the ledger with an idempotency key.
- Every mutation runs inside `db.transaction()`.
- `CHECK (balance >= 0)` stays on every balance column.

## Database
- Forward-only migrations numbered `0001_`, `0002_`, ...
- Never edit an applied migration; the checksum guard will reject it.
- Index every column used in WHERE, ORDER BY or JOIN on a hot path.
- Use partial indexes for filtered hot queries.

## Persian copy
- Modern, warm, meme-aware. Never robotic, never childish, never cringe.
- Persian digits with `٬` as the thousands separator in all player-facing numbers.
- Second person singular. Short sentences. Emoji as structure, not decoration.

## Telegram
- HTML parse mode everywhere. Escape user input.
- Every callback must be ownership-checked (Phase 6).
- Interactive panels auto-expire per `core.menu_cleanup` (Phase 2+).

## Security
- Secrets only via env. Never committed, never logged.
- Constant-time comparison for every credential check.
- Admin actions write to `audit_log`.
