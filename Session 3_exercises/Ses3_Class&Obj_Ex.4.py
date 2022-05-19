'''Convertir el siguiente código para que se pueda ejecutar desde una clase.
El objetivo es crear una lista que tenga la funcionalidad de añadir elementos a la lista
 a partir de la cantidad de elementos que queremos introducir.'''
'''
listaElementos=[]
def anyadirElemento(elemento):
    listaElementos.append(elemento)

def imprimirLista():
    for elemento in listaElementos:
        print(elemento)

numero = int(input("Introduce la cantidad de elementos a introducir:"))
for i in range(numero):
    elemento = input("Introduce el nombre del elemento "+ str(i)    +":")
    anyadirElemento(elemento)

imprimirLista()
'''
class listElement():
    def __init__(self):
        list = []
        self.elementQ = int(input("Please insert how many element you want to assign to the list: "))
        for i in range(self.elementQ):
            element = input("Please insert an element here: ")
            list.append(element)
        return print(list)

listElement()