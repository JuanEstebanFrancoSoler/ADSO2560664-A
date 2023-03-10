from Aprendiz import *                                                  #se importa otra vez las clases aprendiz y curso :D
from Curso import *



with open('herencia/aprendices.txt','r') as flujo:                     #se crea denuevo el "portal = flujo" el cual se utiliza para poder conectar ambos documentos 
    datos=flujo.read()                                                #se crea uan avariable a la cual se le asigana el "portal = Flujo" y se identifica q vamos a leer el documento el cual 
                                                                        #estamos llamando "aprendices.txt"             
    print(datos)                                                      #se imprime la variable anterior 
    #flujo.write('2560664,maria,123')
aprendices=[]                                                           # se crea una lista vacia llamada "aprendices"
with open('herencia/aprendices.txt','r') as flujo:                      #se crea de nuevo un "with" para poder interactuar el archivo q llamamos 
    for linea in flujo:                                                 #se crea un for para poder recorrer el documento "aprendices"
        #print(linea)       
        aprendices.append(linea.rsplit())                               #utilizamos la lista vacia que habiamos creado anterior mente y sele agrega el indice del for el cual es "linia "
                                                                        #se utiliza el "rsplit" para poder "borrar" el backslash el cual contenia , y como resultado nos da una lista llenas de listas 
datosxlinea=[]                                                          #se crea otra  lista vacia 
for aprendiz in aprendices:                                             #se utiliza el for para que su indice recorra la anterior lista 
    datosxlinea.append(aprendiz[0].split(','))                          #se utiliza la lista vacia "datosxlinea" y se le agrega el indice de for "aprendiz"
                                                                        #para poder llegar a separar "mejor dicho romper la lista por comas" se utiliza el [0] para saber q es la posicion
#   print(ob.getNombre())                                               #y el punto split los separa por comas

print(datosxlinea)                                                      # se imprime la lista 

listaDeObjetos=[]                                                       #se crea una nueva lista pero de objetos 
for apr in datosxlinea:                                                 #se crea un nuevo for para poder separar los datos que se rompieron 
     f=apr[0]                                                           #posicion 0 = ficha >>>>>>>>>>> se encuentra en el documento q compartimos todo el tiempo "aprendices"
     n=apr[1]                                                           #posicion 1 = nombre   >>>>>>>>>>> se encuentra en el documento q compartimos todo el tiempo "aprendices"
     d=apr[2]                                                           #posicion 2 = document  >>>>>>>>>>> se encuentra en el documento q compartimos todo el tiempo "aprendices"
     ob=Aprendiz(f,n,d)                                                 #se crea un objeto y se le asigna a la clase aprendiz y como parametros se le da los variable anteriores
     print(ob)                                                          #se imprime el objeto  
     listaDeObjetos.append(ob)                                          #se abre la lista de objetos y se le agrega el objeto "ob"

for xx in listaDeObjetos:                                               #un for para poder ver que esta guardado en esos objetos 
    print(xx.getNombre())                                               # se imprime el nombre etc 
    print(xx.getDocumento())
    print(xx.getFicha())