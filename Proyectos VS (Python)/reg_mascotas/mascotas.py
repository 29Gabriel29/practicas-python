#definicion de clase y constructor
class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad
 
    def __str__(self):
        return f"Animal[Especie: {self.especie}, Edad: {self.edad}]"   
     
#Creacion de objeto de aniomal, ejemplo perro

animalUno = Animal("Perro", "1 Año")
animalDos = Animal("Gato", "8 meses")


#herencia de clases (Mascota hereda de Animal)
class Mascota(Animal):
    def __init__(self, especie, edad, nombre):
        super().__init__(especie, edad) #esto esa por los atributos heredados de la super clase
        self.nombre = nombre

    def info(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}")
    
    def __str__(self):
        return f"Mascota[Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}]"   

mascota = Mascota("Perro", "3 años", "Negro")
print(mascota)