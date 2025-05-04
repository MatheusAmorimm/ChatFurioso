from telegram import Update
from telegram.ext import CallbackContext
from handlers.menu import menu_principal

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "*Fala, Furioso (a)!*🐾🔥\n\n"
        "Seja muito bem-vindo(a) ao *CHAT FURIOSO CSFANS*! 🔥\n\n"
        "Digite uma das opções abaixo para mergulhar no mundo da FURIA!🎯\n",
        reply_markup=menu_principal(),
        parse_mode="Markdown"
    )