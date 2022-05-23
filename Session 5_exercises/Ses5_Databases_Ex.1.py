''' Dado el script productos_sqlite.py que inserta datos en la base de datos productos.sqlite
'''


'''
import sqlite3
conex = sqlite3.connect('productos.sqlite')
cursor = conex.cursor()
def creacion():
    cursor.execute("CREATE TABLE IF NOT EXISTS listado (" +
        "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, " +
        "nombre TEXT NOT NULL, " +
        "proveedor TEXT NOT NULL, " +
        "precio REAL, " +
        "stock INTEGER DEFAULT 0)")
def insertar():
    nombre = input("Nombre del producto: ")
    proveedor = input("Proveedor: ")
    precio = input("Precio: ")
    cursor.execute("INSERT INTO listado (nombre, proveedor, precio) " +
        "VALUES (?, ?, ?)", (nombre, proveedor, precio))
    conex.commit()
creacion()
insertar()
cursor.close()'''

'''
● Cambiar el nombre de la tabla a “productos”
● Modificar el script para pedir al usuario que inserte el stock del producto e
insertarlo en la nueva tabla
● Pedir al usuario el número de productos que desea insertar y crear un bucle
que permita insertar el número de productos introducidos.'''



import sqlite3
conex = sqlite3.connect('productos')
cursor = conex.cursor()
def creacion():
    cursor.execute("CREATE TABLE IF NOT EXISTS listado (" +
        "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, " +
        "nombre TEXT NOT NULL, " +
        "proveedor TEXT NOT NULL, " +
        "precio REAL, " +
        "stock INTEGER DEFAULT 0)")
def insertar():
    nProd = int(input("Inserta el numero de productos: "))
    for i in range(nProd):
        nombre = input("Nombre del producto: ")
        proveedor = input("Proveedor: ")
        precio = input("Precio: ")
        stock = int(input("Stock: "))
        cursor.execute("INSERT INTO listado (nombre, proveedor, precio) " +
            "VALUES (?, ?, ?)", (nombre, proveedor, precio, stock))
    conex.commit()
creacion()
insertar()
cursor.close()