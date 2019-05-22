a=int(input("ingresar valor a: "))
b=0
while b<a+1:
    if b%2==0:
        print(b*-1)
    else:
        if b%2!=0:
            print(b)
    b+=1