import json

async def calendary_command(update, context):
    try:
        with open('data/matches.json', 'r', encoding='utf-8') as file:
            matches = json.load(file)

        if not matches:
            await update.message.reply_text("😥 Nenhuma partida encontrada para a FURIA.")
            return

        message = "🐾 Próximos jogos da FURIA:\n\n"
        for match in matches:
            message += (
                f"🏆 {match['event']}\n"
                f"⚔️ {match['team1']} vs {match['team2']}\n"
                f"🕓 Horário: {match['date']} às {match['time']} (Brasília)\n\n"
            )

        await update.message.reply_text(message)

    except Exception as e:
        await update.message.reply_text(f"❌ Erro ao buscar partidas: {str(e)}")

    