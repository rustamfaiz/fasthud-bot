import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📕 Получить книгу", callback_data="get_book")],
            [InlineKeyboardButton(text="🎯 Что ты получишь из этой книги", callback_data="about_book")]
        ]
    )

    text = (
        "Поздравляю.\n"
        "Новая попытка. Новый заход. Очередной старт против жира, который всё ещё с тобой.\n\n"
        "Давай честно — у тебя уже были диеты, был бег, была надежда увидеть плоский живот — хотя бы один раз, без возврата.\n"
        "Но вместо результата — снова цифры туда-сюда. И снова ничего.\n\n"
        "Привет. Меня зовут Рустам.\n"
        "В 2019 году я сжёг двадцать килограммов — через голод, бег, полное отречение от сладкого, мучного и жизни.\n"
        "Настолько ушёл в процесс, что разобрал физиологию, нутрициологию и тренировочную механику до костей.\n"
        "Потом специально набирал жир — и сжигал его снова. Несколько раз. Системно. Без голода, бега и со вкусом жизни. За 4 месяца.\n\n"
        "Так и появилась эта книга.\n"
        "Не из вдохновения. А из проверенной практики в борьбе с фитнес-мифами и бесполезными ритуалами.\n\n"
        "Это не про мотивацию. Это про метод.\n"
        "Как за 4 месяца убрать жир — и не вернуть его больше никогда.\n\n"
        "⬇️ Жми кнопку ниже — и получи инструкцию."
    )

    await message.answer(text, reply_markup=keyboard)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
