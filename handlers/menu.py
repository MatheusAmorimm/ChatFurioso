from telegram import InlineKeyboardButton, InlineKeyboardMarkup
 
def menu_principal():
    keyboard= [
            [InlineKeyboardButton("📅 Próximos Jogos --> /agenda", callback_data='agenda')],
            [InlineKeyboardButton("📰 Notícias --> /noticias", callback_data='noticias')],
            [InlineKeyboardButton("🎯 Curiosidades Furiosas --> /curiosidades", callback_data='curiosidades')],
        ]
    return InlineKeyboardMarkup(keyboard)