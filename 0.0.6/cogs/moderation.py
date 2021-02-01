import discord, time, asyncio, math, random, traceback, sys
from async_timeout import timeout
from time import gmtime, strftime
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix = '/')
bot.remove_command("help")

class Moderation(Cog):
  def __init__(self, bot):
    self.bot = bot

  @has_permissions(administrator=True)
  @command(name="warn")
  async def warn(ctx,member: discord.Member,*,reason=None):
    try:
      await ctx.send(str(member)+" has been warned for " + str(reason))
    except:
      await ctx.send("Failed to warn member. This could be a sign of no warns, and also a faliure to do set up your guild correctly most likely this is a backend error")
  @has_permissions(administrator=True)    
  @command(name="warns")
  async def warns(ctx,*,member):
    try:
      guild = ctx.guild.id()
      await ctx.send(member + " has been warned in the past for " + reason)
    except:
      await ctx.send("Failed to find past warns. This could be a sign of no warns, and also a faliure to do set up your guild correctly most likely this is a backend error") 

  @has_permissions(administrator=True)
  @command(name="ban")
  async def ban(ctx, member : discord.Member, *, reason=None):
    try:
      await member.ban(reason=reason)
      cchannel = ctx.channel
      channel = bot.get_channel(781220833477132288)
      embed=discord.Embed(title="Audit Log", description="Command Detection", color=0xff8040)
      embed.add_field(name=f"{member} has been banned" + 'at' + strftime("%a, %d %b %Y %I:%M:%S %p", gmtime()), value="Action", inline=False)
      embed.set_footer(text="{}".format(ctx.message.author))
      await channel.send(embed=embed)
    except:
      if member == discord.Permissions.administrator:
        msg = "This user is an administrator"
        await bot.send_message(msg)
      else:
        await ctx.send("Failed to ban this member. This could be a sign of missing permissions or a backend error")

  @has_permissions(administrator=True)
  @command(name="lockdown")
  async def lockdown(ctx):
    try:
      channel = ctx.channel
      await ctx.channel.set_permissions(ctx.guild.get_role(785280980881375242), send_messages=False)
      await ctx.send("Locked channel")
    except:
      await ctx.send("Failed to lock channel. This could be a sign of missing permissions or a backend error")

  @has_permissions(administrator=True)
  @command(name="unlock")
  async def unlock(ctx):
    try:
      channel = ctx.channel
      author = ctx.message.author
      await ctx.channel.set_permissions(ctx.guild.get_role(785280980881375242), send_messages=True)
      await ctx.send("Unlocked channel")
    except:
      await ctx.send("Failed to unlock channel. This could be a sign of missing permissions or a backend error")

  @has_permissions(administrator=True)
  @command(name="kick")
  async def kick(ctx, member : discord.Member, *, reason=None):
    try:
      await member.kick(reason=reason)
      cchannel = ctx.channel
      channel = bot.get_channel(781220833477132288)
      embed=discord.Embed(title="Audit Log", description="Command Detection", color=0xff8040)
      embed.add_field(name=f"{member} has been kicked" + 'at' + strftime("%a, %d %b %Y %I:%M:%S %p", gmtime()), value="Action", inline=False)
      embed.set_footer(text="{}".format(ctx.message.author))
      await channel.send(embed=embed)
    except:
      await ctx.send("Failed to kick member. This could be a sign of missing permissions such as the person in question being a higher role than the bot or a backend error")

  @has_permissions(administrator=True)    
  @command(name="clear")
  async def clear(ctx, amount=1):
    try:
      member = ctx.message.author
      aamount = amount + 1
      await ctx.channel.purge(limit=aamount)
      msg = await ctx.send('Cleared ' + str(amount) + ' messages')
      cchannel = ctx.channel
      channel = bot.get_channel(781220833477132288)
      embed=discord.Embed(title="Audit Log", description="Command Detection", color=0xff8040)
      embed.add_field(name=f"{member} has cleared {amount} messages in #" + str(cchannel) + 'at' + strftime("%a, %d %b %Y %I:%M:%S %p", gmtime()), value="Action", inline=False)
      embed.set_footer(text="{}".format(ctx.message.author))
      await channel.send(embed=embed)
      time.sleep(3)
      await msg.delete()
    except:
      await ctx.send("Failed to clear. This could be a sign of missing permissions or a backend error")

  @Cog.listener()
  async def on_ready(self):
    if not self.bot.ready:
      self.bot.cogs_ready.ready_up("Moderation")
      
def setup(bot):
  bot.add_cog(Moderation(bot))