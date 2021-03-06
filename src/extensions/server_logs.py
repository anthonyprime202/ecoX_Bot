from discord.ext import commands
import discord

from .. import Cog


class ServerLogs(Cog):
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild) -> None:
        users = [(user.id, guild.id) for user in guild.members if not user.bot]
        async with self.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute(
                    "INSERT INTO guilds(id) VALUES($1)", guild.id
                )
                await conn.executemany(
                    "INSERT INTO economy(member, guild) VALUES($1, $2)", users
                )

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild) -> None:
        async with self.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute(
                    "DELETE FROM guilds WHERE id = $1; DELETE FROM economy WHERE guild = $1;", guild.id
                )
   

async def setup(bot) -> None:
    await bot.add_cog(ServerLogs(bot))