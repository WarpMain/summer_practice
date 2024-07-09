import telebot
from telebot import types
from my_token import API_TOKEN  # Подставьте свой API токен сюда

bot = telebot.TeleBot(API_TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправка приветственного сообщения с Inline Keyboard
    keyboard_inline = types.InlineKeyboardMarkup()
    button1_inline = types.InlineKeyboardButton('Кнопка 1', callback_data='button1')
    button2_inline = types.InlineKeyboardButton('Кнопка 2', callback_data='button2')
    keyboard_inline.add(button1_inline, button2_inline)

    bot.send_message(message.chat.id, "Привет! Выберите одну из кнопок (Inline Keyboard):",
                     reply_markup=keyboard_inline)

    # Создание Reply Keyboard
    keyboard_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1_reply = types.KeyboardButton('Кнопка 1')
    button2_reply = types.KeyboardButton('Кнопка 2')
    keyboard_reply.add(button1_reply, button2_reply)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Обработчик callback-запросов от Inline Keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, 'Вы нажали на кнопку 1')
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'Вы нажали на кнопку 2')


# Запуск бота
bot.polling()
