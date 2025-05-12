import discord
from discord.ext import commands
from core.config import DISCORD_TOKEN, TASKS_CHANNEL_ID

class PorypyClient(commands.Bot):
    def __init__(self):
        # Define os intents e prefixo do bot
        intents = discord.Intents.default()
        intents.members = True        
        intents.message_content = True  # Permitir que o bot leia o conteúdo das mensagens
        super().__init__(command_prefix="!", intents=intents)
        self.token = DISCORD_TOKEN
        self.tasks_channel = TASKS_CHANNEL_ID

    async def setup_hook(self):
        # Carrega as extensões, como comandos
        # Lista de extensões a carregar
        extensions = [
            "extensions.commands.basic",
            "extensions.commands.tasks"
        ]

        # Tenta carregar cada extensão individualmente
        for ext in extensions:
            try:
                await self.load_extension(ext)
                print(f"✅ Extensão carregada com sucesso: {ext}")
            except Exception as e:
                print(f"❌ Erro ao carregar extensão {ext}: {e}")

        # Sincronizar comandos de barra
        try:
            synced = await self.tree.sync()
            print(f"✅ Comandos de barra sincronizados: {[cmd.name for cmd in synced]}")
        except Exception as e:
            print(f"❌ Erro ao sincronizar comandos de barra: {e}")

    async def on_ready(self):
        print(f"Bot {self.user} está online!")