#except

def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
    except ValueError:
        print("el valor no concuerda ")
        
var=int(input("ingrese numero   "))
divisores(var)
print('El programa continua en esta linea')


#while
def divisores2():
    while True:
        try:
            num=int(input('ingrese numero'))
            for i in range(num+1):
                if num%i==0:
                    print(i,'es divisor')
                break
        except ZeroDivisionError:
            print('indeterminacion')
        except TypeError:
            print(type(num),'Tipo de dato no soportado')
        except ValueError:
            print("el valor no concuerda ")
            
divisores2()
print('El programa continua en esta linea')