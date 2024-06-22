import discord
from discord.ext import commands, tasks
from datetime import datetime as dt

# System Libraries
import os
import random

#Config import
import config

# MongoDB 
import pymongo
login_url = "mongodb+srv://HiddenDatabase@cluster0.gnwc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongoclient = pymongo.MongoClient(login_url)
db = mongoclient.main
guilds = db.guilds

class welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='welcome_message', aliases=['wm'])
    async def welcome_message(self, ctx, arg = None):
        if not arg:
            e = discord.Embed(title='<:set:872178575028138034> Настройки', description=f'Укажите аргумент - `on/off`', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        if arg.lower() == "on" and guilds.find_one({"id": str(ctx.guild.id)})['config']['welcome'] != True:
            arg = "Включен"
            guilds.update_one({"id": str(ctx.guild.id)}, {"$set": {"config.welcome": True}})
            e = discord.Embed(title='<:set:872178575028138034> Настройки', description=f'Параметр успешно изменен на **{arg}**', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        elif arg.lower() == "off" and guilds.find_one({"id": str(ctx.guild.id)})['config']['welcome'] != False:
            arg = "Выключен"
            guilds.update_one({"id": str(ctx.guild.id)}, {"$set": {"config.welcome": False}})
            e = discord.Embed(title='<:set:872178575028138034> Настройки', description=f'Параметр успешно изменен на **{arg}**', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        if arg.lower() in ['on', 'off']:
            e = discord.Embed(title='Ошибка', description=f'Данное значение уже установлено', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)
        else:
            e = discord.Embed(title='Ошибка', description=f'Вы указали неправильный аргумент', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e)


    @commands.command(name='set_welcome_message', aliases=['sw_message'])
    async def set_welcome_message(self, ctx, *, arg = None): 
        if guilds.find_one({"id": str(ctx.guild.id)})['config']['welcome'] == True:     
            if arg:
                guilds.update_one({"id": str(ctx.guild.id)}, {"$set": {"config.welcome_message": arg}})
                e = discord.Embed(title='<:set:872178575028138034> Настройки', description=f'Сообщения успешно установлено!', color=0x2f3136)
                e.timestamp = dt.utcnow()
                e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                return await ctx.send(embed=e)
        else:
            guilds.update_one({"id": str(ctx.guild.id)}, {"$set": {"config.welcome_message": arg}})
            e = discord.Embed(title='Ошибка', description=f'Параметр **`welcome`** не включен', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)


    @commands.command(name='set_welcome_channel')
    async def set_welcome_channel(self, ctx, arg: discord.TextChannel = None):
        if guilds.find_one({"id": str(ctx.guild.id)})['config']['welcome'] == True:     
            if arg:
                e = discord.Embed(title='<:set:872178575028138034> Настройки', description=f'Канал для сообщений о входе установлен **`{arg}`**', color=0x2f3136)
                e.timestamp = dt.utcnow()
                e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                return await ctx.send(embed=e)
        else:
            e = discord.Embed(title='Ошибка', description=f'Параметр **`welcome`** не включен', color=0x2f3136)
            e.timestamp = dt.utcnow()
            e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=e)

    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_info = guilds.find_one({"id": str(member.guild.id)})['config']
        if guild_info['welcome']:
            text = guild_info['welcome_message']
            if "{{member}}" in text:
                member = member.name
                text = text.replace("{{member}}", member)
            elif "{{member.mention}}" in text:
                member = member.mention
                text = text.replace("{{member.mention}}", member.mention)
            else:
                member = ''
            
            e = discord.Embed(title=f'Добро пожаловать на {member.guild.name}', description=text, color=0x2f3136)
            print(guild_info['welcome_channel'])
            channel = self.bot.get_channel(guild_info['welcome_channel'])
            print(channel)

            await channel.send(member.mention, embed=e)
        
        


def setup(bot):
    bot.add_cog(welcome(bot))
