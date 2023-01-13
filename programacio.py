import random
a = random.randint(0,1000)
Arxiu = open("arxiu.txt", "w")
for i in range(1000):
    if a == i:
        Arxiu.write("TORO\n")
    else: 
        Arxiu.write("VACA\n")
Arxiu.close()

ArxiuR = open("arxiu.txt", "r")
b=0
primeralinia = ArxiuR.readlines(1)
segonalinia = ArxiuR.readlines(2)
terceralinia = ArxiuR.readlines(3)
if primeralinia == segonalinia:
    aux = primeralinia
else:
    aux = terceralinia
ArxiuR.readlines(1)
for linia in ArxiuR:
    b=b+1
    if linia != aux[0]:
        print("La paraula es troba a la linia",b)
