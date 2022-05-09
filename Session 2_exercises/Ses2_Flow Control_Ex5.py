#######################Session 2 - Exercises##########################
############
######Flow Control
############

#Exercise 5
'''Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1
hasta ese número separados por un salto de línea.'''

userNumber = int(input("Please insert a positive integer here: "))

while userNumber <= 0:
    print("Your number should be integer and POSITVE.")
    userNumber = int(input("Please insert a positive integer here: "))
    break

for i in range(1,(userNumber+1),2):
    print(i)

print("\nEnd of the program")


###################################################################
