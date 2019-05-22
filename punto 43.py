cont=0
cont1=0
cont2=0

for i in range(1,4):
    if i==1:
        a=float(input("Ingrese un numero: "))
        cont=a
    if i==2:
      b=float(input("ingrese un numero"))
      cont1=b
    if i==3:
        c=float(input("ingrese un numero: "))
        cont2=c

if cont<cont1<cont2:
    print("los numeros estan acendiendo")
else:
    if cont>cont1>cont2:
        print("los numero decienden ")
    else:
        print(" no se puede determinar")