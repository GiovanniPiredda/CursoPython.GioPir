'''Escribir una función que pida un número entre 1 y 10, lea el fichero
tabla-numero.txt con la tabla de multiplicar de ese número, y devuelve por en
una lista el contenido del fichero. Si el fichero no existe debe mostrar un
mensaje por pantalla informando de ello.'''

def readTable():
    try:
        number = int(input("Please insert the number between 1 and 10 you want the multiplication table here: "))
        path = (("tabla-" + str(number) + ".txt"))
        try:
            f = open(path, "r")
            text = f.read()
            f.close()
            print(text)
        except FileNotFoundError:
            print("Error: File not found.")
            print("Please be ensure the file you inputted exists.")
    except ValueError:
        print("The value you inputted is not valid. Please insert an integer between 1 and 10")

readTable()