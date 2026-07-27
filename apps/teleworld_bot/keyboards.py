"""رابط دکمه‌ای و کاملاً فارسی جهان گروهی."""
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
def b(t,a,style=None):
 kw={'text':t,'callback_data':f'tw:{a}'}
 if style:kw['style']=style
 return InlineKeyboardButton(**kw)
def private(username):return InlineKeyboardMarkup([[InlineKeyboardButton('➕ افزودن به گروه',url=f'https://t.me/{username}?startgroup=true',style='primary')],[b('📘 راهنمای استفاده','guide')]])
def home(country,admin,citizen=False):
 if country:
  r=[[b('🏛 شناسنامه کشور','country','primary'),b('👥 شهروندان','citizens')],[b('💰 اقتصاد و منابع','economy'),b('🗳 سیاست و انتخابات','politics')],[b('🏗 پروژه ملی','project')]]
  if not citizen:r.append([b('🤝 شهروند این کشور می‌شوم','join','success')])
  else:r.append([b('🚪 خروج از شهروندی','leave')])
  r.append([b('📘 راهنمای همین مرحله','guide'),b('🔄 تازه‌سازی','home')]);return InlineKeyboardMarkup(r)
 if admin:return InlineKeyboardMarkup([[b('🏗 ساخت کشور','create','primary')],[b('📘 راهنمای ساخت کشور','guide')],[b('🔄 تازه‌سازی','home')]])
 return InlineKeyboardMarkup([[b('📘 برای ساخت کشور چه کنیم؟','guide','primary')],[b('🔄 تازه‌سازی','home')]])
def governments():return InlineKeyboardMarkup([[b('🏛 جمهوری','gov:republic','primary'),b('👑 پادشاهی','gov:monarchy')],[b('🤝 شورایی','gov:council'),b('🏢 فدرال','gov:federal')],[b('لغو ساخت کشور','home')]])
def country():return InlineKeyboardMarkup([[b('💰 کمک ۵۰ هزار تومان','donate:50000','success'),b('💰 کمک ۲۰۰ هزار تومان','donate:200000')],[b('🗳 انتخابات','politics','primary'),b('👥 شهروندان','citizens')],[b('🏠 خانه جهان','home')]])
def politics(has_open=False):
 r=[[b('🗳 آغاز انتخابات','estart','primary')]] if not has_open else [[b('🙋 نامزد می‌شوم','nominate','primary'),b('🗳 انتخاب نامزد','votehelp')]]
 r += [[b('📊 نظرسنجی‌ها','polls'),b('🏠 خانه جهان','home')]];return InlineKeyboardMarkup(r)
def back(a='home'):return InlineKeyboardMarkup([[b('🏠 خانه جهان',a,'primary')]])
def cancel():return back()
def candidates(rows):
 r=[[b(f"🗳 رأی به {x['first_name']}",f"vote:{x['player_id']}",'primary' if i==0 else None)] for i,x in enumerate(rows)]
 r.append([b('↩️ بازگشت','politics')]);return InlineKeyboardMarkup(r)
def project(active):
 if active:return InlineKeyboardMarkup([[b('💵 کمک ۵۰ هزار تومان','pcon:IRT:50000','success')],[b('🌾 کمک ۵۰ غذا','pcon:food:50'),b('⛏ کمک ۵۰ ماده معدنی','pcon:minerals:50')],[b('🏠 خانه جهان','home')]])
 return InlineKeyboardMarkup([[b('🏗 آغاز پروژه ملی','pstart','primary')],[b('🏠 خانه جهان','home')]])
