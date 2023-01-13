numero = input("La taula del: ")
a = 1
text = ""
for i in range(10):
    resultat = int(numero) * a
    text = text+numero+"x"+str(a)+" = "+str(resultat)+"\n"
    a = a+1
arxiu = open("taula-"+numero+".txt", "w")
arxiu.write(text)

arxiu.close()