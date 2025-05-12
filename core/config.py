import os
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv(dotenv_path='../.env')

# Obter o token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TASKS_CHANNEL_ID = os.getenv("TASKS_CHANNEL_ID")

if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN not found in .env file")