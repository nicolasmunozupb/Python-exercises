contPar=0
contImpar=0
contPositivos=0
contNegativos=0
cont8=0
contn=0
n=int(input("Numero el pimer valor deseado "))
m=int(input("Numero el segundo valor  deseado: "))
if n<m:
    while n<m+1:
        contn+=1
        if n<0:
            contNegativos+=1
        if n>0:
            contPositivos+=1
        if n%2==0:
            contPar+=1
        if n%2!=0:
            contImpar+=1
        if n%8==0:
            cont8+=1
else:
    print("El segundo  valor debe ser mayor")

print("La cantidad de pares fueron: ",contPar,"\nLa cantidad de impares fueron: ",contImpar,"\nLa cantidad de positivos: ",contPositivos,"\nLa cantida de negativos fueron: ",contNegativos,"\nLa cantidad de mutiplos de 8 son: ",cont8)


