from aiogram import Router
from aiogram.types import Message, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode


router = Router()

@router.message(Text("📕 Что ты получишь из этой книги"))
async def what_you_get(message: Message):
    text = (
        "<b>📘 Что ты получишь из этой книги</b>\n\n"
        "<b>Это не книга. Это прямой удар по всем фитнес-мифам, на которых ты сливал годы.</b>\n"
        "Без мотивационных соплей, без “всё получится”, без брокколи на пару.\n\n"
        "Здесь — метод.\n"
        "<b>4 месяца.</b>\n"
        "Без голода. Без бега. Без возврата жира.\n\n"
        "Вот что ты получаешь:\n\n"
        "▪️ <b>Пошаговый план жиросжигания</b>, собранный по физиологии, а не по мнению тренеров\n"
        "▪️ <b>Программа питания</b>, где есть мясо, хлеб, нормальные продукты — и при этом жир уходит\n"
        "▪️ <b>Полная система тренировок</b> — три фазы, весь зал, расписано по неделям\n"
        "▪️ <b>Разбор, почему диеты всегда проваливаются</b> — и как не повторить ту же яму\n"
        "▪️ <b>Честный ответ, почему “ПП” не работает</b>, и что работает вместо\n"
        "▪️ <b>Формулу удержания формы</b> — чтобы не набрать обратно, даже если жизнь снова начнёт валиться\n"
        "▪️ <b>Понимание тела</b> — как оно реально тратит жир, что делает инсулин, и как управлять аппетитом\n"
        "▪️ <b>Новое тело. Реально. За 4 месяца.</b> Без воды. Без отката. Без иллюзий.\n\n"
        "🎬 <b>Выбор, как в «Матрице»:</b>"
    )

    # Отправка текста
    await message.answer(text, parse_mode=ParseMode.HTML)

    # Отправка картинки
    photo = FSInputFile("images/matrix_choice.png")
    await message.answer_photo(photo)

    # Кнопки
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔴 Купить книгу", callback_data="buy_book")],
            [InlineKeyboardButton(text="🔵 Остаться в иллюзии", callback_data="stay_illusion")],
        ]
    )

    await message.answer("⬇️ Выбери:", reply_markup=keyboard)
