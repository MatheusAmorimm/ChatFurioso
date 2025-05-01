from telegram import Update
from telegram.ext import CallbackContext
from handlers.menu import menu_principal

async def trivia_callback(update: Update, context: CallbackContext):
   query = update.callback_query
   await query.answer()
   await query.edit_message_text(text="🤯 Curiosidade Furiosa:\n"
        "Você sabia que a FURIA foi o primeiro time brasileiro a ter uma Gaming House nos EUA? 🇺🇸🐗\n"
        "Isso ajudou muito a evolução dos nossos jogadores no cenário internacional!")
   await query.message.reply_text("Escolha outra opção:", reply_markup=menu_principal())