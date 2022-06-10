import discord

class Embed(discord.Embed):
    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color=discord.Colour.green()
        self.set_footer(text=f"Requested by {ctx.author}")