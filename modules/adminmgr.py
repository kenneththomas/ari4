AdminList=["breezyexcursion#9570"]

def adminCheck(acrequest):
    if acrequest in AdminList:
        print('AdminMgr: ' + acrequest + ' authorized to run admin command.')
        return True
    else:
        print('AdminMgr: ' + acrequest + ' not authorized to run admin command.')
        return False
