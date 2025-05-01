import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from handlers import start_command
from handlers import calendary_command
from handlers import newsletter_command
from handlers import trivia_command
from handlers.start import agenda_callback
from handlers.start import noticias_callback

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("agenda", calendary_command))
app.add_handler(CommandHandler("noticias", newsletter_command))
app.add_handler(CommandHandler("curiosidades", trivia_command))
app.add_handler(CallbackQueryHandler(agenda_callback, pattern="^agenda$"))
app.add_handler(CallbackQueryHandler(noticias_callback, pattern="^noticias$"))

print("Easy peasy lemon squeezy! #GOFURIA🔥")

app.run_polling()