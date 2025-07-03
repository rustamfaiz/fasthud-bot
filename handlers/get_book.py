from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Text

router = Router()

# Клавиатура выбора страны
country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Россия")],
        [KeyboardButton(text="Другие страны")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Обработка кнопки "💸 Получить книгу"
@router.callback_query(F.data == "get_book")
async def handle_get_book(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📍 Укажи регион — для определения способа оплаты:",
        reply_markup=country_keyboard
    )

# Обработка выбора региона
@router.message(F.text.in_(["Россия", "Другие страны"]))
async def handle_country(message: Message):
    if message.text == "Россия":
        await message.answer("💳 Цена книги — 3000 ₽\nПромокод принят: 2000 ₽", reply_markup=None)
    else:
        await message.answer("💳 Цена для других стран — $29", reply_markup=None)
