import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers import start_command
from handlers import calendary_command
from handlers import newsletter_command
from handlers import trivia_command

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("agenda", calendary_command))
app.add_handler(CommandHandler("noticias", newsletter_command))
app.add_handler(CommandHandler("curiosidades", trivia_command))

print("Easy peasy lemon squeezy! #GOFURIA🔥")

app.run_polling()