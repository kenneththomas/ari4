import discord
import re
import random
import time
import markovify
import maricon
from datetime import datetime
import asyncio

version = 'I am running on Ari 4.9!'

with open('personality.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

#regexes
m = re.compile(r'[kK][eE][kK]')
bgbscanner = re.compile(r'whos [a-z][a-z]b$')

client = discord.Client()

#Various Counters
kekcounter = []
dramacounter = []
stattracker=[]
safecounter=[]
totalmessages=[]

#configurable
BannedWords=["netorare"]
AdminList["breezyexcursion#9570"]

#For admin-only commands

def adminCheck(acrequest):
    global isAdmin
    if acrequest in AdminList:
        isAdmin = True
        print('AdminMgr: ' + acrequest + ' authorized to run admin command.')
    else:
        isAdmin = False
        print('AdminMgr: ' + acrequest + ' not authorized to run admin command.')

@client.event
async def on_message(message):

#LogMgr
    strauthor = str(message.author)
    thetimes = str(datetime.now())
    stattracker.append(message.author)
    totalmessages.append(message.author)
    safecounter.append(message.author)
    #how often message stats are generated
    if len(safecounter) >= 3000:
        for safevalue in safecounter:
            safecounter.remove(safevalue)
        totalstr = str(len(totalmessages))
        print('Statistics at ' + totalstr + ' total messages since startup ' + thetimes)
        uniquestat = set(stattracker)
        for entry in uniquestat:
            statstr = str(stattracker.count(entry))
            memstr = str(entry)
            print(memstr + ' ' + statstr)

    #this logs every message
    print('at: ' + thetimes + ' ' + strauthor + ': ' + message.content)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


    if ('retard') in message.content:
        await client.send_typing(message.channel)
        asyncio.sleep(.5)
        msg = '{0.author.mention}, please watch your language. Next time, say r*tard.'.format(message)
        await client.send_message(message.channel, msg)

    if ('white') in message.content:
        msg = 'I think you meant to say, ' + message.content.replace("white", "*whit*")
        await client.send_message(message.channel, msg)

    if ('hentai') in message.content:
        msg = 'Hentai *poisons* the brain, stop watching it!'
        await client.send_message(message.channel, msg)

    if ('joey') in message.content:
        msg = 'who?'
        await client.send_message(message.channel, msg)

    if ('hotlanta') in message.content:
        msg = 'where?'
        await client.send_message(message.channel, msg)


    if ('@ari4') in message.content:
        await client.send_typing(message.channel)
        asyncio.sleep(2)
        msg = text_model.make_short_sentence(140).format(message)
        await client.send_message(message.channel, msg)
        await client.send_typing(message.channel)
        asyncio.sleep(5)
        msg = text_model.make_short_sentence(140).format(message)
        await client.send_message(message.channel, msg)

    match = m.search(message.content)

    if match:
        kekcounter.append(message.author)
        msg = '{0.author.mention} has said a banned word '.format(message) + str(kekcounter.count(message.author)) + ' time(s). Using this word 4 times will result in an automatic ban.'
        await client.send_message(message.channel, msg)
        if kekcounter.count(message.author) == 4:
            msg = '{0.author.mention} has been banned for using a banned word 4 times.'.format(message)
            await client.ban(message.author, delete_message_days=0)
            await client.send_message(message.channel, msg)

#whos bill garlsby

    bgbmatch = bgbscanner.search(message.content)

    if bgbmatch:
        await client.send_typing(message.channel)
        msg = message.content[5] + 'ill ' + message.content[6] + 'arlsby'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!checkdrama'):
        msg = 'drama level in chat is currently: ' + str(len(dramacounter))
        await client.send_message(message.channel, msg)
        if message.author in dramacounter:
            msg = '{0.author.mention}, you currently see drama'.format(message)
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention}, you currently do not see drama'.format(message)
            await client.send_message(message.channel, msg)

    if message.content.startswith('!drama'):
        if message.author in dramacounter:
            msg = '{0.author.mention} no longer sees drama'.format(message)
            dramacounter.remove(message.author)
            await client.send_message(message.channel, msg)
            msg = 'drama counter is now: ' + str(len(dramacounter))
            await client.send_message(message.channel, msg)
        else:
            msg = '{0.author.mention} sees drama'.format(message)
            dramacounter.append(message.author)
            await client.send_message(message.channel, msg)
            msg = 'drama counter is now: ' + str(len(dramacounter))
            await client.send_message(message.channel, msg)

    if len(dramacounter) >= 10:
        await client.delete_message(message)
        msg = 'drama level in chat is currently: ' + str(len(dramacounter))
        await client.send_message(message.channel, msg)
        #In production, we don't actually use this because it's annoying
        messagepicker = random.randint(1, 4)
        if messagepicker == 1:
            msg = 'https://greatist.com/happiness/breathing-exercises-relax'
            await client.send_message(message.channel, msg)
        if messagepicker == 2:
            msg = 'http://www.beeraw.com/calm-down.html'
            await client.send_message(message.channel, msg)
        if messagepicker == 3:
            msg = 'http://i.imgur.com/2jV2Dcq.jpg'
            await client.send_message(message.channel, msg)
        if messagepicker == 4:
            msg = 'https://www.mindbodygreen.com/0-4386/A-Simple-Breathing-Exercise-to-Calm-Your-Mind-Body.html'
            await client.send_message(message.channel, msg)


    if message.content.startswith('+'):
        willitsay = random.randint(1,3)
        if willitsay == 1:
            await client.send_typing(message.channel)
            asyncio.sleep(.5)
            msg = '+'
            await client.send_message(message.channel, msg)

    if message.content.startswith('whos mans is this'):
        messagepicker = random.randint(1, 2)
        await client.send_typing(message.channel)
        asyncio.sleep(2)
        if messagepicker == 1:
            msg = 'absolutely whos mans'
            await client.send_message(message.channel, msg)
        if messagepicker == 2:
            msg = 'come collect'
            await client.send_message(message.channel, msg)

    if message.content.startswith('!nice'):
        await client.send_typing(message.channel)
        asyncio.sleep(2)
        msg = '*please be nice in chat*'
        await client.send_message(message.channel, msg)

    if message.content == 'a':
        willitsay = random.randint(1,8)
        if willitsay == 1:
            await client.send_typing(message.channel)
            asyncio.sleep(.5)
            msg = 'a'
            await client.send_message(message.channel, msg)

 #BannedWordsMgr

            # BannedWordsMgr

        if message.content == ('!banword list'):
            print(BannedWords)
            msg = BannedWords
            await client.send_message(message.channel, msg)

        for BannedWord in BannedWords:
            if BannedWord in message.content:
                asyncio.sleep(2)
                await client.delete_message(message)
                print('BannedWordsMgr: deleted message with ' + BannedWord)

        if message.content.startswith('!banword add'):
            adminCheck(strauthor)
            if isAdmin == False:
                return
            addword = message.content.split(" ")
            BannedWords.append(addword[2])
            msg = addword[2] + " added to banned words list."
            await client.send_message(message.channel, msg)
            print('BannedWordsMgr: Added ' + addword[2] + ' to banned words list.')
            print(BannedWords)

        if message.content.startswith('!banword remove'):
            adminCheck(strauthor)
            if isAdmin == False:
                return
            removeword = message.content.split(" ")
            BannedWords.remove(removeword[2])
            msg = removeword[2] + " removed from banned words list."
            await client.send_message(message.channel, msg)
            print('BannedWordsMgr: Removed ' + removeword[2] + ' from banned words list.')

            # until i can figure out how to put a regex in a list

        if message.content == ('ntr'):
            asyncio.sleep(2)
            await client.delete_message(message)
            print('BannedWordsMgr: deleted ntr message')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(maricon.key)
