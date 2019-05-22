a=float(input("valor de la venta: "))
if a<150000:
    print("El valor del iva con un 19% tiene un valor de: ",a*0.19)
else:
    if a>150000:
        print("el valor del iva del 19% mas el descuento del 5% es de: ",a*0.15)