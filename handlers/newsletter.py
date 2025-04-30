from telegram import Update
from telegram.ext import ContextTypes

async def newsletter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Últimas notícias da FURIA:\n"
        "- Vitória furiosa sobre NAVI!\n"
        "- CS2: FURIA classificada para o Major!\n"
        "- Novas skins inspiradas na FURIA lançadas no CS:GO 🔥"
    )
