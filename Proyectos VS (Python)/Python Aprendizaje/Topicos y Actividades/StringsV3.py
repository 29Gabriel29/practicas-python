
Nombre = "Gabriel"
Edad = 24
Altura = 1.75

print("Hola, me llamo ", Nombre, ", tengo ", Edad, "y mido ", Altura)


print("Hola, me llamo %s , tengo %d y mido %.2f metros" % (Nombre, Edad, Altura))


print("Hola, me llamo {} , tengo {} y mido {:.2f} metros".format(Nombre, Edad, Altura))


print(f"Hola, me llamo {Nombre} , tengo {Edad} y mido {Altura:.2f} metros")
# ESTA ES LA OPCION MAS RECOMENDADA POR TENER CONTROLDEFORMATO, RAPIDEZ, ADMITIR EXPRESIONES DE :.2f por ejemplo, ES LEGIBLE.
