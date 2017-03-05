import numpy as np 

def Implies(inputvals):
	P,Q = inputvals
	if P == 1 and Q == -1:
		return -1
	elif P == 1 and Q == 0:
		return 0
	elif P == 1 and Q == 1:
		return 1
	elif P == 0:
		return 0
	elif P == -1:
		return 1

def Iff(inputvals):
	P,Q=inputvals
	if P == 1 and Q == 1:
		return 1
	elif P == -1 and Q == -1:
		return 1
	elif P == 0 or Q == 0:
		return 0
	else: 
		return -1

def And(inputvals):
	P,Q=inputvals
	if P == 1 and Q == 1:
		return 1
	elif P == -1 or Q == -1:
		return -1
	elif P == 0 or Q == 0:
		return 0
	else:
		return -1

def Or(inputvals):
	P,Q=inputvals
	if P == 1 or Q == 1:
		return 1

	elif P == -1 and Q == -1:
		return -1

	else:
		return 0

def true(P): #a unary sentence that says P is true. Thus if P=False is entered, this sentence returns False.
	return P[0]

def false(P):
	return -1 * P[0]





class KB(object):

	default_model = []

	def __init__(self,current_model={},init_sentences=[]):
		self.model = current_model #initialize KB with a given model
		self.sentences = init_sentences 

	def add_sentence(self,sentence):
		sentences.append(sentence)

	def eval_sentences(self):
		'''This method determines whether or not the specific situation (conceptualized as a knwoledge badse with a model and set of sentences) COULD be true.
		i.e. if it is possible for the given set of sentences to be true under the current model the function returns True.''' 
		eval_vals = [1] #so that first evaluation just returns truth-value of first sentence in KB
		index=0
		for each_sentence in self.sentences:
			index+=1
			eval_vals.append(each_sentence[0]([self.model[i] for i in each_sentence[1]]))
			eval_vals = [And(eval_vals)] #checking to make sure every sentence in KB evaluates to true 
			if eval_vals[0] == -1:
				break
		if eval_vals[0] == -1:
			return False
		else: 
			return True 

def make_0(model):
	for i in model:
		model[i] = 0
	return model

def ttentails(kb,alpha):
	'''This function tests whether or not the sentence alpha is entailed by the sentences in kb.'''
	symbols = list(kb.model.keys()) # returns a list of all model parameters. 
	return ttcheckall(kb,alpha,symbols,make_0(kb.model)) #make_0(model) returns a model where every variable is "unknown" i.e. 0 in value

def ttcheckall(kb,alpha,symbols,model):
	if not symbols: #if symbols is empty
		if KB(model,kb.sentences).eval_sentences():
			return KB(model,alpha).eval_sentences()
		else:
			return True #always implies True if the first object is False
	else: 
		P = symbols[0]
		Rest = symbols[1:]
		model_P_true = model_P_false = model
		model_P_true[P] = 1
		model_P_false[P] = -1
		return ttcheckall(kb,alpha,Rest,model_P_true) and ttcheckall(kb,alpha,Rest,model_P_false)




















