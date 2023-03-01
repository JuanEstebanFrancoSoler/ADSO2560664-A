class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre
    def setDocumento(self,documento):
        self.__documento=documento

"""ob=Persona('Maria',1323123123123)
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())

print(ob.getDocumento())
ob.setDocumento(23134324234)
print(ob.getDocumento())"""

class Aprendiz(Persona):
    def __init__(self,nombre,documento,ficha):
        Persona.__init__(self,nombre,documento)
        self.__ficha=ficha
    def getFicha(self):
        return self.__ficha
    def completo(self):
        print(app.getFicha())
        print(app.getNombre())
        print(app.getDocumento())
        return''

app=Aprendiz('Pedro',12345,2013120312)
"""print(app.getFicha())
print(app.getNombre())
print(app.getDocumento())"""
print(app.completo())