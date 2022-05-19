'''Crear un módulo que tenga una clase que permite añadir y sacar elementos de una lista.
En el programa principal, iniciar la clase indicando el número máximo de elementos y si supera
el máximo de elementos,indicar que no es posible añadir más elementos a  la lista.'''

class ElementosLista():
    def __init__(self, maximo, numero):
        self.maximo_elementos = maximo
        self.numero_elementos = numero
        print("The maximum capacity of the list is: ", maximo," elements.")
        print("The list contains: ", numero, " element.")
    def anyadir_elemento(self,addElement=1):
            if self.numero_elementos + addElement < self.maximo_elementos:
                print("Adding", addElement, "element(s) to the list.")
                self.numero_elementos = self.numero_elementos + addElement
                print("Now the list has",self.numero_elementos,"elements")

            else:
                print("Not possible to add other elements to the list.\nPlease remove one from the list.")
    def sacar_elemento(self,removeElement=1):
        if (self.numero_elementos-removeElement > 0):
            print("Removing", removeElement, "element(s) to the list.")
            self.numero_elementos = self.numero_elementos - removeElement
            print("Now the list has", self.numero_elementos, "elements")
        else:
            print("There are not enough elements to be removed. Please add some elements to the list.")



def main():
    listA = ElementosLista(10,10)
    listA.anyadir_elemento(3)
    listA.sacar_elemento(5)
#    print(listA.numero_elementos)
    listA.anyadir_elemento(3)
#    print(listA.numero_elementos)
'''    print(listA.maximo_elementos)
    print(listA.numero_elementos)
    listA.anyadir_elemento()
    print(listA.numero_elementos)
    listA.sacar_elemento()
    print(listA.numero_elementos)
    listA.anyadir_elemento()
    print(listA.numero_elementos)'''

main()