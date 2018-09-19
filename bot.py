import config
from telebot import TeleBot, types

bot = config.bot
bot.remove_webhook()

@bot.message_handler(commands = ["start"])
def start_menu(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup.row(types.KeyboardButton("О нас"), types.KeyboardButton("Услуги"))
	markup.row(types.KeyboardButton("Кейсы"), types.KeyboardButton("Контакты"))

	bot.send_message(chat_id = message.chat.id, 
					 text = "Привет! :)",
					 reply_markup = markup)


@bot.message_handler(content_types = ["text"])
def repeat_all_messages(message):
	answer = message.text
	if answer == "О нас":
		msg = config.links["about_us"]
	elif answer == "Услуги":
		msg = config.links["services"]
	elif answer == "Кейсы":
		msg = config.links["cases"]
	elif answer == "Контакты":
		msg = config.links["contacts"]
	else:
		msg = "Я не знаю такой команды )="

	bot.send_message(chat_id = message.chat.id,
						 text = msg)

while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		logger.error(e)
		time.sleep(15)