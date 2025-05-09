import discord
from discord.ext import commands
from core.config import DISCORD_TOKEN

class PorypyClient(commands.Bot):
    def __init__(self):
        # Define os intents e prefixo do bot
        intents = discord.Intents.default()
        intents.message_content = True  # Permitir que o bot leia o conteúdo das mensagens
        super().__init__(command_prefix="!", intents=intents)
        self.token = DISCORD_TOKEN

    async def setup_hook(self):
        # Carrega as extensões, como comandos
        await self.load_extension("extensions.commands.basic")
        await self.load_extension("extensions.commands.tasks")
        await self.tree.sync()

    async def on_ready(self):
        print(f"Bot {self.user} está online!")