from discord.ext import commands
from dotenv import dotenv_values

from datetime import datetime


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=self.get_prefix,
            intents=intents,
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Spy×Family",
            ),
        )
        self.token = dotenv_values().get("BOT_TOKEN")
        
    async def on_ready(self):
        print(f"Logged in as {self.user}(ID: {self.user.id}) at {datetime.now()}")