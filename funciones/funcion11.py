def numerosperfectos(n):
    for b in range(1,1000):
        i=1
        contador=0
        while(n>i):
            if n%i==0:                                                  #juan franco ejercicio "mio"
                contador=+1
            i=+1
        if n==contador:
            print("el numero", n,"el numero es perfecto")

numerosperfectos(23)