'''Crear un módulo que dispone de 2 métodos. Uno para calcular el área a partir de su lado
que se pasa por parámetro y otro para calcular el área del círculo a partir del radio
que se pasa por parámetro.'''
import math
def square(side):
    """ Calcula el area del cuadrado a partir de su lado """
#    side = float(input("Please insert the length of the square here: "))
    print("The side of the square is:", side)
    print("The formula to calculate the area of the square is: side^2.")
    print("So, the area of your square is:", side**2)
    return side ** 2

def circle(radius):
    """ Calcula el area del circulo dado el radio """
#    radius = float(input("Please insert the length of the radius fo the circle here: "))
    print("The radius of the circle is:", radius)
    print("The formula to calculate the area of the circle is: (radius^2)*pi.")
    print("So, the area of your square is:", math.pi * radius ** 2)
    return math.pi * radius ** 2

square(3)
circle(2)
