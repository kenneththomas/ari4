import sys
#import modules
sys.path.insert(0, '../modules')
import logmgr
import mememgr
import bannedwordsmgr

#TEST 1 - Delete Banned Words
bannedwordsmgr.bwm('netorare','bobby')

#TEST 2 - Disable/Enable Function
bannedwordsmgr.bwm('!banword disable','breezyexcursion#9570')
bannedwordsmgr.bwm('netorare','bobby')
bannedwordsmgr.bwm('!banword enable','breezyexcursion#9570')
bannedwordsmgr.bwm('netorare','bobby')

#TEST 3 - List Banwords
bannedwordsmgr.bwm('!banword list','whoever')
