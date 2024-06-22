import discord
from discord.ext import commands, tasks
from datetime import datetime as dt

# System Libraries
import os
import random
import asyncio
import datetime

#Config import
from config import *

# MongoDB 
import pymongo
mongoclient = pymongo.MongoClient(LOGIN_URL)
db = mongoclient.main
guilds = db.guilds
marrie = db.marries

class marries(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='marry')
    async def marry(self, ctx, member: discord.Member = None):
        if member:
            if member != ctx.author:
                marry_doc = marrie.find_one({ '$or': [ { "user1":ctx.author.id }, {"user1":member.id }, { "user2":ctx.author.id }, {"user2":member.id }] })
                if not marry_doc:
                    photo = random.choice(marry_gifs)
                    accept = '✅'
                    decline = '❌'
                    waitt = discord.Embed(title = "Запрос на Брак", description = f"{member.mention}, {ctx.author.mention} предложил(-а) вам заключить брачный союз.", color = 0x2f3136)
                    waitt.timestamp = dt.utcnow()
                    waitt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
                    gf = await ctx.send(embed=waitt)
                    await gf.add_reaction(accept)
                    await gf.add_reaction(decline)

                    def check(reaction, user):
                        return user == member and reaction.emoji in '✅❌'
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', check = check, timeout = 30)
                    except asyncio.TimeoutError:
                        waitt2 = discord.Embed(title = "Игнор", description = f"{member.mention} тебя проигнорировал(-а) :c", color = 0x2f3136)
                        waitt2.timestamp = dt.utcnow()
                        waitt2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
                        await gf.clear_reactions()
                        await gf.edit(embed=waitt2)
                        return
                    if reaction.emoji == '✅':
                        ks = discord.Embed(title = "Поздравляю", description = f"{ctx.author.mention} и {member.mention} поженились!!", color = 0x2f3136)
                        ks.set_image(url = photo)
                        ks.timestamp = dt.utcnow()
                        ks.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
                        await gf.clear_reactions()
                        await gf.edit(embed=ks)
                    if reaction.emoji == '❌':
                        ks2 = discord.Embed(title = "Отказ", description = f"{ctx.author.mention}, {member.mention} вам отказал(-а) в браке :(", color = 0x2f3136)
                        ks2.timestamp = dt.utcnow()
                        ks2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
                        await gf.clear_reactions()
                        await gf.edit(embed=ks2)
                    
                else:
                    e = discord.Embed(title='Ошибка', description='Кто-то из вас уже находится в браке', color=0x2f3136)
                    e.timestamp = datetime.datetime.utcnow()
                    e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=e)
            else:
                e = discord.Embed(title='Ошибка', description='Вы не можете жениться на самом себе', color=0x2f3136)
                e.timestamp = datetime.datetime.utcnow()
                e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=e)
        else:
            e = discord.Embed(title='Ошибка', description='Укажите пользователя', color=0x2f3136)
            e.timestamp = datetime.datetime.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e)




def setup(bot):
    bot.add_cog(marries(bot))