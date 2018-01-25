import discord
import maricon
import asyncio

# import ari4 modules
import sys
sys.path.insert(0, 'modules')
import logmgr
import mememgr
import bannedwordsmgr

# regexes
client = discord.Client()

@client.event
async def on_message(message):
    # LogMgr
    thetimes = logmgr.messagelogger(str(message.author), message.content)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # MemeMgr
    memes = mememgr.memes(message.content.lower())
    for meme in memes:
        await client.send_message(message.channel, meme)

    # BannedWordsMgr
    bwm = bannedwordsmgr.bwm(message.content, str(message.author))
    if bwm[0] == 'Delete':
        await client.delete_message(message)
    elif len(bwm) > 1:
        for bwmx in bwm:
            await client.send_message(message.channel, bwmx)

    # Purity
    purity = purity.control(message)
    for pmsg in purity:
        await client.send_message(message.channel, pmsg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(maricon.key)
