"""
for n in range(11):
    if n == 5:
        break
    print(n)
"""

#Uso del brake

"""
for n in range(11):
    if n == 6:
        continue
    print(n)
"""

#Uso del Continue

lista = []
while True:
    producto = input("Ingrese el producto que desea cargar al sistema:   (Colocar TERMINADO cuando se filnalice la carga) ")
    if producto.lower() == "terminado":
        break
    lista.append(producto)

print("\n ----------Lista de Productos---------")
for i, valor in enumerate(lista, start=1):
    print(f"{i}. {valor}")
    