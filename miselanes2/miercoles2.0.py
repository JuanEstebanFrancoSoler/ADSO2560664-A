import random
import statistics
lista=[]
suma=0

rango=random.randint(10,25)
for i in range(rango):
    lista.append(round(random.random()*100))
    suma+=lista[i]
    promedio=suma//rango
print(" la mediana",statistics.median(lista))
print("la media es:",statistics.mean(lista))
print("promedio",promedio)
print(lista)
print("la suma de los numero es:",suma)
print(lista.__len__())