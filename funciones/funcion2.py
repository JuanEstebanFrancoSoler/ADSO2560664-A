import random

def sumlista(lista):
    sum=0
    for i in lista:                                                     #juan franco ejercicio "mio"
        sum+=i
    return sum

def llenarlista(lista):
    tam=round(random.randint(5,15))
    for i in range (tam):
        lista.append(round(random.randrange(100)))
        return lista
lista=[]
print(sumlista(lista))

lista==llenarlista(lista)
print(lista)
