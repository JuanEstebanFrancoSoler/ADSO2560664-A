import random
juan=random.randint(10,25)
def llenar_lista(v):
    for i in range (juan):
        v.append(round(random.random()*100))
    print(v)

def longitud(v):
    print("Cantidad de numeros",len(v))

def primo(v):
    
    a=2
    for i in range(juan):
        for i in range(juan):
            if v[i]%a!=0:
                a=a+1
            elif v[i]==a:
                print(v[i],"es primo")
            else:
                print(v[i],"no es primo")


def par(v):
    """suma=0
    par1=0"""
    for i in range(juan):
        if v[i]%2==0:
            print("es par",v[i])
            """par1=+1
            suma+=v[i]
            print("la suma es ",suma)"""


def insertar(v):
    n=int(input("ingrese numero"))
    if n in v:
        print("el numero esta en la lista")
    else:
        v.append(n)

        
