b=input("ingrese el nombre de usuario: ")
a=int(input("contraseña a ingresar: "))
c="pepitoZanches@gmail.com"
d=2842002
f=0
if b!=c or a!=d :
    while e<1:
        a = int(input("Vuelva a poner la contraseña: :"))
        b= input("vuelva ingrese el nombre de usuario")
        f+=1
        if f>3:
            break
else:
    if b==c and a==d:
        print("bien hecho, discapacitado")

if f>3:
    print("usuario bloqueado")