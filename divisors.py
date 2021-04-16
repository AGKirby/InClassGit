def divisors():
    try: 
        num = int(input("Please enter the number: ")) # get a number from the user
    except: # if the user did not enter an integer
        print("Invalid input: integer expected. Exiting program.")
        return
    print(str(num) + " is divisible by ", end="")
    first = True
    for i in range(1, num//2+1): # numbers from one to half of the user's input plus one
        if(num % i == 0): #divisible by i
            if(not first): #if not the first number then add a comma
                print(", ", end="")
            else: 
                first = False
            print(str(i), end="")
    if(not first):
        print(" and ", end="")
    print(str(num))


divisors()