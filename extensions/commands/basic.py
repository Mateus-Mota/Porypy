import discord
from discord.ext import commands
from discord import app_commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check if the bot is alive")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! 🏓 Latency: `{latency}ms`")

    @app_commands.command(name="help", description="Show available bot commands")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📘 Help - Porypy Bot",
            description="Here are the available commands:",
            color=discord.Color.blurple()
        )
        embed.add_field(name="/ping", value="Check if the bot is alive", inline=False)
        embed.add_field(name="/help", value="Show this message", inline=False)
        embed.add_field(name="/about", value="Learn more about this project", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="about", description="Learn more about Porypy")
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🏠 Porypy Bot",
            description=(
                "Porypy is your real estate planning assistant built for Discord!\n"
                "Plan your first home, set goals, receive alerts, and organize your dreams right from your server."
            ),
            color=discord.Color.green()
        )
        embed.set_footer(text="Developed with 💙 by Mateus-Mota")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Basic(bot))