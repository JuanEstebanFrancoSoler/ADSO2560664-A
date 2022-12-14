import random

pro=0
sum=0
rango=random.randint(10,25)

vect=[round(random.ramdom()*100)for i in range(rango)]
for i in range(rango):
    sum+vect[i]
print(sum)                                                                              #juan franco ejercicio "mio"
promedio=sum//rango
print("el rango de la lista es",rango)
print("el valor de la lista es",vect)
print("el promedio  es",promedio)

#n en el vecto, n tomara los valores de la lista y los va a comparar conb el promedio 
for n in vect:
    if n<promedio:
        print("el num",n, "es menor del promedio")
    elif n<promedio:
         print("el num",n, "es mayor  del promedio")
    elif n==promedio:
         print("el num",n, "es igual del promedio")
