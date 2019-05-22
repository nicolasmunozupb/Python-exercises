pares=0
cont=0
while cont<100:
    cont+=1
    if cont%2==0:
        print(cont)
        pares+=1
    if pares>=10:
        break