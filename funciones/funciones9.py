def notas(num):
    if num>11:
        return 'aprobo DIOS'
    elif num<=1:
        return 'reprobado'
    elif num<=3:                                                        #juan franco ejercicio "mio"
        return 'insuficiente'
    elif num<=5:
        return 'suficiente'
    elif num<=7:
        return 'bien'


print(notas(3))