cont1=100000
a=int(input("poner la cantidad de kilometrsoa recorrer. "))
b=int(input("La cantidad de dias de estancias: "))
if a>=2:
    cont1=cont1+(5000*(a-1))
if a>10000:
    cont1=cont1*0.85
print("El calor de su pasaje sera: ",cont1)