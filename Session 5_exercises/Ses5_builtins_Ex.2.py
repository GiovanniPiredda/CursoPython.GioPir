'''  Dada una lista como entrada, ordenar los elementos en función del número
que aparece junto con cada elemento.

lista= [('Programacion', 3),('Curso', 1), (2022, 4), ('Python', 2)]

En el ejemplo anterior, la lista ordenada queda de la siguiente forma:

[('Curso', 1), ('Python', 2), ('Programacion', 3), (2022, 4)]


'''

lista= [('Programacion', 3),('Curso', 1), (2022, 4), ('Python', 2)]

lista.sort(key = lambda x:x[1])

print (lista)