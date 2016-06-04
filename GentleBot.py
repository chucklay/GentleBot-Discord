import discord
from discord.ext import commands
from datetime import datetime
import GentleBotData

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
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)

@client.event
async def on_message(message):
	"""Handles all bot commands.

	Current commands:
		\"!time [timezone]\" - prints the current time on the machine the bot
							   is running on. A timezone can be specified."""
	if message.content.startswith('!time'):
		time = None
		if(message.content.split()[1] is str):
			#Get time in timezone.
			time = datetime.time(datetime.now, message.content.split()[1])
		else:
			time = datetime.now().time()
		timestr = ('The current time is ' + time.hour() + ':' +
					time.minute() + ':' + time.second())
		tmp = await client.send_message(message.channel, timestr)

client.run(GentleBotData.bot_token);
