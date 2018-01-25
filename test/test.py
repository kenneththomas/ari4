import sys

# import modules
sys.path.insert(0, '../modules')
import logmgr
import mememgr
import bannedwordsmgr

import unittest


class bwmtests(unittest.TestCase):
    def test_netorare(self):
        # payload should come back with "Delete" if a banned word is used
        payload = bannedwordsmgr.bwm('netorare', 'bobby')
        self.assertEqual(payload[0], 'Delete')

    def test_adminvalidation(self):
        # non-admins should not be able to run banword admins
        # part 1 - nonadmin tries to ban word "grapefruit"
        bannedwordsmgr.bwm('!banword add grapefruit', 'bobby')
        # part 2 - user says grapefruit, message should not be deleted
        payload = bannedwordsmgr.bwm('grapefruit', 'jack')
        self.assertEqual(payload[0], 'DoNotDelete')

    def test_banwordsadd(self):
        # admin adds banword magikarp
        bannedwordsmgr.bwm('!banword add magikarp', 'breezyexcursion#9570')
        # user says magikarp, message should be deleted
        payload = bannedwordsmgr.bwm('magikarp', 'bobby')
        self.assertEqual(payload[0], 'Delete')

    def test_nword(self):
        #set some black ppl
        bannedwordsmgr.blackpeople = ['flam','tk']
        #arietty says the n word, it should be deleted
        payload = bannedwordsmgr.bwm('nigga', 'arietty')
        self.assertEqual(payload[0], 'Delete')
        #arietty gets a pass
        bannedwordsmgr.bwm('!pass give arietty', 'flam')
        #arietty says the n word and it doesnt get deleted
        payload = bannedwordsmgr.bwm('my nigga brain', 'arietty')
        self.assertEqual(payload[0], 'DoNotDelete')
        #arietty pass is revoked because that was uncalled for
        bannedwordsmgr.bwm('!pass revoke arietty', 'flam')
        #she cant say it anymore
        payload = bannedwordsmgr.bwm('my nigga brain', 'arietty')
        self.assertEqual(payload[0], 'Delete')


class memetests(unittest.TestCase):
    def test_pushemetotheedge(self):
        uzi1 = mememgr.memes('push me to the edge')
        self.assertEqual(uzi1[0],'all my friends are dead')

    def test_allmyfriendsaredead(self):
        uzi2 = mememgr.memes('all my friends are dead')
        self.assertEqual(uzi2[0],'push me to the edge')

    def test_whosbgb(self):
        who = mememgr.memes('whos bgb')
        self.assertEqual(who[0], 'bill garlsby')