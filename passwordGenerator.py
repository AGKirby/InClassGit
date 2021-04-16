import string
import random

def generatePassword():
    try: 
        length = int(input("Please enter the length of the password to be generated: ")) # get a number from the user
    except: # if the user did not enter an integer
        print("Invalid input: integer expected. Exiting program.")
        return
    password = []
    for i in range(length):
        password += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)) #random uppercase character, lowercase character, or digit



generatePassword()