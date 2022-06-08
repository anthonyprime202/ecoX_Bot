from discord.ext import commands
import discord

class ServerLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None:
        async with self.bot.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute("INSERT INTO guilds(id) VALUES($1)", guild.id)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild) -> None:
        async with self.bot.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute("DELETE FROM guilds WHERE id = $1", guild.id)


async def setup(bot):
    await bot.add_cog(ServerLogs(bot))