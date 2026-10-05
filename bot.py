import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "ضع_التوكن_الخاص_بك_هنا"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_name = message.from_user.first_name
  markup = InlineKeyboardMarkup()
  markup.row_width = 2
  markup.add(
      InlineKeyboardButton("🛠 الخدمات المتوفرة", callback_data="services"),
      InlineKeyboardButton("📞 التواصل والدعم", callback_data="contact"),
  )
  welcome_text = (
      f"أهلاً بك يا {user_name} في بوت الخدمات الرقمية! 👋\nيرجى اختيار ما"
      " تحتاجه من القائمة أدناه:"
  )
  bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == "services":
    bot.answer_callback_query(call.id, "جاري عرض الخدمات...")
    bot.send_message(
        call.message.chat.id,
        "📌 **الخدمات المتاحة حالياً:**\n- شحن الألعاب التطبيقات 🎮\n- بطاقات"
        " الدفع الوهمية Visa 💳\n- توفير مضيفات ومضيفين 🎙️",
        parse_mode="Markdown",
    )
  elif call.data == "contact":
    bot.answer_callback_query(call.id, "جاري عرض بيانات التواصل...")
    bot.send_message(
        call.message.chat.id,
        "📞 للتواصل والاستفسار المباشر، يرجى مراسلتنا عبر الواتساب أو تيليغرام"
        " المعتمد.",
    )


@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(
      message,
      "عذراً، لم أفهم طلبك جيداً. يمكنك استخدام الأمر /start للعودة إلى"
      " القائمة الرئيسية.",
  )


print("البوت يعمل الآن بنجاح...")
bot.infinity_polling()
