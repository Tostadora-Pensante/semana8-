listas = [1, 2, 3, 4, 5, 6, 0, 1, 2, 1, "hola"]
print(listas)

conjuntos = {1, 2, 13, 4, 5, 6, 0, 1, 2 , 1, "hola"}
print(conjuntos)

tuplas = (1, 2, 3, 4, 5, 6, 0, 1, 2 , 1, "hola")
print(tuplas)

diccionarios = {"estudiante" : "Kira", "Sexo": "Hombre", "nota" : "85"}
print(diccionarios)
print(diccionarios["estudiante"])
print(diccionarios["nota"])
print(diccionarios["Sexo"])
diccionarios["nota"] = 80
print(diccionarios)

nuevalista = []
listas.append(conjuntos)
nuevalista.append(listas)
nuevalista.append(conjuntos)
nuevalista.append(tuplas)
nuevalista.append(diccionarios)
print(nuevalista)

for item in nuevalista:
    print(item)

for item in nuevalista:
    print(type(nuevalista))

with open ("texto.txt", "+w", encoding= "utf8") as archivo:
    for item in nuevalista:
        archivo.write(str(item) + "\n")

with open ("texto.txt", "+a", encoding= "utf8") as trial:
   trial.write("Mouth to mouth and eye to eye, sleep where constellations sigh")