def edad():
    try:                                                            #el try el cual es obligatorio para el funcionamiento de la exception
        tuedad=int(input("introduce tu edad"))                          #una variable la cual vamos a utilizar para ingresar digitos "edad"
        print(f'tu edad es  {tuedad}')                              #la F sirve para que se pueda unir "la escritura con los valores que se ganan las variables"
                                                                        #los cuales serian {tu edad}
        #print('Tu edad es ',tuedad)                                  # un print el cual se utiliza para mostrar el "digito " ingresado "edad"
    except ValueError as e:                                             #un except el cual es Valueerror, al cual se le da una variable
        print(e)                                                        #se imprime la varable dada para el exception
        print("La edad debe ser un valor numerico...")                  #le decimos al usuario que tiene q ser un valor numerico 
        edad()                                                          #volvemos a iniciar todo hasta que el usuario ingrese un valor numerico 
    
edad()                                                                  #se llama a la funcion 


#las variables que se les da alas exception son mas q todo para q impriman loq ya esta en relacionado con ese error 