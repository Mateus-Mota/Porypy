import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Select, View, Button
import asyncio
from typing import Optional
from datetime import datetime

# Armazenamento temporário das tarefas (em memória)
task_storage = {}

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="tasks_add", description="Adiciona uma nova tarefa ao planejamento")
    async def tasks_add(self, ctx: commands.Context):
        await ctx.send("Vamos começar a adicionar uma nova tarefa! Responda às próximas perguntas.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Título da tarefa
        await ctx.send("Qual o título da tarefa?")
        try:
            titulo_msg = await self.bot.wait_for('message', check=check, timeout=60)
            titulo = titulo_msg.content
        except asyncio.TimeoutError:
            return await ctx.send("Tempo esgotado para responder o título da tarefa.")

        # Prazo da tarefa
        await ctx.send("Qual o prazo da tarefa? (formato: DD/MM/AAAA ou deixe em branco)")
        try:
            prazo_msg = await self.bot.wait_for('message', check=check, timeout=60)
            prazo = prazo_msg.content or "Sem prazo definido"
        except asyncio.TimeoutError:
            return await ctx.send("Tempo esgotado para responder o prazo.")

        # View principal
        view = View()

        # Prioridade
        prioridade_select = Select(
            placeholder="Escolha a prioridade da tarefa",
            options=[
                discord.SelectOption(label="Baixa", emoji="🟢"),
                discord.SelectOption(label="Média", emoji="🟡"),
                discord.SelectOption(label="Alta", emoji="🔴"),
            ]
        )

        async def prioridade_callback(interaction: discord.Interaction):
            prioridade = prioridade_select.values[0]

            # Categoria
            categoria_select = Select(
                placeholder="Escolha a categoria da tarefa",
                options=[
                    discord.SelectOption(label="Finanças", emoji="💰"),
                    discord.SelectOption(label="Visitas", emoji="🏠"),
                    discord.SelectOption(label="Documentos", emoji="📄"),
                    discord.SelectOption(label="Outros", emoji="🗂️"),
                ]
            )

            async def categoria_callback(cat_interaction: discord.Interaction):
                categoria = categoria_select.values[0]

                # Criar embed
                embed = discord.Embed(
                    title="📝 Nova Tarefa Adicionada!",
                    description=f"**{titulo}**",
                    color=discord.Color.blurple()
                )
                embed.add_field(name="📅 Prazo", value=prazo, inline=True)
                embed.add_field(name="🔖 Prioridade", value=prioridade, inline=True)
                embed.add_field(name="📂 Categoria", value=categoria, inline=True)
                embed.set_footer(text=f"Adicionada por {ctx.author.display_name}")

                # Salvar no dicionário
                user_id = ctx.author.id
                task_storage.setdefault(user_id, []).append({
                    'title': titulo,
                    'due_date': None if prazo == "Sem prazo definido" else datetime.strptime(prazo, "%d/%m/%Y"),
                    'priority': prioridade,
                    'category': categoria,
                    'status': 'pendente'
                })

                # Enviar embed para canal de tarefas
                tasks_channel = self.bot.tasks_channel
                channel = self.bot.get_channel(tasks_channel)
                if channel:
                    await channel.send(embed=embed)

                await cat_interaction.response.send_message("✅ Tarefa adicionada com sucesso!", ephemeral=True)

            categoria_select.callback = categoria_callback
            categoria_view = View()
            categoria_view.add_item(categoria_select)
            await interaction.response.send_message("Escolha a categoria:", view=categoria_view, ephemeral=True)

        prioridade_select.callback = prioridade_callback
        view.add_item(prioridade_select)
        await ctx.send("Escolha a prioridade:", view=view)

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
                value=f"Status: `{task['status']}` | Prioridade: `{task['priority']}` | Prazo: {due} | Categoria: `{task['category']}`",
                inline=False
            )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Tasks(bot))