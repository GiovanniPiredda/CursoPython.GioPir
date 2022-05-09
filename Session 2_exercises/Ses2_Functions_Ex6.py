#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 6
'''Un generador es un tipo concreto de iterador y es una función que permite obtener sus resultados paso a paso.
Implementar una función que cada vez que la llamemos nos de el próximo número par.'''

'''iterador = numeros_pares()
print(next(iterador)) #0
print(next(iterador)) #2
print(next(iterador)) #4
print(next(iterador)) #6
print(next(iterador)) #8'''


def even_number(): #definining even number function
    n=0
    while True:
        n = n+2
        yield n

evenNumber = even_number()
print(next(evenNumber)) #2
print(next(evenNumber)) #4
print(next(evenNumber)) #6
print(next(evenNumber)) #8

###################################################################
