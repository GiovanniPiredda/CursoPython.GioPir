'''Implementar una clase CestaCompra que ofrezca la posibilidad de añadir productos que el usuario
introduce desde el teclado. Nuestro programa principal solicita la cantidad de productos y posteriormente
se van introduciendo el nombre y el precio de los productos.
La función imprimirProductos() hace un resumen de los productos y obtiene el total.'''

#Aquí la clase producto no debería de ir con los paréntesis ya que con ellos no hace una buena referencia.
class Producto:
    #Se ha renombrado el atributo elemento por producto para tener una mejor declaración.
    def __init__(self,producto,precio):
        self.producto = producto
        self.precio = precio

class CestaCompra():
    def __init__(self):
        self.basket=[]
        self.total=0

    #En la función añadir producto se añade dentro el producto gracias a la función append de las listas.
    def anyadirProducto(self,producto):
    	self.basket.append(producto)

    #Se ha replanteado la función de imprimir los productos, recorre la lista de los productos y los devuelve por pantalla, prod se puede cambiar por la palabra que quieras pero yo he elegido prod para que vaya relacionado.
    #Por último en la función se imprime el total del precio.
    def imprimirProductos(self):
        for prod in self.basket:
        	print("Producto:"+prod.producto+" Precio:"+str(prod.precio))
        	self.total = self.total + prod.precio
        print("Total:"+str(self.total))

def main():
    cestaCompra = CestaCompra()
    numero = int(input("Introduce la cantidad de productos:"))
    for i in range(numero):
        elemento = input("Introduce el nombre del producto "+ str(i+1)+":")
        precio = float(input("Introduce el precio del producto "+ elemento+":"))
        cestaCompra.anyadirProducto(Producto(elemento,precio)) #el problema está aquí: no consigo realizar el codigo para esta funcion en particular
        #Ahora la función de anyadirProducto funciona, lo que pasaba es que la función la habías dejado vacía.

    cestaCompra.imprimirProductos() #esta funcion va dentro del main() ???????
    #En efecto, esta función va dentro del main()

#Por último se añade la llamada a la función.
main()