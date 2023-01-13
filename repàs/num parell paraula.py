paraula = input("Escriu una paraula: ")
llista = paraula.strip()
print(llista)
for i in range(len(paraula)):
    if i % 2 == 0 and i != 0:
        print(i)