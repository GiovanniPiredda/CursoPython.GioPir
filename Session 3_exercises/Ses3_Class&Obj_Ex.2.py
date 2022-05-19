'''Convertir la siguiente clase Persona en una data class utilizando la notación @dataclass sobreescribiendo
los métodos __init__ constructor y el método __eq__ que permite comparar 2 objetos de la clase y decir si son iguales
 o no. Añadir tipos a los campos nombre y apellidos de tipo string y la edad de tipo entero.'''
from dataclasses import dataclass
class Persona:
    def __init__ (self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))
    def __str__(self):
        return self.Nombre + " "+ self.Apellidos

persona1 = Persona("Giovanni","Piredda","34")
persona1.MostrarPersona()
#print(persona1)

@dataclass
class PersonaDataClass(object):
    name: str
    lastName: str
    age: int
    def ShowPersonaDC(self):
        print("Nombre: ", self.name)
        print("Apellidos: ", self.lastName)
        print("Edad: ", self.age)
    def __str__(self) -> str:
        return self.name + " " + self.lastName

person2 = PersonaDataClass("Irene","Cuadrado Martin", 24)
person2.ShowPersonaDC()

print(person2)