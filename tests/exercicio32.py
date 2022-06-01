ano = int(input("digite um ano "))
if (ano%400 == 0) :
    print("o ano {} é bissexto".format(ano))
else :
    print("o ano {} não é bissexto".format(ano))