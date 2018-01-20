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
