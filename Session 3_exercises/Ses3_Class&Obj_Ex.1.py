'''Implementar una clase Calculadora con las operaciones de suma, resta,
multiplicación y división, teniendo como entrada 2 valores que se introducen
por teclado como se muestra en el código.'''

class Calculadora:
    def __init__(self):
        self.valor1=float(input("Please insert your first value: "))
        self.valor2=float(input("Please insert your second value: "))
        print("Your values are", self.valor1, "and", self.valor2)
    def operation(self):
        oper1=(input("Type 'Addition' or '+' to add value1 to value2\n"
              "Type 'Subtraction' or '-' to subtract value2 from value1\n"
              "Type 'Multiplication' or '*' to mutiply value 1 and value 2\n"
              "Type 'Division' or'/' to divide value 1 into value 2\n"
              "Please insert the operation you want to calculate:"))
        result = 0
        if oper1 == "Addition" or oper1 == "+" or oper1 == "addition":
            result = self.valor1 + self.valor2
            return result
        elif oper1== "Subtraction" or oper1 == "-" or oper1 == "subtraction":
            result = self.valor1 - self.valor2
            return result
        elif oper1== "Multiplication" or oper1 == "*" or oper1 == "multiplication":
            result = self.valor1 * self.valor2
            return result
        elif oper1== "Division" or oper1 == "/" or oper1 == "division":
            result = self.valor1 / self.valor2
            return result
        else:
            print('''Your value is not valid. Try again!''')


            #try to insert a loop here

calcolatrice = Calculadora()
print(calcolatrice.operation())

'''Ingrese el primer valor: 4
Ingrese el segundo valor: 4
Los valores son:
Valor 1: 4
Valor 2: 4
El resultado de la suma de los valores es: 8
El resultado de la resta de los valores es: 0
El resultado de la multiplicación de los valores es: 16
El resultado de la división de los valores es: 1.0'''