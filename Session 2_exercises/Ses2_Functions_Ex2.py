#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 2
'''Escribir una función que pida un número al usuario y almacena ese número en una lista.
El proceso no termina hasta que se introduzca la cadena “fin”.
Además, si lo que introduce el usuario no es un número, devuelve el mensaje
 ”El dato introducido no es un número entero, por favor vuelve a introducirlo o escribe "fin" para terminar.”'''

'''Introduce un número: 1
Introduce un número: 2
Introduce un número: 10
Introduce un número: python
El dato introducido no es un número entero, por favor vuelve a introducirlo o
escribe "fin" para terminar.
Introduce un número: 5
Introduce un número: fin
[1, 2, 10, 5]'''

listA =[]
def askNumber ():
    userN = input("Please input an integer to add your number at the list, or insert 'end' to close the list: ")

    while userN != "end":
        if userN.isnumeric() == True:
            listA.append(userN)
            print("Number ", userN, " is added to the list")
            userN = input("Please input another integer to add your number at the list, or insert 'end' to close the list: ")
        else:
            userN = input("Your input is not an integer, please insert it again or type 'end' to close the list: ")

    print("The list is now closed.\n\n", listA)

askNumber()

###################################################################
