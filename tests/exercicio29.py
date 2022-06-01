velocidade = float(input("qual era avelocidade do veiculo? "))
if velocidade >= 80.0:
    acima = velocidade-80.0
    print("você ultrapassou a velocidade permitida em {}. ".format(acima))
    multa= acima*7
    print("sua multa é de {}.".format(multa)) 