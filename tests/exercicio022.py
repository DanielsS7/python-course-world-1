Nome =  str(input('Digite seu nome completo ')).strip()
print ('analisando seu nome ...')
print ('Nome completo em maiusculas é  ',Nome.upper())
print ('Seu nome em minusculas é ',Nome.lower())
print ('seu nome ao todo tem ao todo {} letras'.format(len(Nome) - Nome.count(' ')))
print ('seu primeiro nome tem {} letras'.format(Nome.find(' ')))