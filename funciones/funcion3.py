def sumDivi(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=i
    return sum                                                      #juan franco ejercicio "mio"


print(sumDivi(10))



def perfecto(num2):
    suma=sumDivi(num2)
    if num2==suma:
        return 'perfecto'
    else:
        return 'no es perfecto'

print(sumDivi(10))
print(perfecto(10))