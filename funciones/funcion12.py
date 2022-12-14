def contrario(n):
   
    cont=0
    while True:
        
        contrario=n*-1
        if n==0:
            print("la cantidad de numeros puestos es:",cont)                        #juan franco ejercicio "mio"
            break
        elif n>0:
            print("el numero es",n,"y el contrario es",contrario)
        else:
            print("el numero es:",n,"y su contario es:",contrario)
        cont=+1

contrario()