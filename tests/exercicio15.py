d = int(input('por quantos dias o carro foi alugado?'))
km = float(input('quantos quilometros o carro percorreu enquanto estava sendo alugado?'))
vd=(d*60)
vk=(km*0.15)
vt=vd+vk
print('o carro alugado por {} dias que equivale a R${:.2f} e rodou {} km que equivale a R${:.2f} totalizando R${}.'.format(d,vd,km,vk,vt))