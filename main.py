from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

# Твой токен от BotFather
BOT_TOKEN = "7289091311:AAGBbPawqeHo2XyydeROar_UD_6C8RsU_js"

# Логирование
logging.basicConfig(level=logging.INFO)

# Хранилище расходов
user_data = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это бот учёта расходов.\n"
        "Добавь расход командой:\n"
        "/add 120\n"
        "Посмотреть сумму:\n"
        "/total"
    )

# Команда /add <сумма>
async def add_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        amount = float(context.args[0])
        user_data[user_id] = user_data.get(user_id, 0) + amount
        await update.message.reply_text(f"Добавил: {amount} zł\nВсего: {user_data[user_id]} zł")
    except:
        await update.message.reply_text("Используй так: /add 25.5")

# Команда /total
async def total(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    total = user_data.get(user_id, 0)
    await update.message.reply_text(f"Всего потрачено: {total} zł")

# Запуск
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add_expense))
app.add_handler(CommandHandler("total", total))
app.run_polling()
