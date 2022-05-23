'''Utilizar el módulo sys para sumar los argumentos pasados a un programa'''

'''
$ python suma_argumentos_sys.py 1 5 10
Has introducido 4 argumentos
La suma es 16
'''
import sys
def sum():
    listA = sys.argv[1:]
    try:
        for i in listA:
            if type(i) == int or float:
                if listA == []:
                    print("Please insert some argument in the script.")
                #print(listA)
                count = 0
                sumA = 0
                for i in listA:
                    count += 1
                    sumA += float(i)
                print("You inputted", count, "arguments.")
                print("The sum of the arguments is:", sumA)
                return sumA

    except:
        print("Please insert a numeric value as argument.")

sum()

