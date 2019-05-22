122
a= float(input("nota 1: "))
b= float(input("nota 2: "))
c= float(input("nota 3: "))
d= float(input("nota 4: "))
e= float(input("nota 5: "))
n1=a*0.15
n2=b*0.20
n3=c*0.15
n4=d*0.3
n5=e*0.2
nota= (n1+n2+n3+n4+n5)
if nota>=3 and nota<=5:
  if nota>= 4.5:
   print("felicitaciones pancho con una nota de: ", nota)
  else:
   print("aprobaste con una nota de: ", nota)
else:
  if nota<3 and nota>=2.1:
    print("reprobaste con una nota de: ", nota, " pero puedes habilitar")
  else:
    if nota>=0 and  nota<=2:
        print("fuera de la universidad")