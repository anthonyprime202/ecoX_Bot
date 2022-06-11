from discord.ext import commands
from dotenv import dotenv_values
import asyncpg
import discord

from datetime import datetime
import os


INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=INTENTS,
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Spy×Family",
            ),
        )
    
    @property
    def __token(self) -> str:
        return dotenv_values().get("BOT_TOKEN")
    
    @property
    def __dsn(self) -> str:
        return dotenv_values().get("PG_DSN")
    
    @property
    def color(self) -> hex:
        return 0x9ce1f2
    
    @property 
    def curr_time(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def run(self) -> None:
        super().run(self.__token)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}(ID: {self.user.id}) at {self.curr_time}")
    
    async def setup_hook(self) -> None:
        self.db = await asyncpg.create_pool(dsn=self.__dsn)
        await bot.load_extension("jishaku")
        for extension in os.listdir("src/extensions"):
            if extension.endswith(".py") and extension != "config.py":
                await self.load_extension(f"src.extensions.{extension[:-3]}")