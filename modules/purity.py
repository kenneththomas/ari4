import asyncio
repeatercache=[]

#quickly purify chat by spamming the same message
def repeater(message):
    global repeatercache
    if message not in repeatercache:
        #reset repeatercache if the message is not the same as the last
        repeatercache=[]
        repeatercache.append(message)
    if message in repeatercache:
        repeatercache.append(message)
        if len(repeatercache) > 4:
            repeatercache=[]
            return True

def control(message):
    payload=[]
    if repeater(message):
        payload.append('hi')
    return payload



