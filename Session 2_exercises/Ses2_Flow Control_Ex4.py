#######################Session 2 - Exercises##########################
############
######Flow Control
############

#Exercise 4
'''Escribe un programa que pida el email y contraseña y compruebe las credenciales con los siguientes valores
email=user@email.com, contraseña = password.
El programa tiene que pedir introducir los valores al usuario hasta que los valores sean correctos.'''

correctEmail = "user@email.com"
correctPsw = "password"

userEmail = input("Please insert your email here: ")
userPsw = input("Please insert your password here: ")


while userEmail != correctEmail or userPsw != correctPsw:
    print("Your email or password are not correct.\n\nPlease insert your credentials again.")
    userEmail = input("Please insert your email here: ")
    userPsw = input("Please insert your password here: ")
    break
print("Access correct")

###################################################################
