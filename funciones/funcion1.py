def sumDivi(num):
    sum=0
    sum2=0
    for i in range(1,num+1):
        if num%i==0:
            sum+=i                                                          #juan franco ejercicio "mio"
    return sum
          
def amigos(x,y):
    sumx=sumDivi(x)
    sumy=sumDivi(y)
    if sumx==sumy and sumy==sumx:
        return 'son amigos'
    else:
        return 'no son amigos :('

print(amigos(220,284))