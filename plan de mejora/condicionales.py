#ejercicio 1

a=21
if a >=10:
    if a <=20:
        print("a esta entre 10 y 20 ")             #ejercicio 1 pagina 109 "python 3 curso practico"
    if a >20:                                               #if anidado 
        print("a es mayor q 20")


#ejercicio 2


numero=eval(input("introduce numero:"))                         #pagina 111 "python 3 curso practico"
if numero>0:                                                        #if y else
    print("el numero es positivo o diferente a 0")
else:
    print("el numero es menor q 0")


#ejercicio 3

numero=eval(input("introduce numero:"))                         #pagina 112 "python 3 curso practico"
if numero>0:                                                        #ejemplo explicativo
    print("el numero es positivo o diferente a 0")
else:
    if numero==0:
        print("el numero es 0")
    else:
        print("el numero es negativo")


#ejercicio 4
edad=int(input("ingrese edad"))
if edad >= 18:                                              # IF + condición 
    print("Tu eres")                                         #  |        | bifurcación 1 
    print("mayor de edad")                                    #   |        v 
else:                                                          #  ELSE 
       print("Tu eres")                                         # |        | bifurcación 2 
       print("menor de edad")                                   #v        v 
print("Terminado")


#ejercicio 5

nah=int(input("ingrese el primer digito"))
n=int(input("ingrese segundo digito"))
if nah<n:                                                       #libro =aprende a pensar como un programador con python 
    print(nah,"es menor q ",n)                                      # pagina 38
elif nah>n:
    print(nah,"es mayor q ",n)
else:
    print(nah,"ambos numeros son iguales")