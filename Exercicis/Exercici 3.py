any = input("Introdueix l'any: ")
with open("PIB-Espanya.txt", "r") as arxiu:
    for i in arxiu.readlines():
        any2 = i.split()
        if any2[0] == any:
            print(any2[1])

