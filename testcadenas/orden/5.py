#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
def murci():
    texto=input('Escriba su palabra o frase: ').lower()
    codigo=['m','u','r','c','i','e','l','a','g','o'] #es una lista
    print("murcielago")
    print("0123456789")
    salida=''
    """if texto in codigo:"""
    for i in range(len(texto)):
                if texto[i] in codigo:
                    salida+=str(codigo.index(texto[i]))
                else:
                    salida+=texto[i]
                
    print(salida)
        
murci()