from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8983091532:AAGh55RWEBvOsBGczs1Rhiw6VryoTVrSGG8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Eu sou um bot.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
