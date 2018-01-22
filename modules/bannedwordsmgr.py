import adminmgr

BannedWords = ["netorare']

BannedWordsEnabled = True
payload=['DoNotDelete']


def permission(author):
    if adminmgr.adminCheck(author) is False:
        return False


def bwadmin(message, author):
    global BannedWordsEnabled

    if message.startswith('!banword'):
        if permission(author) is False:
            return

    if message.startswith('!banword add'):
        addword = message.split(" ")
        BannedWords.append(addword[2])
        print('BannedWordsMgr: Added ' + addword[2] + ' to banned words list.')
        return BannedWords

    if message.startswith('!banword remove'):
        addword = message.split(" ")
        BannedWords.remove(addword[2])
        print('BannedWordsMgr: Added ' + addword[2] + ' to banned words list.')
        return BannedWords

    if message.startswith('!banword enable'):
        BannedWordsEnabled = True
        print('BannedWordsMgr: Enabled')

    if message.startswith('!banword disable'):
        BannedWordsEnabled = False
        print('BannedWordsMgr: Disabled')


def checkword(message):
    for BannedWord in BannedWords:
        if BannedWord in message:
            print('BannedWordsMgr: deleted message with banned phrase: ' + BannedWord)
            return True

    if message == ('ntr'):
        print('BannedWordsMgr: deleted ntr message')
        return True


nwordvariants = ['nigga', 'nigger', 'niqqa']
blackpeople = []
passpeople = []


def nwordcheck(message, author):
    for nword in nwordvariants:
        if nword in message:
            if isuserblack(author):
                return True
            else:
                return False


def isuserblack(author):
    if author in blackpeople:
        print('BannedWordsMgr: ' + author + ' is black')
        return True
    if author in passpeople:
        print('BannedWordsMgr: ' + author + ' has a pass')
        return True
    else:
        print('BannedWordsMgr: ' + author + ' is not black, deleting message')
        return False


def blackcess(message, author):
    if author in blackpeople:
        if message.startswith('!pass give'):
            giveblackcess = message.split(" ")
            print(author + ' has given ' + giveblackcess[2] + ' a pass')
            passpeople.append(giveblackcess[2])
        if message.startswith('!pass revoke'):
            removeblackcess = message.split(" ")
            print(author + ' has revoked the rights of ' + removeblackcess[2])
            passpeople.remove(removeblackcess[2])

def bwm(message, author):
    payload = ['DoNotDelete']
    bwadmin(message, author)
    #bwlist
    if message == ('!banword list'):
        payload.append('Banned Words include: ' + str(BannedWords))
    blackcess(message, author)
    msgdelete = False
    if BannedWordsEnabled is True:
        if checkword(message) is True:
            msgdelete = True
        if nwordcheck(message, author) is False:
            msgdelete = True
    if msgdelete == True:
        payload[0] = 'Delete'
    return payload

