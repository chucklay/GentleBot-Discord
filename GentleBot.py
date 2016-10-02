import discord
from discord.ext import commands
from datetime import datetime
import GentleBotData
import asyncio

description = '''A discord bot, mostly for learning the API.

Requires a file "GentleBotData.py", which must contain the following variables:
	client_id
	client_secret
	bot_id
	bot_username
	bot_token

By Charlie Laymon
chucklay@users.noreply.github.com'''

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)

@client.event
@asyncio.coroutine
def on_message(message):
	"""Handles all bot commands.

	Current commands:
		\"!time [timezone]\" - prints the current time on the machine the bot
							   is running on. A timezone can be specified."""
	if message.content.startswith('!time'):
		time = datetime.now().time()
		timestr = ('The current time is ' + str(time.hour) + ':' +
			    str(time.minute) + ':' + str(time.second))
		tmp = yield from client.send_message(message.channel, timestr)

client.run(GentleBotData.bot_token);
