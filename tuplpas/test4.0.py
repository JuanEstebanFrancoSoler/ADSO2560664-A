canciones={"bad bunny":{"trap":"trap",
                        "safaera":"duracion 4:56",
                        "efecto":"duracion 3:34",
                        "ojitos":"duracion 4:19",
                        "moscow mule":"duracion 4:06",
                        "verano sin ti":"4:10"},
           "tego calderon":{"genero":"regueton",
                            "pa que se lo gozen":"duracion 2:22",
                            "metele sazon":"duracion 4:19",
                            "al natural":"duracion 4:18",
                            "no pasa de moda":"duracion 3:51"},
           "jose jose":{}
}

def nombre():
    for i in canciones:
        a1=input("busque al artista")
        if a1 in canciones[i]:
            print("esta en la lista",canciones[i])
        else:
            print("dato no registrado")
        for x in canciones.values():
            return x
        
def nuevo():
    nombre1=input("ingrese una cancion")
    if nombre1 in canciones:
        return "ya existe"
    else:
        canciones.update({nombre1:"ingrese canciones"}) 
    print(canciones)       

def eliminar(canciones):
    buscar=input('¿Que cancion desde elminiar?: ')
    for i in sorted(canciones.keys()): 
        if buscar==i: 
            del canciones[i] 
            print('La cancion',buscar,'fue eliminada correctamente') 
            return None 
    print('La cancion no se encuentra, ingrese el nombre primero')
    print(canciones)

def imprimir():
    print(canciones)

def agregar(canciones):
    cancion=input('Ingrese el nombre de la cancion: ')
    if cancion not in canciones: 
        print('La cancion no se encuentra, agreguela primero') 
        return canciones 
    artista=input('Ingrese el nombre del artista: ') 
    genero=input('Ingrese el genero musical: ') 
    duracion=input('Ingrese la duracion en formato xx(mm):xx(ss): ')
    


while True:
    print('1-buscar artista')
    print('2-ingresar artista')
    print('3-Eliminar artista')
    print('4-lista')
    print('5-salir')
    print('6-agreagar cancion')
    
    ctrl=int(input('Ingrese la opcion'))
    match ctrl:
        case 1:
            nombre()
        case 2:
            nuevo()
        case 3:
            eliminar(canciones)
        case 4:
            imprimir()
        case 5:
            break
        case 6:
            agregar(canciones)
 
 
           
