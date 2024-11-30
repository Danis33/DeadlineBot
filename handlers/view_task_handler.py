from utils.database import get_tasks


def views_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == "view")
    async def list_tasks(call):
        user_id = call.message.chat.id
        tasks = get_tasks(user_id)
        if tasks:
            task_list = "\n".join(f"{task[0]}. {task[1]}" for task in tasks)
            await bot.send_message(call.message.chat.id, f"Текущие задачи:\n{task_list}")
        else:
            await bot.send_message(call.message.chat.id, "Список задач пуст.")
