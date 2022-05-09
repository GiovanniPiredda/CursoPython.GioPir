#######################Session 2 - Exercises##########################
############
######Flow Control
############

#Exercise 1
'''Un n-grama es una secuencia de n caracteres consecutivos de una cadena.
Por ejemplo, los 3-gramas de la cadena 'Python' son 'Pyt', 'yth', 'tho' y 'hon'.
Escribir un programa que pregunte por una cadena y
un número entero positivo n y muestre por pantalla todos los n-gramas de la cadena.'''

from nltk import ngrams

userString = input("Please insert a string here: ")
userInt = int(input("Please insert an integer here: "))
c = len(userString)
if userInt > c:
    print ("Your input is incorrect. Please be insure that your integer should be lower than string lenght")
    userString = input("Please insert again a string here: ")
    userInt = int(input("Please insert an integer (lower than string lenght) here: "))
else:
    print("Thank you!")
    print("Here is your n-gram:")
d = 0
for i in userString:
    print(userString[d:userInt])
    d = d+1
    userInt = userInt+1

###################################################################
