#######################Session 2 - Exercises##########################
############
######Flow Control
############

#Exercise 2
'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable
y pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

password = input("Please insert your password here: ")
confPsw = input("If you want to confirm your password please insert 'True', otherwise 'False': ")

if confPsw == "True":
    print("Thank you!\nNow your password has been saved!")
    pswAttempt = input("Hi, could you please insert your password? ")
    while (pswAttempt != password):
        print("Password not correct")
        pswAttempt = input("Hi, could you please insert your password? ")
        if pswAttempt == password:
            print("\nYour password is correct!")
            break
    print("End of the program")
else:
    print("Alright. Let's start from the begin than.\n\nPlease run again the program\n\n\nEnd of the program")






###################################################################
