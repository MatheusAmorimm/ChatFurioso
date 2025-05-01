from telegram import Update
from telegram.ext import CallbackContext
from handlers.start import menu_principal

async def newsletter_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="📰 Aqui estão as notícias da FURIA! (em breve...)")
    await query.message.reply_text("Escolha outra opção:", reply_markup=menu_principal())
    
