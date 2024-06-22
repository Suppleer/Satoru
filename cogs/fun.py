import asyncio
import discord
import typing
from discord.ext import commands
from discord_components import *

# System Librares
import datetime
import time
import os
import random
import io
import requests

# Import Configs
import config

class fun(commands.Cog):
	def __init__(self, bot):
		self.bot=bot
				
	@commands.command(aliases=['обнять'])
	async def hug(self, ctx, member: discord.Member = None):
		gifs_hug = config.hug
		gh = random.choice(gifs_hug)

		if not member and len(ctx.message.mentions) == 0:
			hs = discord.Embed(title = "Реакция: обьятия", description = f"{ctx.author.mention}, обнял(-a) всех", color = 0x2f3136)
			hs.set_image(url = gh)
			hs.timestamp = datetime.datetime.utcnow()
			hs.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=hs)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			hs = discord.Embed(title = "Реакция: обьятия", description = f"{ctx.author.mention}, обнял(-a) {member.mention}", color = 0x2f3136)
			hs.set_image(url = gh)
			hs.timestamp = datetime.datetime.utcnow()
			hs.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=hs)


	@commands.command(aliases=['плакать', 'заплакать'])
	async def cry(self, ctx, member: discord.Member = None):
		gifs_cry = config.cry
		gcry = random.choice(gifs_cry)

		if not member and len(ctx.message.mentions) == 0:
			cr = discord.Embed(title = "Реакция: плакать", description = f"{ctx.author.mention} расплакался(-ась)", color = 0x2f3136)
			cr.set_image(url = gcry)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			cr = discord.Embed(title = "Реакция: плакать", description = f"{ctx.author.mention} расплакался(-ась) из-за {member.mention}", color = 0x2f3136)
			cr.set_image(url = gcry)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)

	@commands.command(aliases=['укусить', 'кусь'])
	async def bite(self, ctx, member: discord.Member = None):
		gifs_bite = config.bite
		gcry = random.choice(gifs_bite)

		if not member and len(ctx.message.mentions) == 0:
			cr = discord.Embed(title = "Реакция: укусить", description = f"{ctx.author.mention} укусил(-а) всех", color = 0x2f3136)
			cr.set_image(url = gcry)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			cr = discord.Embed(title = "Реакция: укусить", description = f"{ctx.author.mention} укусил(-а) {member.mention}", color = 0x2f3136)
			cr.set_image(url = gcry)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)

	@commands.command(aliases=['лизнуть'])
	async def lick(self, ctx, member: discord.Member = None):
		gifs_lick = config.lick
		glick = random.choice(gifs_lick)

		if not member and len(ctx.message.mentions) == 0:
			lc = discord.Embed(title = "Реакция: лизнуть", description = f"{ctx.author.mention} лизнул(-а) всех", color = 0x2f3136)
			lc.set_image(url = glick)
			lc.timestamp = datetime.datetime.utcnow()
			lc.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=lc)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			lc = discord.Embed(title = "Реакция: лизнуть", description = f"{ctx.author.mention} лизнул(-а) {member.mention}", color = 0x2f3136)
			lc.set_image(url = glick)
			lc.timestamp = datetime.datetime.utcnow()
			lc.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=lc)


	@commands.command(aliases=['ударить'])
	async def punch(self, ctx, member: discord.Member = None):
		gifs_punch = config.punch
		gpunch = random.choice(gifs_punch)
		
		if not member and len(ctx.message.mentions) == 0:
			p = discord.Embed(title = "Реакция: ударить", description = f"{ctx.author.mention} ударил(-а) всех", color = 0x2f3136)
			p.set_image(url = gpunch)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=p)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			p = discord.Embed(title = "Реакция: ударить", description = f"{ctx.author.mention} ударил(-а) {member.mention}", color = 0x2f3136)
			p.set_image(url = gpunch)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=p)

	@commands.command()
	async def hand(self, ctx, member: discord.Member = None):
		gifs_hand = config.hand
		gpunch = random.choice(gifs_hand)

		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if not member:
			p = discord.Embed(title='Ошибка', description=f'{ctx.author.mention} Укажи пользователя которого хочешь **взять за руку**.', color = 0x2f3136)
			p.set_image(url = gpunch)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			return await ctx.send(embed=p)
		else:
			p = discord.Embed(title = "Реакция: взять за руки", description = f"{ctx.author.mention} взял(-a) за руку {member.mention}", color = 0x2f3136)
			p.set_image(url = gpunch)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=p)

	@commands.command(aliases=['танцевать'])
	async def dance(self, ctx, member: discord.Member = None):
		gifs_dance = config.dance
		gifs_dance_solo = config.dance_solo
		gdance = random.choice(gifs_dance)
		gdance_solo = random.choice(gifs_dance_solo)

		if not member and len(ctx.message.mentions) == 0:
			p = discord.Embed(title='Реакция: танцевать', description=f'{ctx.author.mention} танцует', color = 0x2f3136)
			p.set_image(url = gdance_solo)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			return await ctx.send(embed=p)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			p = discord.Embed(title = "Реакция: танцевать", description = f"{ctx.author.mention} танцует с {member.mention}", color = 0x2f3136)
			p.set_image(url = gdance)
			p.timestamp = datetime.datetime.utcnow()
			p.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=p)


	@commands.command(aliases=['погладить'])
	async def pat(self, ctx, member: discord.Member = None):
		gifs_pat = config.pat
		gpat = random.choice(gifs_pat)

		if not member and len(ctx.message.mentions) == 0:
			pt = discord.Embed(title = "Реакция: погладить", description = f"{ctx.author.mention} погладил(-а) всех", color = 0x2f3136)
			pt.set_image(url = gpat)
			pt.timestamp = datetime.datetime.utcnow()
			pt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=pt)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			pt = discord.Embed(title = "Реакция: погладить", description = f"{ctx.author.mention} погладил(-а) {member.mention}", color = 0x2f3136)
			pt.set_image(url = gpat)
			pt.timestamp = datetime.datetime.utcnow()
			pt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=pt)

	@commands.command(aliases=['убежать', 'бегать'])
	async def run(self, ctx, member: discord.Member = None):
		gifs_run = config.run
		grun = random.choice(gifs_run)

		if not member and len(ctx.message.mentions) == 0:
			pt = discord.Embed(title = "Реакция: убежать", description = f"{ctx.author.mention} убегает", color = 0x2f3136)
			pt.set_image(url = grun)
			pt.timestamp = datetime.datetime.utcnow()
			pt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=pt)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			pt = discord.Embed(title = "Реакция: убежать", description = f"{ctx.author.mention} убегает с {member.mention}", color = 0x2f3136)
			pt.set_image(url = grun)
			pt.timestamp = datetime.datetime.utcnow()
			pt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=pt)


	@commands.command(aliases=['покормить'])
	async def nom(self, ctx, member: discord.Member = None):
		gifs_nom = config.nom
		gnom = random.choice(gifs_nom)

		if not member and len(ctx.message.mentions) == 0:
			nm2 = discord.Embed(title = "Реакция: покоромить", description = f"{ctx.author.mention} покормил(-а) всех", color = 0x2f3136)
			nm2.set_image(url = gnom)
			nm2.timestamp = datetime.datetime.utcnow()
			nm2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=nm2)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			nm = discord.Embed(title = "Реакция: покормить", description = f"{ctx.author.mention} покормил(-а) {member.mention}", color = 0x2f3136)
			nm.set_image(url = gnom)
			nm.timestamp = datetime.datetime.utcnow()
			nm.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=nm)

	@commands.command()
	async def slap(self, ctx, member: discord.Member = None):
		gifs_slap = config.slap
		gslap = random.choice(gifs_slap)

		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		if not member and len(ctx.message.mentions) == 0:
			cr = discord.Embed(title = "Реакция: дать пощёчину", description = f"{ctx.author.mention} дал(-а) пощёчину", color = 0x2f3136)
			cr.set_image(url = gslap)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		else:
			cr = discord.Embed(title = "Реакция: дать пощёчину", description = f"{ctx.author.mention} дал(-а) пощёчину {member.mention}", color = 0x2f3136)
			cr.set_image(url = gslap)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)

	@commands.command(aliases=['тыкнуть'])
	async def poke(self, ctx, member: discord.Member = None):
		gifs_poke = config.poke
		gpoke = random.choice(gifs_poke)

		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if not member and len(ctx.message.mentions) == 0:
			cr = discord.Embed(title = "Реакция: тыкнуть", description = f"{ctx.author.mention} тыкнул(-а) всех", color = 0x2f3136)
			cr.set_image(url = gpoke)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)
		else:
			cr = discord.Embed(title = "Реакция: тыкнуть", description = f"{ctx.author.mention} тыкнул(-а) в {member.mention}", color = 0x2f3136)
			cr.set_image(url = gpoke)
			cr.timestamp = datetime.datetime.utcnow()
			cr.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=cr)

#============================================
# ===== COMMANDS WITH REACTION ACCEPTS ======
#============================================

	@commands.command(aliases=['заснуть', 'спать'])
	async def sleep(self, ctx, member: discord.Member = None):
		gifs_sleep = config.sleep
		gslp = random.choice(gifs_sleep)

		if not member and len(ctx.message.mentions) == 0:
			sl2 = discord.Embed(title = "Реакция: спать", description = f"{ctx.author.mention} спит", color = 0x2f3136)
			sl2.set_image(url = gslp)
			sl2.timestamp = datetime.datetime.utcnow()
			sl2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=sl2)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		if member.bot:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к Накане', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		else:
			accept = '✅'
			decline = '❌'

			waitt = discord.Embed(title = "Реакция: спать", description = f"{member.mention}, {ctx.author.mention} хочет **уснуть** с тобой. Что ответишь?", color = 0x2f3136)
			waitt.timestamp = datetime.datetime.utcnow()
			waitt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			gf = await ctx.send(embed=waitt)
			await gf.add_reaction(accept)
			await gf.add_reaction(decline)

			def check(reaction, user):
				return user == member and reaction.emoji in '✅❌'
			try:
				reaction, user = await self.bot.wait_for('reaction_add', check = check, timeout = 30.0)
			except asyncio.TimeoutError:
				waitt2 = discord.Embed(title = "Реакция: игнор", description = f"{member.mention} тебя проигнорировал(-а) :(", color = 0x2f3136)
				waitt2.timestamp = datetime.datetime.utcnow()
				waitt2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
				await gf.edit(embed=waitt2)
				await gf.clear_reactions()
				return
			if reaction.emoji == '✅':
				sl2 = discord.Embed(title = "Реакция: спать", description = f"{ctx.author.mention} спит с {member.mention}", color = 0x2f3136)
				sl2.set_image(url = gslp)
				sl2.timestamp = datetime.datetime.utcnow()
				sl2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
				await gf.edit(embed=sl2)
				await gf.clear_reactions()
				return
			if reaction.emoji == '❌':
				sl3 = discord.Embed(title = "Реакция: отказ", description = f"{member.mention} отказался(-ась)", color = 0x2f3136)
				sl3.timestamp = datetime.datetime.utcnow()
				sl3.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
				await gf.edit(embed=sl3)
				await gf.clear_reactions()
				return
				
	@commands.command(aliases=['поцеловать'])
	async def kiss(self, ctx, member: discord.Member = None):
		gifs_kiss = config.kiss
		gk = random.choice(gifs_kiss)

		if not member and len(ctx.message.mentions) == 0:
			ks = discord.Embed(title = "Ошибка", description = f"{ctx.author.mention} укажи пользователя которого хочешь поцеловать", color = 0x2f3136)
			ks.timestamp = datetime.datetime.utcnow()
			ks.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await ctx.send(embed=ks)
		elif len(ctx.message.mentions) > 0:
			member = ctx.message.mentions[0]
		if member == ctx.author:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к самому себе', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)
		if member.bot:
			e = discord.Embed(title='Ошибка', description='Вы не можете применить эту команду к Накане', color=0x2f3136)
			e.timestamp = datetime.datetime.utcnow()
			e.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
			return await ctx.send(embed=e)

		accept = '✅'
		decline = '❌'

		waitt = discord.Embed(title = "Реакция: поцелуй", description = f"{member.mention}, {ctx.author.mention} тебя хочет **поцеловать**. Что ответишь?", color = 0x2f3136)
		waitt.timestamp = datetime.datetime.utcnow()
		waitt.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
		gf = await ctx.send(embed=waitt)
		await gf.add_reaction(accept)
		await gf.add_reaction(decline)

		def check(reaction, user):
			return user == member and reaction.emoji in '✅❌'
		try:
			reaction, user = await self.bot.wait_for('reaction_add', check = check, timeout = 30)
		except asyncio.TimeoutError:
			waitt2 = discord.Embed(title = "Реакция: игнор", description = f"{member.mention} тебя проигнорировал(-а) :c", color = 0x2f3136)
			waitt2.timestamp = datetime.datetime.utcnow()
			waitt2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await gf.clear_reactions()
			await gf.edit(embed=waitt2)
			return
		if reaction.emoji == '✅':
			ks = discord.Embed(title = "Реакция: поцелуй", description = f"{ctx.author.mention} поцеловал(-а) {member.mention}", color = 0x2f3136)
			ks.set_image(url = gk)
			ks.timestamp = datetime.datetime.utcnow()
			ks.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await gf.clear_reactions()
			await gf.edit(embed=ks)
		if reaction.emoji == '❌':
			ks2 = discord.Embed(title = "Реакция: отказ", description = f"{ctx.author.mention}, {member.mention} вам отказал(-а)", color = 0x2f3136)
			ks2.timestamp = datetime.datetime.utcnow()
			ks2.set_footer(text = f"{ctx.author.name}", icon_url = ctx.author.avatar_url)
			await gf.clear_reactions()
			await gf.edit(embed=ks2)
		

def setup(bot):
	bot.add_cog(fun(bot))
