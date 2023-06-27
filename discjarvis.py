import discord
import time
import random
from datetime import datetime
from discord.ext import commands, tasks
from discord import activity
import asyncio
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

passwords = ["List",
            "of",
            "event",
            "passwords"]

@client.event

async def on_message(message):
    if message.author == client.user:
        return

### Advertise a Discord event for ´n´ days, once a day ###
  
    if message.content.startswith('$event'):
        vals = message.content.split(" ")
        days = int(vals[1])
        link = vals[2]
        n=1
        await message.delete()
        await message.channel.send(link)
        while n < days:
            await asyncio.sleep(86400)
            await message.channel.send(link)
            n += 1

### Delete X number of messages ###
  
    if message.content.startswith('$del'):
        vals = message.content.split(" ")
        NumberX = int(vals[1])
        await message.channel.purge(limit=NumberX+1)

### Runs the event: chooses a random password from the list and sends challenges every 6 hours with an additional random password
  
    if message.content.startswith('$challenge'):
       await message.delete()
       with open('challenges.txt','r') as l:
            content=l.read()
            sep_challenges=content.split('\n')
            integer_map=map(str, sep_challenges)
            challenges=list(integer_map)
       await message.channel.send('Welcome to the event of this week! The password will be the following:')
       await message.channel.send('**--------------------**\n ** {eventpwd} ** \n**--------------------**'.format(eventpwd=random.choice(passwords)))
       await message.channel.send('🚨 *Challenges will start in 3h!* 🚨')
       await asyncio.sleep(10800)
       desnum=int(1)
       while desnum<28:
            await message.channel.send('<@&role_id>\n{des}\n{passa}'.format(des=random.choice(challenges), passa=random.randrange(199,999,1)))
            desnum=desnum+1
            await asyncio.sleep(7200)

    if message.content.startswith('$faq'):
       await message.delete()
       with open('faq.txt', 'r') as l:
            content=l.read()
            await message.channel.send(content)

client.run('Your_BOT_Token')
