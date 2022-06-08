from discord.ext import commands
from dotenv import dotenv_values
import asyncpg
import discord

from datetime import datetime


INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True


class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=self.get_prefix,
            intents=INTENTS,
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="Spy×Family",
            ),
        )
        self.__token = dotenv_values().get("BOT_TOKEN")
        self.__dsn = dotenv_values().get("PG_DSN")

    @property 
    def curr_time(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property 
    async def db(self) -> asyncpg.Pool:
        return asyncpg.create_pool(dsn=self.__dsn)

    async def run(self) -> None:
        super().run(self.__token)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}(ID: {self.user.id}) at {self.curr_time}")