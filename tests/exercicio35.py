print("-="*20)
print("ANALISADOR DE TRIANGULO")
print("-="*20)
r1 = float(input("qual o valor da primeira reta? "))
r2 = float(input("qual o valor da segunda reta? "))
r3 = float(input("qual o valor da terceira reta? "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os seguimentos acima PODEM FORMAR triangulo")
else:
    print("os seguimentos acima NÃO PODEM FORMAR triangulo")
