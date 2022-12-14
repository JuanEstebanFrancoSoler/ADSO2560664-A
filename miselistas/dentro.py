import random
"""lista=[]
lista.append(round(random.random()*100))
tam=random.randint(2,6)
v1=[(round(random.random()*100)) for i in range(10)]
v2=[(round(random.random()*100)) for i in range(10)]
for i in range (tam):
    v1.append(round(random.random()*100))
    v1.append(round(random.random()*100))"""


lista=[(round(random.random()*100)) for i in range(10)]
print(lista)

impar=[x for x in lista if x%2!=0]
print(impar)

par=[x for x in lista if x%2==0]
print(par)

impaypar=[x if x%2!=0 else 0 for x in lista]
print(impaypar)



board=[]                                                    #juan franco ejercicio "mio"
for i in range (5):
    board.append([])
print(board)

board=[[] for i in range(3)]
print(board)
