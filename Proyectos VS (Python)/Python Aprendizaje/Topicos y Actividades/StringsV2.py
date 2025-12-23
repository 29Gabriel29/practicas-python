texto = 'Hello Guys'
print(texto)
print(texto.upper())
print(texto.lower())

texto = 'hello GuyS'
print(texto.capitalize())
texto = 'hello hello hello world'
print(texto.count('hello'))

print(texto.find("world"))
# Busca en que caracter aparece

print(texto.replace("e", "a"))
# Como dice el nombre, reemplaza caracter

print("Esta la r en el texto: ", ('r' in texto))