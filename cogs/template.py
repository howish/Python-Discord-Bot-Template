""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 2.7
"""

# import json
# import os
# import sys

from discord.ext import commands
from helpers.json_manager import load_config


config = load_config()


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.command(name="testcommand")
    async def testcommand(self, context):
        """
        This is a testing command that does nothing.
        """
        # Do your stuff here

        # Don't forget to remove "pass", that's just because there's no content in the method.
        pass


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
def setup(bot):
    bot.add_cog(Template(bot))
