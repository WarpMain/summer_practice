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
    button3 = types.KeyboardButton('/zoom_instruction')
    button4 = types.KeyboardButton('/bot_instruction')
    button5 = types.KeyboardButton('/install_office')
    button6 = types.KeyboardButton('/install_vpn')
    button7 = types.KeyboardButton('/contact')
    reply_markup.add(button1, button2, button3, button4, button5, button6, button7)

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
    button1 = types.KeyboardButton('/menu')
    button2 = types.KeyboardButton('/help')
    button3 = types.KeyboardButton('/zoom_instruction')
    button4 = types.KeyboardButton('/bot_instruction')
    button5 = types.KeyboardButton('/install_office')
    button6 = types.KeyboardButton('/install_vpn')
    button7 = types.KeyboardButton('/contact')
    reply_markup.add(button1, button2, button3, button4, button5, button6, button7)

    bot.send_message(message.chat.id, "Вот список команд:", reply_markup=reply_markup)
    bot.send_message(message.chat.id, (
        "/start - получить приветственное сообщение;\n"
        "/help - получить список команд;\n"
        "/zoom_instruction - получить инструкцию по пользованию Zoom;\n"
        "/bot_instruction - получить инструкцию по созданию Telegram ботов;\n"
        "/install_office - получить инструкцию по установке MS Office;\n"
        "/install_vpn - получить инструкцию по установке VPN;\n"
        "/contact - получить контактную информацию."
    ))


# Обработчик команды /zoom_instruction
@bot.message_handler(commands=['zoom_instruction'])
def send_zoom_instruction(message):
    instruction = (
        "Инструкция по пользованию Zoom:\n"
        "1. Скачайте и установите приложение Zoom.\n"
        "2. Зарегистрируйтесь или войдите в свой аккаунт.\n"
        "3. Для участия в конференции введите ID встречи и пароль.\n"
        "4. Используйте кнопки управления для включения/выключения камеры и микрофона.\n"
        "5. Для завершения встречи нажмите 'Выйти'."
    )
    bot.send_message(message.chat.id, instruction)


# Обработчик команды /bot_instruction
@bot.message_handler(commands=['bot_instruction'])
def send_bot_instruction(message):
    instruction = (
        "Инструкция по созданию Telegram бота:\n"
        "1. Откройте Telegram и найдите @BotFather.\n"
        "2. Отправьте команду /newbot и следуйте инструкциям для создания бота.\n"
        "3. Получите токен вашего бота и сохраните его.\n"
        "4. Используйте этот токен в вашем коде для взаимодействия с ботом.\n"
        "5. Разработайте функции вашего бота и запустите его."
    )
    bot.send_message(message.chat.id, instruction)


# Обработчик команды /install_office
@bot.message_handler(commands=['install_office'])
def send_install_office(message):
    instruction = (
        "Инструкция по установке MS Office:\n"
        "1. Перейдите на официальный сайт Microsoft Office.\n"
        "2. Войдите в свою учетную запись Microsoft или создайте новую.\n"
        "3. Купите подписку на Office 365 или используйте пробную версию.\n"
        "4. Скачайте установочный файл и запустите его.\n"
        "5. Следуйте инструкциям мастера установки для завершения процесса."
    )
    bot.send_message(message.chat.id, instruction)


# Обработчик команды /install_vpn
@bot.message_handler(commands=['install_vpn'])
def send_install_vpn(message):
    instruction = (
        "Инструкция по установке VPN:\n"
        "1. Выберите надежный VPN-сервис (например, NordVPN, ExpressVPN).\n"
        "2. Перейдите на сайт выбранного VPN-сервиса.\n"
        "3. Зарегистрируйтесь и приобретите подписку.\n"
        "4. Скачайте и установите приложение VPN на ваше устройство.\n"
        "5. Войдите в приложение с помощью учетной записи и подключитесь к серверу VPN."
    )
    bot.send_message(message.chat.id, instruction)


# Обработчик команды /contact
@bot.message_handler(commands=['contact'])
def send_contact(message):
    contact_info = (
        "Контактная информация:\n"
        "634040, Россия, г. Томск,\n"
        "ул. Высоцкого, 33\n"
        "\n"
        "Email: npp@mail.npptec.ru\n"
        "Телефоны:\n"
        "8 (3822) 63-38-37\n"
        "8 (3822) 63-39-54"
    )
    bot.send_message(message.chat.id, contact_info)


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text + ' - не является командой, пожалуйста используйте существующие команды, узнать их можно с помощью /help')


# Запуск бота
bot.polling()
