"""همه صفحه‌های زندگی با دکمه‌های درون‌پیامی فارسی."""
from telegram import InlineKeyboardMarkup
from packages.core.ui import Keyboard,Style,button,cb
NS="tl"
def B(t,a,o,arg="",style=Style.GLASS):return button(t,cb(NS,a,o,arg),style=style)
def home(o:int,daily:bool,onboarding:int=4)->InlineKeyboardMarkup:
 k=Keyboard()
 if onboarding<4:k.row(B("🚀 ادامه مسیر شروع","journey",o,style=Style.PRIMARY))
 k.row(B("🎯 کارهای امروز","missions",o,style=Style.SUCCESS),B("🎁 هدیه روزانه","daily",o,style=Style.SUCCESS if daily else Style.GLASS))
 k.row(B("💼 کار و دریافت درآمد","jobs",o,style=Style.PRIMARY),B("💳 دارایی و بانک","economy",o))
 k.row(B("💵 بازار ارز","market",o),B("🏠 خانه و زندگی","housing",o))
 k.row(B("🪪 شخصیت من","profile",o),B("🗺 مسیر پیشرفت","unlocks",o))
 return k.build()
def journey(o,step):
 labels={0:"✨ تعیین هدف نخست",1:"🎁 دریافت سرمایه آغازین",2:"🎯 انجام نخستین کار روزانه",3:"🏁 ورود به زندگی اصلی"}
 return Keyboard().row(B(labels.get(step,"🏁 ورود به زندگی اصلی"),"jstep",o,str(step),style=Style.PRIMARY)).row(B("🏠 خانه","home",o)).build()
def back(o,a="home"):return Keyboard().row(B("🏠 خانه",a,o,style=Style.PRIMARY)).build()
def daily(o,ready):
 k=Keyboard()
 if ready:k.row(B("🎁 دریافت هدیه","claim",o,style=Style.SUCCESS))
 k.row(B("🎯 ادامه با کارهای امروز","missions",o,style=Style.PRIMARY),B("🏠 خانه","home",o));return k.build()
def missions(o,keys):
 k=Keyboard()
 for i,x in enumerate(keys):k.row(B(f"🎁 دریافت پاداش کار {i+1}","mclaim",o,x,style=Style.SUCCESS))
 k.row(B("🔄 تازه‌سازی","missions",o),B("🏠 خانه","home",o));return k.build()
def economy(o):return Keyboard().row(B("🏦 مدیریت پس‌انداز","savings",o,style=Style.PRIMARY),B("🧾 پرداخت هزینه زندگی","living",o,style=Style.SUCCESS)).row(B("🏠 انتخاب خانه","housing",o),B("🏠 منوی اصلی","home",o)).build()
def savings(o):return Keyboard().row(B("واریز ۵۰ هزار","deposit",o,"50000",Style.PRIMARY),B("برداشت ۵۰ هزار","withdraw",o,"50000")).row(B("واریز ۲۰۰ هزار","deposit",o,"200000"),B("برداشت ۲۰۰ هزار","withdraw",o,"200000")).row(B("↩️ بازگشت","economy",o)).build()
def housing(o):return Keyboard().row(B("اجاره اتاق","hrent",o,"room",Style.PRIMARY),B("خرید اتاق","hbuy",o,"room")).row(B("اجاره آپارتمان","hrent",o,"apartment"),B("خرید آپارتمان","hbuy",o,"apartment")).row(B("خرید ویلا","hbuy",o,"villa"),B("↩️ بازگشت","economy",o)).build()
def jobs(o,has):
 k=Keyboard()
 if has:k.row(B("🛠 کار کن و درآمد بگیر","jcollect",o,style=Style.SUCCESS)).row(B("⚙️ ارتقای مهارت","jupgrade",o,"production",Style.PRIMARY),B("🗄 افزایش ظرفیت","jupgrade",o,"storage"))
 else:k.row(B("🌾 کشاورز","jchoose",o,"farmer",Style.PRIMARY),B("⛏ معدن‌کار","jchoose",o,"miner")).row(B("💻 برنامه‌نویس","jchoose",o,"programmer"),B("📈 بازرگان","jchoose",o,"trader")).row(B("⚡ مهندس","jchoose",o,"engineer"),B("🩺 پزشک","jchoose",o,"doctor")).row(B("📰 روزنامه‌نگار","jchoose",o,"journalist"))
 k.row(B("🏠 منوی اصلی","home",o));return k.build()
def market(o):return Keyboard().row(B("خرید ۱۰ دلار","mbuy",o,"1000",Style.PRIMARY),B("فروش ۱۰ دلار","msell",o,"1000")).row(B("خرید ۵۰ دلار","mbuy",o,"5000"),B("فروش ۵۰ دلار","msell",o,"5000")).row(B("🔄 تازه‌سازی","market",o),B("🏠 خانه","home",o)).build()
