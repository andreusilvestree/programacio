numero = int(input("Introdueix un nombre: "))
for i in range(numero+1):
    if numero == 0 or numero%2 != 0:
        print("El número introduït no és vàlid.")
    elif i % 2 == 0 and i != 0:
        print(i)
   