import asyncio
from asyncio.tasks import wait_for
import discord
import typing
from discord.ext import commands
from discord_components import *

# Database Librares 
import pymongo
login_url = "mongodb+srv://HiddenDatabase@cluster0.gnwc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongoclient = pymongo.MongoClient(login_url)
db = mongoclient.main
privates = db.privates
guilds = db.guilds


# System Librares
import datetime
import time
import os
import io
import requests

# Import Configs
import config


class system(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name="profile", aliases=['p'])
    @commands.has_permissions(administrator=True)
    async def profile(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        e = discord.Embed(title=f'Профиль • {member.display_name}', description='Пока что в разработке', color=0x2f3136)
        e.set_image(url=member.avatar_url)
        await ctx.reply(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        sett = discord.Embed(title='Информация', description=f"**```py\nPing: {ping}ms \n```**", color=0x2f3136)
        sett.timestamp = datetime.datetime.utcnow()
        sett.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=sett)

    @commands.command(name="avatar", aliases=["ava", 'av'])
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
          member = ctx.author
          
        emb = discord.Embed(title=f"Аватар • {member.name}", description='', color=0x2f3136)
        emb.set_image(url = member.avatar_url_as(static_format="png"))
        emb.timestamp = datetime.datetime.utcnow()
        emb.set_footer(text=f'Запросил: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        e = discord.Embed(title='<:lock:868827681423257661> Блокировка', description=f'Канал {ctx.channel.mention} заблокирован.', color=0x2f3136)
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text=f'Выполнил(a) {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        e = discord.Embed(title='<:lock:868827681423257661> Разблокировка', description=f'Канал {ctx.channel.mention} разблокирован.', color=0x2f3136)
        e.timestamp = datetime.datetime.utcnow()
        e.set_footer(text=f'Выполнил(a) {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def test(self, ctx, ch: discord.VoiceChannel = None):
        await ch.delete()
        print(ch)
        await ctx.send("Felya lox")

        

def setup(bot):
    bot.add_cog(system(bot))
