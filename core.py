from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send("🏓 Pong!")

    @commands.command(name="sobre")
    async def sobre(self, ctx):
        await ctx.send(
            "Sou o **Porypy**, um bot para te ajudar a organizar suas metas, tarefas e finanças! 🧠🏡"
        )

    @commands.command(name="ajuda")
    async def ajuda(self, ctx):
        ajuda_msg = (
            "Comandos disponíveis:\n"
            "`!ping` - Testa se estou online.\n"
            "`!sobre` - Conheça o propósito do Porypy.\n"
            "(em breve) `!add_tarefa`, `!listar_tarefas`, `!meta`, etc."
        )
        await ctx.send(ajuda_msg)


async def setup(bot):
    await bot.add_cog(Core(bot))