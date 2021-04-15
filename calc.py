def calc():
    try: 
        num1 = int(input("Please enter the first number: ")) # get a number from the user
        operation = input("Please enter the operation (+, -, *, /): ") # get a character from the user
        num2 = int(input("Please enter the second number: ")) # get a number from the user
    except: # if the user did not enter an integer
        print("Invalid input: integer expected. Exiting program.")
        return
    result = 0
    # call a function based on the inputted operation
    if(operation == "+"):
        result = add(num1, num2)
    elif(operation == "-"):
        result = subract(num1, num2)
    elif(operation == "*"):
        result = multiply(num1, num2)
    elif(operation == "/"):
        try: 
            result = divide(num1, num2)
        except: # if divide by zero error
            print("Invalid divisor: the second number cannot be zero in a division statement!")
            return
    else: #if inputted operation is not valid
        print("Invalid operation: expected one of the follow: '+', '-', '*', or '/'")
        return
    # print the results
    print(str(num1) + " " + operation + " " + str(num2) + " = " + str(result))
    #change made


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

calc()