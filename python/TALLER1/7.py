"""
7. Cuál es la diferencia entre un condicional simple y un
condicional compuesto?

R/en la simples si la condicion se cumple se hace una accion y nada mas

R/en el compuesto depende de la condicion se cumple  una accion u otra
"""
#simple
sueldo=int(input("Ingrese cual es su sueldo:"))
if sueldo>3000:
    print("Esta persona debe abonar impuestos")


#compuesto
num1=int(input("Ingrese primer valor:"))
num2=int(input("ingrese segundo valor:"))
print("El valor mayor es")
if num1>num2:
    print(num1)
else:
    print(num2)