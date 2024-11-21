import sqlite3


def register_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "add_task")
    async def handle_button1(call):
        await bot.send_message(call.message.chat.id, "Введите описание задачи:")

        @bot.message_handler(func=lambda message: True)
        async def save_task(message):
            user_id = message.from_user.id
            task_text = message.text

            conn = sqlite3.connect("database/bot.db")
            cursor = conn.cursor()

            cursor.execute('''
            INSERT INTO task (user_id, task_text) VALUES(?, ?)
            ''', (user_id, task_text))

            conn.commit()
            conn.close()

            await bot.send_message(message.chat.id, f"Задача '{task_text}' добавлена.")
