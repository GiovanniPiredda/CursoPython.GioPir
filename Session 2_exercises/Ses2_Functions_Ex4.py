#######################Session 2 - Exercises##########################
############
######Functions
############

#Exercise 4
'''Implementar un método recursivo para obtener el número de Fibonacci
 de un número a partir del input introducido por el usuario'''

'''print(fibonacci(2)) #1
   print(fibonacci(10)) #55 '''

def fibonacci():
    numA = int(input("Please insert a positive integer here: "))
    fiboList = [1]
    if numA <= 0:
        print("Your number should be positive!")
        numA = int(input("Please insert a positive integer here: "))
    v = 1
    for i in range(1,numA):
        fiboList.append(v)
        v = v + fiboList[i-1]
        #fiboList.append(i)
        #prev = fiboList[i - 1]

    print("The Fibonacci number for number",numA ,"is:", fiboList[numA-1])
fibonacci()

###################################################################
