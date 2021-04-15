def calc():
    # get user input
    try: 
        num1 = int(input("Please enter the first number: ")) # get a number from the user
        num2 = int(input("Please enter the second number: ")) # get a number from the user
    except: # if the user did not enter an integer
        print("Invalid input: integer expected. Exiting program.")
        return
    result = 0
    # calculate the results
    sum = num1 + num2
    difference = num1 - num2
    multiply = num1 * num2
    try: 
        divide = num1 / num2
    except: #divide by zero error!
        divide = None

calc()