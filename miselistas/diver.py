import random
temp=[]
for i in range(31):
    temp.append(round(random.randint(4,30)))
print(temp[:16])
print(temp[15:31])
m1=temp[:15]
m2=temp[15:31]                                                      #juan franco ejercicio "mio"
s1,s2=0,0

for i in range(16):
    s1=s1+m1[i]
    s2=s2+m2[i]

print("promedio m1", (s1/len(m1)))
print("promedio m2",(s2/len(m2)))