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

print('''We're proving the claim there is no pit at [1,2] by assuming there is a pit and showing that that is impossible. The program says that it is {} that there is no pit at P12.'''.format(ar.pl_resolution(sentences2,Not_Alpha2)))