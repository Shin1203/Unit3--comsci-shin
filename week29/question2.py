# this program will take a number from user, and create passwords
number = int(input("Enter number of passwords to be made"))
import random
import string

def randomPassword():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(20))
for i in range(number):
    print(randomPassword())
