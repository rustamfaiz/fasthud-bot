import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    Message,
    CallbackQuery,
)
from aiogram.filters import CommandStart
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Приветственное сообщение
text_welcome = (
    "🎯 <b>Поздравляю.</b>\n"
    "Новая попытка. Новый заход. Очередной старт против жира, который всё ещё с тобой.\n\n"
    "— — — — — — — — — — —\n\n"
    "Давай честно — у тебя уже были диеты, был бег, была надежда увидеть плоский живот — хотя бы один раз, без возврата.\n"
    "Но вместо результата — снова цифры туда-сюда. И снова ничего.\n\n"
    "— — — — — — — — — — —\n\n"
    "👋 <b>Привет. Меня зовут Рустам.</b>\n"
    "В 2019 году я сжёг двадцать килограммов — через голод, бег, полное отречение от сладкого, мучного и жизни.\n\n"
    "Настолько ушёл в процесс, что разобрал физиологию, нутрициологию и тренировочную механику до костей.\n"
    "Потом специально набирал жир — и сжигал его снова. Несколько раз.\n"
    "Системно. Без голода, без бега и со вкусом жизни. За 4 месяца.\n\n"
    "Так и появилась эта книга.\n"
    "Не из вдохновения. А из проверенной практики в борьбе с фитнес-мифами и бесполезными ритуалами.\n\n"
    "🚫 Это не про мотивацию. Это про метод.\n"
    "🔥 Как за 4 месяца убрать жир — и не вернуть его больше никогда.\n\n"
    "⬇️ Жми кнопку — и получи инструкцию."
)

# Кнопки под приветствием
welcome_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💸 Получить книгу", callback_data="get_book")],
    [InlineKeyboardButton(text="🎯 Что ты получишь из этой книги", callback_data="book_info")]
])

# Кнопки выбора страны
country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Россия")],
        [KeyboardButton(text="США / Другая страна")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Обработка команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text_welcome, reply_markup=welcome_keyboard)

# Обработка нажатия на "Получить книгу"
@dp.callback_query(F.data == "get_book")
async def handle_get_book(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("📕 Сейчас начнём. Выбери страну проживания:", reply_markup=country_keyboard)

# Обработка выбора страны
@dp.message(F.text.in_(["Россия", "США / Другая страна"]))
async def handle_country(message: Message):
    if message.text == "Россия":
        await message.answer("💳 Цена для России: 990₽. (Здесь будет кнопка оплаты)", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("💳 Цена для других стран: $19. (Здесь будет кнопка оплаты)", reply_markup=types.ReplyKeyboardRemove())

# Обработка нажатия на "Что ты получишь из книги"
@dp.callback_query(F.data == "book_info")
async def handle_book_info(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📚 <b>Что внутри книги:</b>\n"
        "— Как сжигать жир без голода\n"
        "— Почему бег не работает\n"
        "— Система питания, тренировок и контроля\n"
        "— Мифы, маркетинг и реальность\n\n"
        "Полный план на 4 месяца. Без мотивационного мусора. Только работающая схема."
    )

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
