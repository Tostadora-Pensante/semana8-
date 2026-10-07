#leer los nombes, apellido, edad y carrera de un student
#guardarlo en un archivo llamado estudiante.txt

nombres = ("Dime tus nombres: ")
apellidos = ("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")

datos = f"Nombre: {nombres.title()}\nApellidos: {apellidos.tittle()} \nEdad: {edad}\nCarrera: {carrera.tittle()}\n"

with open("estudiante.txt", "w", endoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado satifactoriamente.")