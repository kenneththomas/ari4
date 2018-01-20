import adminmgr

BannedWords=["netorare"]


def bwadmin(message, user):

    if message == ('!banword list'):
        return BannedWords

    if message.startswith('!banword add'):
        isAdmin = adminmgr.adminCheck(user)
        if isAdmin == False:
            return
        addword = message.split(" ")
        BannedWords.append(addword[2])
        print('BannedWordsMgr: Added ' + addword[2] + ' to banned words list.')
        return BannedWords

    if message.startswith('!banword remove'):
        isAdmin = adminmgr.adminCheck(user)
        if isAdmin == False:
            return
        addword = message.split(" ")
        BannedWords.remove(addword[2])
        print('BannedWordsMgr: Added ' + addword[2] + ' to banned words list.')
        return BannedWords

def checkword(message):

    for BannedWord in BannedWords:
        if BannedWord in message:
            print('BannedWordsMgr: deleted message with ' + BannedWord)
            return True

    if message == ('ntr'):
        print('BannedWordsMgr: deleted ntr message')
        return True

nwordvariants = ['nigga','nigger','niqqa']
blackpeople = []
passpeople = []

def nwordcheck(message,author):
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

def blackcess(message,author):
    if author in blackpeople:
        if message.startswith('!pass give'):
            giveblackcess = message.split(" ")
            print(author + ' has given ' + giveblackcess[2] + ' a pass')
            passpeople.append(giveblackcess[2])
        if message.startswith('!pass revoke'):
            removeblackcess = message.split(" ")
            print(author + ' has revoked the rights of ' + removeblackcess[2])
            passpeople.remove(removeblackcess[2])
