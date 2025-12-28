tupla = ()
print(type(tupla))
# Definicion de tupla (Funciona diferente a una lista)
lista = []
lista.append("Gabriel")
lista.append("29")
lista.append(19)
lista.append("Juan")

print(lista)
miTupla = tuple(lista)
print(miTupla)
print(miTupla[1])
print(miTupla[-1])

print(miTupla[0:2])
# Generar un slice para trabajar con una particion deseada
print(miTupla[::2])
# Muestro los elementos pares (Arranca siempre desde la posicion 0)
print(miTupla.index(19))
# Busca y si encuentra te da el valor de su posicion en la tupla
