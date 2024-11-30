import asyncio
import aiohttp

from telebot.async_telebot import AsyncTeleBot
from config import BOT_TOKEN
from handlers import (start_handler,
                      add_handler,
                      view_task_handler,
                      delete_handler,
                      )

bot = AsyncTeleBot(BOT_TOKEN)

start_handler.register_handler(bot)
add_handler.register_handlers(bot)
view_task_handler.views_handlers(bot)
delete_handler.delete_handlers(bot)


async def main():
    print("Бот запущен!")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())
