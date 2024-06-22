# Discord Librares
import discord
from discord.ext import commands
from discord_components import *

# System Librares
import datetime
import time
import os

# Database Librares 
import pymongo

login_url = "mongodb+srv://HiddenDatabase@cluster0.gnwc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongoclient = pymongo.MongoClient(login_url)
db = mongoclient.PrivateVoices
privates = db.privates

# Import Configs
import config

# Variables
prefix = config.PREFIX

# Discord Client
bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())

# Token
Token = "enter Token"

@bot.event
async def on_ready():
    guilds = db.guilds
    private = db.privates

    for x in guilds.find({"parent_private_id": {"$ne": "0"}}):
        channel = bot.get_channel(int(x["parent_private_id"]))
        guild = bot.get_guild(int(x["id"]))

        if len(channel.members) > 0:
            for member in channel.members:
                voice = await member.guild.create_voice_channel(f"{member.name}", category=channel.category)
                await voice.set_permissions(member, connect=True,
                                            manage_channels=True,
                                            speak=True)
                idchannel = voice.id
                try:
                    await member.edit(voice_channel=voice)
                    private.insert_one({"id": str(idchannel), "owner": str(member.id), "guild_id": str(guild.id)})
                except:
                    await voice.delete()
                    private.delete_one({"id": str(idchannel), "guild": str(guild.id)})

    for x in private.find():
        channel = bot.get_channel(int(x["id"]))
        guild = bot.get_guild(int(x["guild_id"]))
        if len(channel.members) == 0:
            try:
                await channel.delete()
            except:
                pass
            private.delete_one({"id": str(channel.id), "guild_id": str(guild.id)})

    await bot.change_presence(activity=discord.Streaming(name=f"Yokai", url="https://twitch.tv/gteety"),
                              status=discord.Status.do_not_disturb)
    DiscordComponents(bot)
    print(
        f"[{datetime.datetime.utcfromtimestamp(int(time.time()) + 10800).strftime('%H:%M:%S')}] Запустилась "
        f"{bot.user} <3")


@bot.command()
@commands.is_owner()
async def zagruzka(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print("[Bot Log] " + f"Загружен модуль - {extension}")
    if not commands.NotOwner:
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
    else:
        print(bot.owner_id)
        await ctx.message.delete()
        emb = discord.Embed(description=f"Модуль **{extension}** успешно загружен!", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


@bot.command()
@commands.is_owner()
async def razgruzka(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print("[Bot Log] " + f"Выгружен модуль - {extension}")
    if not commands.NotOwner:
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
    else:
        await ctx.message.delete()
        emb = discord.Embed(description=f"Модуль **{extension}** успешно выгружен!", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


@bot.command()
@commands.is_owner()
async def perezagruz(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    print("[Bot Log] " + f"Перезагружен модуль - {extension}")
    if not commands.NotOwner:
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)
    else:
        await ctx.message.delete()
        emb = discord.Embed(description=f"Модуль **{extension}** успешно перезагружен!", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

@bot.command()
async def proverka(ctx):
    await ctx.send('OK!')


@zagruzka.error
async def reload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


@razgruzka.error
async def reload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


@perezagruz.error
async def reload_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.message.delete()
        emb = discord.Embed(title='Ошибка', description=f"Вы не являетесь разработчиком", color=0x2f3136)
        emb.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'[COG] {filename[:-3]} подключен!')

bot.run(Token)
