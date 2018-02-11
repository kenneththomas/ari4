import random
from re import compile


def chance(x):
    saychance = random.randint(1,x)
    if saychance == 1:
        chancerespond = True
        print('MemeMgr: Memed with a chance of 1/' + str(x))
    else:
        chancerespond = False
    return chancerespond

bgbscanner = compile(r'whos [a-z][a-z][a-z]$')

def memes(message):

    mememessages=[] #contains all messages that mememgr will return

    if message == 'hi':
        if chance(6):
            mememessages.append('hi')

    if message == '+':
        if chance(6):
            mememessages.append('+')

    if message == 'a':
        if chance(7):
            mememessages.append('a')

    if message == 'push me to the edge':
        mememessages.append('all my friends are dead')

    if message == 'all my friends are dead':
        mememessages.append('push me to the edge')

    if 'wendy' in message:
        if chance(5):
            mememessages.append(wendy())


    bgbmatch = bgbscanner.search(message)
    if bgbmatch:
        response = message[5] + 'ill ' + message[6] + 'arlsby'
        print('MemeMgr: Found BGB Match')
        mememessages.append(response)

    return mememessages

def wendy():
    wendypicker = messagepicker(4)
    if wendypicker == 1:
        return('i heard wendy is hot')
    if wendypicker == 2:
        return('do you think wendy is hot?')
    if wendypicker == 3:
        return('i bet wendy isn\'t even hot')
    if wendypicker == 4:
        return('do you think wendy is hot?')


def messagepicker(choices):
    return random.randint(1, choices)