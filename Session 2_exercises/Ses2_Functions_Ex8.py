#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 8
'''Desarrollar una función que devuelva los números
primos menores de un determinado número utilizando
 la siguiente función lambda que devuelve True si el número es primo,
 False en caso contrario.
Un número es primo si es divisible por sí mismo'''

'''es_primo = lambda numero: all( numero%i != 0 for i in range(2, int(numero)) )

Introduce número de entrada : 15
2
3
5
7
11
13'''

es_primo = lambda numero: all( numero%i != 0 for i in range(2, int(numero)) )

def prime_number_in():
    n = int(input("Please input an integer number here: "))
    for i in range(1 , n):
        if es_primo(i) == True:
            print(i)


prime_number_in()

###################################################################
