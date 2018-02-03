# import ari4 modules
import sys

import discord

sys.path.insert(0, 'modules')
from modules import maricon
import logmgr
import mememgr
import bannedwordsmgr
import purity
# regexes
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

    # MemeMgr
    memes = mememgr.memes(message.content.lower())
    for meme in memes:
        await client.send_message(message.channel, meme)

    # BannedWordsMgr
    bwm = bannedwordsmgr.bwm(message.content.lower(), str(message.author))
    if bwm[0] == 'Delete':
        await client.delete_message(message)
    elif len(bwm) > 1:
        await client.send_message(message.channel, bwmx[1])

    # Purity
    prcntrl = purity.control(message.content)
    for pmsg in prtyx:
        await client.send_message(message.channel, pmsg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(maricon.key)
