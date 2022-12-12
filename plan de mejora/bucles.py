#ejercicio 1

numero=0
suma=0                                  #ejercicio pagina 126 "ejercicio explicativo"
while numero !=7:                             #python 3 curso practico 
    numero=numero+1.0                    
    suma=suma+numero
print("la suma de todos los numeros es:", suma )

#ejercicio 2

suma1=0
for i in range(10):
    if i>7:
        break
suma1=suma1+i                                   #ejercicio 2 pagina 130 "ejercicio explicativo"
print("la suma con break ha sido:" , suma1)             #python 3 curso practico
suma1=0
for i in range(10):
    suma1=suma1+i
print("la suma sin break ha sido:",suma1)


#ejercicio 3

print("Antes de la instrucción For") 
for i in range(3):                                          # Creación del bucle ##belearn libros =python
  print("  Inicio del cuerpo del bucle")                    # || Cuerpo ##ejemplo explicativo
  print("  i =",i)                                          # || 
  print("  Final del cuerpo del bucle")                     # \/ 
print("Después de la instrucción For ") 

#belearn libros =python
#ejemplo explicativo

#ejercicio 4

#Para asimilar el funcionamiento del bucle for, 
for i in range(3): 
   print(i) 				                               #ejemplo explicativo
   if i == 1:                                              #le proponemos otro ejemplo. Determine cuál será 
    print("i vale 1")                                       #la salida en pantalla producida por el código siguiente:
    print("----") 



#ejercicio 5

for i in range(0,3):
    print("i",i ,"-->j ", end="")                               #ejercicio explicativo 
    for j in range(8):                                          #belearn libros =python
        print(j,end="")
    print()
