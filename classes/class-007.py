#(+ é adição 
#(- é subtração
#(* é multiplicação
#(/ é divisão
#(** potência
#(// divisão inteira

n1=int(input('digite um numero:'))
n2=int(input('digite mais um:'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e= n1**n2
print('a soma entre eles é {}, a multiplicação é {} e a divisão é {}'.format(s,m,d))
print('a divisão inteira é {} e a potência é {}'.format(di,e))
