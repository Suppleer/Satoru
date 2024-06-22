import discord
from discord.ext import commands

# Database Librares 
import pymongo
login_url = "mongodb+srv://HiddenDatabase@cluster0.gnwc2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongoclient = pymongo.MongoClient(login_url)
db = mongoclient.main
privates = db.privates

# System import
import random
import os
import time
import datetime

class new_guild(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		guilds = db.guilds
		if guilds.count({ "id": str(guild.id) }) == 0:
			guilds.insert_one({ 
			  "id": str(guild.id), 
			  "parent_private_id": "0",
			  "config": {
				  "welcome": False,
				  "verification": False,
				  "welcome_channel": 0,
				  "welcome_message": ""
			  }
			})
		else:
			return
		log_channel = self.bot.get_channel(867874537983049738)
		owner = guild.get_member(guild.owner_id)
		e = discord.Embed(title='Бот добавлен на новый сервер', description="", color=0x2f3136)
		e.description = f"""
	Название сервера: **{guild.name}**
	Владелец сервера: {owner.mention} (`{owner.id}` | `{owner}`)
	Количество участников: `{len(list(filter(lambda x: x.bot is False, guild.members)))}`
	Количество ботов: `{len(list(filter(lambda x: x.bot is True, guild.members)))}`
	Дата создания сервера: `{guild.created_at.strftime('%H:%M:%S %d.%m.%Y')}`
	"""
		e.timestamp = datetime.datetime.utcnow()
		await log_channel.send(embed=e)

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		guilds = db.guilds
		guilds.delete_one({ 
			"id": str(guild.id), 
			"parent_private_id": "0",
			"config": {
				"welcome": False,
				"verification": False,
				"welcome_channel": 0,
				"welcome_message": ""
			}
		})
		log_channel = self.bot.get_channel(867874537983049738)
		owner = guild.get_member(guild.owner_id)
		e = discord.Embed(title='Бот был удален с сервера', description="", color=0x2f3136)
		e.description = f"""
	Название сервера: **{guild.name}**
	Владелец сервера: {owner.mention} (`{owner.id}` | `{owner}`)
	Количество участников: `{len(list(filter(lambda x: x.bot is False, guild.members)))}`
	Количество ботов: `{len(list(filter(lambda x: x.bot is True, guild.members)))}`
	Дата создания сервера: `{guild.created_at.strftime('%H:%M:%S %d.%m.%Y')}`
	"""
		e.timestamp = datetime.datetime.utcnow()
		await log_channel.send(embed=e)

	

def setup(bot):
	bot.add_cog(new_guild(bot))
