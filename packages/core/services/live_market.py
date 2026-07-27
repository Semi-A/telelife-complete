"""Validated server-side synchronization with Zipodo's live USDT/IRT endpoint."""
from __future__ import annotations
import asyncio, json, logging, math
from datetime import UTC, datetime
from urllib.request import Request, urlopen
from packages.core import db

logger=logging.getLogger(__name__)
URL="https://api.zipodo.ir/usdt/"

def extract_price(payload: object) -> int:
    """Accept common JSON envelopes while rejecting booleans, NaN, and implausible rates."""
    keys=("price","last","value","rate","sell","close")
    candidates=[]
    def walk(value, depth=0):
        if depth>4:return
        if isinstance(value,dict):
            for key in keys:
                if key in value:candidates.append(value[key])
            for child in value.values():walk(child,depth+1)
        elif isinstance(value,list):
            for child in value[:20]:walk(child,depth+1)
    walk(payload)
    if not candidates and isinstance(payload,(int,float,str)):candidates=[payload]
    for raw in candidates:
        if isinstance(raw,bool):continue
        try:
            number=float(str(raw).replace(",","").strip())
        except (TypeError,ValueError):continue
        if math.isfinite(number):
            price=round(number)
            # USDT/IRT guardrail: intentionally broad enough for inflation, narrow enough for corrupt JSON.
            if 1_000 <= price <= 100_000_000:return price
    raise ValueError("zipodo_price_missing_or_implausible")

def _fetch(timeout: float=7.0)->int:
    req=Request(URL,headers={"Accept":"application/json","User-Agent":"TeleLife/1.0"})
    with urlopen(req,timeout=timeout) as response:
        if response.status!=200:raise RuntimeError(f"zipodo_http_{response.status}")
        raw=response.read(256_000)
    text=raw.decode("utf-8-sig").strip()
    try: payload=json.loads(text)
    except json.JSONDecodeError: payload=text
    return extract_price(payload)

async def sync()->dict[str,object]:
    checked=datetime.now(UTC)
    try:
        price=await asyncio.to_thread(_fetch)
        async with db.transaction() as conn:
            await conn.execute("""UPDATE usd_market_state SET reference_price_toman=$1,updated_at=now()
                WHERE singleton=TRUE""",price)
            await conn.execute("""UPDATE market_prices SET current_price_toman=$1,source='zipodo',
                source_checked_at=$2,source_error=NULL,updated_by='zipodo-live',updated_at=now()
                WHERE asset_code='USD'""",price,checked)
            await conn.execute("""INSERT INTO market_price_snapshots(asset_code,price_toman,captured_at)
                VALUES('USD',$1,date_trunc('minute',now()))
                ON CONFLICT(asset_code,captured_at) DO UPDATE SET price_toman=EXCLUDED.price_toman""",price)
        return {"price":price,"source":"zipodo","stale":False}
    except Exception as exc:
        logger.warning("live USDT sync failed; keeping last valid price",exc_info=True)
        await db.execute("""UPDATE market_prices SET source_checked_at=$2,source_error=$1
            WHERE asset_code='USD'""",f"{type(exc).__name__}: {str(exc)[:300]}",checked)
        raise