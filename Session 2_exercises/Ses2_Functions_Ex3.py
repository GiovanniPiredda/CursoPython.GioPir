#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 3
'''Implementar un método que recibe un número y devuelva una lista de número primos menores al número introducido.
La siguiente función determina si un número es o no primo.'''

'''def es_primo(num):
for i in range(2, num):
if num % i == 0:
return False
return True

Introduce un número entero: 30
Los primos igual o menores a 30 son [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] '''

def isPrime ():
    numA = int((input("Please insert an integer number here: ")))
    listA = []

    for i in range(numA-1,1,-1):
        d = 2
        if i == d:
            listA.append(i)
        while i % d != 0:
            d = d+1
            if i == d:
                listA.append(i)
    listA.append(1)
    print("The prime numbers lower than", numA, "are: \n",listA)

isPrime()

###################################################################
