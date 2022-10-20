n1=int(input("ingrese primer digito:"))
n2=int(input("ingrese segundo digito: "))
n3=int(input("ingrese tercer digito: "))

if n1==n2==n3:
    print("todos los numero son iguales")

elif n1==n2:
    print("primer y segundo digito se parecen")

elif n2==n3:
    print("segundo y tercer digito se parecen")

elif n1==n3:
    print("primero y tercer digito son iguales")

else:
    print("todos son diferentes")