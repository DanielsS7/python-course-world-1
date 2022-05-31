from typing import Optional


n= input('digite algo')
print(type(n))
print('o que você digitou é númerico?', n.isnumeric())
print('o que você digitou é alfa numerico?', n.isalnum())
print('o que você digitou é letras?',n.isalpha())
print('o que você digitou é espaço vazio? ',n.isspace)
print('o que você digitou tem letras maiusculs?',n.isupper())
print('o que você digitou esta em minuscula?',n.islower())
print('o que você digitou é a sua mãe?',n.isascii())