# import ari4 modules
import sys

import discord
import asyncio

sys.path.insert(0, 'modules')
from modules import maricon
import logmgr
import mememgr
import bannedwordsmgr
import purity
import intelligence


client = discord.Client()

@client.event
async def on_message(message):
    # LogMgr
    activity = logmgr.logmain(str(message.author),message.content)
    if activity:
        await client.send_message(message.channel, activity)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # this isnt ready
    #if message.content == '!talk':
    #    await client.send_message(message.channel, intelligence.generate())
    #    return  #if ari4 talks dont do anything else

    # MemeMgr
    memes = mememgr.memes(message.content.lower())
    for meme in memes:
        await client.send_typing(message.channel)
        asyncio.sleep(1)
        await client.send_message(message.channel, meme)

    # BannedWordsMgr
    bwm = bannedwordsmgr.bwm(message.content.lower(), str(message.author))
    if bwm[0] == 'Delete':
        await client.delete_message(message)
    elif len(bwm) > 1:
        await client.send_message(message.channel, bwm[1])

    # Purity
    prcntrl = purity.control(message.content)
    for pmsg in prcntrl:
        await client.send_message(message.channel, pmsg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(maricon.key)
