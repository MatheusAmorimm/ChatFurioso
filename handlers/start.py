from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐾 Fala, Furioso(a)!\n\nEscolha uma opção:\n"
        "/agenda - Proximos jogos\n"
        "/noticias - Ultimas Noticias\n"
        "/quiz - Teste seus conhecimentos furiosos 🔥\n"
        "/curiosidades - Descubra algo novo"
    )