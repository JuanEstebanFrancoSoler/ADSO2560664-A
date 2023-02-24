def keyboard():
    try:
        while True:
            ingrese=int(input("ingrese su edad: "))
            print("su edad es:", ingrese)
            break
    except KeyboardInterrupt:
        cerrar=input("estas seguro de cerrar el programa? (S/N)")
        if cerrar.upper()=="S":
            print("aplicacion cerrada por usuario")
    except:
        print("no has ingresado un numero vuelve a intentarlo")
    else:
        if ingrese >= 18 and ingrese <50:
            print("es mayor de edad", ingrese)
        elif ingrese< 18:
            print("es menor de edad", ingrese)
        elif ingrese >= 50  and ingrese <= 100:
            print("es de la tercera edad", ingrese)
        else:
            print("DEAD")
            
            
keyboard()