import sys
import math

def main():

    result = float()

    print(f'\nCurrent Result: {result}')
    operations()

numberList = []


def getUserChoice():
    try:
        choice = str(input("\nEnter Menu Selection: "))
        return choice
    except :
        print("\nInvalid Selection!")
        operationsNoMenu()


def operations():
    try:

        menu()

        choice = int(getUserChoice())

        if choice == 0:
            import sys
            print("Thanks for using this calculator. Goodbye!")
            sys.exit()
        elif choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            exponentiation()
        elif choice == 6:
            logarithm()
        elif choice == 7:
            average()
        elif choice < 0 or choice > 7:
            print('Error: Invalid selection!')
            operationsNoMenu()

    except TypeError:
        print("Error: Invalid seleection!")
        operationsNoMenu()


def operationsNoMenu():
    try:

        choice = int(getUserChoice())

        if choice == 0:
            closeApp()
        elif choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            exponentiation()
        elif choice == 6:
            logarithm()
        elif choice == 7:
            average()
        elif choice not in range(8) :
            print('Error: Invalid seleection!')
            operationsNoMenu()

    except TypeError:
        print("Error: Invalid selection!")
        operationsNoMenu()

def menu():
    print(
          "\nCalculator Menu"
          "\n---------------"
          "\n0. Exit Program"
          "\n1. Addition"
          "\n2. Subtraction"
          "\n3. Multiplication"
          "\n4. Division"
          "\n5. Exponentiation"
          "\n6. Logarithm"
          "\n7. Display Average")


def closeApp():
        import sys
        print("Thanks for using this calculator. Goodbye!")
        sys.exit()

def addition():
    try:
        operand1 = str(input("Enter first operand: "))
        operand2 = str(input("Enter second operand: "))
        if operand1 == 'RESULT':
            operand1 = numberList[-1]
        if operand2 == 'RESULT':
            operand2 = numberList[-1]
        operand1 = float(operand1)
        operand2 = float(operand2)
        result = operand1 + operand2
        numberList.append(result)
        print(f'\nCurrent Result: {result}')
        operations()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()


def subtraction():
    try:
        operand1 = str(input("Enter first operand: "))
        operand2 = str(input("Enter second operand: "))
        if operand1 == 'RESULT':
            operand1 = numberList[-1]
        if operand2 == 'RESULT':
            operand2 = numberList[-1]
        operand1 = float(operand1)
        operand2 = float(operand2)
        result = operand1 - operand2
        numberList.append(result)
        print(f'\nCurrent Result: {result}')
        operations()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()

def multiplication():
    try:
        operand1 = str(input("Enter first operand: "))
        operand2 = str(input("Enter second operand: "))
        if operand1 == 'RESULT':
            operand1 = numberList[-1]
        if operand2 == 'RESULT':
            operand2 = numberList[-1]
        operand1 = float(operand1)
        operand2 = float(operand2)
        result = operand1 * operand2
        numberList.append(result)
        print(f'\nCurrent Result: {result}')
        operations()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()

def division():
    try:
        operand1 = str(input("Enter first operand: "))
        operand2 = str(input("Enter second operand: "))
        if operand1 == 'RESULT':
            operand1 = numberList[-1]
        if operand2 == 'RESULT':
            operand2 = numberList[-1]
        operand1 = float(operand1)
        operand2 = float(operand2)
        if operand2 != 0:
            result = operand1 / operand2

            numberList.append(result)
            print(f'\nCurrent Result: {result}')
            operations()
        else:
            print("Division by Zero ERROR")
            operationsNoMenu()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()

def exponentiation():
    try:
        operand1 = str(input("Enter first operand: "))
        operand2 = str(input("Enter second operand: "))
        if operand1 == 'RESULT':
            operand1 = numberList[-1]
        if operand2 == 'RESULT':
            operand2 = numberList[-1]
        operand1 = float(operand1)
        operand2 = float(operand2)
        result = operand1 ** operand2
        numberList.append(result)
        print(f'\nCurrent Result: {round(result,2)}')
        operations()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()


def logarithm():
    try:
        operand1 = str(input("Enter first operand: "))
        if operand1 == 'RESULT' and len(numberList) > 0:
            operand1 = numberList[-1]
        elif operand1 == 'RESULT' and len(numberList) == 0:
            print('Error: Invalid selection!')
            operationsNoMenu()
        operand2 = str(input("Enter second operand: "))
        if operand2 == 'RESULT' and len(numberList) > 0:
            operand2 = numberList[-1]
        elif operand2 == 'RESULT' and len(numberList) == 0:
            print('Error: Invalid selection!')
            operationsNoMenu()
        operand1 = float(operand1)
        operand2 = float(operand2)
        if operand2 < 0:
            print('Error: Invalid selection!')
            operationsNoMenu()
        else:
            result = math.log(operand2, operand1)
            numberList.append (result)
            print(f'\nCurrent Result: {result}')
            operations()
    except TypeError:
        print('Error: Invalid selection!')
        operationsNoMenu()


def average():
        total = sum(numberList)
        numberOfItems = len(numberList)


        if len(numberList) > 0:
            average = total / numberOfItems

            print(f'Sum of calculations: {round(total,2)}\n'
                  f'Number of Calculations: {numberOfItems}\n'
                  f'Average of calculations: {round(average, 2)}')
            operationsNoMenu()
        else:
            print(f'\nError: No calculations yet to average!')
            operationsNoMenu()





if __name__ == '__main__':
    main()

