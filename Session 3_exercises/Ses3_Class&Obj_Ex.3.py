'''Crear un decorador que devuelva los elementos de una cadena como si fuera una lista.
Por ejemplo,ante la entrada de la cadena “Bienvenido al curso de Python”,
devuelve cada uno de los elementos en una nueva lista.'''


def separateStr(funParameter):
    def wrapper():
        str2 = funParameter()
        lst = []
        for i in str2:
            lst.append(i)
        return lst
    return wrapper

@separateStr
def insertStr():
    str1 = str(input("Please insert a string here: "))
    return str1

print(insertStr())
