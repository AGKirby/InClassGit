def divisors():
    try: 
        num = int(input("Please enter the first number: ")) # get a number from the user
    except: # if the user did not enter an integer
        print("Invalid input: integer expected. Exiting program.")
        return
    for i in range(1, num//2+1): # numbers from one to half of the user's input plus one
        if(num % i == 0): #divisible by i
            print(str(i), end=" ")
    print(str(num))


divisors()