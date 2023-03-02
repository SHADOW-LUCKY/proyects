"""
2. N atletas han pasado a finales en salto triple en los juegos
olímpicos de 2022.

Diseñe un programa que pida por teclado los nombres de cada
atleta finalista y a su vez, sus marcas del salto en metros.

Informar el nombre de la atleta campeona que se quede
con la medalla de oro y si rompió récord, reportar el pago que
será de 500 millones. El récord esta en 15,50 metros.
"""
atletas=[]
height=[] 
program = True
while program==True:
    atletas.append(input('Nombre de la atleta: '))
    height.append(float(input('Altura de salto: ')))
    if input('¿Quiere continuar? [S/N] ').upper() == 'N'or None:
        program = False
        print(height.index(max(height)))
    
"""
 if input('¿Quieres continuar? [S/N] ').upper() == 'N'or None:
        program = False
if atletas == 'exit' or 'salir':
        print(max(height))
        Champion=height.index(max(height))
        print(atletas[Champion])
        break;
    
"""