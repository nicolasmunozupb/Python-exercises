cont1=0
cont2=0
cont3=0
cont4=0
a=float(input("valor de la variable: "))
while cont1<a:
    cont1+=1
    if cont1<100:
        cont2+=1
    if cont1>100:
        cont3+=1
    if cont1==100:
        cont4+=1
print("los numero mayores a 100 fueron: ",cont3,"\nlos menores a 100 fueron: ",cont2," \nY los iguales fueron: ",cont4)