a=float(input("primer valor : "))
b=float(input("segundo valor: "))
c=float(input("tercer valor: "))
if a+b>c:
    print("la suma del primer valor con el segundo: ",a+b," es mayor que la del tercer valor: ",c)
else:
    if c>a+b:
        print("si el tercer valor : ",c," es mayo que la suma de los 2 anteriores: ",a+b)
    else:
        print("los valores son iguales")