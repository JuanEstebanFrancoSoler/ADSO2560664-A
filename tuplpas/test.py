#valor =6.5000
trabajo = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    horas = int(input("Ingresa la cantidad de hora extras "))
    if horas in range (0, horas):
	    
    
    if  name in trabajo:
        trabajo[name] += (horas,)
    else:
        trabajo[name] = (horas,)
        
for name in sorted(trabajo.keys()):
    adding = 0
    counter = 0
    for score in trabajo[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
