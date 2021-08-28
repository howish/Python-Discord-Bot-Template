""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 2.7
"""

import discord
from discord.ext import commands
from helpers.json_manager import load_config


config = load_config()


class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, context):
        """
        List all commands from every Cog the bot has loaded.
        """
        prefix = config["bot_prefix"]
        if not isinstance(prefix, str):
            prefix = prefix[0]
        embed = discord.Embed(title="Help", description="List of available commands:", color=0x42F56C)
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            cog_cmds = cog.get_commands()
            cog_cmd_list = (cmd.name for cmd in cog_cmds)
            cog_cmd_description = (cmd.help for cmd in cog_cmds)
            help_text = '\n'.join(f'{prefix}{n} - {h}' for n, h in zip(cog_cmd_list, cog_cmd_description))
            embed.add_field(name=i.capitalize(), value=f'```{help_text}```', inline=False)
        await context.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
