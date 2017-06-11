import discord

#only admins should be able to use admin commands

#list of admins, should we use discord usernames? this can easily break but idk how else to do it
adminlist = ['breezyexcursion#9570']

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

# prevents checking the authorized user list for every message. seems less expensive
    if message.content.startswith('!admin'):
        if message.author in adminlist:
            #example admin command
            if message.content.startswith('!admin check'):
                msg ='{0.author.mention} is authorized to perform admin commands'.format(message)
                await client.send_message(message.channel, msg)
        else:
        return
