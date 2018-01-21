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
    memes = mememgr.memes(message.content)
    for meme in memes:
        await client.send_message(message.channel, meme)

    who = mememgr.whosbgb(message.content.lower())

    if who:
        await client.send_message(message.channel, who)

    # BannedWordsMgr

    bwadmin = bannedwordsmgr.bwadmin(message.content, str(message.author))
    if bwadmin:
        await client.send_message(message.channel, bwadmin)

    bwcheck = bannedwordsmgr.checkword(message.content.lower())

    if bwcheck:
        if bwadmin:  # it looks stupid if you run an admin and then it deletes it so never delete any bwadmin messages
            return
        asyncio.sleep(2)
        await client.delete_message(message)

    haspass = bannedwordsmgr.nwordcheck(message.content.lower(), str(message.author))

    if haspass == False:
        await client.delete_message(message)

    bannedwordsmgr.blackcess(message.content, str(message.author))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(maricon.key)
