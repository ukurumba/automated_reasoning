import automated_reasoning.automated_reasoning as ar

print('\n \n')
print('Question 1: Prove Modus Ponens works in this system')
print('----------------------------------------------------\n')
print('''Input KB: [['P'],['!P','Q']] \n
Alpha: [['Q']] \n
Not Alpha: [['!Q']] \n''')
sentences = [['P'],['!P','Q']]
Alpha =  [['Q']] 
Not_Alpha =  [['!Q']]
print('If P is true and P implies Q, computer program says that Q is', ar.pl_resolution(sentences,Not_Alpha),'\n')

print('Question 2: The Wumpus World')
print('----------------------------------------------------\n')
print('''Input KB: [['!B11'],['B21'],['!P11'],['!B12','P11','P22','P31'],['!B11','P12','P21'],
	['!P12','B11'],['!P21','B11'],['!P11','B12',],['!P22','B12'],['!P31','B12']] \n
Alpha: [['!P12']] \n
Not Alpha: [['P12']] \n''')

sentences2 = [['!B11'],['B21'],['!P11'],['!B12','P11','P22','P31'],['!B11','P12','P21'],['!P12','B11'],['!P21','B11'],['!P11','B12',],['!P22','B12'],['!P31','B12']]
Alpha2 = [['!P12']]
Not_Alpha2 = [['P12']]

print('''We're proving the claim there is no pit at [1,2] by assuming there is a pit and showing that that is impossible. The program says that it is {} that there is no pit at P12. \n'''.format(ar.pl_resolution(sentences2,Not_Alpha2)))

print('Question 3: The Horn Clauses')
print('----------------------------------------------------\n')

print('''For this question we start with the CNF form of the knowledge base from part1: \n
	sentences = [['!Myth','!Mort'],['Myth','Mort'],['Myth','Mamm'],['Mort','Horn'],['!Mamm','Horn'],['!Horn','Mag']] \n
	Then we apply our theorems we wish to prove: \n''')

sentences3 = [['!Myth','!Mort'],['Myth','Mort'],['Myth','Mamm'],['Mort','Horn'],['!Mamm','Horn'],['!Horn','Mag']] 
alpha_a = [['Myth']]
alpha_b = [['Mag']]
alpha_c = [['Horn']]

not_alpha_a = [['!Myth']]
not_alpha_b = [['!Mag']]
not_alpha_c = [['!Horn']]

alphas = [alpha_a,alpha_b,alpha_c]
not_alphas = [not_alpha_a,not_alpha_b,not_alpha_c]

print('Please be patient, this code takes a while to run. If it does not run within a few minutes it is probably erroring. Apologies for the delay. \n ')

for i in range(0,3):
	print('We wish to prove {} so we add {} to the knowledge base. This evaluates to: {}.'.format(alphas[i],not_alphas[i],ar.pl_resolution(sentences3,not_alphas[i])))


print('''\n Thus we conclude:
a) We cannot prove whether the unicorn is mythical or not. \n
b) We can prove and do prove that the unicorn is magical. \n 
c) We can prove and do prove that the unicorn is horned. \n ''')