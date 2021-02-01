import discord, time, asyncio, math, random, traceback, sys
from async_timeout import timeout
from time import gmtime, strftime
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions

class m-cog(Cog):
  @command(name="help")
  async def help(ctx):
    embed=discord.Embed(title="Commands:", description="Usefull commands and usages", color=0xff8040)
    embed.add_field(name="help", value="Shows this page silly!~", inline=False)
    embed.add_field(name="ban", value="Bans a user", inline=False)
    embed.add_field(name="kick", value="Kicks a user ", inline=False)
    embed.add_field(name="ping", value="Returns a helpfull command output time", inline=False)
    embed.add_field(name="clear", value="Clears messages", inline=False)
    embed.add_field(name="ticket", value="Makes a ticket", inline=False)
    embed.add_field(name="tc", value="Closes a ticket (WARNING: using this in any other channel will restrict access strictly for you only)", inline=False)
    embed.add_field(name="tellmeajoke", value="Tells you a joke", inline=False)
    embed.add_field(name="lockdown", value="Locks a channel", inline=False)
    embed.add_field(name="unlock", value="Unlocks a channel", inline=False)
    embed.add_field(name="animal_fact", value="Sends an animal fact!", inline=False)
    embed.add_field(name="Echo", value="Repeats what you say", inline=False)
    embed.add_field(name="Alias:", value="say", inline=True)
    embed.add_field(name="slap_member", value="Physically Assults someone..", inline=False)
    embed.add_field(name="Alias:", value="hit", inline=True)
    embed.add_field(name="role_dice", value="Rolls a dice", inline=False)
    embed.add_field(name="Alias:", value="roll", inline=True)
    embed.add_field(name="Hello", value="Hi there!", inline=False)
    embed.add_field(name="afk", value="Marks you as AFK, by typing again it will remove your afk status", inline=False)
    embed.add_field(name="defWelcome", value="Defines welcome channel", inline=False)
    
    await ctx.send(embed=embed)