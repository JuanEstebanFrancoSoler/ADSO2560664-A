import random

lista=[0,1 ,]
tam=random.randint(10,25)
                                                                                    #juan franco ejercicio "mio"
for i in range (2,tam):
    lista.append(lista[i-1]+lista[i-2])
print(lista)
print("la longitud de la lista es",tam)


