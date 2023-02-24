try:
    #print(1/1))                             #al momento de hacerlo manualmente el codigo funciona o sea me refiero al momento de utilizar raise 
    raise SyntaxError        #por q si dejamos que siga el codigo osea el print no entra por el except de synt pero si nos mande el erros de syntax

except SyntaxError as e:       #en esta liniea de codigo se le asigna una variable al error como seria en este caso la E             
    print(e)                        #aqui imprimimos la variable la cual le dimos 
    print('Cierra el parentesis')   # se le envia el mensaje el cual se puso cuando entre al excep  
    
try:
    #raise ZeroDivisionError                #en este caso es todo lo contrario , me refiero a que si lo hacemos de manera manual no entra al exception
    print(1/0)                                # pero si lo hacemos siguiendo el codigo este se mantendra funcionando 
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:                #lo mismo que la parte de arrriba pero en este caso si funciona al momento de imprimirla por su variable 
    print(zde)
    #print('prueba error')
    
    
#las variables que se les da alas exception son mas q todo para q impriman loq ya esta en relacionado con ese error 