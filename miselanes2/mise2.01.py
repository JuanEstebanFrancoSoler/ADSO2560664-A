valor=0
for i in range(100,1000):
    valor=i
    u=i%10
    i=i//10
    d=i%10
    i=i//10
    c=i%10
    u**=3
    d**=3
    c**=3
    suma=u+d+c
    if suma==valor:
        print("el valor es:",valor)
