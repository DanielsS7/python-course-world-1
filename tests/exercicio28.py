import random


numero = random.randrange(0,6)
adv= input("em que numero de 0 a 5 eu estou pensando?")
if numero == adv:
    print("MEUS PARABÉNS!! VOCê ACERTOU")
else:
    print("UMA LÁSTIMA MAS VOCê ERROU!")