from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard= [
        [InlineKeyboardButton("📅 Agenda", callback_data='agenda')],
        [InlineKeyboardButton("📰 Notícias", callback_data='noticias')],
        [InlineKeyboardButton("🎲 Curiosidades", callback_data='curiosidades')],
        [InlineKeyboardButton("🧠 Quiz", callback_data='quiz')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "*Fala, Furioso (a)!*🐾🔥\n\n"
        "Escolha uma das opções abaixo clicando nos botões:\n"
        "- (Ou envie o comando se preferir)\n",
        reply_markup=reply_markup
    )

async def agenda_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("📅 Aqui está a agenda da FURIA! (em breve...)")

async def noticias_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("📰 Aqui estão as notícias da FURIA! (em breve...)")