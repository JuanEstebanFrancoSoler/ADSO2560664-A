numero=int(input("ingrese el digito q quiera: "))

if numero>=1 and numero<=9:
    print("solo tiene un digito")

elif numero>=10 and numero<=99:
    print("solo tiene dos digitos")

elif numero>=100 and numero<=999:
    print("solo tiene 3 digitos")

elif numero>=1.000 and numero<=9.999:
    print("solo tiene 4 digitos") 

else:
    numero>=10.00
    print("no se puede hacer el calculo ")   