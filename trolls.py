import assets
from discord.ext import commands


class troll_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def troll(self, ctx):
        if ctx.channel.id == '936902313589764146' or '939028644175699968':
            await ctx.send(f"```{assets.troll_command()}```")
        await self.bot.process_commands()


async def setup(bot):
    await bot.add_cog(troll_commands(bot))
