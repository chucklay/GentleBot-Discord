import discord
from discord.ext import commands
import GentleBotData

description = '''A discord bot, mostly for learning the API.

Requires a file "GentleBotData.py", which must contain the following variables:
	client_id
	client_secret
	bot_id
	bot_username
	bot_token

By Charlie Laymon
laymon.charlesr@gmail.com'''

client = discord.Client()

@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)

client.run(GentleBotData.bot_token);
