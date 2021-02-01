import discord
import asyncio
import json
import discord, time, asyncio, math, random, traceback, sys
from async_timeout import timeout
from time import gmtime, strftime
from discord.ext import commands, tasks
from discord.utils import get
from discord.ext.commands import has_permissions

class invite(Cog):
    async def fetch():
        global last
        global invites
        await bot.wait_until_ready()
        gld = bot.get_guild(int(guild_id))
        logs = bot.get_channel(int(logs_channel))
        while True:
            invs = await gld.invites()
            tmp = []
            for i in invs:
                for s in invites:
                    if s[0] == i.code:
                        if int(i.uses) > s[1]:
                            usr = gld.get_member(int(last))
                            eme = discord.Embed(description="Just joined the server", color=0x03d692, title=" ")
                            eme.set_author(name=usr.name + "#" + usr.discriminator, icon_url=usr.avatar_url)
                            eme.set_footer(text="ID: " + str(usr.id))
                            eme.timestamp = usr.joined_at
                            eme.add_field(name="Used invite",
                                          value="Inviter: " + i.inviter.mention + " (`" + i.inviter.name + "#" + i.inviter.discriminator + "`)\nCode: `" + i.code + "`\nUses: `" + str(
                                              i.uses) + "`", inline=False)
                            await logs.send(embed=eme)
                tmp.append(tuple((i.code, i.uses)))
            invites = tmp
            await asyncio.sleep(4)