from xml.dom import ValidationErr


distancia = float(input("qual a distancia da viagem? "))
if distancia <= 200.00:
    valor = distancia * 0.50
    print("o valor da passagem é de {}".format(valor))
else:
    valor = distancia *0.45
    print("o valor da passagem é {}.".format(valor))