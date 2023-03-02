"""
Campus requiere administrar algunos datos de sus Campers
como por ejemplo, la creación, eliminación o búsqueda de los
developers, entre otros, por tal razón, ha solicitado el diseño de
un programa que cuente con el siguiente menú como panel de
control
"""



program= True 

while program == True:
    print(
    '------------------------------Menu----------------------------------\n'
    '1. CREAR GRUPO ARTEMIS:\n'
    '1.1 LISTAR CAMPERS DE ARTEMIS\n'
    '1.2 AGREGAR CAMPERS A ARTEMIS\n'
    '1.3 ELIMINAR CAMPERS DE ARTEMIS\n'
    '1.4 ORDENAR ALFABETICAMENTE EN LISTA DE ARTEMIS\n'
    '1.5 BUSCAR CAMPER EN LISTA DE ARTEMIS\n'
    '2.1 LISTAR CAMPERS DE SPUTNIK:\n'
    '2.2 AGREGAR CAMPERS A SPUTNIK\n'
    '2.3 ELIMINAR CAMPERS DE SPUTNIK\n'
    '2.4 ORDENAR ALFABETICAMENTE EN LISTA DE SPUTNIK\n'
    '2.5 BUSCAR CAMPER EN LISTA DE SPUTNIK\n'
    '3. EXIT'
    )
    opcion=float(input('Digite Opcion: '))
    if opcion == 1.0:
        artemis=[]
        print('grupo creado')
    elif opcion == 1.1:
       try:
            for element in artemis:
                print(element)
       except:
           print('Error intentelo otravez')
    elif opcion == 1.2:
        try:
            artemis.append(input('Nombre del individuo'))
        except:
            print('Error intentelo otra vez')
    elif opcion == 1.3:
        try:
            artemis.remove(input('Nombre del individuo'))
        except:
            print('Error intentelo otra vez')
    elif opcion == 1.4:
        artemis.sort()
    elif opcion == 1.5:
        try:
            print(artemis.index(input('Nombre del individuo')))
        except:
            print('Error intentelo otra vez')
    elif opcion == 2.0:
        sputnik=[]
        print('grupo creado')
    elif opcion == 2.1:
        try:
            for element in sputnik:
                print(element)
        except:
           print('Error intentelo otravez')
    elif opcion == 2.2:
        try:
            sputnik.append(input('Nombre del individuo'))
        except:
            print('Error intentelo otra vez')
    elif opcion == 2.3:
        try:
            sputnik.remove(input('Nombre del individuo'))
        except:
            print('Error intentelo otra vez')
    elif opcion == 2.4:
        sputnik.sort()
    elif opcion == 2.5:
        try:
            print(sputnik.index(input('Nombre del individuo')))
        except:
            print('Error intentelo otra vez')
    elif opcion == 3.0:
        program=False
    else:
        print('Opcion no valida')