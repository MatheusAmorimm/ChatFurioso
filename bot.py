import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start_command

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

print("Easy peasy lemon squeezy! #GOFURIA🔥")

app.run_polling()