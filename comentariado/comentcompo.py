class Curso:                                            # se crea una nueva clase llamada "curso"
    def __init__(self,titulo):                          # el constructor de la nueva clase "curso" con sus parametros y el self 
        self.__titulo=titulo                            # se crea un nuevo atributo llamado "self.__titulo"

    def getTitulo(self):                                # se crea un metodo nuevo llamado "getTitulo" con su self
        return self.__titulo                            # nos retorna lo que teniamos guardado en "self.__titulo"

class Aprendiz:                                         #nueva clase llamada "Aprendiz"
    def __init__(self,nombre):                          #el constructor de la nueva clase llamada "Aprendiz" con un parametro
        self.__nombre=nombre                            #nuevo atributo llamado "self.__nombre= nombre"
        self.__cursos=[]                                # se crea un nuevo atrinuto el cual tiene una lista vacia "self.__cursos=[]"

    def agregarCurso(self,nombreCursito):               #se crea un nuevo metodo el cual se va a llamar "agregarcurso" con un nuevo parametro
        cursito=Curso(nombreCursito)                    #se crea un obejeto el cual se le esta asignando ala clase "CURSO" el cual contiene el parametro de la clase "APRENDIZ"
        self.__cursos.append(cursito)                   #se utiliza el atributo el cual tenia una lista vacia "self.__cursos=[]" y se le agrega cursito el cual es el objeto recien creado 

    def getCursos(self):                                # se crea un nuevo metodo 
        return self.__cursos                            # retorna la lista "self.__cursos=[]"
    
ap=Aprendiz('Sofia')                                    #un objeto el cual se le asigno a la clase "aprendiz"
ap.agregarCurso('Python Basico')                        #se utiliza el objeto para poder y se utiliza el metodo "agregarcurso" "python basico"
ap.agregarCurso('Python Intermedio')                    #se utiliza el objeto para poder y se utiliza el metodo "agregarcurso" "python basico"

for c in ap.getCursos():                                #se usa un "for" para poder recorrer la lista 
    print(c.getTitulo())                                #nos retorna los valores de la lista utilizando el metodo "getcurso"

del ap                                                  #se usa para borra el objeto "AP"