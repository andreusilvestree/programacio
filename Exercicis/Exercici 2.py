nom = input("Llegir l'arxiu amb la taula de: ")
with open("taula-"+nom+".txt", "r") as arxiu:
    text = arxiu.read()
print(text)