import automated_reasoning.automated_reasoning as ar	
print('\n \n')
print('Question 1: Prove Modus Ponens works in this system')
print('----------------------------------------------------\n')
print('''Input KB: [[ar.true,'P'],[ar.Implies,'P','Q']] \n
Input Model: {'P' : 0, 'Q' : 0} \n
Input Sentence: [ar.true,'Q'] \n''')
sentences = [[ar.true,'P'],[ar.Implies,'P','Q']]
model = {'P' : 0, 'Q' : 0}
kb = ar.KB(model,sentences)
alpha = [ar.true,'Q']
print('If P is true and P implies Q, computer program says that Q is', ar.ttentails(kb,alpha),'\n')

print('See Python code to verify =). \n')

print('Question 2: The Wumpus World')
print('----------------------------------------------------\n')
print('''Input KB: [[ar.false,'P11'],[ar.Iff,'B11',[ar.Or,'P12','P21']], \n [ar.Iff,'B21',[ar.Or,'P11',[ar.Or,'P22','P31']]],[ar.false,'B11'],[ar.true,'B21']] \n
Input Model: {'P11' : 0,'B11' : 0, 'B21' : 0, 'P22' : 0, 'P31' : 0} \n
Input Sentence: [ar.true,'P12'] \n''')
sentences = [[ar.false,'P11'],[ar.Iff,'B11',[ar.Or,'P12','P21']],[ar.Iff,'B21',[ar.Or,'P11',[ar.Or,'P22','P31']]],[ar.false,'B11'],[ar.true,'B21']]
model = {'P11' : 0,'B11' : 0, 'B21' : 0, 'P22' : 0, 'P31' : 0, 'P12' : 0, 'P21' : 0}
kb = ar.KB(model,sentences)
alpha = [ar.true,'P12']
alpha2 = [ar.false,'P12']
if ar.ttentails(kb,alpha):
	print('If KB is true, then computer program says we can conclude there is a Pit at (1,2).')

elif ar.ttentails(kb,alpha2):
	print('''If KB is true, then computer program says that we can conclude there is no Pit at (1,2). \n This makes sense because if there's no breeze at (1,1) then there cannot be a pit at (!,2).''')

print('See Python code to verify =). \n')

print('Question 3: The Horn Clauses')
print('----------------------------------------------------\n')
print(' Although this solver does not take specific advantage of Horn clauses, it should be able to compute the overall veracity via model-checking. \n')
print('There are 32 possible worlds: \n')
models = []
truth_vals = [-1,1]
for i in truth_vals:
	for j in truth_vals:
		for k in truth_vals:
			for l  in truth_vals:
				for m in truth_vals:
					model = {'Mythical' : i,'Mortal' : j, 'Mammal' : k, 'Horned' : l, 'Magical' : m}
					print(model)
					models.append(model)
sentences = [[ar.Implies,'Mythical',[ar.false,'Mortal']],[ar.Implies,[ar.false,'Mythical'],[ar.And,'Mortal','Mammal']],[ar.Implies,[ar.Or,'Mammal',[ar.false,'Mortal']],'Horned'],[ar.Implies,'Horned','Magical']]


print('\n I add the sentences of a), b), and c) to the KB (i.e. add [ar.true,Mythical]) and check whether this set of sentences can exist in any possible world. The results are below: \n')
kb = ar.KB(model,sentences)
alpha = [ar.true,'Mythical']
alpha2 = [ar.false,'Mythical']
alpha3 = [ar.true,'Magical']
alpha4 = [ar.false,'Magical']
alpha5 = [ar.true,'Horned']
alpha6 = [ar.false,'Horned']
test_sentences = [alpha,alpha2,alpha3,alpha4,alpha5,alpha6]
for i in test_sentences:
	sentences.append(i)
	for element in models:
		kb = ar.KB(element,sentences)
		if kb.multi_eval(sentences,element) == 1:
			print('There is a possible world for sentence: {} in model: {}'.format(i,element))
			break
	sentences.pop()

print(''' \n Thus we conclude that: \n
a) No conclusion can be made about whether the unicorn is mythical. \n
b) There is no world where the unicorn is not magical. Thus the unicorn is magical. \n
c) There is no world where the unicorn is not horned. Thus the unicorn is horned. \n \n ''')