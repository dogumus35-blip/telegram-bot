import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def mesaj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat:
        print("CHAT ID:", update.effective_chat.id, "Message:", update.message.text)
        print("CHAT TYPE:", update.effective_chat.type)
        print("CHAT TITLE:", update.effective_chat.title)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(
        MessageHandler(filters.ALL, mesaj)
    )
    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
