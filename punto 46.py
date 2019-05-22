a=float(input("digite numero: "))
b=float(input("digite numero: "))
c=float(input("digite numero: "))
if (a!=b and a!=c) and (b!=a and b!=c) and (c!=a and c!=b):
    print("son diferents")
else:
    if a==b or b==a:
                print("hay dos valores igaules los cuales son: ",a,b)
    else:
        if a==c or c==a:
             print("hay 2 valores iguales los cauels son: ",a,c)
        else:
            if b==c or c==b:
                 print("hay 2 numeros iguales los cuales son: ",b,c)
