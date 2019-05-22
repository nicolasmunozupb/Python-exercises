contpares=0
contimpares=0
a=int(input("valor deseado: "))
for i in range(0,a):
    if i%2==0:
        contpares+=1
    if i%2!=0:
        contimpares+=1
print("El promedio de pares: ",(contpares/a))
print("El promedio de imare:: ",(contimpares/a))