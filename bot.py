import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from handlers.start import start
from handlers.calendary import calendary_callback
from handlers.newsletter import newsletter_callback
from handlers.trivia import trivia_callback
from handlers.quiz import quiz_callback

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(calendary_callback, pattern="^agenda$"))
app.add_handler(CallbackQueryHandler(newsletter_callback, pattern="^noticias$"))
app.add_handler(CallbackQueryHandler(trivia_callback, pattern="^curiosidades$"))
app.add_handler(CallbackQueryHandler(quiz_callback, pattern='^quiz$'))

print("Easy peasy lemon squeezy! #GOFURIA🔥")

app.run_polling()