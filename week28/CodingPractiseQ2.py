# given a user input number n, create a dictionary that defines i:i*i where i is a number between 1, n.
number = int(input("enter number"))
dictionary = {i:i*i for i in range(1, number+1)}
print(dictionary)
