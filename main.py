import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

class PurchaseStates(StatesGroup):
    choosing_region = State()
    entering_promocode = State()
    confirming_promocode = State()
    waiting_for_payment = State()
    collecting_user_data = State()
    generating_pdf = State()

def start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💸 Получить книгу", callback_data="get_book")],
        [InlineKeyboardButton(text="🎯 Что ты получишь из этой книги", callback_data="book_details")]
    ])

def region_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Россия", callback_data="region_ru")],
        [InlineKeyboardButton(text="🌍 Другие страны", callback_data="region_world")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="back_to_start")]
    ])

@dp.message(F.text, commands=["start"])
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Поздравляю. Новый заход. Очередной старт против жира...

⬇️ Жми «Получить книгу».",
        reply_markup=start_keyboard()
    )

@dp.callback_query(F.data == "get_book")
async def on_get_book(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PurchaseStates.choosing_region)
    await callback.message.edit_text(
        "Укажи регион — для определения способа оплаты.",
        reply_markup=region_keyboard()
    )

@dp.callback_query(F.data == "book_details")
async def on_book_details(callback: CallbackQuery):
    await callback.message.edit_text(
        "📘 Что ты получишь из этой книги:

"
        "— Всю правду о диетах
"
        "— Пошаговый план
"
        "— Питание без голода
"
        "— Объяснение, как работает жир
"
        "— Тренировки на 4 месяца
"
        "— Как удержать результат
"
        "— Новое тело

⬇️ Готов? Жми «Получить книгу».",
        reply_markup=start_keyboard()
    )

@dp.callback_query(F.data == "back_to_start")
async def on_back_to_start(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("⬅ Возвращаемся в начало.", reply_markup=start_keyboard())

@dp.callback_query(F.data.startswith("region_"))
async def on_region_chosen(callback: CallbackQuery, state: FSMContext):
    region = callback.data.split("_")[1]
    await state.update_data(region=region)
    await callback.message.edit_text(f"✅ Регион выбран: {region.upper()}.
🔜 Дальше — промокод.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())