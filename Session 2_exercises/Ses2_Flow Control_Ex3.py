#######################Session 2 - Exercises##########################
############
######Flow Control
############

#Exercise 3
'''Escribe un programa que pida números desde teclado y los vaya sumando hasta que la suma supere el valor 100'''


nUser = float(input("Please insert a number here:"))

print("Thank you!\n\nNow the following number given by you are going to be added to the previous one"
      "\nuntill the total sum will be greater than 100")
while nUser < 100:
    nUser = float(input("Please insert another number"))+nUser
print("\nNow the total sum of the number is: ",nUser)
print("\nEnd of the program")




###################################################################
