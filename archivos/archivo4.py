#crea un progama que permita guardar n cantidad de notas en un archivo, leer las notas, calcular el promedio, la nota mas alta y la nota mas baja.

notas = []

def pedirNotas():
    while True:
        try:
            nota = int(input("Dime la nota: "))
            return nota
        except ValueError:
            print("Error, Escriba un numero entero.")


def agregarNota():
    while true:
        nota = pedirNotas()
        if nota >=0 and nota <=100:
            notas.append(nota)
        

def guadarNota():
    with open("notas.txt", "a")as notas:
        for nota in notas:
            notasFile.write(nota + " \n ")
    print("Registro guardado")



def calcularpromedio():
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def calcularMayor():
    mayor = notas[0]
    for nota in notas:
        if notas > mayor:
            mayor = nota
    return mayor

def calcularMenor():
    menor = notas

agregarNota()
guadarNota()