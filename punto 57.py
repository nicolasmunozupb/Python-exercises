impares=0
cont=0
while cont<100:
    cont+=1
    if cont%2!=0:
        print(cont)
        impares+=1
    if impares>=10:
        break