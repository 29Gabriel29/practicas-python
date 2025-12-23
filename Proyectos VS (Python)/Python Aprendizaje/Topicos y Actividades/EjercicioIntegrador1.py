# Ejercicio que integra los contenidos de las secciones 1..6

# Un cine quiere controlar la entrada de personas 

listaDeAdmitidos = []
# lista para guardar a los admitidos

n = int(input("¿cuantas personas desean ingresar?"))
# Aca tomamos un numero de personas a verificar

for i in range(n):
    nombre = input("Ingresa tu nombre: ")

    # Validamos DNI 
    dni = (input("Ingresa tu DNI: "))
    if not (len(dni) == 8 and dni.isdigit()):
         print("DNI INVALIDO. No podes entrar :(.\n")
         continue # pasa a la siguiente persona sin evaluarla

    edad = int(input("ingresa tu edad: "))  
    # Creamos un  "para" (ciclo) que itera la cantidad de veces que sean necesarias segun la cantidad que haya ingresado el usuario

    if edad >=  18 or (edad < 18 and input("¿Vienes con algun adulto? (SI/NO) ").lower() == "si"):
          print("Acceso Permitido")
          listaDeAdmitidos.append((nombre.upper(), dni)) 
          # append solo acepta un argumento por lo que usamos doble parentesis para usar los argumentos como tupla
    else: 
         print("ACCESO DENEGADO\n")

# una vez terminado mostramos los resultados como Tuplas
print("\n--- Lista de admitidos ---")
for pos, persona in enumerate(listaDeAdmitidos, start=1):
     fila = (pos, persona[0], persona[1])
     # Generamos la tupla con posicion, nombre y DNI
     print(fila)