from datetime import datetime

totalmessages=[]

def messagelogger(author,message):
    thetimes = str(datetime.now())
    totalmessages.append(author)
    print('at: ' + thetimes + ' ' + author + ': ' + message)
    return thetimes

def activity(message):
    if message == '!activity':
        return totalmessages

def logmain(author,message):
    messagelogger(author,message)
    if activity(message):
        return str.acmsg + ' messages since startup'