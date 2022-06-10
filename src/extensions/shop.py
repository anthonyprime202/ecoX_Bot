from discord.ext import commands
from discord import app_commands
import discord

import config


class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(**config.shop)
    async def shop(self):
        pass
    


async def setup(bot):
    await bot.add_cog(Shop(bot))

