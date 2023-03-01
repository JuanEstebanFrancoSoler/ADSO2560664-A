class Persona:                                      #en esta linea de code se crea la clase "persona" mejor dicho un nuevo tipo de dato
    def __init__(self,nombre):                      #se crea el constructor con el "__init__" y se utiliza el self para identificar que eso es de la clase 
                                                        #persona
        self.__nombre=nombre                        #se utiliza el self aca para saber que el primer nombre "es el primer atributo" y pertenece a la clase 
                                                        #persona
        #print('Constructor Activado')        

    def getNombre(self):                             #Esta función sirve para poder visualizar el "atributo" nombre de la clase "persona "
        return self.__nombre                            #devuelve lo que tiene guardado en atributo nombre

    def setNombre(self,nombre):                     #Esta función sirve para poder cambiar el "atributo" "nombre" de la clase persona 
        self.__nombre=nombre                        #self = para saber a que clase pertenece "persona"
                                                    #.__nombre = es el nombre del atributo     
                                                    #nombre = es el parametro 

ob=Persona('Maria')                                #para identificar que el objeto pertenece ala clase persona "y el atributo" 
print(ob.getNombre())                               # muestra lo que tiene guardado el "atributo"
ob.setNombre('Ana')                                 #para cambiar lo que tiene guardado el "atributo"
print(ob.getNombre())                                # muestra lo que tiene guardado el "atributo"
#print(type(ob))


class Aprendiz(Persona):                            #se crea una clase hija "se identifica que pertenece a la clase padre por el (persona)" 
    def __init__(self,nombre,ficha):                #se inicia el constructor de la clase hija 
        Persona.__init__(self,nombre)               #se llama el constructor de la clase padre  
        self.__ficha=ficha                          #se crea una nuevo atributo el cual pertenece a la clase hija "aprendiz"

    def getFicha(self):                             #Esta función sirve para poder visualizar el "atributo" nombre de la clase  hija "aprendiz"
        return self.__ficha                         #devuelve lo que tiene guardado en atributo nombre

app=Aprendiz('Pedro',12345)                         #un objeto al cual se le da una clase , como por ejemplo "aprendiz"
print(app.getFicha())                               #imprime lo que tiene guardado el "atributo" "ficha"
print(app.getNombre())                              #imprime lo que tiene guardado el "atributo" "nombre de la clase padre"