''' Aplicar la función reduce sobre una lista de elementos numéricos para
multiplicar sus elementos.

from functools import reduce
lista = [1, 3, 5]

'''

from functools import reduce

def multiply_elements(el1,el2):
    return el1*el2

listA = [1,3,5]
result = reduce(multiply_elements,listA)
print (result)