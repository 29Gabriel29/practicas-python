print("---- Bienvenido, procede a cargar los Usuarios para su posterior listeo ----")

# Generamos la lista 
listaPrueba = []

n = int(input("¿Cuantos ingresantes del anio 2026 desea ingresar?"))

for i in range(n):
    nombre = input("Ingresa Nombre del Ingresante")

    dni = input("Ingrese DNI del ingresante")
    if not(len(dni) == 8 and dni.isdigit()):
        print("------DNI INVALIDO-----\n")
        continue 

    edad = int(input("<<< Ingrese edad del ingresante >>>"))
    if edad >= 18:
        print("---Ingreso Correcto---")
        listaPrueba.append((nombre.upper(), dni, edad))
    else:
        print("---Ingresado denegado---\n")

print("\n ---------Lista de Ingresados 2026---------")
for pos, persona in enumerate(listaPrueba, start=1):
    fila = (pos, persona[0], persona[1], persona[2])
    # genero la tupla con posicion, nombre, dni y edad. Asigno la tupla a la variable Fila
    print(fila)   
    # imprimo en pantalla la variable fila, asi hasta terminar el bucle "for"
    
