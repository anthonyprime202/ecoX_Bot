from discord.ext import commands
from discord import app_commands
import discord

from itertools import islice

from config import shop_config
from .. import Cog


class Shop(Cog):
    @app_commands.command(**shop_config["shop"])
    async def shop(self, interaction: discord.Interaction) -> None:
        items = self.db.fetch("SELECT * FROM shops WHERE guild = $1", interaction.guild.id)

    @staticmethod
    def items_to_embed(items: list[asyncpg.Record], size: int, embed_class=discord.Embed) -> list[list[discord.Embed]]:
        list_of_items = [[seq[i:i+size]] for i in range(0, len(items), size)]
        for list_of_item in list_of_items:
            


async def setup(bot) -> None:
    await bot.add_cog(Shop(bot))
