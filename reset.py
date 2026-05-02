from discord.ext import commands
import os

OWNER_ID = 123456789012345678  # replace with YOUR Discord user ID

class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="update")
    async def update(self, ctx):
        if ctx.author.id != OWNER_ID:
            return await ctx.send("nah this command not for you 💀")

        await ctx.send("Pulling latest GitHub code and restarting... 🔄")

        os.system("git pull")

        await ctx.send("Restarting now ✅")

        await self.bot.close()

async def setup(bot):
    await bot.add_cog(Update(bot))
