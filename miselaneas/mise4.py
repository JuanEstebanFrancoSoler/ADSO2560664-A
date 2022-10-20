print("colon descubrio america?")
print("la indenpendecia de colombia fue en 1810?")
print("The Doors fue un grupo de rock Americano?")
pregunta1="colon descubrio america?"
pregunta2="la indenpendecia de colombia fue en 1810?"
pregunta3="The Doors fue un grupo de rock Americano?"

respuesta1="si"
respuesta2="si"
respuesta3="si"

entrada1=input("pregunta 1 ")
entrada2=input("respuesta 2 ")
entrada3=input("respuesta  3  ")



aciertos1=False
aciertos2=False
aciertos3=False

if (entrada1 == respuesta1):
    aciertos1=True

else:
    aciertos1:False  


if (entrada2 == respuesta2):
    aciertos2=True

else:
    aciertos2:False


if (entrada3 == respuesta3):
    aciertos3=True

else:
    aciertos3:False    


print("\n")


if(aciertos1 == True):
    print("pregunta es correcta")

else:
    print("pregunta es incorrecta") 

if(aciertos2 == True):
    print("pregunta correcta")

else:
    print("pregunta incorrecta") 

if(aciertos3==True):
    print("pregunta correcta")

else:
    print("pregunta incorrecta")
