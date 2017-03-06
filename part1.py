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
if ar.ttentails(kb,alpha):
	print('If KB is true, then computer program says we can conclude there is a Pit at (1,2).')

else:
	print('''If KB is true, then computer program says that we cannot conclude there is a Pit at (1,2). \n This makes sense because if there's no breeze at (1,1) then there cannot be a pit at (!,2).''')

print('See Python code to verify =). \n')
