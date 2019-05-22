valor=int(input("Valor del dinero a extraer: "))
bill50=valor/50000
residuo50=valor%50000
bill20=residuo50/20000
residuo20=residuo50%20000
bill10=residuo20/10000
residuo10=residuo20%10000
bill5=residuo10/5000
residuo5=residuo10%5000
print("\nla cantidad de billetes de 50000 son: ",bill50, "\nla cantidad de billetes de 20 es: ",bill20, "\nla cantidad de billetes de 10 es: ",bill10, "\ny la cantidad de billetes de 5000 es:", bill5)
