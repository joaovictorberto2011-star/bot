from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8983091532:AAGh55RWEBvOsBGczs1Rhiw6VryoTVrSGG8")  # Token salvo no Railway

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://picsum.photos/800/600",
        caption="""
👋 Olá!

Seja bem-vindo ao meu bot.

✅ Aqui você receberá informações e atualizações.
🚀 Aproveite!
"""
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot iniciado!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
