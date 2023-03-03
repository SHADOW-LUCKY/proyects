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
    program=input('desea continuar?[S/N]')
    if program == 'n' or program == 'N':
        if height[height.index(max(height))] >= 15.50:
                print('nuevo record', height[height.index(max(height))] )
                print('Nombre del atleta: ',atletas[height.index(max(height))], ' felicidades 500 millones pal bolsillo')
                 #referencia el nombre del atleta de la posicion del mayor salto 
                program=False

        else:
                print('salto mayor: ',height[height.index(max(height))]);
                print('Nombre del atleta: ',atletas[height.index(max(height))])    
                program=False
    else:
        program=True
"""
print('salto mayor: ',height[height.index(max(height))])
        print('Nombre del atleta:',atletas[height.index(max(height))])
"""