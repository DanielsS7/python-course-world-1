from math import sqrt
co = float(input('qual o valor do cateto oposto ao angulo? '))
ca = float(input('qual o valor do cateto adjacente angulo? '))
hipotenusa = sqrt(co**2+ca**2)
print ('a hipotenusa do triangulo é {:.2f} o seno do triangulo é {:.3f} o cosseno {:.3f} e a tangente {:.3f}'.format((hipotenusa),(co/hipotenusa),(ca/hipotenusa),(co/ca)))