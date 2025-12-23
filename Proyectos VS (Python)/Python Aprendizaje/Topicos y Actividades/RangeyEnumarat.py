"""
frutas = ["Pera", "Manzana", "Banana", "Anana", "Sandia"]

for n, fruta in enumerate(frutas, start=1):
   print(n, fruta) # Estoy enumerando e imprimiendo mi lista previamente armada de frutas
"""
contador = 0
lista_frutas = []
fruta = ''

while fruta.lower() != 'terminado':
    fruta = input("Ingrese la fruta que desea cargar para el negocio: (Escriba TERMINADO cuando desee finalizar la carga)   ")
    lista_frutas.append(fruta)

print("\nLista de frutas del Local: La Buena Fruta ")
for indice, fruta in enumerate(lista_frutas, start=1):
    print(f"{contador}. {fruta}")
    contador += 1
    