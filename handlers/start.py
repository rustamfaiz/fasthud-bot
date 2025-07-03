from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

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

@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💸 Получить книгу", callback_data="get_book")],
            [InlineKeyboardButton(text="🎯 Что ты получишь из этой книги", callback_data="book_info")],
        ]
    )
    await message.answer(text_welcome, reply_markup=keyboard)
