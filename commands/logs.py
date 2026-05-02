from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="logs")
    async def logs(self, ctx):
        try:
            with open("log.txt", "r") as f:
                lines = f.readlines()

            last = "".join(lines[-50:])

            if len(last) > 1900:
                last = last[-1900:]

            await ctx.send(f"```{last}```")

        except Exception as e:
            await ctx.send(f"error: {e}")

async def setup(bot):
    await bot.add_cog(Logs(bot))
