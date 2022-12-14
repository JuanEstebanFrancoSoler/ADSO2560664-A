def inverso(Numero):
    Reverso=0
    while Numero>0:
        Restante=Numero%10
        Reverso=Reverso*10+Restante
        Numero//=10                                                         #nicolas juez ejercicio
    return Reverso

Numero=int(input('Ingrese el numero a revertir: '))
print(inverso(Numero))