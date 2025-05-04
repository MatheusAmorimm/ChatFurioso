import json

async def newsletter_command(update, context):
    try:
        with open('data/news.json', 'r', encoding='utf-8') as file:
            news = json.load(file)

        if not news:
            await update.message.reply_text("😥 Nenhuma notícia recente sobre a FURIA.")
            return

        message = "📰 Últimas notícias da FURIA:\n\n"
        for item in news:
            message += f"🔹 [{item['title']}]({item['link']})\n\n"

        await update.message.reply_text(message, parse_mode='Markdown')

    except Exception as e:
        await update.message.reply_text(f"❌ Erro ao buscar notícias: {str(e)}")