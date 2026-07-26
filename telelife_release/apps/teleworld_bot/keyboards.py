"""منوهای شیشه‌ای فارسی TeleWorld."""
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
def b(t,a,style=None):
 kw={'text':t,'callback_data':f'tw:{a}'}
 if style:kw['style']=style
 return InlineKeyboardButton(**kw)
def private(username):return InlineKeyboardMarkup([[InlineKeyboardButton('➕ افزودن به گروه',url=f'https://t.me/{username}?startgroup=true',style='primary')],[b('📘 راهنمای جهان','guide')]])
def home(country,admin,citizen=False):
 r=[]
 if country:
  r+=[[b('🏛 وضعیت کشور','country','primary'),b('👥 شهروندان','citizens')],[b('💰 اقتصاد و منابع','economy'),b('🗳 سیاست و انتخابات','politics')],[b('🏗 پروژه ملی','project'),b('💼 شغل شخصی','jobs')]]
  if not citizen:r.append([b('🤝 شهروند این کشور می‌شوم','join','success')])
  r.append([b('📘 راهنما','guide'),b('🔄 تازه‌سازی','home')])
 elif admin:r=[[b('🏗 ساخت کشور','create','primary')],[b('📘 قبل از ساخت بخوان','guide')]]
 else:r=[[b('⏳ هنوز کشوری ساخته نشده','guide','primary')],[b('🔄 تازه‌سازی','home')]]
 return InlineKeyboardMarkup(r)
def governments():return InlineKeyboardMarkup([[b('🏛 جمهوری','gov:republic','primary'),b('👑 پادشاهی','gov:monarchy')],[b('🤝 شورایی','gov:council'),b('🏢 فدرال','gov:federal')],[b('لغو','home')]])
def country():return InlineKeyboardMarkup([[b('💰 کمک ۵۰ هزار','donate:50000','success'),b('💰 کمک ۲۰۰ هزار','donate:200000')],[b('🗳 انتخابات','politics','primary'),b('👥 شهروندان','citizens')],[b('🚪 خروج از کشور','leave'),b('🏠 خانه جهان','home')]])
def politics(has_open=False):
 r=[[b('🗳 شروع انتخابات','estart','primary')]] if not has_open else [[b('🙋 نامزد می‌شوم','nominate','primary'),b('🗳 رأی‌دادن','votehelp')]]
 r += [[b('📊 نظرسنجی‌ها','polls'),b('🏠 خانه جهان','home')]];return InlineKeyboardMarkup(r)
def jobs(has):
 r=[[b('📦 دریافت درآمد','jcollect','success')],[b('⚙️ ارتقای مهارت','jup:production','primary'),b('🗄 ارتقای ظرفیت','jup:storage')]] if has else [[b('🌾 کشاورز','job:farmer','primary'),b('💻 برنامه‌نویس','job:programmer')],[b('📈 بازرگان','job:trader'),b('⚡ مهندس','job:engineer')],[b('🩺 پزشک','job:doctor'),b('📰 روزنامه‌نگار','job:journalist')]]
 r.append([b('🏠 خانه جهان','home')]);return InlineKeyboardMarkup(r)
def back(a='home'):return InlineKeyboardMarkup([[b('🏠 خانه جهان',a,'primary')]])
def cancel():return back()

def candidates(rows):
 r=[]
 for x in rows:r.append([b(f"🗳 رأی به {x['first_name']}",f"vote:{x['player_id']}",'primary' if not r else None)])
 r.append([b('بازگشت','politics')]);return InlineKeyboardMarkup(r)
def project(active):
 if active:return InlineKeyboardMarkup([[b('💵 کمک ۵۰ هزار تومان','pcon:IRT:50000','success')],[b('🌾 کمک ۵۰ غذا','pcon:food:50'),b('⛏ کمک ۵۰ معدن','pcon:minerals:50')],[b('🏠 خانه جهان','home')]])
 return InlineKeyboardMarkup([[b('🏗 آغاز پروژه ملی','pstart','primary')],[b('🏠 خانه جهان','home')]])
