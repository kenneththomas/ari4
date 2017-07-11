import discord
import re
import random
import time

version = 'I am running on Ari 4.5 Lite!'


m = re.compile(r'[kK][eE][kK]')


client = discord.Client()

kekcounter = []
dramacounter = []

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


#bannedwords, refactor later

    match = m.search(message.content)

    if match:
        kekcounter.append(message.author)
        #We are commenting this out for now in the lite version. It may be a little much.
        #msg = '{0.author.mention} has said a banned word '.format(message) + str(kekcounter.count(message.author)) + ' time(s). Using this word 4 times will result in an automatic ban.'
        #await client.send_message(message.channel, msg)
        if kekcounter.count(message.author) == 1:
            msg = '{0.author.mention}, I *hope* you\'ll stop saying that.'.format(message)
            await client.send_message(message.channel, msg)
        if kekcounter.count(message.author) == 4:
            msg = '{0.author.mention} has been banned for using a banned word 4 times.'.format(message)
            await client.ban(message.author, delete_message_days=0)
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

    if message.content.startswith('+'):
        willitsay = random.randint(1,6)
        if willitsay == 1:
            await client.send_typing(message.channel)
            time.sleep(.5)
            msg = '+'
            await client.send_message(message.channel, msg)

    if message.content.startswith('!version'):
        await client.send_typing(message.channel)
        time.sleep(2)
        await client.send_message(message.channel, version)

    if message.content.startswith('!nice'):
        await client.send_typing(message.channel)
        time.sleep(2)
        msg = '*please be nice in chat*'
        await client.send_message(message.channel, msg)

    if message.content == 'a':
        willitsay = random.randint(1,8)
        if willitsay == 1:
            await client.send_typing(message.channel)
            time.sleep(.5)
            msg = 'a'
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('yourbotkey')
