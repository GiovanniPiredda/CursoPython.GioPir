'''  Dada una lista de números obtener de forma separada pares e impares. Uso de
lambda, filter y sort.

Ejecución:
lista = [1,2,3,5,15,20,30,35,50]
Pares [2, 20, 30, 50]
Impares [1, 3, 5, 15, 35]
'''

import random

listA = [random.randint(0,100) for x in range(10)]
listA.sort()
print(listA)

listOdd = list(filter(lambda x: x % 2 != 0, listA))
listA = list(filter(lambda x: x % 2 == 0, listA))

print ("Odds: ", listOdd)
print ("Evens: ",listA)


