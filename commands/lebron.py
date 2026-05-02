from discord.ext import commands

# 🔒 HARD CODED CHANNEL
LEBRON_CHANNEL_ID = 1500100267067179009

class Lebron(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.startswith("."):
            return

        if message.channel.id != LEBRON_CHANNEL_ID:
            return

        await message.reply("lebron", mention_author=False)

async def setup(bot):
    await bot.add_cog(Lebron(bot))
