

def factores(num):
    div=2
    while div<=num:
        if num%div==0:
            print(div)
            num/=div
        else:
            div+=1
num=int(input("ingrese numero"))
factores(num)


cont=1
for i in range(25):
    print(cont)
    cont=cont+i
    

"""
import random
valor=int(random.randint(1,100))
if valor%2==0:
    print("par",valor)
    for i in range(1,valor+1):
        if i%2==0:
            print("es par,",i)
else:
    print("no es par",valor)"""