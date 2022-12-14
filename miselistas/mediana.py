import random

tam=random.randint(10,25)
vect=[round(random.random()*100)for i in range(tam)]
vect.sort()
print("lista ordenada:" , vect )
lamitad=int(tam//2)                                                             #juan franco ejercicio "mio"
if tam %2==0:
    median=(vect[lamitad-1]+vect[lamitad])//2
else:
    median=vect[lamitad]
print("la longitud de vector es" , tam)
print("mediana:" , median)