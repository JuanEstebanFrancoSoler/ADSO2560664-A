
def multi():
    cuanto=int(input("cuantas tablas quiere:"))
    for numero in range(1,cuanto+1):
        print('\n tabla de ',numero)
        for i in range(1,10+1):
            solu=numero*i
            print(numero,"x",i,"=",solu)    

    
    
def multiplos():
    print("infinito")
    while True:
        numero=int(input("hasta cuantos numeros quiere:"))
        numero2=int(input("que numero quiere saber si es multiplo:"))
        for i in range(numero+1):
            if i%numero2==0: 
                print(i,' es multiplo de',numero2)
            else:
                print(i,' NO es multiplo de', numero2)
                
                
def condicional1():
    print("convercion si un numero es positivo o negativo ")
    numero=int(input("ingrese un numero q quiera convertir :):"))
    if numero<0:
        positivo=numero*-1
        print(positivo)
    else:
        negativo=numero*-1
        print(negativo)


def creciente():
    num1=int(input("ingrese numero 1:"))
    num2=int(input("ingrese numero 2:"))
    num3=int(input("ingrese numero 3:"))
    if num1<num2 and num2<num3:
        print(num1,num2,num3,"estan de manera creciente")
    else:
        print("digite los numero de manera creciente",num1,num2,num3)
        print("fin del mensaje")
        





while True:
    print('1-bucle 1')
    print('2-bucle 2')
    print('3-condicional 1')
    print('4-condicional 2')
    print('5-exit')
    ctrl=int(input('Ingrese la opcion:'))
    match ctrl:
        case 1:
            multi()
        case 2:
            multiplos()
        case 3:
            condicional1()
        case 4:
            creciente()
        case 5:
            break
       