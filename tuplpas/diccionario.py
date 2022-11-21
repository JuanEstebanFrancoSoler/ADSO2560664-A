test={
    "nombre":"juan",
    "apellido":"soler",
}

print(test["nombre"])

#diccionario

dic={"gato":"chat",
    "perro":"chien",
    "caballo":"cheval"
}

#metodo get

print(dic.get("gato"))
print(dic["gato"])

#eliminar

del dic["perro"]
print(dic)

#update

dic.update({"pollo":"chiken"})
dic["pato"]="duck"
print(dic)

#metodo popitem

dic.popitem()
print(dic)

#metodo items

"""for esp, fr in dic.items():
    print(esp,"->"fr)"""


#metodo values

for x in dic.values():
    print(x)

for i in dic.keys():
    print(i)

    # generrar un dicionario de canciones 
    #anexar artista
    #  
    # buscar artista
    # buscar cancion
    # eliminar artista
    # ordenar alfabeticamente
    # el que mas canciones
    # el que tiene la cancion mas larga
    # el que tiene la cancion mas corta)