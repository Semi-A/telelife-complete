"""All player-facing Persian copy for TeleWorld."""
CREATE_USAGE="روش استفاده: /createcountry نام | republic | توضیحات"
ADMIN_REQUIRED="فقط مدیر گروه تلگرام می‌تواند کشور را ثبت کند."
COUNTRY_CREATED="🏛 کشور <b>{name}</b> ساخته شد. حفاظت اولیه فعال است."
COUNTRY_JOINED="🤝 شهروند کشور شدی."
COUNTRY_EXISTS="این گروه قبلاً کشور دارد."
COUNTRY_MISSING="این گروه هنوز کشور ندارد."
COUNTRY_STATUS="🏛 <b>{name}</b>\n{description}\nحکومت: {government}\nخزانه: {treasury}"
DONATE_USAGE="روش استفاده: /donate IRT 10000"
DONATED="🎁 {amount} واحد {asset} به کشور اهدا شد."
TAX_PAID="🧾 مالیات پرداخت شد."
JOBS="شغل‌ها: farmer, miner, trader, journalist, doctor, programmer, engineer"
JOB_CHOSEN="⚙️ شغل انتخاب شد. تولید از همین حالا شروع شد."
COLLECTED="📦 {amount} واحد جمع شد و {xp} XP گرفتی."
UPGRADED="⬆️ {kind} به سطح {level} ارتقا یافت."
ELECTION_STARTED="🗳 انتخابات شروع شد."
NOMINATED="نامزدی ثبت شد."
VOTED="رأی محرمانه ثبت شد."
DUPLICATE_VOTE="قبلاً در این رأی‌گیری شرکت کردی."
PROJECT_STARTED="🏗 پروژه ملی شروع شد."
CONTRIBUTED="🤝 {amount} واحد به پروژه اضافه شد."
POLL_STARTED="📊 نظرسنجی شروع شد."
FLAG_SET="🏳 پرچم کشور ثبت شد."
ANNOUNCED="📣 اطلاعیه در صف انتشار قرار گرفت."
CITIZEN_REQUIRED="اول با /joincountry شهروند شو."
PRESIDENT_REQUIRED="این کار فقط دست رئیس‌جمهور است."
PRIVATE_ONLY="این دستور را داخل گروه اجرا کن."
ERROR="انجام عملیات ممکن نشد. کمی بعد دوباره امتحان کن."
HELP="/createcountry /joincountry /country /donate /paytax /jobs /choosejob /collect /upgrade /startelection /nominate /vote /startproject /contribute /poll /polls /pollvote /setflag /announce"
TAX_USAGE = "روش استفاده: /paytax 10000"
CHOOSE_JOB_USAGE = "روش استفاده: /choosejob farmer"
UPGRADE_USAGE = "روش استفاده: /upgrade production یا /upgrade storage"
INVALID_AMOUNT = "مقدار باید یک عدد صحیح مثبت باشد."
INVALID_INPUT = "ورودی معتبر نیست: {reason}"

START_PRIVATE = (
    "🌐 <b>به TeleWorld خوش آمدید</b>\n\n"
    "TeleWorld بخش گروهی بازی است؛ کشور، اقتصاد، شغل، انتخابات و پروژه‌های ملی "
    "داخل گروه‌های تلگرام اجرا می‌شوند.\n\n"
    "ربات را به گروه اضافه کنید و همان‌جا /start یا /status را بزنید."
)
START_GROUP = (
    "🌍 <b>TeleWorld در این گروه فعال شد</b>\n\n"
    "از منوی زیر شروع کنید. برای ساخت کشور، مدیر گروه می‌تواند از /createcountry استفاده کند."
)

# Guided TeleWorld experience
WORLD_PRIVATE = (
    "🌐 <b>من TeleWorld هستم</b>\n\n"
    "بخش گروهی دنیای TeleLife؛ اینجا گروه شما تبدیل به یک کشور می‌شود، "
    "شهروند می‌گیرد، اقتصاد می‌سازد و وارد سیاست می‌شود.\n\n"
    "برای شروع من را به یک گروه اضافه کنید."
)
WORLD_ADDED = (
    "🌍 <b>TeleWorld وارد گروه شد</b>\n"
    "<code>─────────────────</code>\n"
    "من این گروه را به یک دنیای زنده تبدیل می‌کنم: کشور، شغل، تولید، "
    "انتخابات و پروژه‌های ملی.\n\n"
    "👑 <b>مدیر گروه:</b> از منوی زیر «ساخت کشور» را بزن.\n"
    "👥 <b>اعضا:</b> بعد از ساخت کشور، با یک دکمه شهروند شوید.\n\n"
    "هر وقت گم شدید /menu را بزنید."
)
WORLD_HOME_EMPTY_ADMIN = (
    "🧭 <b>شروع TeleWorld</b>\n\n"
    "این گروه هنوز کشور ندارد. ساخت کشور فقط سه مرحله ساده دارد:\n"
    "۱) نام کشور  ۲) نوع حکومت  ۳) توضیح کوتاه\n\n"
    "دکمه ساخت کشور را بزنید؛ من قدم‌به‌قدم همراهتان هستم."
)
WORLD_HOME_EMPTY_MEMBER = (
    "🧭 <b>TeleWorld آماده است</b>\n\n"
    "هنوز کشوری در این گروه ساخته نشده. از یکی از مدیرهای گروه بخواهید "
    "با دکمه «ساخت کشور» راه‌اندازی را انجام دهد."
)
WORLD_HOME_COUNTRY = (
    "🏛 <b>{name}</b>\n"
    "مرکز فرمان کشور آماده است. از دکمه‌ها برای دیدن کشور، شغل، سیاست و اقتصاد استفاده کنید."
)
WORLD_GUIDE = (
    "📘 <b>راهنمای خیلی سریع</b>\n\n"
    "<b>۱. کشور:</b> مدیر گروه آن را با Wizard می‌سازد.\n"
    "<b>۲. شهروندی:</b> اعضا دکمه عضویت را می‌زنند.\n"
    "<b>۳. شغل:</b> /choosejob programmer و بعد /collect\n"
    "<b>۴. اقتصاد:</b> /donate IRT 10000 یا /paytax 10000\n"
    "<b>۵. سیاست:</b> بعد از شکل‌گیری کشور انتخابات و پروژه ملی فعال‌اند.\n\n"
    "دستورهای اصلی: /menu، /country، /jobs، /help"
)
WIZARD_NAME = "🏗 <b>مرحله ۱ از ۳ — نام کشور</b>\n\nنامی بین ۳ تا ۸۰ حرف بفرستید.\nمثال: جمهوری آفتاب"
WIZARD_NAME_ERROR = "نام کشور باید بین ۳ تا ۸۰ حرف باشد. یک نام دیگر بفرستید."
WIZARD_GOVERNMENT = "🏗 <b>مرحله ۲ از ۳ — نوع حکومت</b>\n\nیکی از مدل‌های زیر را انتخاب کنید:"
WIZARD_DESCRIPTION = "🏗 <b>مرحله ۳ از ۳ — معرفی {name}</b>\n\nدر یک یا دو جمله کشور را معرفی کنید (۱۰ تا ۵۰۰ حرف)."
WIZARD_DESCRIPTION_ERROR = "توضیح باید بین ۱۰ تا ۵۰۰ حرف باشد. کمی کامل‌تر بنویسید."
COUNTRY_CREATED_GUIDED = (
    "🎉 <b>{name} ساخته شد!</b>\n\n"
    "شما بنیان‌گذار و اولین شهروند هستید. حالا اعضای گروه می‌توانند از منوی /menu عضو شوند، "
    "شغل انتخاب کنند و اقتصاد کشور را بسازند."
)
ALREADY_CITIZEN = "شما قبلاً شهروند یک کشور هستید."
JOBS_GUIDE = (
    "💼 <b>شغل و تولید</b>\n\n"
    "شغل‌ها: farmer، miner، trader، journalist، doctor، programmer، engineer\n\n"
    "انتخاب: <code>/choosejob programmer</code>\n"
    "جمع‌آوری درآمد: <code>/collect</code>\n"
    "ارتقای تولید: <code>/upgrade production</code>\n"
    "ارتقای انبار: <code>/upgrade storage</code>"
)
POLITICS_GUIDE = (
    "🗳 <b>سیاست کشور</b>\n\n"
    "شروع انتخابات: /startelection\nنامزدی: /nominate\n"
    "رأی: روی پیام نامزد Reply کنید و /vote بزنید.\n"
    "پروژه ملی: /startproject"
)
DONATE_GUIDE = (
    "🎁 <b>کمک به کشور</b>\n\n"
    "کمک پولی: <code>/donate IRT 10000</code>\n"
    "مالیات: <code>/paytax 10000</code>\n"
    "برای منابع، IRT را با food، oil، minerals، energy یا technology جایگزین کنید."
)
GOVERNMENT_NAMES = {"republic":"جمهوری","monarchy":"پادشاهی","dictatorship":"دیکتاتوری","federal":"فدرال","council":"شورایی"}
ERROR_NAMES = {"invalid_government":"نوع حکومت معتبر نیست.","invalid_name":"نام کشور معتبر نیست.","invalid_description":"توضیح کشور معتبر نیست.","country_already_exists":"این گروه قبلاً کشور دارد."}