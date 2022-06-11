from discord.ext import commands
from discord import app_commands
import discord

from itertools import islice

from config import shop_config
from .. import Cog, PaginateEmbed


class Shop(Cog):
    @app_commands.command(**shop_config["shop"])
    async def shop(self, interaction: discord.Interaction) -> None:
        data = await self.db.fetch("SELECT * FROM shops WHERE guild = $1", interaction.guild.id)
        guild_data = await self.db.fetchrow("SELECT currency, description FROM guilds WHERE id = $1", interaction.guild.id)
        items = [f"<@&{item['role']}>**———(***{item['price']}{guild_data['currency']}***)**\n{item['description']}" for item in data]
        embeds = self.items_to_embed(items=items, size=15, description=guild_data["description"], embed_class=PaginateEmbed)

    @staticmethod
    def items_to_embed(ctx, items: list[str], size: int, description: str, embed_class=discord.Embed) -> list[list[discord.Embed]]:
        embed_list = []
        for n in range(0, len(items), size):
            description = f"{description}\n\n{'\n\n'.join(items[n:n+size])}"
            embed = embed_class(title="Shop", description=description, color=ctx.bot.color)
            embed_list.append(embed)
        return embed_list


async def setup(bot) -> None:
    await bot.add_cog(Shop(bot))
