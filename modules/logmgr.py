from datetime import datetime

totalmessages=[]

def messagelogger(author,message):
    thetimes = str(datetime.now())
    totalmessages.append(author)
    print('at: ' + thetimes + ' ' + author + ': ' + message)
    return thetimes
