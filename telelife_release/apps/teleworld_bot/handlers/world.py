"""Single-message, Persian and button-first TeleWorld controller."""
from __future__ import annotations
from datetime import UTC,datetime
from uuid import uuid4
from telegram import Update
from telegram.constants import ChatMemberStatus,ChatType
from telegram.error import BadRequest,Forbidden
from telegram.ext import CallbackQueryHandler,ChatMemberHandler,CommandHandler,ContextTypes,MessageHandler,filters
from apps.teleworld_bot import keyboards as kb
from apps.teleworld_bot.texts import fa
from packages.core.repositories import country_repo,election_repo,group_repo,player_repo,production_repo,project_repo,ui_state_repo
from packages.core.services import country as countries,economy,elections,national_project,production
from packages.core.utils import fmt
GROUPS={ChatType.GROUP,ChatType.SUPERGROUP};FLOW='world_creation'
STATUS={'forming':'در حال ساخت','temporary':'موقت','official':'رسمی'};GOV={'republic':'جمهوری','monarchy':'پادشاهی','dictatorship':'دیکتاتوری','federal':'فدرال','council':'شورایی'}
async def admin(u,c):
 m=await c.bot.get_chat_member(u.effective_chat.id,u.effective_user.id);return m.status in {ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER}
async def player(u):
 x=u.effective_user;return await player_repo.get_or_create(x.id,username=x.username,first_name=x.first_name or 'شهروند',language_code=x.language_code or 'fa')
async def show(u,c,text,markup):
 chat=u.effective_chat;q=u.callback_query;state=await ui_state_repo.world(chat.id);mid=q.message.message_id if q and q.message else int(state['message_id']) if state else None
 if mid:
  try:await c.bot.edit_message_text(chat_id=chat.id,message_id=mid,text=text,reply_markup=markup);await ui_state_repo.set_world(chat.id,mid);return
  except BadRequest as e:
   if 'message is not modified' in str(e).lower():return
  except Forbidden:pass
 msg=await c.bot.send_message(chat.id,text,reply_markup=markup);await ui_state_repo.set_world(chat.id,msg.message_id)
async def facts(chat_id):
 row=await country_repo.by_chat(chat_id)
 if not row:return None,0,None
 count=int(await __import__('packages.core.db',fromlist=['fetchval']).fetchval('SELECT count(*) FROM citizenships WHERE country_id=$1 AND is_active',row['id']) or 0)
 leader=await __import__('packages.core.db',fromlist=['fetchval']).fetchval('SELECT first_name FROM players WHERE id=$1',row['president_player_id']) if row['president_player_id'] else None
 return row,count,leader
async def home(u,c):
 chat=u.effective_chat
 if chat.type not in GROUPS:await show(u,c,fa.PRIVATE,kb.private(c.bot.username or ''));return
 await group_repo.get_or_create(chat.id,chat.title or 'سرزمین بی‌نام');row,count,leader=await facts(chat.id);p=await player(u);cit=bool(row and await country_repo.citizenship(p.id))
 if not row:await show(u,c,fa.HOME_EMPTY,kb.home(False,await admin(u,c)));return
 goal='شهروند جذب کنید' if row['status']=='forming' else 'انتخابات رهبر را کامل کنید' if not row['president_player_id'] else 'پروژه و اقتصاد کشور را رشد دهید'
 text=fa.HOME.format(name=row['name'],status=STATUS.get(row['status'],row['status']),citizens=fmt.number(count),leader=leader or 'هنوز انتخاب نشده',treasury=fmt.toman(row['treasury_toman']),goal=goal);await show(u,c,text,kb.home(True,await admin(u,c),cit))
async def country_page(u,c):
 row,count,leader=await facts(u.effective_chat.id);await show(u,c,fa.COUNTRY.format(name=row['name'],government=GOV.get(row['government_type'],row['government_type']),status=STATUS.get(row['status'],row['status']),citizens=fmt.number(count),leader=leader or 'انتخاب نشده',treasury=fmt.toman(row['treasury_toman']),description=row['description']),kb.country())
async def economy_page(u,c):
 row,_,_=await facts(u.effective_chat.id);rs=await country_repo.resources(row['id']);assets={'oil':'نفت','food':'غذا','minerals':'مواد معدنی','energy':'انرژی','technology':'فناوری'};lines='\n'.join(f"• {assets.get(x['asset_code'],x['asset_code'])}: {fmt.number(x['quantity'])}" for x in rs);await show(u,c,fa.ECONOMY.format(treasury=fmt.toman(row['treasury_toman']),income=fmt.toman(row['daily_income_toman']),expense=fmt.toman(row['daily_expense_toman']),resources=lines),kb.back())
async def citizens_page(u,c):
 row,count,_=await facts(u.effective_chat.id);ids=await country_repo.citizens(row['id']);names=[]
 for pid in ids:
  n=await __import__('packages.core.db',fromlist=['fetchval']).fetchval('SELECT first_name FROM players WHERE id=$1',pid);names.append(f"• {n or 'شهروند'}")
 await show(u,c,fa.CITIZENS.format(count=fmt.number(count),members='\n'.join(names[:25]) or 'هنوز شهروندی ثبت نشده است.'),kb.back('country'))
async def politics_page(u,c):
 row,_,_=await facts(u.effective_chat.id);e=await election_repo.open_for_country(row['id']);state='انتخابات بازی وجود ندارد.' if not e else ('مرحله نام‌نویسی نامزدها باز است.' if e['status']=='nominations' else 'رأی‌گیری باز است.');await show(u,c,fa.POLITICS.format(state=state),kb.politics(bool(e)))
async def jobs_page(u,c):
 p=await player(u);row=await production_repo.get(p.id);body='هنوز شغلی نداری؛ از سطح ۵ انتخاب کن.'
 if row:
  a=production.accrue(row,datetime.now(UTC));body=f"شغل: <b>{row['job_code']}</b>\nدرآمد آماده: <b>{fmt.number(a.stored)} از {fmt.number(a.capacity)}</b>"
 await show(u,c,fa.JOBS.format(body=body),kb.jobs(bool(row)))
async def start(u,c):await home(u,c)
async def callback(u,c):
 q=u.callback_query;a=(q.data or '')[3:]
 try:
  if a=='home':await q.answer();c.chat_data.pop(FLOW,None);await home(u,c)
  elif a=='guide':await q.answer();await show(u,c,fa.GUIDE,kb.back())
  elif a=='country':await q.answer();await country_page(u,c)
  elif a=='economy':await q.answer();await economy_page(u,c)
  elif a=='citizens':await q.answer();await citizens_page(u,c)
  elif a=='politics':await q.answer();await politics_page(u,c)
  elif a=='jobs':await q.answer();await jobs_page(u,c)
  elif a=='create':
   await q.answer()
   if not await admin(u,c):await q.answer('فقط مدیر گروه می‌تواند ساخت را شروع کند.',show_alert=True);return
   c.chat_data[FLOW]={'step':'name','owner':q.from_user.id,'panel':q.message.message_id};await show(u,c,fa.WIZARD_NAME,kb.cancel())
  elif a.startswith('gov:'):await q.answer();c.chat_data[FLOW]['government']=a.split(':')[1];c.chat_data[FLOW]['step']='description';await show(u,c,fa.WIZARD_DESC,kb.cancel())
  elif a=='join':p=await player(u);ok=await countries.join_country(chat_id=u.effective_chat.id,player_id=p.id);await q.answer('شهروند شدی.' if ok else 'از قبل شهروندی.',show_alert=True);await home(u,c)
  elif a=='leave':p=await player(u);await countries.leave_country(chat_id=u.effective_chat.id,player_id=p.id);await q.answer('از کشور خارج شدی.',show_alert=True);await home(u,c)
  elif a.startswith('donate:'):p=await player(u);row,_,_=await facts(u.effective_chat.id);await economy.transfer(p.id,row['id'],'IRT',int(a.split(':')[1]),reason='donation',idempotency_key=f"world:{p.id}:{uuid4().hex}");await q.answer('کمک مالی ثبت شد.',show_alert=True);await country_page(u,c)
  elif a=='estart':p=await player(u);row,_,_=await facts(u.effective_chat.id);await elections.start(row['id'],p.id);await q.answer('انتخابات آغاز شد.',show_alert=True);await politics_page(u,c)
  elif a=='nominate':p=await player(u);row,_,_=await facts(u.effective_chat.id);e=await election_repo.open_for_country(row['id']);await elections.nominate(e['id'],p.id,u.effective_chat.id,q.message.message_id);await q.answer('نامزدی ثبت شد.',show_alert=True);await politics_page(u,c)
  elif a=='votehelp':
   await q.answer()
   row,_,_=await facts(u.effective_chat.id);e=await election_repo.open_for_country(row['id'])
   rows=await __import__('packages.core.db',fromlist=['fetch']).fetch('SELECT ec.player_id,p.first_name FROM election_candidates ec JOIN players p ON p.id=ec.player_id WHERE ec.election_id=$1 ORDER BY ec.created_at',e['id']);await show(u,c,'🗳 <b>انتخاب رهبر</b>\n\nنامزد موردنظر را انتخاب کن. رأی فقط یک‌بار ثبت می‌شود.',kb.candidates(rows))
  elif a.startswith('vote:'):
   p=await player(u);row,_,_=await facts(u.effective_chat.id);e=await election_repo.open_for_country(row['id']);ok=await elections.vote(e['id'],p.id,int(a.split(':')[1]));await q.answer('رأی ثبت شد.' if ok else 'قبلاً رأی داده‌ای.',show_alert=True);await politics_page(u,c)
  elif a.startswith('job:'):p=await player(u);await production.choose(p.id,a.split(':')[1]);await q.answer('شغل انتخاب شد.',show_alert=True);await jobs_page(u,c)
  elif a=='jcollect':p=await player(u);x,g=await production.collect(p.id,f"world-collect:{p.id}:{uuid4().hex}");await q.answer(f"{fmt.number(x)} واحد و {fmt.number(g)} تجربه گرفتی.",show_alert=True);await jobs_page(u,c)
  elif a.startswith('jup:'):p=await player(u);lvl=await production.upgrade(p.id,a.split(':')[1],f"world-up:{p.id}:{uuid4().hex}");await q.answer(f"به سطح {fmt.number(lvl)} رسید.",show_alert=True);await jobs_page(u,c)
  elif a=='project':
   await q.answer()
   row,_,_=await facts(u.effective_chat.id);pr=await project_repo.active(row['id']);body='هنوز پروژه‌ای فعال نیست.'
   if pr:
    rs=await project_repo.status(pr['id']);body='\n'.join(f"• {x['asset_code']}: {fmt.number(x['contributed_amount'])}/{fmt.number(x['required_amount'])}" for x in rs)
   await show(u,c,'🏗 <b>پروژه ملی</b>\n\n'+body,kb.project(bool(pr)))
  elif a=='pstart':
   p=await player(u);row,_,_=await facts(u.effective_chat.id);await national_project.start(row['id'],p.id);await q.answer('پروژه ملی آغاز شد.',show_alert=True);await home(u,c)
  elif a.startswith('pcon:'):
   p=await player(u);row,_,_=await facts(u.effective_chat.id);pr=await project_repo.active(row['id']);_,asset,amount=a.split(':');accepted,done=await national_project.contribute(pr['id'],p.id,asset,int(amount),f"world-project:{p.id}:{uuid4().hex}");await q.answer(f"{fmt.number(accepted)} واحد ثبت شد."+(" پروژه تکمیل شد!" if done else ''),show_alert=True);await home(u,c)
  elif a=='polls':await q.answer('هنوز نظرسنجی فعالی نیست.',show_alert=True)
 except (ValueError,PermissionError,TypeError):await q.answer('این عملیات فعلاً مجاز نیست یا شرایطش کامل نشده است.',show_alert=True)
async def text(u,c):
 f=c.chat_data.get(FLOW);m=u.effective_message
 if not f or u.effective_user.id!=f['owner']:return
 value=(m.text or '').strip()
 try:await m.delete()
 except Exception:pass
 if f['step']=='name':
  if not 3<=len(value)<=80:await c.bot.edit_message_text(chat_id=u.effective_chat.id,message_id=f['panel'],text='نام باید ۳ تا ۸۰ نویسه باشد.',reply_markup=kb.cancel());return
  f['name']=value;f['step']='government';await c.bot.edit_message_text(chat_id=u.effective_chat.id,message_id=f['panel'],text=fa.WIZARD_GOV,reply_markup=kb.governments());return
 if f['step']=='description':
  if not 10<=len(value)<=500:await c.bot.edit_message_text(chat_id=u.effective_chat.id,message_id=f['panel'],text='معرفی باید ۱۰ تا ۵۰۰ نویسه باشد.',reply_markup=kb.cancel());return
  p=await player(u);await countries.create_country(chat_id=u.effective_chat.id,chat_title=u.effective_chat.title or '',player_id=p.id,name=f['name'],government=f['government'],description=value);c.chat_data.pop(FLOW,None);await home(u,c)
def register(app):app.add_handler(CommandHandler('start',start));app.add_handler(CallbackQueryHandler(callback,pattern=r'^tw:'));app.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND,text))
