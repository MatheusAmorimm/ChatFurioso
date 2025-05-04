from telegram import Update
from telegram.ext import ContextTypes
from handlers.furia_curiosities import get_curiosities

async def trivia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
     curiosity = get_curiosities()
     await update.message.reply_text(f"✨ Curiosidade FURIOSA:\n\n{curiosity}")
   