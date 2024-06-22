import discord
from discord import permissions
from discord.abc import _Overwrites
from discord.ext import commands
from discord_components import *

# Database Librares 
import pymongo
login_url = "mongodb+srv://HiddenDatabase@cluster0.gnwc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongoclient = pymongo.MongoClient(login_url)
db = mongoclient.main
privates = db.privates

# System Librares
import datetime
import time
import os

# Import Configs
import config

class private_voices(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        privates = db.privates
        guilds = db.guilds
    
        if before.channel:
            private = privates.find_one({"id": str(before.channel.id), "guild_id": str(member.guild.id) })
            if private:
                if len(before.channel.members) == 0:
                    try:
                        await before.channel.delete()
                    except:
                        pass
                    privates.delete_one({"id": str(before.channel.id), "guild_id": str(member.guild.id)})
        
        guild_info = guilds.find_one({ "id": str(member.guild.id) })
    
        if after.channel:
            if after.channel.id == int(guild_info["parent_private_id"]):
                voice = await member.guild.create_voice_channel(f"災 • {member.name}", category=after.channel.category)
                idchannel = voice.id
                privates.insert_one({ "id": str(idchannel), "owner": str(member.id), "guild_id": str(member.guild.id) })
                await voice.set_permissions(member, connect=True,
                                                    manage_channels=True,
                                                    speak=True)
                try:
                    await member.edit(voice_channel=voice)
                except:
                    await voice.delete()
                    privates.delete_one({ "id": str(idchannel), "guild_id": str(member.guild.id) })

    @commands.command(name="voicesetup", aliases=['vsetup', 'vs'])
    @commands.has_permissions(administrator=True)
    async def vsetup(self, ctx):
        guilds = db.guilds
        guild_info = guilds.find_one({ "id": str(ctx.guild.id) })
        if guild_info["parent_private_id"] == "0" or not ctx.guild.get_channel(int(guild_info["parent_private_id"])):
            category = await ctx.guild.create_category_channel("Private Rooms")
            channel = await ctx.guild.create_voice_channel("[+] Create room", category=category)
            await channel.set_permissions(ctx.guild.default_role, speak=False)
            guilds.update_one({ "id": str(ctx.guild.id) }, { "$set": { "parent_private_id": str(channel.id) } })
            e = discord.Embed(title='', description='Канал для создания приватных комнат создан.', color=0x2F3136)
            e.set_author(name='Установка приватных комнат')
            e.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=e)
        else:
            channel = ctx.guild.get_channel(int(guild_info["parent_private_id"]))
            e = discord.Embed(title='', description=f'У вас уже есть канал для создания приваток: `{channel.name}`', color=0x2F3136)
            e.set_author(name='Установка приватных комнат')
            e.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
            e.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=e)


            
    @commands.command(name="voicelimit", aliases=['vlimit', 'vlim', 'vl'])
    async def vlimit(self, ctx, limit=None):
        e = discord.Embed(color=discord.Colour(0x2F3136))
        e.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        if ctx.author.voice == None:
            e.description = "Ты не находишься в голосовом канале."
            return await ctx.send(embed=e)
        owner_room = None
        if privates.count_documents({"id": str(ctx.author.voice.channel.id)}) != 0:
            owner_room = ctx.guild.get_member(int(privates.find_one({ "id": str(ctx.author.voice.channel.id), "guild_id": str(ctx.guild.id) })["owner"]))
        if privates.count_documents({"owner": str(ctx.author.id), "guild_id": str(ctx.guild.id)}) == 0 or ctx.author != owner_room:
            e.description = "Ты находишься не в своем личном канале."
            return await ctx.send(embed=e)
        if not limit:
            e.description = "Укажите лимит, который нужно поставить. (Максимальный лимит: 99)\n`0` для удаления лимита."
            return await ctx.send(embed=e)
        try:
            limit = int(limit)
        except:
            e.description = "Лимит может состоять только из чисел от 0 до 99!"
            return await ctx.send(embed=e)
        if limit < 0 or limit >= 100:
            e.description = "Укажите лимит, который нужно поставить. (Максимальный лимит: 99)\n`0` для удаления лимита."
            return await ctx.send(embed=e)
        try:
            channel = ctx.author.voice.channel
            await channel.edit(user_limit=limit)
            e.description = "Лимит изменен."
            await ctx.send(embed=e)
        except:
            pass

    @commands.command(name="voicename", aliases=['vname', 'vn'])
    async def vname(self, ctx, *name):
        e = discord.Embed(color=discord.Colour(0x2F3136))
        e.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        if ctx.author.voice == None:
            e.description = "Ты не находишься в голосовом канале."
            return await ctx.send(embed=e)
        owner_room = None
        if privates.count_documents({"id": str(ctx.author.voice.channel.id)}) != 0:
            owner_room = ctx.guild.get_member(int(privates.find_one({ "id": str(ctx.author.voice.channel.id), "guild_id": str(ctx.guild.id) })["owner"]))
        if privates.count_documents({ "owner": str(ctx.author.id), "guild_id": str(ctx.guild.id) }) == 0 or ctx.author != owner_room:
            e.description = "Ты находишься не в своем личном канале."
            return await ctx.send(embed=e)
        if len(name) == 0 or name[0] == "":
            e.description = "Укажите название, котороу нужно установить."
            return await ctx.send(embed=e)
        name_i = " ".join(name)
        if len(name_i) > 999:
            e.description = "Максимальный лимит символов в названии - 999."
            return await ctx.send(embed=e)
        try:
            channel = ctx.author.voice.channel
            await channel.edit(name=name_i)
            e.description = "Название изменено."
            await ctx.send(embed=e)
        except:
            e.description = "Что то пошло не так при смене названия твоего личного канал, возможно ты слишком часто используешь эту команду. Подожди 2 минуты и попробуй снова!"
            await ctx.send(embed=e)

    @commands.command(name="voicekick", aliases=['vkick', 'vk'])
    async def vkick(self, ctx, member: discord.Member):
        e = discord.Embed(color=discord.Colour(0x2F3136))
        e.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        if ctx.author.voice == None:
            e.description = "Ты не находишься в голосовом канале."
            return await ctx.send(embed=e)
        owner_room = None
        if privates.count_documents({"id": str(ctx.author.voice.channel.id)}) != 0:
            owner_room = ctx.guild.get_member(int(privates.find_one({ "id": str(ctx.author.voice.channel.id), "guild_id": str(ctx.guild.id) })["owner"]))
        if privates.count_documents({ "owner": str(ctx.author.id), "guild_id": str(ctx.guild.id) }) == 0 or ctx.author != owner_room:
            e.description = "Вы не являетесь владельцем комнаты"
            return await ctx.send(embed=e)
        if not member:
            e.description = "Укажите пользователя"
            return await ctx.send(embed=e)
        try:
            channel = ctx.author.voice.channel
            await member.move_to(None)
            e.description = "Пользователь изгнан с вашей комнаты"
            await ctx.send(embed=e)
        except:
            e.description = "Что то пошло не так, возможно ты слишком часто используешь эту команду. Подожди ``2 минуты`` и попробуй снова!"
            await ctx.send(embed=e)

    @commands.command(name='voicelock', aliases=['vlock', 'vcl', 'voice_unlock'])
    async def vlock(self, ctx):
        e = discord.Embed(color=discord.Colour(0x2F3136))
        e.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        if ctx.author.voice == None:
            e.description = "Ты не находишься в голосовом канале."
            return await ctx.send(embed=e)
        owner_room = None
        if privates.count_documents({"id": str(ctx.author.voice.channel.id)}) != 0:
            owner_room = ctx.guild.get_member(int(privates.find_one({ "id": str(ctx.author.voice.channel.id), "guild_id": str(ctx.guild.id) })["owner"]))
        if privates.count_documents({ "owner": str(ctx.author.id), "guild_id": str(ctx.guild.id) }) == 0 or ctx.author != owner_room:
            e.description = "Вы не являетесь владельцем комнаты"
            return await ctx.send(embed=e)
        if ctx.author.voice.channel.overwrites == {ctx.guild.default_role: discord.PermissionOverwrite(connect=False), ctx.author: discord.PermissionOverwrite(manage_channels=True, connect=True)}:
            e.description = 'Приватная комната уже заблокирована.'
            return await ctx.send(embed=e)
        try:
            channel = ctx.author.voice.channel
            perm = { 
                ctx.guild.default_role: discord.PermissionOverwrite(connect=False),
                ctx.author: discord.PermissionOverwrite(manage_channels=True, connect=True)
            }
            await channel.edit(overwrites=perm)
            print(dir(ctx.author.voice.channel))
            e.description = "Приватная комната заблокирована."
            await ctx.send(embed=e)
        except:
            e.description = "Что то пошло не так, возможно ты слишком часто используешь эту команду. Подожди ``2 минуты`` и попробуй снова!"
            await ctx.send(embed=e)

    @commands.command(name='voiceunlock', aliases=['vunlock', 'vun'])
    async def vunlock(self, ctx):
        e = discord.Embed(color=discord.Colour(0x2F3136))
        e.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
        e.timestamp = datetime.datetime.utcnow()
        if ctx.author.voice == None:
            e.description = "Ты не находишься в голосовом канале."
            return await ctx.send(embed=e)
        owner_room = None
        if privates.count_documents({"id": str(ctx.author.voice.channel.id)}) != 0:
            owner_room = ctx.guild.get_member(int(privates.find_one({ "id": str(ctx.author.voice.channel.id), "guild_id": str(ctx.guild.id) })["owner"]))
        if privates.count_documents({ "owner": str(ctx.author.id), "guild_id": str(ctx.guild.id) }) == 0 or ctx.author != owner_room:
            e.description = "Вы не являетесь владельцем комнаты"
            return await ctx.send(embed=e)
        if ctx.author.voice.channel.overwrites == {ctx.guild.default_role: discord.PermissionOverwrite(connect=True), ctx.author: discord.PermissionOverwrite(manage_channels=True, connect=True)}:
            e.description = 'Приватная комната не заблокирована.'
            return await ctx.send(embed=e)
        try:
            channel = ctx.author.voice.channel
            perm = {
                ctx.guild.default_role: discord.PermissionOverwrite(connect=True),
                ctx.author: discord.PermissionOverwrite(manage_channels=True, connect=True)
            }
            await channel.edit(overwrites=perm)
            print(dir(ctx.author.voice.channel))
            e.description = "Приватная комната разблокирована."
            await ctx.send(embed=e)
        except:
            e.description = "Что то пошло не так, возможно ты слишком часто используешь эту команду. Подожди ``2 минуты`` и попробуй снова!"
            await ctx.send(embed=e)





def setup(bot):
    bot.add_cog(private_voices(bot))
