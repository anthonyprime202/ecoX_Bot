from discord.ext import commands
import discord

class ServerLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        async with self.bot.db.acquire() as conn:
            conn.execute("INSERT INTO guilds(id, prefix) VALUES($1, '.')", guild.id)

