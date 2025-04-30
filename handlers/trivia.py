from telegram import Update
from telegram.ext import ContextTypes

async def trivia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤯 Curiosidade Furiosa:\n"
        "Você sabia que a FURIA foi o primeiro time brasileiro a ter uma Gaming House nos EUA? 🇺🇸🐗\n"
        "Isso ajudou muito a evolução dos nossos jogadores no cenário internacional!"
    )