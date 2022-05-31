import random
a1 = str (input('qual o nome do primeiro aluno? '))
a2 = str (input('qual o nome do segundo aluno? '))
a3 = str (input('qual o nome do terceiro aluno? '))
a4 = str (input('qual o nome do quarto aluno? '))
print('o escolhido para limpar a lousa é {}'.format(random.choice([a1,a2,a3,a4])))