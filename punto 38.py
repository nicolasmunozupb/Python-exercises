a=int(input("año a analizar: "))
if a%4==0 or (a%100!=0 and a%400==0):
    print("El año es biciesto")
else:
    print("no  es año biciesto")