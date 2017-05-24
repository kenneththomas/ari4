import discord
import re
import random
import time
import markovify

with open('example.txt') as f:
    text = f.read()

text_model = markovify.Text(text)


m = re.compile(r'[k|K][e|E][k|K]')


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


    if ('retard') in message.content:
        await client.send_typing(message.channel)
        time.sleep(.5)
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

    if ('ari4') in message.content:
        await client.send_typing(message.channel)
        time.sleep(2)
        msg = text_model.make_short_sentence(140).format(message)
        await client.send_message(message.channel, msg)
        await client.send_typing(message.channel)
        time.sleep(5)
        msg = text_model.make_short_sentence(140).format(message)
        await client.send_message(message.channel, msg)

#bannedwords, refactor later

    match = m.search(message.content)

    if match:
        kekcounter.append(message.author)
        msg = '{0.author.mention} has said a banned word '.format(message) + str(kekcounter.count(message.author)) + ' times. Using this word 4 times will result in an automatic ban.'
        await client.send_message(message.channel, msg)
        if kekcounter.count(message.author) == 4:
            msg = '{0.author.mention} has been banned for using a banned word 4 times.'.format(message)
            await client.ban(message.author, delete_message_days=0)
            await client.send_message(message.channel, msg)

    if message.content.startswith('!checkdrama'):
        msg = 'drama level in chat is currently: ' + str(len(dramacounter))
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

    if ('trump') in message.content:
        willitsay = random.randint(1,8)
        if willitsay == 1:
            messagepicker = random.randint(1,4)
            if messagepicker == 1:
                msg = 'no politica'
                await client.send_message(message.channel, msg)
            if messagepicker == 2:
                msg = 'please tone down the politica'
                await client.send_message(message.channel, msg)
            if messagepicker == 3:
                msg = '3 big evil 1. racism 2. religion 3. politica'
                await client.send_message(message.channel, msg)
            if messagepicker == 4:
                msg = 'politica = enemy universume love'
                await client.send_message(message.channel, msg)

    if message.content.startswith('+'):
        willitsay = random.randint(1,3)
        if willitsay == 1:
            await client.send_typing(message.channel)
            time.sleep(.5)
            msg = '+'
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run('absolutelynot')
