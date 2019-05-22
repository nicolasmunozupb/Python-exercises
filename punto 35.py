a=float(input("Valor de a: "))
b=float(input("valor de b: "))
c=float(input("valor de c: "))
if a>b and a>c:
    print("El valor de a es mayor y el valor c")
else:
    if a>c and a>b:
        print("El valor de a es el mayor y el de b es el menor")
    else:
        if b>a and b>c:
            print("El valor de b es mayor y el menor es c")
        else:
            if b>c and b>a:
                print("El mayor es b y el menor es a")
            else:
                if c>b and c>a:
                    print("El mayor es c y el valor menor es a")
                else:
                    if c>a and c>b:
                        print("El mayor valor es c y el valor menor es b")

