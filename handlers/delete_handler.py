from utils.database import get_tasks, delete_task

USER_STATES = {}


def delete_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "delete")
    async def delete_register(call):
        user_id = call.message.chat.id
        tasks = get_tasks(user_id)
        if tasks:
            tasks_text = "\n".join([f"{idx + 1}. {task[1]}" for idx, task in enumerate(tasks)])
            await bot.send_message(
                call.message.chat.id, f"Введите номер задачи, которую хотите удалить:\n{tasks_text}\n"
            )

            USER_STATES[user_id] = {
                "action": "delete_task",
                "tasks": tasks
            }
        else:
            await bot.send_message(call.message.chat.id, "У вас нет задач для удаления.")

    @bot.message_handler(func=lambda message: message.from_user.id in USER_STATES and USER_STATES[message.from_user.id][
            "action"] == "delete_task")
    async def process_task_deletion(message):
        user_id = message.from_user.id
        try:
            task_number = int(message.text)
            tasks = USER_STATES[user_id]["tasks"]

            if 1 <= task_number <= len(tasks):
                task_id = tasks[task_number - 1][0]
                delete_task(user_id, task_id)
                await bot.send_message(message.chat.id, f"Задача №{task_number} успешно удалена!")
                USER_STATES.pop(user_id, None)
            else:
                await bot.send_message(message.chat.id, "Некорректный номер. Введите номер задачи из списка.")
        except ValueError:
            await bot.send_message(message.chat.id, "Пожалуйста, введите корректный номер задачи.")
