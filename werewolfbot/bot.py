"""Main script to define bot methods, and start the bot."""

import logging

from discord.ext.commands import Bot, when_mentioned_or
from electionsbot.log import DiscordHandler


logger = logging.getLogger(__name__)

bot = Bot(command_prefix=when_mentioned_or("...", ":"),
          help_command=None, case_insensitive=True)

logger.addHandler(DiscordHandler(bot))
logger.setLevel(logging.INFO)

bot.log = logger


# Load cogs
bot.load_extension("electionsbot.cogs.general")
