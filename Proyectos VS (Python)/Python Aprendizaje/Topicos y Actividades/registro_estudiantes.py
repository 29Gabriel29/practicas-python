
registro_estudiantes = []

while True:
    print("1_ Registrar Estudiante")
    print("2_ Mostrar Registro")
    print("3_ SALIR")

    opcion = input("\nSeleccione una opcion:    ")

    if opcion == '1':
        # Registramos estudiante
        nombre = input("Ingrese el nombre del estudiant:  ")
        edad = int(input("Ingrese la edad del estudiante:  "))
        curso = input("Ingrese el curso del estudiante:  ")

        estudiante = {"Nombre":nombre, "Edad":edad, "Curso":curso}
        registro_estudiantes.append(estudiante)
        print("\nESTUDIANTE REGISTRADO EXITOSAMENTE")
    elif opcion == '2':
        if registro_estudiantes:
            print("\n----Registro de Estudiantes----")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso: {estudiante["Curso"]}\n")
        else:
            print("El registro esta Vacio. Registre estudiantes primero")        
    elif opcion == '3':
        print("Saliendo del Programa\n")
        break
    else:
        print("Opcion NO valida, Intente nuevamente\n")
    