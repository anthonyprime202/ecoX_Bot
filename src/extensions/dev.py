from discord.ext import commands
import discord

import config


class Dev(commands.Cog):
    async cog_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.reply(embed=)

    def cog_check(self, ctx):
        return ctx.author.id == ctx.bot.owner_id
    
    @commands.command(**config.tsync)
    async def tsync(self, ctx: commands.Context):
        await ctx.bot.tree.copy_global_to(guild=ctx.guild)
        await ctx.bot.tree.sync(guild=ctx.guild)
    
    
async def setup(bot):
    await bot.add_cog(Dev())