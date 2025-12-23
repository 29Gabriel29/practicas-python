# Agregamos anotaciones de tipo para informar que tipos de argumentos deberian ir en una funcion por ejemplo

a: int = 400
print(a)

# De esta manera informamos el tipo de dato a tomar y el que devolvera la funcion
def suma(a:int, b:int) -> int:
    return a + b
print(suma(705, 980))

def saludo(nombre:str, veces:int=1) -> str:
    return(f"Hola {nombre}" * veces)
print(saludo("Gabriel", 3))
