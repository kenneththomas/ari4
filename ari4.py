import discord
import re
import random
import time
import maricon
from datetime import datetime
import asyncio

#import ari4 modules
import sys
sys.path.insert(0, 'modules')
import logmgr
import mememgr


#regexes
client = discord.Client()


@client.event
async def on_message(message):

#LogMgr
    thetimes = logmgr.messagelogger(str(message.author),message.content)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#MemeMgr
    memes = mememgr.memes(message.content)
    for meme in memes:
        await client.send_message(message.channel, meme)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(maricon.key)

