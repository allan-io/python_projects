from calendar import firstweekday

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)
def calculate():
    first_boot = True
    num1 = 0
    while True:
        if first_boot:
            num1 = float(input("What's the first number? "))
        operator = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What's the next number? "))

        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        use_result = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation')

        if use_result == "y":
            num1 = result
            first_boot = False
        else:
            calculate()
calculate()