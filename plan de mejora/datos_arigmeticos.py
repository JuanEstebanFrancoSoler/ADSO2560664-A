#ejercicio 1 

a=5                                         #ejercicio 1 ejemplo de explicacion pagina 102 "python3 ,curso practico"
b=a>2
print(b)
print(not b)
c=10
print(a>2 and c>7)
print(a>2 and c>12)
print(a>10 or c>12)
print(a>4 or c>12)


#ejercicio 2 


a1="hola"
b1=12.34
c1=True
d1=21                                                 #pagina 102
print(a1=="hola"and b1>10) and c1                     #podemos hacer expreciones todo lo complejas q queramos , anidandolas mediantes parentesis
print((a1=="hola" and b1 >10)and c1)or(d1<15)
print((a1=="hola" and b1 <10)and c1)or(d1<15)
print((a1=="hola" and b1 <10)and c1)or(d1>15)


#ejercicio 3
Precio = 18  # precio sin IVA                        #gestion de datos ejemplo explicativo
Precio = Precio * (1+19) 				                    #belearn =libro python
Suma =+ Precio 
print( Precio, Precio/(1+19), Suma) 

#ejercicio 4

t = 18 
t = t * (1+1000) 						                #ejemplo explicativo
p =+ t 								                    ##belearn =libro python
print( t / (1+t) , t , p) 


#ejercicio 5

a="123"
b=int(a)                                                #libro=aprende a programar proyectos ludicos "seccion tipos de variables part3"
print(b+1)
print(type(b))