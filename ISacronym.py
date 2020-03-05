#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:53:33 2020

@author: henskyconsulting
"""

import unittest

class isacroym:
    #: class to spot acronmyms in text
    def __init__(self,nmMax=15,nmMin=2,allcaps=True,noNums=False):
        self.nmMax = nmMax
        self.nmMin = nmMin
        self.allcaps = allcaps
        self.noNums = noNums
        
    def isshrtname(self,themention):
        
        if themention is None:
            return False
        if themention is not str:
            themention = str(themention)
        menlen = len(themention)
        if menlen < self.nmMin:
            return False
        if menlen > self.nmMax:
            return False
        
        if themention[0] in ('#','@'):
            return False
        
        if not themention.isupper():
            return False
        
        return True
        
        
    def isHash(self,themention):
        if themention is None:
            return False
        if themention == '':
            return False
        if themention[0] != '#':
            return False
        if len(themention) > self.nmMax:
            return False
        
        return True

    def isAt(self,themention):
        if themention is None:
            return False
        if themention == '':
            return False
        if themention[0] != '@':
            return False
        if len(themention) > self.nmMax:
            return False
        return True
    
class Test(unittest.TestCase):
    @unittest.skip
    def test_init(self):  
        print('\n','start_test_init','\n',40*'*')
        tstinit = isacroym()
        self.assertEqual(tstinit.nmMin,2)
        self.assertEqual(tstinit.nmMax,15)
        self.assertTrue(tstinit.allcaps)
        self.assertFalse(tstinit.noNums)
        
        print('\n','end_test_init','\n',40*'*')    
    @unittest.skip
    def test_shrtname(self):  
        print('\n','start_test_init','\n',40*'*')
        tstinit2 = isacroym()
        self.assertTrue(tstinit2.isshrtname('DOG'))
        self.assertFalse(tstinit2.isshrtname('DoG'))
        self.assertFalse(tstinit2.isshrtname('D'))
        self.assertFalse(tstinit2.isshrtname('123'))
        self.assertTrue(tstinit2.isshrtname('D23'))
        self.assertTrue(tstinit2.isshrtname('D23456789012345'))
        self.assertFalse(tstinit2.isshrtname('D234567890123456'))
        self.assertFalse(tstinit2.isshrtname('word1'))
        self.assertTrue(tstinit2.isshrtname('TOK1'))
        self.assertFalse(tstinit2.isshrtname('#TOK1'))
        self.assertFalse(tstinit2.isshrtname('@TOK1'))                                     
        self.assertFalse(tstinit2.isshrtname(None))
        self.assertFalse(tstinit2.isshrtname(1))
        self.assertFalse(tstinit2.isshrtname(''))
        self.assertFalse(tstinit2.isshrtname('.'))
        print('\n','end_test_init','\n',40*'*')    
    @unittest.skip
    def test_hashmark(self):  
        print('\n','start_hash_mark','\n',40*'*')
        tstinit2 = isacroym()
        self.assertTrue(tstinit2.isHash('#DOG'))
        self.assertFalse(tstinit2.isHash('D#OG'))
        self.assertTrue(tstinit2.isHash('#dog'))
        self.assertFalse(tstinit2.isHash('@dog'))                                
        print('\n','end_hash_mark','\n',40*'*') 
    #@unittest.skip
    def test_at_mark(self):  
        print('\n','start_at__mark','\n',40*'*')
        tstinit2 = isacroym()
        self.assertTrue(tstinit2.isAt('@DOG'))
        self.assertFalse(tstinit2.isAt('D@OG'))
        self.assertTrue(tstinit2.isAt('@dog'))
        self.assertFalse(tstinit2.isAt('#dog'))                                
        print('\n','end_at_mark','\n',40*'*')
        
if __name__ == '__main__':
    unittest.main()          