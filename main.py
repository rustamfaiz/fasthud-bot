import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# --- КНОПКИ ---
start_keyboard = InlineKeyboardMarkup(row_width=1)
start_keyboard.add(
    InlineKeyboardButton("💸 Получить книгу", callback_data="get_book"),
    InlineKeyboardButton("🎯 Что ты получишь из этой книги", callback_data="about_book")
)

back_keyboard = InlineKeyboardMarkup()
back_keyboard.add(
    InlineKeyboardButton("⬅ Вернуться", callback_data="back_to_start")
)

# --- ТЕКСТЫ ---
start_text = (
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
    "Как за 4 месяца убрать жир — и не вернуть его больше никогда."
)

about_text = (
    "Это не книга про “жить без сахара” и “верить в себя”.\n"
    "Это — пошаговый инструмент для тех, кто устал начинать сначала.\n\n"
    "Вот, что ты получишь:\n"
    "— Всю правду о диетах и почему они всегда заканчиваются провалом\n"
    "— Пошаговый план, как сбрасывать жир, даже если ешь перед сном\n"
    "— Систему питания без голода, с нормальной, человеческой едой\n"
    "— Объяснение, как реально работает жир и почему «ПП» не работает\n"
    "— Программу тренировок на 4 месяца, где жир горит, пока ты спишь\n"
    "— Формулу, как удержать результат и не возвращаться к прежнему телу\n"
    "— Новое тело, о котором ты даже не мечтал\n\n"
    "Всё, что мешало — разобрано. Всё, что нужно — собрано. Осталось только применить."
)

# --- ХЕНДЛЕРЫ ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(start_text, reply_markup=start_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'about_book')
async def process_about(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, about_text, reply_markup=back_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'back_to_start')
async def process_back(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, start_text, reply_markup=start_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'get_book')
async def process_get_book(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "🔻 Начинаем. Укажи регион для оплаты.")
    # Тут пойдёт следующий шаг — выбор региона

# --- ЗАПУСК ---
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
