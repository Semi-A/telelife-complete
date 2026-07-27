"""Canonical country identity for every group-facing system message."""
from __future__ import annotations
from html import escape
from packages.core import db

SETUP_TEXT="🏗 این گروه هنوز کشور ثبت‌شده ندارد.\n\nیکی از مدیران گروه وارد TeleWorld شود و از «ساخت کشور» نام، حکومت و مشخصات کشور را کامل کند. تا آن زمان خبرها و رویدادهای سیستمی این گروه منتشر نمی‌شوند."

async def destination(chat_id:int):
 """Return None for non-world destinations, or a row with nullable country fields."""
 return await db.fetchrow("""SELECT g.id group_id,g.telegram_id,c.id country_id,c.name country_name,c.status
  FROM groups g LEFT JOIN countries c ON c.group_id=g.id WHERE g.telegram_id=$1""",chat_id)

async def by_chat(chat_id:int):
 row=await destination(chat_id)
 return row if row and row["country_id"] else None

def masthead(country_name:str, text:str)->str:
 return f"🏛 <b>خبرگزاری {escape(country_name)}</b>\n\n{text}"

async def should_send_setup_notice(chat_id:int)->bool:
 key=f"missing-country-notice:{chat_id}"
 return bool(await db.fetchval("""INSERT INTO product_audit_log(event_key,event_type,chat_id,details)
  VALUES($1,'missing_country_notice',$2,'{}'::jsonb) ON CONFLICT DO NOTHING RETURNING id""",key,chat_id))