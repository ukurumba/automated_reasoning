"""
test_langevin_dynamics
----------------------------------
Tests for `langevin_dynamics` module.
"""


import sys
import unittest
import numpy as np
from contextlib import contextmanager


import automated_reasoning.automated_reasoning as ar




class TestAutoReason(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    # def test_or(self):
    # 	self.assertTrue(ar.kb.Or(True,False))
    # 	self.assertFalse(ar.kb.Or(False,False))   
    # 	self.assertTrue(ar.kb.Or(True,True))
    # 	self.assertTrue(ar.kb.Or(False,True)) 

    # def test_and(self):
    # 	self.assertFalse(ar.kb.And(True,False))
    # 	self.assertFalse(ar.kb.And(False,False))   
    # 	self.assertTrue(ar.kb.And(True,True))
    # 	self.assertFalse(ar.kb.And(False,True)) 

    # def test_not(self):
    # 	self.assertTrue(ar.kb.Not(False))
    # 	self.assertFalse(ar.kb.Not(True))

    def test_implies(self):
    	kb = ar.KB()
    	self.assertTrue(kb.implies(False,False))
    	self.assertFalse(kb.implies(True,False))   
    	self.assertTrue(kb.implies(True,True))
    	self.assertTrue(kb.implies(False,True)) 

    def test_iff(self):
    	kb = ar.KB()
    	self.assertFalse(kb.iff(True,False))
    	self.assertTrue(kb.iff(False,False))   
    	self.assertTrue(kb.iff(True,True))
    	self.assertFalse(kb.iff(False,True)) 

        
tests = unittest.TestLoader().loadTestsFromTestCase(TestAutoReason)
unittest.TextTestRunner().run(tests)
        


