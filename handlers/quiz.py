from telegram import Update
from telegram.ext import CallbackContext
from handlers.menu import menu_principal

async def quiz_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="Aqui teremos um quiz de CS e Furia")
    await query.message.reply_text("Escolha outra opção:", reply_markup=menu_principal())