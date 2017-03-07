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


    def multi_eval(self,sent,model):
        if type(sent[0])!=type(Iff): # for the collection of sentences in KB
            val = 1
            for element in sent:
                val = And([val,self.multi_eval(element,model)])
                if val == -1:
                    break
            return val
        else:
            if sent[0]!= true and sent[0] != false: #for the case where there are 3 elements in the list
                if (type(sent[1]) == str or type(sent[1]) == int) and (type(sent[2]) == str or type(sent[2]) == int):
                    return self.eval(sent,model)
                elif (type(sent[1]) == list) and (type(sent[2]) == int or type(sent[2]) == str):
                    return self.eval([sent[0],self.multi_eval(sent[1],model),sent[2]],model)
                elif (type(sent[1]) == int or type(sent[1]) == str) and (type(sent[2]) == list):
                    return self.eval([sent[0],sent[1],self.multi_eval(sent[2],model)],model)
                else: # if both arguments are non-unary sentences:
                    return self.eval([sent[0],self.multi_eval(sent[1],model),self.multi_eval(sent[2],model)],model)
            else:
                if (type(sent[1]) == str or type(sent[1]) == int):
                    return self.eval(sent,model)
                elif (type(sent[1]) == list):
                    return self.eval([sent[0],self.multi_eval(sent[1],model)],model)



    def eval(self,sentence,model):
        sentence = sentence.copy()
        for i in range(1,len(sentence)):
            if type(sentence[i]) == str:
                sentence[i] = model[sentence[i]]
        if len(sentence) == 2:
            return sentence[0]([sentence[1]])
        elif len(sentence) == 3:
            return sentence[0]([sentence[1],sentence[2]])





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
        if KB(model,kb.sentences).multi_eval(kb.sentences,model) == 1:
            if KB(model,alpha).multi_eval(alpha,model) == 1:
                return True
            else:
                return False
        else:
            return True #always implies True if the first object is False
    else: 
        P = symbols[0]
        Rest = symbols[1:]
        model_P_true = model.copy()
        model_P_false = model.copy()

        model_P_false[P] = -1
        model_P_true[P] = 1
        return (ttcheckall(kb,alpha,Rest,model_P_true) and ttcheckall(kb,alpha,Rest,model_P_false))

def pl_resolution(kb,alpha):
    '''cnf form looks like this:
        [['B','!C','A'],['!A','D','!F','E'],...] where each inner clause is a disjunction
        and all the inner clauses are in a conjunction.'''
    clauses = cnf(kb.sentences)
    for clause in cnf(negate(alpha)): 
        clauses.append(clause)
    new = []
    while True:
        for clause_i in clauses: 
            for clause_j in clauses:
            	if clause_i != clause_j:
	                resolvents = pl_resolve(clause_i,clause_j)
	                if bool(clause) != True: #if resolvent is empty
	                    return True
	                new.append(resolvents)
        if contains(new,clauses):
            return false
        for clause in new:
            clauses.append(clause)


def pl_resolve(clause_i,clause_j):
    '''inputs are two single-list disjunctions, i.e. ['B','!A','C'],['D'].
    The output will be a single list with the non-complementary literals in either list.'''
    output = []
    clause_i = clause_i.copy()
    clause_j = clause_j.copy()
    clause_i = remove_redundancies(clause_i) #just making sure no two 'B's in a list.
    clause_j = remove_redundancies(clause_j)
    for literal in clause_i:
        if contains_literal(literal_negate(literal),clause_j):
            pass
        else: 
            output.append(literal)
    return remove_redundancies(output)

def remove_redundancies(clause):
    #got the idea for this fx from http://stackoverflow.com/questions/6764909/python-how-to-remove-all-duplicate-items-from-a-list
    output = []
    for literal in clause:
        if contains_literal(literal,output):
            pass
        else:
            output.append(literal)
    return output

def contains_literal(literal,clause):
	#checks to see if a literal is within a clause
    for element in clause:
        if literal == element:
            return True
    return False

def literal_negate(literal):
	'''negates a literal. i.e. '!B' -> 'B' and 'B' -> '!B'.'''
    if literal[0] == '!':
        literal = literal[1:]
    else:
        literal = '!' + literal
    return literal

def negate(sentence):
    return [false,sentence]