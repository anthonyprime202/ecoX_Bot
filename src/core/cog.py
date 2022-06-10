class Cog(commands.Cog):
    async def cog_unload(self):
        print(f"{self.name} has been unloaded")