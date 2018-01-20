import random

def chance(x):
    saychance = random.randint(1,x)
    if saychance == 1:
        chancerespond = True
        print('MemeMgr: Memed with a chance of 1/' + str(x))
    else:
        chancerespond = False

    return chancerespond

def memes(message):


    mememessages=[] #contains all messages that mememgr will return

    if message == 'hi':
        chancerespond = chance(6)
        if chancerespond == True:
            mememessages.append('a')

    if message == '+':
        chancerespond = chance(6)
        if chancerespond == True:
            mememessages.append('+')

    if message == 'a':
        chancerespond = chance(7)
        if chancerespond == True:
            mememessages.append('a')


    return mememessages
