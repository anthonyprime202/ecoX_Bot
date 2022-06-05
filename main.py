from discord.ext import commands
from dotenv import dotenv_values
import discord

class ecoX(commands.Bot):
    def __init__(self):
        # Sets bot prefix to bot mention.
        super().__init__(
            command_prefix=commands.when_mentioned,
        )
        
        # Sets the bot's status to idle.
        self.status = discord.Status.idle
        
    async def on_ready(self):
        print("Bot is ready")


def main():
    bot = ecoX()
    token = dotenv_values().get("BOT_TOKEN")
    bot.run(token)


if __name__ == '__main__':
    main()