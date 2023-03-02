"""
9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
telefono =int (input("ingrese su telefono: "))
edad = int(input("Ingrese su edad: "))
año = int(input("año en el que entro a la empresa: "))
print(f"Su expediente Nombre: {nombre} apellido: {apellido} año de ingreso: {año} telefono: {telefono} edad: {edad}")