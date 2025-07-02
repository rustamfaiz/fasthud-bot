=== FastHood Telegram Bot ===

📦 Как запустить:

1. Зарегистрируйся на https://railway.app
2. Создай новый проект → PostgreSQL
3. Скопируй ссылку DATABASE_URL
4. Создай .env файл по образцу из .env.example
5. Добавь переменные:
   - BOT_TOKEN=твой токен от @BotFather
   - DATABASE_URL=твоя ссылка на PostgreSQL
6. Заливай файлы в Railway
7. Railway сам установит зависимости и запустит бота

🔃 Создание таблиц:
1 раз выполни: `python create_tables.py`