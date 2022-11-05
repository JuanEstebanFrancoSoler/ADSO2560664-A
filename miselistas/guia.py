from cmath import sqrt
import random
import statistics
"""lista=[]
suma=0
ordenado=[]
cont=0
rango=random.randint(10,25)
for i in range(rango):
    lista.append(round(random.random()*100))
    suma+=lista[i]
    promedio=suma//rango
    media=suma//lista.__len__()
    cont=0
    for j in lista:
        if lista[i]==j:
            cont+=1
    if cont!=0:
        ordenado.append(cont)
    else:
        ordenado.append(0)

mayor=0
pos=0
for i in range(lista.__len__()):
    if mayor<ordenado[i]:
       mayor=ordenado[i]
print('El mayor es ',mayor)
for j in range(len(ordenado)):
    if mayor==ordenado[j]:
        print('la moda es ',lista[j])
    
print("la mediana es:",statistics.median(lista))
media=float(media)
print("la media es:",media)
print("promedio",promedio)
print("lista",lista)
print("la suma de los numero es:",suma)
print("cantidad de numero",lista.__len__())



#print("Lista : " + str(lista))"""

#mean = suma / len(lista)
#pinocho = sum((l-mean)**2 for l in lista) / len(lista)
#desviacion = sqrt(pinocho)

#print("desviacion estandar ",desviacion)"""


import random

numero=int(input("ingrese su numero:"))
if numero > 1:
    cont=0
    for i in range (2,numero):
        resto=numero%i
        if resto==0:
            cont=+1
    if cont==0:
        print("el numero es primo:", numero)
    else:
        print("no es un numero primo:", numero)
else:
    print("no es un numero primo:", numero)
