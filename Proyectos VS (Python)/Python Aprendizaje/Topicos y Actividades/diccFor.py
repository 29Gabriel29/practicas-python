datos = {"Nombre":"Lopez", "Pais":"Bolivia", "Edad":"23"}
#Imprimo las claves del Diccionario
for valor in datos:
     print(valor)
#Imprimo los valores del diccionario
for valor in datos:
     print(datos[valor])
#Otra version para imprimir valores
for valor in datos.values():
     print(valor)
#Imprimo tanto la clave como su valor en forma de Duplas
for clave, valor in datos.items():
     print(clave, valor)
