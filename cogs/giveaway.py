import discord
from discord.ext import commands, tasks

#System libraries
import random
import time
import datetime
import asyncio

# config
import config

class giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gcreate(self, ctx, time=None, *, prize=None):
        if time == None:
            e = discord.Embed(title='', description=f'Правильно использование команды.\n**```py\n{config.PREFIX}gcrate [time] [prize]\n```**', color=0x2f3136)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        if prize == None:
            e = discord.Embed(title='', description=f'Правильно использование команды.\n**```py\n{config.PREFIX}gcrate [time] [prize]\n```**', color=0x2f3136)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        e1 = discord.Embed(title='<:tada:868640190850273280> РОЗЫГРЫШ <:tada:868640190850273280>', description='', color=0x2f3136)
        e1.add_field(name='Приз', value=prize)
        e1.add_field(name='Организатор', value=ctx.author.mention)
        time_convert = {"s":1, "m":60, "h":3600, "d":86400}
        gaw_time = int(time[0]) * time_convert[time[-1]]
        e1.set_footer(text=f'Розыгрыш закончится через {time}')
        gaw_msg = await ctx.send(embed=e1)
        
        await gaw_msg.add_reaction("<:tada:868640190850273280>")
        await asyncio.sleep(gaw_time)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        e2 = discord.Embed(title='<:tada:868640190850273280> РОЗЫГРЫШ ЗАКОНЧЕН <:tada:868640190850273280>', description='', color=0x2f3136)
        e2.set_footer(text=f'Розыгрыш закончился {time}')
        e2.add_field(name='Приз', value=prize)
        e2.add_field(name='Победитель', value=winner.mention)
        e2.add_field(name='Организатор', value=ctx.author.mention)
        await gaw_msg.edit(embed=e2)

def setup(bot):
    bot.add_cog(giveaway(bot))
