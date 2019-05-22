a=float(input("Valor de a: "))
b=float(input("valor de b: "))
c=float(input("valor de c: "))
if a>b and a>c:
    print("El valor de a es mayor")
else:
    if b>a and b>c:
        print("El valor de b es mayor")
    else:
        if c>a and c>b:
            print("El valor c es el mayor")
        else:
            print("son iguales")