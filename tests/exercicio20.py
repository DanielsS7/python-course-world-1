import random
a1 = str (input('qual nome do primeiro aluno? '))
a2 = str (input('qual nome do segundo aluno? '))
a3 = str (input('qual o nome do terceiro aluno? '))
a4 = str (input('qul nome do ultimo aluno? '))
list = [a1,a2,a3,a4]
random.shuffle(list)
print('a ordem dos alunos é {}'.format(list))