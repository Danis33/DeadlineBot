from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def register_handler(bot):
    @bot.message_handler(commands=['start'])
    async def send_welcome(message):
        markup = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("Cоздание задачи", callback_data="add_task")
        button2 = InlineKeyboardButton("Посмотреть задачи", callback_data="view")
        button3 = InlineKeyboardButton("Напоминание", callback_data="reminder")
        button4 = InlineKeyboardButton("Редактировать", callback_data="edit")
        button5 = InlineKeyboardButton("Удалить", callback_data="delete")
        markup.add(button1, button2, button3, button4, button5)

        await bot.send_message(message.chat.id,
                               "Добро пожаловать! Нажмите одну из кнопок:",
                               reply_markup=markup
                               )
