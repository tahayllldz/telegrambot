from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8953886144:AAES9pajsnEbYmzbyDvZucnzHTDvvzApZGM"

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🥤 1 Kola - 6000 TL", url="https://t.me/FERRRBBB")],
        [InlineKeyboardButton("🌿 2 Nane - 2000 TL", url="https://t.me/FERRRBBB")]
    ]

    await update.message.reply_text(
        "Merhaba 👋\n\nLütfen aşağıdaki ürünlerden birini seçiniz.\n\n🕒 Çalışma Saatleri: 16:00 - 04:00",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", menu))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

print("Bot çalışıyor...")
app.run_polling()
