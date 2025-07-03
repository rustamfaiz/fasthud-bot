import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

# Загрузка переменных из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# FSM Состояния
class PurchaseStates(StatesGroup):
    choosing_region = State()
    entering_promocode = State()
    confirming_promocode = State()
    waiting_for_payment = State()
    collecting_user_data = State()
    generating_pdf = State()

# Инициализация
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Приветственное сообщение
WELCOME_TEXT = (
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
    "⬇️ Выбери, с чего начать:"
)

# Кнопки
def start_keyboard():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💸 Получить книгу", callback_data="get_book")],
            [InlineKeyboardButton(text="🎯 Что ты получишь из этой книги", callback_data="about_book")]
        ]
    )
    return kb

# Хэндлер /start
@dp.message(F.text == "/start")
async def cmd_start(message: Message, state: FSMContext):
    print("[LOG] Пользователь запустил /start")
    await message.answer(WELCOME_TEXT, reply_markup=start_keyboard())

# Заглушки для кнопок (временно)
@dp.callback_query(F.data == "get_book")
async def handle_get_book(callback: CallbackQuery, state: FSMContext):
    print("[LOG] Нажата кнопка 'Получить книгу'")
    await callback.answer("Этап покупки будет добавлен позже.")

@dp.callback_query(F.data == "about_book")
async def handle_about_book(callback: CallbackQuery, state: FSMContext):
    print("[LOG] Нажата кнопка 'Что ты получишь'")
    await callback.answer("Описание книги будет добавлено позже.")

# Запуск
async def main():
    print("[LOG] Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
