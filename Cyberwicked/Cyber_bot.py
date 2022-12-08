import asyncio
import functools
import itertools
import math
import random
import requests
import setuptools
import json

import discord
import os
import inspirobot
import ffmpeg
import youtube_dl

client = discord.Client()

@client.event
async def on_ready():
  print('{0.user} has entered the room'.format(client))



#Simple messages, trigger symbol "¤"  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  
  if message.content.startswith('¤hello'):
    await message.channel.send('BeepBoop! hello entity.Human')

  if message.content.startswith('¤bye'):
    await message.channel.send('Initiating sleep cycle')

  if message.content.startswith('¤test'):
    await message.channel.send('Test failed successfully')

#InspiroBot

  if message.content.startswith('¤quote'):
    quote = inspirobot.generate()
    await message.channel.send (quote.url)


#Token1 is bot password "secret", usefull to hide if using replit.
client.run(os.getenv('TOKEN1'))
