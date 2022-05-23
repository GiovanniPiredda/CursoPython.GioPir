'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla
todos los años que ha cumplido (desde 1 hasta su edad).
'''
import datetime

def ask_age():
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Please enter JUST your age.")

    date = datetime.date.today()
    y = int(date.strftime("%Y"))

    for i in range(1,age+1):
        print("Year", str(i), "->", str(y-(age-i)))

ask_age()