from telegram import InlineKeyboardButton, InlineKeyboardMarkup
 
def menu_principal():
    keyboard= [
            [InlineKeyboardButton("📅 Próximos Jogos", callback_data='agenda')],
            [InlineKeyboardButton("📰 Notícias", callback_data='noticias')],
            [InlineKeyboardButton("🎯 Curiosidades Furiosas", callback_data='curiosidades')],
            [InlineKeyboardButton("🎮 Quiz Furioso", callback_data='quiz')],
        ]
    return InlineKeyboardMarkup(keyboard)