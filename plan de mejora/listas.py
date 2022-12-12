#ejercicio 1

listaA=[1,2,3]
listaB=[4,5,6]           #listas "libro aprende a programar con pyhton"
listaA+=listaB                 #pagina 49 autor=j lujan
print(listaA)


#ejercicio 2


listaA=[1,2,3]                #listas "libro aprende a programar con p
listaA.insert(0,'m')			#pagina 51 autor=j lujan
print(listaA)                   #insertar datos en una lista

#ejercicio 3

listaA=[1,2,3,2,4,5]          #listas "libro aprende a programar con python
listaA.remove(2)				#pagina 52 autor =j lujan
print(listaA)                       #remover datos de una lista


#ejercicio 4


lista=[0, 10 , 20 ,30 ,40 ,50 ,60 ,70 ,80]
for i in range(0,lista):

    print(i)
    
print(lista[0:2])
print(lista[2:-2])                                                  #ejercicio explicativo rebanadas
print(lista[3:])
print(lista[:3])


#ejercicio 5
import random
lista=[4, 15, 7]
 
for i in range(1,20,3):
    lista.append(i)
    print(lista)
    
ju=[1,2,10,8,9]
lista=ju[::-1]
print(lista)


for i in range(len(ju)-1,-1,-1):
    print(ju[i],end="-")
    
while True:
    for i in range(0,6):
        lista.append(i)
        print(lista)   
    

    
