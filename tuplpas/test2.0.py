diccio={"bad bunny" :{
        "genero" : "urbano trap",
        "cancion" : "coco",
        "duracion" : "3.30",
        "cancion1" : "soy peor",
        "duracion1" : "2:14"},

        "los cangris" :{
        "genero" :"reggueton",
        "cancion" : "donde estan las gatas",
        "duracion" : "2:00"},

        "la etnia" :{
        "genero" : "rap",
        "cancion": "nocturno",
        "duracion": "4:13"}

}

print(diccio['bad bunny']["cancion"])
print(diccio['bad bunny']["duracion"])

def nombre(nombre):
    if nombre in diccio:
        print("se encuentra en la playlist")
    else:
        print("no se encuentra en la playlist")
nombre(nombre('bad bunny'))

def nuevo(nombre2):
    if nombre in diccio:
        return'existe'
    else:
        diccio.up

###"bad bunn", "los cangris", "la etnia"]