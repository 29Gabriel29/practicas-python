#Los elementos de un diccionario se componen de clave y valor, debe ser unica la clave
datos_personales = { "nombre":"Gabriel", "edad":"24", "ciudad":"Corrientes" }

print("\nMuestreo de los valores de el diccionario creado de datos personales")
print(datos_personales["ciudad"])
print(datos_personales["edad"])
print(datos_personales["nombre"])

print("\nMuestro si existe una clave -----> ", "nombre" in datos_personales)

#Al usar get en el diccionario, el primer parametro es el que se desea obtener y en el segundo parametro coloco un mensaje en caso de no encontrarlo
print("\nPractica de get: ", datos_personales.get("pais", "No especificado"))

#Adicion de un nuevo elemento o reemplazo de uno ya existente
datos_personales["Pais"] = "Argentina"
print(datos_personales["Pais"])
datos_personales["Pais"] = "Angola"
print(datos_personales["Pais"])

#Metodo update
datos_personales.update({"edad":"24"})
datos_personales.update({"Domicilio":"Barrio Jardin"})

print("\nMuestreo de los valores de el diccionario creado de datos personales")
print(datos_personales["ciudad"])
print(datos_personales["edad"])
print(datos_personales["nombre"])
print(datos_personales["Pais"])
print(datos_personales["Domicilio"])

#Metodo delete
del datos_personales["Pais"]
print(datos_personales.pop("edad"))
print(len(datos_personales))
print(list(datos_personales.keys()))
print(list(datos_personales.values()))
print(datos_personales.items())
print(list(datos_personales.items()))