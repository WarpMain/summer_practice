import telebot
from telebot import types
from my_token import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    inline_markup = types.InlineKeyboardMarkup(row_width=2)
    inline_button1 = types.InlineKeyboardButton('Начать', callback_data='inline_button1')
    inline_markup.add(inline_button1)

    bot.send_message(message.chat.id,
                     "Здравствуйте! Вы обратились к боту НПП ТЭК.", reply_markup=inline_markup)


# Обработчик команды /menu
@bot.message_handler(commands=['menu'])
def send_menu(message):
    # Создание ReplyKeyboardMarkup
    reply_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton('/start')
    button2 = types.KeyboardButton('/help')
    reply_markup.add(button1, button2)

    bot.send_message(message.chat.id, "Что вас интересует? Выберите опцию из меню.", reply_markup=reply_markup)


# Обработчик нажатий на inline кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'inline_button1':
        bot.answer_callback_query(call.id, "Хорошего пользования ботом!")
        # Создание сообщения, имитирующего команду /menu
        menu_message = types.Message(
            message_id=call.message.message_id,
            from_user=call.from_user,
            chat=call.message.chat,
            date=call.message.date,
            content_type='text',
            options={},
            json_string=None
        )
        menu_message.text = "/menu"
        send_menu(menu_message)


# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    # Создание ReplyKeyboardMarkup
    reply_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button1 = types.KeyboardButton('/start')
    button2 = types.KeyboardButton('/help')
    reply_markup.add(button1, button2)

    bot.send_message(message.chat.id, "Вот список команд:", reply_markup=reply_markup)
    bot.send_message(message.chat.id, "/start - получить приветственное сообщение; \n/help - получить список команд;")


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text + ' - не является командой, пожалуйста используйте существующие команды, узнать их можно с помощью /help')


# Запуск бота
bot.polling()
