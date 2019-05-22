a=float(input("numero a evaluar:"))
if a>0 and a%2==0:
    print("El numero: ", a , "es par positivo")
else:
    if a<0 and a%2==0:
        print("El numero: " ,a, "es par negativo")
    else:
        if a>0 and a%2!=0:
            print("el numero: ",a,"es impar positivo")
        else:
            if a<0 and a%2!=0:
                print("El numero: ",a,"es impar negativo")
            else:
                print("El  numero es 0")