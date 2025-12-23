palabra = input("Ingrese una palabra para validar si es o no un PALINDROMO (Se lee igual al derecho y al reves)")

palabra = palabra.lower()

palabra = palabra.replace(" ", "")

palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print(f"{palabra} es un palindromo")
else: 
    print(f"{palabra} NO es un palindromo")