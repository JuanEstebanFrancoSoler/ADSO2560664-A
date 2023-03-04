class Aprendiz:                                                 # se crea una clase llamada aprendiz 
    def __init__(self,nombre):                                  # se crea el constructor de la clase "aprendiz" 
                                                                #con un parametro y el self el cual identifica quer pertenece ala clase aprendiz
        self.__nombre=nombre                                    #se crea un nuevo atributo llamdao nombre "self.__nombre=nombre"
        self.__cursos=[]                                        #se crea una lista la cual es una lista vacia "self.__cursos=[]"
    def agregarCurso(self,nombreCurso):                         # se crea un metodo el cual se llama "agregar curso" , el cu8al tiene self para saber 
        self.__cursos.append(nombreCurso)                       #de que clase pertenece y un parametro llamado "nombre curso"
    def verCursos(self):                                        #un metodo el cual nos sirve para poder saber q esta guardado en "self.__curso=[]" 
        return self.__cursos                                    # retorna los cursos 

class Curso:                                                    # una nueva clase llamada "curso"
    def __init__(self,nombreCurso):                             # el constructor de la nueva clase con sus parametros y su self
        self.__nombreCurso=nombreCurso                          # se crea el atributo de nombre curso 

    def getNombreCurso(self):                                   # un metodo para poder visualizar lo q esta guardado en "self.__nombrecurso"
        return self.__nombreCurso                               #retorna lo que esta guardado 
    
ob=Aprendiz('Miguel')                                           # un objeto al cual se le asigna una clase y su parametro "miguel "
c1=Curso('Python Basico')                                       #un objeto el cual se le asigno la clase curso
c2=Curso('Python Intermedio')                                   #un objeto el cual se le asigno la clase curso
c3=Curso('Java Basico')                                         #un objeto el cual se le asigno la clase curso

ob.agregarCurso(c1)                                             #se utiliza el objeto "ob" para poder agregar los demas objetos con el metodo "agregarcurso">
ob.agregarCurso(c2)                                             #se utiliza el objeto "ob" para poder agregar los demas objetos con el metodo "agregarcurso">
ob.agregarCurso(c3)                                             #se utiliza el objeto "ob" para poder agregar los demas objetos con el metodo "agregarcurso">

for curso in ob.verCursos():                                    # se usa el "for" para poder recorrer la lista q teniamos al inicio 
    print(curso.getNombreCurso())                               #nos retorna lo que teniamos guardado en esa lista osea sus nombre 

del ob                                                          #borramos el objeto "ob"
#print(ob)
print('.....',c1.getNombreCurso())                              #podemos ver q aunq se borra al objeto "ob" se pueden seguir imprimiendo los nombres de los cursos 
