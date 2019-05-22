a=int(input("por favor ingrese un numero menor a 100000: "))
if a>=100000:
    print("no sebes leer?, mete bien el numero con la condicion dada")
else:
   if 0<a and a<10:
       print("el numero tiene 1 digitos")
   else:
       if a>=10 and a<100:
           print("el numero es de 2 digitos")
       else:
           if a>=100 and a<1000:
               print("El numero es de 3 digitos")
           else:
               if a>=1000 and a<10000:
                   print("El numero es de 4 digitos")
               else:
                   if a>=10000 and a<100000:
                       print("El numero es de 5 digitos")