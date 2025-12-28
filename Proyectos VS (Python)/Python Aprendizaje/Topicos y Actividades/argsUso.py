# Argumentos indefinidos por posicion
def args_func(*args):
    print(args)
# Me devuelve una tupla
args_func("Hola como estas????", 2025, False)

def suma(a, b):
    print(f"a es igual a la variable a ----> a = {a} y b = {b}")
    return a + b
# 1 er manera de poner el argumento
suma(76, 80) 
# 2 da manera de poner el argumento
suma(b = 500, a = 1000)

# Argumentos indefinidos con nombre
# Me devuelve un diccionario
def kwargsGab_func(**kwargs):
    print(kwargs)

kwargsGab_func(nombre = "Gabriel", a = 50, b = 90)

# Este seria el orden para combinar los 3 argumentos
def argumentos(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

argumentos(600, "Hello", False, 500, nombre = "Gabriel", b = 20)
