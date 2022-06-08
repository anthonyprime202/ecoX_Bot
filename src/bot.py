from discord.ext import commands
from dotenv import dotenv_values
import asyncpg

from datetime import datetime


INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=self.get_prefix,
            intents=INTENTS,
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Spy×Family",
            ),
        )
        self.token = dotenv_values().get("BOT_TOKEN")
        
    async def on_ready(self):
        print(f"Logged in as {self.user}(ID: {self.user.id}) at {datetime.now()}")