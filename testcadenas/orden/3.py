
def mayusculas():
    print("seleccione si en mayuscula o minuscula")
    palabra=str(input("ingrese una de las opciones"))
    if palabra=="mayuscula":
        print("ingrese una palabra en minuscula")
        n=str(input("ingrese una palabra: "))
        conta2=n.upper()
        print(conta2)
    else:
        print("ingrese una palabra en mayuscula")
        n=str(input("ingrese una palabra: "))
        conta2=n.lower()
        print(conta2)

mayusculas()