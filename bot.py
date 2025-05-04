import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.start import start
from handlers.calendary import calendary_command
from handlers.newsletter import newsletter_command
from handlers.trivia import trivia_command

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("agenda",calendary_command))
app.add_handler(CommandHandler("noticias",newsletter_command))
app.add_handler(CommandHandler("curiosidades", trivia_command))

print("Easy peasy lemon squeezy! #GOFURIA🔥")

app.run_polling()