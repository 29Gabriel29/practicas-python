colores = ['azul', 'rojo', 'amarillo', 'cyan']

print(colores[2])
print(colores[3])
print(colores[0])
print(colores[1])

colores.append('negro')
#metodo append sirve para agregar
print(colores)

colores.remove('azul')
#metodo para remover color
print(colores)

colores[0] = 'Rojo'
# uso el indice y realizo una modificacion en una posicion deseada
print(colores)

print('Rojo' in colores)