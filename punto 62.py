n=int(input("ingrese un numero: "))
m=int(input("ingrese un numero: "))
cont=0
if m>n:
    while n<m+1:
        cont=cont+n
        n += 1

else:
    print("ingrese otros valors donde el segundo valor sea mayor")
print(cont)