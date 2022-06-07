from discord.ext import commands
from dotenv import dotenv_values
import asyncpg
import discord

from datetime import datetime


INTENTS = discord.Intents.default()
INTENTS.message_content = True
INTENTS.members = True

CREDENTIALS = {
    "user": dotenv_values().get("PG_USERNAME"),
    "password": dotenv_values().get("PG_PASSWORD"),
    "host": dotenv_values().get("PG_HOST"),
    "port": int(dotenv_values().get("PG_PORT")),
    "database": dotenv_values().get("PG_DBNAME"),
}


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
    
    @property 
    def token(self):
        return dotenv_values().get("BOT_TOKEN")
    
    
    @property 
    async def db(self) -> asyncpg.Pool:
        return asyncpg.create_pool(**CREDENTIALS)

    @property 
    def curr_time(self):
        return(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}(ID: {self.user.id}) at {self.curr_time}")