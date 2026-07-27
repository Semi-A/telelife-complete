"""Small in-process limiter dedicated to /start commands."""
from __future__ import annotations

import asyncio
from collections import defaultdict, deque
from time import monotonic
from typing import Any

_WINDOW_SECONDS = 60.0
_MAX_STARTS = 2
_LOCK_KEY = "_start_rate_limit_lock"
_BUCKETS_KEY = "_start_rate_limit_buckets"


async def allow_start(context: Any, user_id: int, chat_id: int) -> bool:
    """Allow at most two /start commands per user/chat in a rolling minute."""
    data = context.application.bot_data
    lock = data.get(_LOCK_KEY)
    if lock is None:
        lock = data[_LOCK_KEY] = asyncio.Lock()
    async with lock:
        buckets = data.get(_BUCKETS_KEY)
        if buckets is None:
            buckets = data[_BUCKETS_KEY] = defaultdict(deque)
        key = (int(user_id), int(chat_id))
        bucket = buckets[key]
        now = monotonic()
        while bucket and now - bucket[0] >= _WINDOW_SECONDS:
            bucket.popleft()
        if len(bucket) >= _MAX_STARTS:
            return False
        bucket.append(now)
        return True
