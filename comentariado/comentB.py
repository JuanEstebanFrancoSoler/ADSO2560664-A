values = (1, 2)                       #aqui se le da el valor a una variable, cual valor seria el de un tupla "1,0"
#x,y=10,12                          
#print(divmod(10,3))
try:                                        #el try el cual es obligatorio para el funcionamiento de la exception
                                                #divmod sirve para hacer una division     
    q, r = divmod(*values)                   #aqui hacemos de que dos variables tomen el valor el cual se le dio en values 
    #print('valor de q=',q)                         #el cual seria q= 1 y r =0 pero estos valores se les dan por el * 
                                                    # en values ya q este divide los valores de la tupla 
    print(f'q={q}')                                 #la F sirve para que se pueda unir "la escritura con los valores que se ganan las variables"
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:         #en esta linea lo q se hace es el except lo solo pertenezca a una excepcion si no a varias 
    print(type(e), e)                                  # el type sirve para saber el tipo de fallo el cual ingreso  
    
    
#las variables que se les da alas exception son mas q todo para q impriman loq ya esta en relacionado con ese error 