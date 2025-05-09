import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from typing import Optional
from datetime import datetime

# Armazenamento temporário das tarefas (em memória)
task_storage = {}

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="tasks_add", description="Add a new task")
    async def tasks_add(self, ctx: commands.Context):
        await ctx.send("📌 Qual o **título da tarefa**? Responda abaixo.")

        try:
            title_msg = await self.bot.wait_for(
                "message",
                check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                timeout=60.0
            )
            title = title_msg.content
            await ctx.send(f"✅ Título recebido: **{title}**")
        
        except asyncio.TimeoutError:
            await ctx.send("⏰ Tempo esgotado! Tente novamente com o comando `/tasks_add`.")

        # Pergunta prioridade com reações
        priority_prompt = await ctx.send(
            "**Qual a prioridade da tarefa?**\n\n🔴 - Alta\n🟡 - Média\n🟢 - Baixa"
        )

        emojis = ["🔴", "🟡", "🟢"]
        for emoji in emojis:
            await priority_prompt.add_reaction(emoji)

        def reaction_check(reaction, user):
            return (
                user == ctx.author and 
                str(reaction.emoji) in emojis and 
                reaction.message.id == priority_prompt.id
            )

        try:
            reaction, _ = await self.bot.wait_for("reaction_add", timeout=30.0, check=reaction_check)
            priority_map = {
                "🔴": "Alta",
                "🟡": "Média",
                "🟢": "Baixa"
            }
            priority = priority_map[str(reaction.emoji)]
        except asyncio.TimeoutError:
            return await ctx.send("⏰ Tempo esgotado para escolher a prioridade.")

        # Confirmação
        embed = discord.Embed(
            title="✅ Tarefa Criada",
            description=f"**Título:** {title}\n**Prioridade:** {priority}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)            

    @app_commands.command(name="tasks_list", description="Listar suas tarefas")
    async def tasks_list(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        tasks = task_storage.get(user_id, [])

        if not tasks:
            await interaction.response.send_message("📭 Você ainda não tem tarefas registradas.")
            return

        embed = discord.Embed(
            title=f"📋 Tarefas de {interaction.user.display_name}",
            color=discord.Color.blue()
        )

        for i, task in enumerate(tasks, 1):
            due = task['due_date'].strftime("%d/%m/%Y") if task['due_date'] else "Sem prazo"
            embed.add_field(
                name=f"{i}. {task['title']}",
                value=f"Status: `{task['status']}` | Prioridade: `{task['priority']}` | Prazo: {due}",
                inline=False
            )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Tasks(bot))
