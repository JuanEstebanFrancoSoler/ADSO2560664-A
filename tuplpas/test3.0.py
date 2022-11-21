canciones={"bad bunny":{"safaera":"duracion 4:56",
                        "efecto":"duracion 3:34",
                        "ojitos":"duracion 4:19",
                        "moscow mule":"duracion 4:06",
                        "verano sin ti":"4:10"},
           "tego calderon":{"pa que se lo gozen":"duracion 2:22",
                            "metele sazon":"duracion 4:19",
                            "al natural":"duracion 4:18",
                            "no pasa de moda":"duracion 3:51"}
}

def nombre(nombre):
    if nombre in canciones:
        print("esta en la lista")
    else:
        print("no esta en la lista ")
nombre(nombre("bad bunny"))

def nuevo(nombre1):
    if nombre in canciones:
        return "ya existe"
    else:
        canciones.update({nombre1:"ingrese canciones"})
print(nuevo("estefania"))
print(canciones)

"""def buscar(artista):
    canciones.values
    print(artista)
buscar(canciones["bad bunny"]["ojitos"])
print(canciones)"""


def eliminar(canciones):
    cancion=input("que artistas buscas")
    for e in (canciones.values()):
        if cancion==e["artista"]:
            print("el artista",cancion,"se encuentra en la lista")
            return None
    print("el artista se encuentra en la lista")

      