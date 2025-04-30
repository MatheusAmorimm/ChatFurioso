from telegram import Update
from telegram.ext import ContextTypes

async def calendary_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📅 Próximos jogos da FURIA:\n"
        "- 02/05 vs Team Liquid\n"
        "- 05/05 vs G2 Esports\n"
        "#GOFURIA 🔥"
    )