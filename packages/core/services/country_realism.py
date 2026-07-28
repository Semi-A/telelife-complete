"""Deterministic daily macro economy, rare shocks, and country newspaper."""
from __future__ import annotations
import hashlib
from datetime import UTC,datetime
from packages.core import db
from packages.core.repositories import outbox_repo

def _roll(country_id:int, day, salt:str, modulo:int)->int:
 return int.from_bytes(hashlib.sha256(f"{country_id}:{day}:{salt}".encode()).digest()[:4],"big")%modulo

async def daily_tick()->dict[str,int]:
 day=datetime.now(UTC).date();indicators=shocks=papers=0
 async with db.transaction() as conn:
  countries=await conn.fetch("""SELECT c.*,g.telegram_id,
   COALESCE((SELECT sum(quantity) FROM country_resources r WHERE r.country_id=c.id),0) resources,
   (SELECT count(*) FROM citizenships z WHERE z.country_id=c.id AND z.is_active) citizens
   FROM countries c JOIN groups g ON g.id=c.group_id WHERE g.is_active""")
  for c in countries:
   citizens=int(c['citizens'] or 0);resources=int(c['resources'] or 0);treasury=int(c['treasury_toman'])
   prev=await conn.fetchrow("SELECT * FROM country_indicator_daily WHERE country_id=$1 ORDER BY indicator_date DESC LIMIT 1",c['id'])
   active=await conn.fetchrow("SELECT * FROM country_shocks WHERE country_id=$1 AND ends_at>now() ORDER BY starts_at DESC LIMIT 1",c['id'])
   adverse=bool(active and active['shock_code'] in {'sanctions','drought'})
   reserve_buffer=min(250,int(c['fx_reserve_cents'])//1_000_000) if adverse else 0
   shock_inflation=max(100,500-reserve_buffer) if adverse else -150 if active else 0
   shock_growth=min(-75,-350+reserve_buffer) if adverse else 450 if active else 0
   base_inflation=int(prev['inflation_bp']) if prev else 1800
   policy_gap=int(c['interest_rate_bp'])-int(c['inflation_target_bp'])
   inflation=max(-500,min(100000,base_inflation-policy_gap//20+shock_inflation+_roll(c['id'],day,'inflation',101)-50))
   unemployment=max(0,min(10000,(int(prev['unemployment_bp']) if prev else 1200)-shock_growth//4+_roll(c['id'],day,'jobs',61)-30))
   interest_drag=max(0,policy_gap)//25
   organic_growth=250+resources//max(1000,citizens*100)-unemployment//20-interest_drag
   growth=max(-10000,min(10000,organic_growth+shock_growth))
   release_b=await conn.fetchrow("SELECT satisfaction,food_shortage_bp,energy_shortage_bp FROM country_economy_state WHERE country_id=$1",c['id'])
   base_satisfaction=int(release_b['satisfaction']) if release_b else 70
   shortage_penalty=((int(release_b['food_shortage_bp'])+int(release_b['energy_shortage_bp']))//2500) if release_b else 0
   satisfaction=max(0,min(100,base_satisfaction-inflation//500-unemployment//500-shortage_penalty+min(5,treasury//max(1,100_000_000))))
   gdp=max(0,citizens*5_000_000+resources*1000+treasury//10)
   result=await conn.execute("""INSERT INTO country_indicator_daily(country_id,indicator_date,inflation_bp,unemployment_bp,satisfaction,growth_bp,gdp_toman)
    VALUES($1,$2,$3,$4,$5,$6,$7) ON CONFLICT DO NOTHING""",c['id'],day,inflation,unemployment,satisfaction,growth,gdp)
   indicators+=int(result.rsplit(' ',1)[-1])
   shock=None
   if not active and _roll(c['id'],day,'shock',1000)<8:
    code=('sanctions','drought','export_boom')[_roll(c['id'],day,'kind',3)]
    title={'sanctions':'موج تازه تحریم تجاری','drought':'خشکسالی در مناطق تولیدی','export_boom':'رونق ناگهانی صادرات'}[code]
    effects={'inflation_bp':500,'growth_bp':-350} if code!='export_boom' else {'inflation_bp':-150,'growth_bp':450}
    shock=await conn.fetchrow("""INSERT INTO country_shocks(country_id,shock_code,title,effects,ends_at,announced_at)
      VALUES($1,$2,$3,$4,now()+interval '3 days',now()) RETURNING id,title""",c['id'],code,title,effects);shocks+=1
   headline=(shock['title'] if shock else f"نبض اقتصاد {c['name']}: رشد {growth/100:+.1f}٪")
   body=f"تورم {inflation/100:.1f}٪ · بیکاری {unemployment/100:.1f}٪ · رشد {growth/100:+.1f}٪ · رضایت {satisfaction} از ۱۰۰\nنرخ بهره بانک مرکزی {int(c['interest_rate_bp'])/100:.1f}٪ و ذخیره ارزی {int(c['fx_reserve_cents'])/100:,.0f} دلار است."
   row=await conn.fetchrow("""INSERT INTO country_newspapers(country_id,issue_date,headline,body,indicators,shock_id)
    VALUES($1,$2,$3,$4,$5,$6) ON CONFLICT DO NOTHING RETURNING country_id""",c['id'],day,headline,body,{'inflation_bp':inflation,'unemployment_bp':unemployment,'growth_bp':growth,'satisfaction':satisfaction},shock['id'] if shock else None)
   if row:
    text=f"🗞 <b>{headline}</b>\n\n{body}"
    if await outbox_repo.enqueue(conn,f"country-paper:{c['id']}:{day}","country_newspaper",{'text':text},c['telegram_id']):papers+=1
 return {'indicators':indicators,'shocks':shocks,'newspapers':papers}


async def policy_view(country_id:int):
 return await db.fetchrow("""SELECT c.interest_rate_bp,c.inflation_target_bp,c.fx_reserve_cents,c.treasury_toman,
  i.inflation_bp,i.unemployment_bp,i.satisfaction,i.growth_bp,i.gdp_toman,i.indicator_date
  FROM countries c LEFT JOIN LATERAL(SELECT * FROM country_indicator_daily WHERE country_id=c.id ORDER BY indicator_date DESC LIMIT 1)i ON TRUE
  WHERE c.id=$1""",country_id)

async def set_interest(country_id:int,player_id:int,delta_bp:int):
 if delta_bp not in {-100,100}:raise ValueError('invalid_policy_step')
 return await db.fetchval("""UPDATE countries SET interest_rate_bp=interest_rate_bp+$3,updated_at=now()
  WHERE id=$1 AND president_player_id=$2 AND interest_rate_bp+$3 BETWEEN 0 AND 10000 RETURNING interest_rate_bp""",country_id,player_id,delta_bp)

async def buy_reserve(country_id:int,player_id:int,toman:int=10_000_000):
 if toman<=0:raise ValueError('invalid_amount')
 async with db.transaction() as conn:
  price=int(await conn.fetchval("SELECT current_price_toman FROM market_prices WHERE asset_code='USD'") or 0)
  if price<=0:raise ValueError('market_not_initialized')
  cents=toman*100//price
  row=await conn.fetchrow("""UPDATE countries SET treasury_toman=treasury_toman-$3,fx_reserve_cents=fx_reserve_cents+$4,updated_at=now()
   WHERE id=$1 AND president_player_id=$2 AND treasury_toman>=$3 RETURNING fx_reserve_cents""",country_id,player_id,toman,cents)
  if not row:raise ValueError('president_or_balance_required')
  return cents
