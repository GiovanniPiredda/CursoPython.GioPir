#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 5
'''Implementar la función matriz_aleatoria(n, m, max) que permita generar
 una matriz de tantas filas y columnas como indique el usuario.
Además le indicamos cual es el máximo valor aleatorio que contendrá la matriz.'''

'''def print_matriz(M):
for i in range(len(M)):
for j in range(len(M[i])):
print(M[i][j], end = '\t')
print()
n = int(input('Dame el número de filas: '))
m = int(input('Dame el número de columnas: '))
max = int(input('Dame el valor máximo aleatorio: '))
M = matriz_aleatoria(n, m, max)
print_matriz(M)

Dame el número de filas: 3
Dame el número de columnas: 3
Dame el valor máximo aleatorio: 4
2.5850215084552217 1.5425389317238993 0.7935125836991488
3.3194733958537963 1.8983850594028504 2.845316988342773
2.0067961233238485 3.342438647663114 3.676714583063357'''
from random import uniform
def randomMatrix():
    M = []
    n = int(input('Please insert the number of the rows: '))
    m = int(input('Please insert the number of the columns: '))
    max = float(input('Please insert the max random number: '))
    for r in range(n):
        raw = []
        for c in range(m):
            raw.append(uniform(1,max))

        M.append(raw)
    print("The matrix generated with your parameters is: ")
    for line in M:
        print('  '.join(map(str, line)))
randomMatrix()



###################################################################
