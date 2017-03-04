import numpy as np 

class KB(object):

	default_model = []
	def __init__(self,current_model=default_model):
		self.model = current_model #initialize KB with a given model

	def implies(self,bool1,bool2):
		if bool1 == True and bool2 == False:
			return False
		else: 
			return True

	def iff(self,bool1,bool2):
		if bool1 == bool2:
			return True
		else:
			return False



