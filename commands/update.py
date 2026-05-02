from discord.ext import commands
import os

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update")
    async def update(self, ctx):
        await ctx.send("pulling latest code... 🔄")

        os.system("git pull")

        await ctx.send("restarting now 😈")

        await self.bot.close()

async def setup(bot):
    await bot.add_cog(Update(bot))
