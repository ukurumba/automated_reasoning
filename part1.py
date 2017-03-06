import automated_reasoning.automated_reasoning as ar	

print('Question 1: Prove Modus Ponens works in this system')
print('----------------------------------------------------\n')
print('''Input KB: [[ar.true,['P']],[ar.implies['P','Q']]] \n
Input Model: {'P' : 0, 'Q' : 0} \n
Input Sentence: [[ar.true,['Q']]]) \n''')
sentences = [[ar.true,['P']],[ar.Implies,['P','Q']]]
model = {'P' : 0, 'Q' : 0}
kb = ar.KB(model,sentences)
alpha = [[ar.true,['Q']]]
print('If P is true and P implies Q, computer program says that Q is', ar.ttentails(kb,alpha),'\n')

print('See Python code to verify =).')

print('Question 2: The Wumpus World')
print('----------------------------------------------------\n')
print('''Input KB: [[ar.false,['P11']],[ar.iff,['b11']]] \n
Input Model: {'P' : 0, 'Q' : 0} \n
Input Sentence: [[ar.true,['Q']]]) \n''')
sentences = [[ar.true,['P']],[ar.Implies,['P','Q']]]
model = {'P' : 0, 'Q' : 0}
kb = ar.KB(model,sentences)
alpha = [[ar.true,['Q']]]
print('If P is true and P implies Q, computer program says that Q is', ar.ttentails(kb,alpha),'\n')

print('See Python code to verify =).')
