def get_operation ():
    operation = int(input("What operation would you like to do? 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division "))
    if operation<0 or operation>4:
        print("No can do sir make sure you input a number from the choices above")
        operation = int(input("What operation would you like to do? 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division "))

def calculator ():
    firstNumber = float(input("Input your first number: "))
    operation = get_operation()
    secondNumber = float(input("Input your second number: "))

    if operation == 1:
        result = firstNumber + secondNumber
        operation = " + "
    elif operation == 2:
        result = firstNumber - secondNumber
        operation = " - "
    elif operation == 3:
        result = firstNumber * secondNumber
        operation = " x "
    else:
        result = firstNumber / secondNumber
        operation = " ÷ "

    result = round(result,3)
    print(f"{firstNumber}{operation}{secondNumber} = {result}")

calculator()

