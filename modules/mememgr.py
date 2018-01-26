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

bgbscanner = compile(r'whos [a-z][a-z]b$')

def memes(message):

    mememessages=[] #contains all messages that mememgr will return

    if message == 'hi':
        chancerespond = chance(6)
        if chancerespond == True:
            mememessages.append('hi')

    if message == '+':
        chancerespond = chance(6)
        if chancerespond == True:
            mememessages.append('+')

    if message == 'a':
        chancerespond = chance(7)
        if chancerespond == True:
            mememessages.append('a')

    if message == 'push me to the edge':
        mememessages.append('all my friends are dead')

    if message == 'all my friends are dead':
        mememessages.append('push me to the edge')


    bgbmatch = bgbscanner.search(message)
    if bgbmatch:
        response = message[5] + 'ill ' + message[6] + 'arlsby'
        print('MemeMgr: Found BGB Match')
        mememessages.append(response)

    return mememessages
