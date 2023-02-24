def try_syntax(numerator, denominator):
    try:                                                            #el try el cual es obligatorio para el funcionamiento de la exception
        print(f'In the try block: {numerator}/{denominator}')      #la F sirve para que se pueda unir "la escritura con los valores que se ganan las variables"
        print(numerator/denominator)                                 #los cuales serian {numerator}/{denominator}
        result = numerator / denominator                             #aqui el resultado de la operacion se guarda en otra variable llamda result 
    except ZeroDivisionError as zde:                                  #se le asigna una variable a la exception "ZeroDivisionError"
        print(zde)                                                          #se imprime la vraiable 
    else:                                                            # este else funciona tipo como para seguir el programa en tal caso que no se encuentre 
                                                                        #el error "ZeroDivisionError"                   
        print('The result is:', result )                                #en este linea sirve para imprimir el resultado de la operacion "utilizando su variable"
        return result                                                   #un return el cual devuelve la variable "result" 
    finally:                                                          # en esta es como la clausura del code el cual no siempre se imprimira aunque se encuentre un error   
        print('Exiting')                                                #imprime  una salida del code 
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 20))                                              #se llama la funcion y se utiliza el print para que el return de arriba se vea 



#las variables que se les da alas exception son mas q todo para q impriman loq ya esta en relacionado con ese error 