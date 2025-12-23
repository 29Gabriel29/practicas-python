import random 

print("Bienvenido al juego de Adivinar el numero")

num_sec = random.randint(1, 100)
intentos_maximos = 10
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    intento = int(input("Adivina el numero entre uno y cien (INGRESA EL NUMERO)------> :  "))
    intentos_realizados += 1
    
    if intento == num_sec:
        print(f"Felicidades, has adivinado el Numero en {intentos_realizados} Intentos ;) ")
        break
    elif intento < num_sec:
        print(f"El numero es mayor. \nTe quedan {intentos_maximos-intentos_realizados} intentos:")
    else:
        print(f"El numero es menor. \nTe quedan {intentos_maximos-intentos_realizados} intentos:")
if intentos_realizados == intentos_maximos:
    print("GAME OVER")