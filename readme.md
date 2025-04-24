# 🐾 CHAT FURIOSO CSFANS

Um bot de Telegram criado para os fãs do time de CS da FURIA, desenvolvido como parte do desafio de estágio em Engenharia de Software da organização. O bot oferece uma experiência conversacional interativa com foco na comunidade, trazendo conteúdos relevantes e dinâmicos para a torcida.

---

## 🚀 Funcionalidades

- `/start` — Mensagem de boas-vindas com menu de comandos
- `/agenda` — Próximos jogos do time
- `/noticias` — Últimas notícias sobre a FURIA
- `/quiz` — Teste seu conhecimento sobre o time
- `/curiosidade` — Curiosidades aleatórias da FURIA e do cenário CS
- ⚙️ Mais interações em desenvolvimento!

---

## 📸 Demonstração

> [Vídeo de demonstração em breve]  
> *Vídeo de até 3 minutos mostrando as funcionalidades do bot.*

---

## 🧪 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

## 🛠️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/chat-furioso-csfans.git
cd chat-furioso-csfans

# Crie o arquivo .env com seu token do bot
echo "BOT_TOKEN=seu_token_aqui" > .env

# Instale as dependências
pip install -r requirements.txt

# Execute o bot
python bot.py
