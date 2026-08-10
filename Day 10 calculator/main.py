def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

operations = {'+': add,
               '-': sub,
               '*': mul,
               '/': div}


def calc():
    calculate = True
    number1 = float(input('Enter first number: '))

    while calculate:

        operator = input('pick an operator  "+", "-", "*" or "/"): ')
        number2 = float(input('What is the next number?: '))
        answer = operations[operator](number1, number2)
        print(f"{number1} {operator} {number2} = {answer}")
        again = input("Type 'y' to continue calculating with 3.0, or type 'n' to start a new calculation:").lower()

        if again == 'n':
            calculate = False
        elif again == 'y':
            number1 = answer
        else:
            print("wrong input enter either y or n")


calc()