# Uso del While

lista_productos = []
producto = ''



while producto.lower() != 'hecho':
    producto = input("Ingrese el nombre del prioducto: (escriba 'hecho' para terminar)")
    lista_productos.append(producto)

print("\nLista de Productos")
contador = 1

"""
indice = 0

while indice < len(lista_productos):
    print(f"{contador}. {lista_productos[indice]}")
    indice += 1
    contador += 1 

"""
# Comento el ciclo de arriba ya que usando el FOR de abajo, no lo voy a necesitar

for producto in lista_productos:
    print(f"{contador}. {producto}")
    contador += 1
