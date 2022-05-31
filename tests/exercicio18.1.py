import math
a = float(input('qual o valor do ângulo? '))
seno = math.sin(math.radians(a))
print('o SENO do ângulo {} é {:.2f}'.format(a,seno))
cosseno = math.cos(math.radians(a))
print('o COSSENO do ângulo {} é {:.2f}.'.format(a,cosseno))
tang = math.tan(math.radians(a))
print('a tangente do ângulo {} é {:.2f}'.format(a,tang))