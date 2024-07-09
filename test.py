import telebot
from telebot import types
from my_token import API_TOKEN  # Подставьте свой API токен сюда

bot = telebot.TeleBot(API_TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание Inline Keyboard
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='button1')
    button2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='button2')
    keyboard.add(button1, button2)

    # Отправка сообщения с Inline Keyboard
    bot.reply_to(message, "Привет! Выберите одну из кнопок:", reply_markup=keyboard)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


# Обработчик callback-запросов от кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, 'Вы нажали на кнопку 1')
    elif call.data == 'button2':
        bot.send_message(call.message.chat.id, 'Вы нажали на кнопку 2')


# Запуск бота
bot.polling()
