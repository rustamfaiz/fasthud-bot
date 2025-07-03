import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Бот запущен. Привет! Выбери опцию:")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
