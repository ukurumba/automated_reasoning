"""
test_langevin_dynamics
----------------------------------
Tests for `langevin_dynamics` module.
"""


import sys
import unittest
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
    # 	self.assertTrue(ar.Or(True,False))
    # 	self.assertFalse(ar.Or(False,False))   
    # 	self.assertTrue(ar.Or(True,True))
    # 	self.assertTrue(ar.Or(False,True)) 

    # def test_and(self):
    # 	self.assertFalse(ar.And(True,False))
    # 	self.assertFalse(ar.And(False,False))   
    # 	self.assertTrue(ar.And(True,True))
    # 	self.assertFalse(ar.And(False,True)) 

    # def test_not(self):
    # 	self.assertTrue(ar.Not(False))
    # 	self.assertFalse(ar.Not(True))

    def test_booleans(self):
    	possible_cases = [[1,1],[1,0],[1,-1],[0,1],[0,0],[0,-1],[-1,1],[-1,0],[-1,-1]]
    	iff_val = [1,0,-1,0,0,0,-1,0,1]
    	implies_val = [1,0,-1,0,0,0,1,1,1]
    	and_val = [1,0,-1,0,0,-1,-1,-1,-1]
    	or_val = [1,1,1,1,0,0,1,0,-1]
    	index=0
    	for case in possible_cases:
    		self.assertEqual(iff_val[index],ar.Iff(case))
    		self.assertEqual(implies_val[index],ar.Implies(case))
    		self.assertEqual(and_val[index],ar.And(case))
    		self.assertEqual(or_val[index],ar.Or(case))
    		index+=1
    
    def test_eval_sentences(self):
    	model = {'P' : 1,'Q' : -1,'R' : 0, 'S' : 1}
    	sentences = [[ar.Implies,['P','Q']],[ar.And,['R','S']],[ar.Or,['Q','P']]]
    	sentences2 =  [[ar.Implies,['P','S']],[ar.And,['R','S']],[ar.Or,['Q','P']],[ar.false,['Q']]]
    	sentences3 = [[ar.Implies,['P','S']],[ar.And,['P','S']],[ar.Or,['Q','P']],[ar.true,['P']]]

    	kb = ar.KB(model,sentences)
    	kb2 = ar.KB(model,sentences2)
    	kb3 = ar.KB(model,sentences3)
    	self.assertEqual(kb.eval_sentences(),False)
    	self.assertEqual(kb2.eval_sentences(),True)
    	self.assertEqual(kb3.eval_sentences(),True)

    def test_tt_entails(self):
    	model = {'P' : 1,'Q' : -1,'R' : 0, 'S' : 1}
    	sentences = [[ar.Implies,['P','Q']],[ar.Implies,['Q','R']],[ar.true,['P']]]
    	kb =ar.KB(model,sentences)
    	alpha = [[ar.true,['R']]]
    	alpha2 = [[ar.true,['S']]]
    	self.assertTrue(ar.ttentails(kb,alpha))
    	self.assertFalse(ar.ttentails(kb,alpha2))




        
tests = unittest.TestLoader().loadTestsFromTestCase(TestAutoReason)
unittest.TextTestRunner().run(tests)
        


