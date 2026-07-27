"""Real 30-minute OHLC chart rendered as a Telegram-ready PNG."""
from __future__ import annotations
from dataclasses import dataclass
from io import BytesIO
from packages.core import db

@dataclass(frozen=True,slots=True)
class Candle:
 time:object;open:int;high:int;low:int;close:int;trades:int

async def candles(hours:int=24)->list[Candle]:
 rows=await db.fetch("""WITH price AS (
   SELECT date_bin(interval '30 minutes',captured_at,TIMESTAMPTZ '2000-01-01') bucket,
          (array_agg(price_toman ORDER BY captured_at))[1] open,
          max(price_toman) high,min(price_toman) low,
          (array_agg(price_toman ORDER BY captured_at DESC))[1] close
   FROM market_price_snapshots WHERE asset_code='USD' AND captured_at>=now()-($1::int*interval '1 hour') GROUP BY 1),
 trades AS (SELECT date_bin(interval '30 minutes',created_at,TIMESTAMPTZ '2000-01-01') bucket,count(*) trades
   FROM usd_trades WHERE created_at>=now()-($1::int*interval '1 hour') GROUP BY 1)
 SELECT p.bucket,p.open,p.high,p.low,p.close,COALESCE(t.trades,0) trades
 FROM price p LEFT JOIN trades t USING(bucket) ORDER BY p.bucket""",hours)
 return [Candle(r['bucket'],int(r['open']),int(r['high']),int(r['low']),int(r['close']),int(r['trades'])) for r in rows]

def render(rows:list[Candle])->BytesIO:
 from PIL import Image,ImageDraw,ImageFont
 w,h=1200,660;left,right,top,bottom=92,36,68,96
 image=Image.new('RGB',(w,h),'#07131f');d=ImageDraw.Draw(image)
 try:font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22);small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17);title=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',27)
 except OSError:font=small=title=ImageFont.load_default()
 d.text((left,20),'USDT / IRT  |  REAL 30M OHLC  |  LAST 24H',fill='#eaf5ff',font=title)
 if not rows:
  d.text((left,280),'No valid market snapshots yet',fill='#8ca6b8',font=font);out=BytesIO();image.save(out,'PNG',optimize=True);out.seek(0);out.name='usdt_30m.png';return out
 lo=min(x.low for x in rows);hi=max(x.high for x in rows);span=max(hi-lo,1);plot_h=h-top-bottom
 def y(v):return top+(hi-v)*plot_h/span
 for i in range(5):
  yy=top+i*plot_h/4;price=round(hi-i*span/4);d.line((left,yy,w-right,yy),fill='#183144',width=1);d.text((8,yy-10),f'{price:,}',fill='#7893a7',font=small)
 slot=(w-left-right)/max(48,len(rows));body=max(5,min(15,int(slot*.55)))
 for i,c in enumerate(rows):
  x=left+(i+.5)*slot;up=c.close>=c.open;color='#35d7c0' if up else '#ff6f91'
  d.line((x,y(c.high),x,y(c.low)),fill=color,width=2)
  y1,y2=y(c.open),y(c.close);d.rectangle((x-body/2,min(y1,y2),x+body/2,max(y1,y2)+1),fill=color)
  if i%8==0:d.text((x-25,h-bottom+18),c.time.strftime('%H:%M'),fill='#7893a7',font=small)
 change=(rows[-1].close-rows[0].open)*100/rows[0].open
 d.text((left,h-38),f'O {rows[0].open:,}   H {hi:,}   L {lo:,}   C {rows[-1].close:,}   {change:+.2f}%',fill='#b9cad6',font=font)
 d.text((w-300,24),f'{rows[-1].close:,} IRT',fill='#35d7c0' if change>=0 else '#ff6f91',font=title)
 out=BytesIO();image.save(out,'PNG',optimize=True);out.seek(0);out.name='usdt_30m.png';return out