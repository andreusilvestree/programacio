nom = input("Escriu el nom de la persona que busques: ")
agenda = open("agenda/agenda.txt", "r")
for i in agenda.readlines():
    contacte = i.split(",")
    if contacte[0] == nom:
        print(i)
