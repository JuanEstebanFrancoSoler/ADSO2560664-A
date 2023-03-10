from Aprendiz import *                                                              #se importa una nueva clase la cual se llama "aprediz"
from Curso import *                                                                 #lo mismo se importa una clase "curso"

nombre=input('ingrese nombre del aprendiz')                                         #se obliga al usuario a que ingrese un "nombre"
documento=int(input('ingrese documento del aprendiz'))                              #lo mismo pero con un "documento "
ficha=input('ingrese ficha del aprendiz')                                           # lo mismo pero con "ficha"

ap=Aprendiz(ficha,nombre,documento)                                                 #se crea un obejeto el cual se le asigana a la clase de aprendiz

nombreCurso=input('ingrese nombre del curso')                                       #se obliga al usuario a que ingrese el nombre de un curso "teclado"
horas=int(input('ingrese intensidad horaria del curso'))                            #lo mismo pero con las horas
c1=Curso(nombreCurso,horas)                                                         #se crea un objeto el cual se le asigna a la clase "curso"
ap.agregarCurso(c1)                                                                 #se utiliza el primer objeto y un metodo de la clase aprendiz "agregarCurso" 
                                                                                    #y se le agrega el objeto anterior que se creo
                                                                                     
with open('herencia/aprendices.txt','a') as flujo:                                  # se trata de un bloque de codigo que abre un documento
                                                                                    #el cual se llama "herencia/aprenidz" el cual se creo para poder guardar tales datos y se llama con su rama "relativa"
    
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')   #la variable cual creamos llamada "flujo" se utiliza como tubo para poder comunicar estos dos documentos "files2 y aprendiz"    
                                                                                    #ya despues de haber comunicado ambos docuemntos con el tubo "flujo" sele agrega los datos "nombre , documento y ficha"
                                                                                    #pero utilizando sus metodos de get     
#posdata= el bloque que biene de la linea 16 hasta la 19 sirve para q abra automaticamente el tubo "flujo" 
#y lo cierre automaticamente 