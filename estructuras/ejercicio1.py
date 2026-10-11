"""Cree una aplicacion que lea los datos de un estudiante: nombres, apellidos, nota. calcular. 
calcular el promedio de las notas, la nota mas alta, y la nota mas baja y mostrar 
los tres estudiantes con nota mas alta"""

notas = []
nombres = []
apellidos = []

print("Registro de Estudiantes")
print("Para terminar este programa solo escriba fin en el apartado de nombres :v.")
while True:
    nombres = input("Escriba el Nombre del estudiante a evaluar: ")
    if nombres.lower() == "fin":
        break
    apellidos = input("Ingrese el apellido del estudiante a evaluar: ")
while True:
    try: 
        notas = float(input("Ingrese la nota del estudiante: "))
        if 0 <= notas <= 100:
            break
        print("La nota debe estar entre 0 y 100 para ser valida")
    except ValueError:
        print("Error. Porfavor ingrese un numero para que la nota sea valida.")

