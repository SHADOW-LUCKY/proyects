"""
3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos.
"""
program = True
while program == True:
    basickm=float(input('cual es el sueldo kilometro basico?'))
    name= input('Nombre del ciclista')
    numkmrun=float(input('cuantos kilometros ha recorrido su ciclista'))
    
