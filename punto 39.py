a = float(input("numero a:  "))
b = float(input("numero b: "))
c = float(input("numero c: "))
d = (((b ** 2) - (4 * a * c)) ** (1 / 2))
x1 = (((-1 * b) - (d ** (1 / 2)) / (2 * a)))
x2 = (((-1 * b) + (d ** (1 / 2)) / (2 * a)))
if d > 0:
    print("la parte negativa es: ", x1, "y la parte postiva es: ", x2)
else:
    if d == 0:
        print("el valor x1 que es: ", (-d / 2 * a), "es igual al valor x2 que es: ", (-d / 2 * a))
    else:
        if d < 0:
            print("no existe solucion en los numeros reales")



