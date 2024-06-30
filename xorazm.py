import logging
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Bot hodisalarini ko'rsatish uchun loglarni sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bu yerda bot tokeningizni kiriting
BOT_TOKEN = "7188417837:AAGtSQR57I_-9YOAYoEWaS1Fekg-eTS5Sok"

# Foydalanuvchilar ma'lumotlarini saqlash uchun fayl nomi
USER_DATA_FILE = "users.json"

# Foydalanuvchilar ma'lumotlarini faylga yozish
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)

# Foydalanuvchilar ma'lumotlarini fayldan yuklash
def load_users():
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# /start buyrug'i uchun handler funktsiyasini aniqlang
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    users = load_users()
    users[user.id] = {"first_name": user.first_name, "last_name": user.last_name, "username": user.username}
    save_users(users)

    keyboard = [
        [InlineKeyboardButton("Qadimgi Xorazm tarixi", callback_data='xorazm_tarixi')],
        [InlineKeyboardButton("Xiva xonligi tarixi", callback_data='xiva_xonligi')],
        [InlineKeyboardButton("Hozirgi Xorazm", callback_data='hozirgi_xorazm')],
        [InlineKeyboardButton("Xorazmshohlar tarixi", callback_data='xorazmshohlar')],
        [InlineKeyboardButton("Islomxo'ja minorasi tarixi", callback_data='islomxoja_minorasi')],
        [InlineKeyboardButton("Kalta Minor tarixi", callback_data='kalta_minor')],
        [InlineKeyboardButton("Ichan Qal'a tarixi", callback_data='ichan_qala')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Kerakli bo\'limni tanlang va menga obuna bo`lish esdan chiqmasin @hikmatdev_xudayberganov:', reply_markup=reply_markup)

# Tugmani bosganda bajariladigan funktsiyani aniqlang
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()


    if query.data == 'xorazm_tarixi':
        text = "Xorazm tarixi: \nXorazm O`rta Osiyo hududidagi eng qadimiy davlatlardan biri bo`lib, aholisi o`troq va ko`chmanchi qabilalardan iborat bo`lgan va kelib chiqishi haqida ko`plab afsonalar bor. Xorazm atamasinig kelib chiqishi kuda qadimga borib taqaladi ammo bu haqda aniq va tiniq malumotlar yo`q. Ammo eng haqiqatga yaqin ma`no bu bita rivoyatga borib taqaladi: QADIMDA BIR PODSHOH ISYON QILGAN AHOLINI CHO`LU BIYOBONGA SURGUN QILISHNI BUYURGAN VA ULAR CHO`LGA SURGUN QILINGA KEYINCHALIK ORADAN YILLAR O`TGANDAN SO`NG PODSHOH CHO`LGA SURGUN QILINGAN ISYONKORLARDAN XABAR OLIDINGMI DEYA SO`RAYDI MULOZIMLAR YO`Q DEGAN JAVOBNI BERADI. KEYIN PODSHOH O`RNIDAN TURIB SURGUN QILINGAN INSONLARNI KO`RISHGA BORADI BORIB NE KO`Z BILAN KO`RSINLAR-KI BU YERDA QUM O`RNIGA YASHIL BOG` VA O`RMONLAR PAYDO BO`LGAN. SHUNFA PODSHOH 'BIZ ULARNI XOR BO`LSIN DEB SURGUN QILDIK ULAR BU YERNI AZM QILIBDI DEGAN EKAN VA SURGUN QILGAN INSONLARGA SHU YERNI HADYA QILIADI VA BU YER XORAZMga aylanadi' batafsil:https://uz.wikipedia.org/wiki/Xorazm "
        photo_url = 'https://www.gazeta.uz/media/img/2022/02/SEIK0z16439064081903_l.jpg'
    elif query.data == 'xiva_xonligi':
        text = "Xiva xonligi tarixi: \nXiva xonligi tarixi Xiva xonligi XVII asrda Xorazmda tashkil topgan davlatdir. Temuriylar tasarrufida bo`lgan Xorazm hududini Shayboniyxon 1505 yilda bosib olgan. Shayboniyxon vafoti (1510 yil) dan keyin Xorazm Eron safaviylari qo`l ostiga o`tdi. Ularga qarshi xalq qo`zg`olonlari bo`lib, unga Vazir qal`asi qozisi Umar va Baqirg`on qishlog`idan mulla Sayd Hisomiddin boshchilik qildi. Ikki yil davom etgan kurashlar natijasida eroniylar mamlakatdan quvib chiqarilgan va xorazmliklar taklifi bilan 1511 yilda Vazir shahrini egallagan shayboniylardan Elbarsxon Xorazm hukmdori deb tan olingan.1512 yilga kelib xonlik hokimiyati ko`chmanchi o`zbeklarning boshqa urug`i (shajarasi) rahbari Elbarsxon qo`liga o`tadi. Shu vaqtdan boshlab Xiva xonligi yuzaga keladi, uning poytaxti turli yillarda Vazir, Ko`na Urganch va Xiva shaharlari bo`lgan. Xonlik tarkibiga Xorazmdan tashqari Mang`ishloq, Balxan tog`lari, Dehiston, O`zboy(Uzboy) va O`rta Xuroson hududlari kirgan."
        photo_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Khiva_Khanate_19th_century.png/1200px-Khiva_Khanate_19th_century.png'
    elif query.data == 'hozirgi_xorazm':
        text = "Hozirgi Xorazm: \nHozirgi Xorazm, O'zbekiston Respublikasining g'arbiy qismida joylashgan va Xorazm viloyatini tashkil etadi.Xorazm viloyati — O`zbekiston Respublikasi tarkibidagi viloyat. 1925-yil fevraldan 1938-yil yanvargacha Xorazm okrugi, 1938-yil 15-yanvarda viloyat maqomiga o`tkazilgan. Viloyat shimoldan Qoraqalpog`iston respublikasi, janubdan Turkmaniston respublikasining Toshhovuz viloyati, sharqdan Buxoro viloyati bilan chegaradosh. Shaharlari — Urganch , Xiva va Pitnak. Umumiy maydoni — 6,05 ming kvadrat kilometr. Ma`muriy markazi — Urganch shahri. Xorazm viloyati qadimda juda katta yerlarga egalik qilishiga qaramsdan Rossiya imperiyasi va SSSR tufayli hozirgi ko`rinishga keltirilgan. Xorazmning markazi Urganch shahri hisoblanadi. batafsil:https://uz.wikipedia.org/wiki/Xorazm_viloyati"
        photo_url = 'https://ru-static.z-dn.net/files/d00/d3f01c711ec330a8dc7002133117995d.jpg'
    elif query.data == 'xorazmshohlar':
        text = "Xorazmshohlar tarixi: \nXorazmshohlar davlati XII-XIII asrlarda Markaziy Osiyoda mavjud bo'lgan kuchli va qudratli davlatlardan biridir. Xorazmshohlar hozirgi Markaziy Osiyo, Eron, Pokiston, Afg`oniston, Azarbayjon,Gruziya va boshqa bir qancha davlatlarni egallagan batafsil:https://uz.wikipedia.org/wiki/Xorazmshohlar_davlati"
        photo_url = 'https://i.pinimg.com/originals/36/05/55/3605557df553fc75e9c735d109cce87f.jpg'
        text = "Islomxo'ja minorasi tarixi: \nIslomxo`ja minorasi – Xivadagi minora, Islomxo`ja majmuasi tarkibiga kiruvchi Ichan-qal`a qal`asi markazida shu nomdagi madrasa bilan birga joylashgan. Bu Xivaning eng baland binosi bo`lib, ba`zi ma`lumotlarga ko`ra, 56,6 metr ko`rsatkichi bilan O`rta Osiyodagi ikkinchi eng baland minoradir (uchinchi o`rinda Buxorodagi Kalon minorasi – 46,5 metr), birinchi o`rinda Ko`hna Urganchdagi Qutlug` Temur minorasi 60 metrdan ortiq[3]). Biroq, L. Y. Mankovskiy va V. A. Bulatovaning so`zlariga ko`ra, minoraning g`ayrioddiy yuqoriga surishi optik effekt bo`lib, u diametrning yuqoriga qarab tez qisqarishi va minoraning ritmik qoplamasi bilan bog`liq, minoraning haqiqiy vertikal o`lchami esa atigi 44,5 metrni tashkil qiladi. Minora va Islomxo`ja madrasasi qurilishi Xiva xonligi hukmdori Asfandiyorxonning qaynotasi va bosh vaziri Islomxo`ja tashabbusi bilan 1908-yilda boshlangan. Minora va madrasa qurilishida taniqli me`mor Xudoybergan hoji, shuningdek, mohir naqqosh Eshmuhammad Xudoyberdiyev, Bolta Voisovlar ishtirok etgan. Ikkala ob`ektning qurilishi 1910-yilga kelib tugallandi."
        photo_url = 'https://uzbekistan.travel/storage/app/uploads/public/5e9/848/7b4/thumb_684_600_480_0_0_auto.jpg'
    elif query.data == 'kalta_minor':
        text = "Kalta Minor tarixi: \n Kaltaminor Xiva xonligi xoni Muhammad Aminxon tomonidan musulmon olamidagi eng katta va eng baland minora bo`lishi maqsadida yaratilgan. Xonning rejasiga ko`ra, minoraning balandligi 70-80 metr bo`lishi, balandligi oshgan sayin keskin pasayib boruvchi diametri minoraning mustahkamligini oshirishi kerak edi. Muhammad Aminxon hatto 73 metrlik Hindiston Qutb minordan ham oshib ketadigan dunyodagi eng baland minorani qurishga qaror qiladi[2]. Uning poydevorining diametri 14,2 metrni tashkil qiladi. Ba`zi bir manbalarda 110 metrga yetkazilishi qayd etilgan batasfil:https://uz.wikipedia.org/wiki/Kaltaminor "
        photo_url = 'https://lh3.googleusercontent.com/proxy/4P1INeAVreE0lc_HSHjomLpB8984IXAoz97uCIHCEA-CUWFZ9YJpHVuUByf_al7PZP7nC2D00_gh2a-ZPpZ0EwKkWFgIjf0DqsRMMmP_0PkbzKzzgfQhCKM'
    elif query.data == 'ichan_qala':
        text = "Ichan Qal'a tarixi: \nIchan-qal`a (o`zbekcha: Ichan Qa'la) – O`zbekistonning tarixiy o`zbek shahri Xivaning mustahkam devor bilan o`ralgan ichki shahri bo`lib, Markaziy Osiyodagi birinchi Jahon me`rosi ob`ektiga aylandi. Asrlar davomida qad rostlagan (eng qadimiy me`moriy yodgorliklar XIV asrga to`g`ri keladi), istehkom, saroylar, masjid, madrasalar, maqbara, minoralar, karvonsaroy va hammomlar Ichan qal`ani o`ziga xos yodgorlik shahriga aylantirdi. Ko`hna Xiva 1968-yilda rasman qo`riqxona maqomini oldi. Kelib chiqishi Rivoyatda aytilishicha, Ichan-Qal`a qo`rg`oni qurilishida Muhammad payg`ambar Madinani qurishda uni olib ketgan joylardan loy ishlatilgan. Keyinchalik paydo bo`lgan ko`l muqaddas hisoblanadi. Boshqa bir afsonada aytilishicha, suvi ajoyib ta`mga ega bo`lgan Xeyvak qudug`i Injil Nuhning o`g`li Shem tomonidan qazilgan. Shuningdek, rivoyatlarga ko`ra, Xorazm qurilishi Shem tomonidan boshlangan. batafsil:https://uz.wikipedia.org/wiki/Ichan_qal%CA%BCa"
        photo_url = 'https://khivamuseum.uz/sites/default/files/2_69.jpg'
    
    try:
        await query.edit_message_media(media=InputMediaPhoto(media=photo_url))
        await query.edit_message_caption(caption=text)
    except Exception as e:
        logger.error(f"Rasmni yuborishda xatolik: {e}")
        await query.message.reply_photo(photo=photo_url, caption=text)

# Foydalanuvchilar ro'yxatini ko'rsatish uchun handler
    users = load_users()
    user_list = "\n".join([f"{user_id}: {info['first_name']} {info.get('last_name', '')} (@{info.get('username', 'no_username')})" for user_id, info in users.items()])
    await update.message.reply_text(f"Botga obuna bo'lgan foydalanuvchilar:\n{user_list}")

# Botni sozlash va ishga tushirish uchun asosiy funktsiyani aniqlang
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling(timeout=120, read_timeout=120)

if __name__ == '__main__':
    main()
